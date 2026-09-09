"""Decision Lab: local, read-only API for historical experimental records.

Start with: python main.py
Open: http://127.0.0.1:8000/docs
The PostgreSQL password is prompted for and kept only in process memory.
Optional DB settings: PGHOST, PGPORT, PGDATABASE, PGUSER, PGPASSWORD.
Historical replay with held-out LSTM inference on PostgreSQL-built feature prefixes.
"""
import getpass
import os
from typing import Annotated, Literal

import psycopg
from psycopg.rows import dict_row
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse, FileResponse
from pathlib import Path
import uvicorn
import numpy as np
from objectives import evaluate

app = FastAPI(
    title='Decision Lab API',
    version='0.5.0',
    description='Explore historical decisions. Elapsed time starts at the first own sample, not the round start. Held-out LSTM predictions use PostgreSQL-built feature prefixes.',
)
Session = Literal['feb18', 'feb20', 'march6']
PositiveInt = Annotated[int, Query(ge=1)]
Game = Annotated[int, Query(ge=1, le=4)]
DB_SETTINGS = {
    'host': os.getenv('PGHOST', 'localhost'),
    'port': os.getenv('PGPORT', '5432'),
    'dbname': os.getenv('PGDATABASE', 'decision_lab'),
    'user': os.getenv('PGUSER', 'postgres'),
    'password': os.getenv('PGPASSWORD'),
    'connect_timeout': 5,
}


def fetch(query, params=()):
    """Run a parameterized SELECT, return dictionaries, close the connection.

    A connection per request is sufficient for this local first version.
    A later deployment can use a connection pool and a dedicated DB role.
    """
    with psycopg.connect(**DB_SETTINGS, row_factory=dict_row) as conn:
        conn.read_only = True
        with conn.cursor() as cur:
            cur.execute(query, params)
            return cur.fetchall()


@app.exception_handler(psycopg.Error)
def database_error(request, exc):
    # Do not send raw connection details or database errors to the browser.
    return JSONResponse(status_code=503, content={
        'detail': 'Database request failed. Check PostgreSQL is running, connection settings, and that import_data.py and import_functions.py completed.'
    })


@app.get('/')
def home():
    return FileResponse(Path(__file__).resolve().parent / 'replay.html')


@app.get('/health')
def health():
    fetch('SELECT 1')
    return {'status': 'ok', 'database': 'connected'}


@app.get('/sessions')
def sessions():
    """List sessions and their imported round/sample counts."""
    return fetch('''
        SELECT e.session_id, e.session_date, e.x_min, e.x_max,
               COUNT(DISTINCT r.participant_round_id) AS participant_rounds,
               COUNT(s.sample_id) AS samples
        FROM experiment_sessions e
        LEFT JOIN participant_rounds r ON r.session_id = e.session_id
        LEFT JOIN samples s ON s.participant_round_id = r.participant_round_id
        GROUP BY e.session_id, e.session_date, e.x_min, e.x_max
        ORDER BY e.session_date
    ''')


@app.get('/rounds')
def rounds(session_id: Session, game_number: Game):
    """Find participants and recorded rounds for a session/game."""
    return fetch('''
        SELECT r.participant_id, r.round_number, COUNT(s.sample_id) AS sample_count
        FROM participant_rounds r
        JOIN samples s ON s.participant_round_id = r.participant_round_id
        WHERE r.session_id = %s AND r.game_number = %s
        GROUP BY r.participant_id, r.round_number
        ORDER BY r.participant_id, r.round_number
    ''', (session_id, game_number))


@app.get('/samples')
def samples(session_id: Session, game_number: Game, participant_id: PositiveInt,
            round_number: PositiveInt,
            through_step: Annotated[int | None, Query(ge=1)] = None):
    """Return own decisions in order, optionally stopping at a replay step.

    Running best and elapsed time only use the returned history. These are
    display calculations, not the LSTM's merged own/teammate feature builder.
    The final round payoff and winning status are deliberately not returned.
    """
    rows = fetch('''
        SELECT s.step_number, s.x_value, s.observed_value, s.sampled_at
        FROM samples s
        JOIN participant_rounds r ON r.participant_round_id = s.participant_round_id
        WHERE r.session_id = %s AND r.game_number = %s
          AND r.participant_id = %s AND r.round_number = %s
        ORDER BY s.step_number
    ''', (session_id, game_number, participant_id, round_number))
    if not rows:
        raise HTTPException(status_code=404, detail='No recorded samples for this participant-round.')
    if through_step is not None:
        rows = [row for row in rows if row['step_number'] <= through_step]
    function = get_function(session_id, game_number, round_number)
    xmin, xmax = function['x_min'], function['x_max']
    maximum = function['estimated_maximum']
    first_time = rows[0]['sampled_at']
    best = float('-inf')
    previous_x = None
    for row in rows:
        best = max(best, row['observed_value'])
        row['best_value_so_far'] = best
        row['position_fraction'] = (row['x_value'] - xmin) / (xmax - xmin)
        row['quality_fraction'] = row['observed_value'] / maximum
        row['best_quality_fraction_so_far'] = best / maximum
        row['change_in_x'] = None if previous_x is None else row['x_value'] - previous_x
        row['seconds_since_first_sample'] = (row['sampled_at'] - first_time).total_seconds()
        previous_x = row['x_value']
    return {
        'session_id': session_id, 'game_number': game_number,
        'participant_id': participant_id, 'round_number': round_number,
        'time_reference': 'first own recorded sample; not round start',
        'normalization': {'x_min': xmin, 'x_max': xmax, 'estimated_maximum': maximum,
                          'maximum_method': function['maximum_method'],
                          'perspective': 'analyst view; full objective used for scaling'},
        'samples': rows,
    }


def get_function(session_id, game_number, round_number):
    rows = fetch("""
        SELECT f.function_family, f.parameters, f.estimated_maximum, f.maximum_method,
               e.x_min, e.x_max
        FROM round_functions f
        JOIN experiment_sessions e ON e.session_id = f.session_id
        WHERE f.session_id=%s AND f.game_number=%s AND f.round_number=%s
    """, (session_id, game_number, round_number))
    if not rows:
        raise HTTPException(status_code=404, detail='Round function not found. Run import_functions.py and check the selected round.')
    return rows[0]


@app.get('/landscape')
def landscape(session_id: Session, game_number: Game, round_number: PositiveInt,
              points: Annotated[int, Query(ge=50, le=2000)] = 500):
    """Full objective for optional analyst reveal; not an LSTM input.

    Curve sampling is for plotting only. Normalization uses the stored
    maximum computed with the original model's denser numerical procedure.
    """
    function = get_function(session_id, game_number, round_number)
    x = np.linspace(function['x_min'], function['x_max'], points)
    y = evaluate(x, function['function_family'], function['parameters'])
    position = (x - function['x_min']) / (function['x_max'] - function['x_min'])
    quality = y / function['estimated_maximum']
    return {
        'session_id': session_id, 'game_number': game_number, 'round_number': round_number,
        **function,
        'perspective': 'analyst reveal; not necessarily visible to participants',
        'curve': [dict(x_value=float(xi), objective_value=float(yi),
                       position_fraction=float(pi), quality_fraction=float(qi))
                  for xi, yi, pi, qi in zip(x, y, position, quality)],
    }


@app.get('/predict')
def predict(session_id: Session, game_number: Game, participant_id: PositiveInt,
            round_number: PositiveInt, after_step: PositiveInt):
    """Build an observed event prefix from PostgreSQL and predict its next action."""
    from sql_runtime import load_prefix, MissingRound, InvalidStep
    try:
        with psycopg.connect(**DB_SETTINGS) as conn:
            conn.isolation_level = psycopg.IsolationLevel.REPEATABLE_READ
            conn.read_only = True
            seq, meta = load_prefix(conn, (session_id,game_number,round_number,participant_id), after_step)
        from inference import get_predictor
        return get_predictor().predict((session_id,game_number,round_number,participant_id),after_step,seq,meta)
    except MissingRound as exc:
        raise HTTPException(status_code=404,detail=str(exc))
    except InvalidStep as exc:
        raise HTTPException(status_code=422,detail=str(exc))
    except FileNotFoundError:
        raise HTTPException(status_code=503,detail='Missing original model weights or results in models/.')
    except ImportError:
        raise HTTPException(status_code=503,detail='Missing model/feature code or dependency. Check the update files.')
    except ValueError as exc:
        raise HTTPException(status_code=409,detail=str(exc))


if __name__ == '__main__':
    if DB_SETTINGS['password'] is None:
        DB_SETTINGS['password'] = getpass.getpass(f"PostgreSQL password for {DB_SETTINGS['user']}: ")
    try:
        fetch('SELECT 1')
    except psycopg.Error:
        raise SystemExit('Could not connect. Check PostgreSQL is running and the password/settings are correct.')
    # Loopback binding: this learning server is accessible on your PC only.
    uvicorn.run(app, host='127.0.0.1', port=8000)
