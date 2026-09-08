"""Add objective parameters to the existing decision_lab database.
Run python import_functions.py [--check-only]. Uses existing import_data.py.
Raw samples and existing participant-rounds are never modified.
"""
import argparse
import getpass
import math
import os
from pathlib import Path
import re

import pandas as pd
import psycopg
from psycopg.types.json import Jsonb
from import_data import SESSIONS
from objectives import estimate_maximum, MAXIMUM_METHOD

SCHEMA = '''CREATE TABLE IF NOT EXISTS round_functions (
 session_id TEXT NOT NULL REFERENCES experiment_sessions(session_id),
 game_number INTEGER NOT NULL CHECK (game_number BETWEEN 1 AND 4),
 round_number INTEGER NOT NULL CHECK (round_number > 0),
 function_family TEXT NOT NULL CHECK (function_family IN ('gaussian','cauchy')),
 parameters JSONB NOT NULL,
 estimated_maximum DOUBLE PRECISION NOT NULL CHECK (estimated_maximum > 0),
 maximum_method TEXT NOT NULL,
 PRIMARY KEY(session_id, game_number, round_number)
)'''


def read_functions(root):
    functions = []
    for session, (_, xmin, xmax, pattern) in SESSIONS.items():
        family = 'cauchy' if session == 'march6' else 'gaussian'
        for game in range(1, 5):
            matches = list(root.rglob(pattern.format(game)))
            if len(matches) != 1:
                raise ValueError(f'Expected one {pattern.format(game)}; found {len(matches)}')
            path = matches[0]
            df = pd.read_csv(path) if path.suffix == '.csv' else pd.read_excel(path)
            rounds = sorted(int(c.split('.')[1]) for c in df if re.fullmatch(rf'guess4{game}\.\d+\.player.samples', c))
            if not rounds:
                raise ValueError(f'No round columns: {path.name}')
            for rnd in rounds:
                prefix = f'guess4{game}.{rnd}.group.'
                names = [f'{letter}_{i}' for letter in 'abc' for i in range(1, 4)]
                values = df[[prefix + name for name in names]].dropna(how='all')
                if values.empty or values.isna().any().any() or len(values.drop_duplicates()) != 1:
                    raise ValueError(f'Missing/conflicting function parameters: {session}/{game}/{rnd}')
                params = dict(zip(names, map(float, values.iloc[0])))
                if not all(math.isfinite(v) for v in params.values()):
                    raise ValueError('Nonfinite objective parameters')
                if family == 'cauchy' and any(params[f'c_{i}'] <= 0 for i in range(1,4)):
                    raise ValueError('Cauchy denominator must be positive')
                maximum = estimate_maximum(family, params, xmin, xmax)
                functions.append((session, game, rnd, family, params, maximum, MAXIMUM_METHOD))
            print(f'{session} game {game}: {len(rounds)} functions validated')
    print(f'TOTAL: {len(functions)} round functions')
    return functions


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--raw-dir', type=Path, default=Path(__file__).resolve().parent / 'data' / 'raw')
    parser.add_argument('--check-only', action='store_true')
    args = parser.parse_args()
    try:
        records = read_functions(args.raw_dir)
        if args.check_only:
            return
        password = os.getenv('PGPASSWORD')
        if password is None:
            password = getpass.getpass('PostgreSQL password: ')
        with psycopg.connect(host=os.getenv('PGHOST','localhost'), port=os.getenv('PGPORT','5432'),
                             dbname=os.getenv('PGDATABASE','decision_lab'), user=os.getenv('PGUSER','postgres'),
                             password=password, connect_timeout=5) as conn:
            with conn.cursor() as cur:
                cur.execute(SCHEMA)
                cur.execute('SELECT pg_advisory_xact_lock(20260908)')
                for session, (date, xmin, xmax, _) in SESSIONS.items():
                    cur.execute('SELECT session_date::text, x_min, x_max FROM experiment_sessions WHERE session_id=%s', (session,))
                    if cur.fetchone() != (date, xmin, xmax):
                        raise ValueError(f'Session metadata missing/different: {session}. Check the original import.')
                added = unchanged = 0
                for record in records:
                    cur.execute('''SELECT function_family, parameters, estimated_maximum, maximum_method
                                   FROM round_functions WHERE session_id=%s AND game_number=%s AND round_number=%s''', record[:3])
                    existing = cur.fetchone()
                    if existing:
                        if existing != record[3:]:
                            raise ValueError(f'Existing function differs: {record[:3]}; refusing to overwrite.')
                        unchanged += 1
                    else:
                        cur.execute('INSERT INTO round_functions VALUES (%s,%s,%s,%s,%s,%s,%s)',
                                    record[:4] + (Jsonb(record[4]),) + record[5:])
                        added += 1
        print(f'COMMITTED: {added} new round functions; {unchanged} identical functions already present.')
    except Exception as exc:
        print(f'ERROR: {exc}\nThis run did not commit any database changes.')
        raise SystemExit(1)


if __name__ == '__main__':
    main()
