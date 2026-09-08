r"""Import the 12 original experiment exports into decision_lab.

Run from VS Code (Windows):
  .\.venv\Scripts\python.exe import_data.py --check-only
  .\.venv\Scripts\python.exe import_data.py

No model filtering/normalization is applied. Blank sequences are counted and
skipped; one-sample rounds are retained. Original files remain untouched.
Passwords are requested privately at runtime, never embedded in this script.
"""
import argparse
import ast
import getpass
import json
import math
from pathlib import Path
import re

import pandas as pd

SESSIONS = {
    'feb18': ('2026-02-18', 0, 100, 'all_apps_wide-2026-02-18-{}.csv'),
    'feb20': ('2026-02-20', 0, 100, 'all_apps_wide-2026-02-20-{}.csv'),
    'march6': ('2025-03-06', -20, 20, 'Game {}.xlsx'),
}
SCHEMA = """
CREATE TABLE IF NOT EXISTS experiment_sessions (
 session_id TEXT PRIMARY KEY, session_date DATE NOT NULL,
 x_min DOUBLE PRECISION NOT NULL, x_max DOUBLE PRECISION NOT NULL,
 CHECK (x_max > x_min));
CREATE TABLE IF NOT EXISTS participant_rounds (
 participant_round_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 session_id TEXT NOT NULL REFERENCES experiment_sessions(session_id),
 participant_id INTEGER NOT NULL,
 game_number INTEGER NOT NULL CHECK(game_number BETWEEN 1 AND 4),
 round_number INTEGER NOT NULL CHECK(round_number > 0),
 group_id INTEGER, opponent_group_id INTEGER,
 recorded_payoff DOUBLE PRECISION, team_won BOOLEAN,
 UNIQUE(session_id, participant_id, game_number, round_number));
CREATE TABLE IF NOT EXISTS samples (
 sample_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
 participant_round_id BIGINT NOT NULL REFERENCES participant_rounds(participant_round_id),
 step_number INTEGER NOT NULL CHECK(step_number > 0),
 x_value DOUBLE PRECISION NOT NULL, observed_value DOUBLE PRECISION NOT NULL,
 sampled_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
 UNIQUE(participant_round_id, step_number));
"""


def number(value):
    if value is None or pd.isna(value):
        return None
    result = float(value)
    if not math.isfinite(result):
        raise ValueError(f'Non-finite number: {value}')
    return result


def integer(value):
    result = number(value)
    if result is None or result != int(result):
        raise ValueError(f'Expected an integer, got {value}')
    return int(result)


def sequence(value):
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return []
    if isinstance(value, str):
        if not value.strip():
            return []
        try:
            value = json.loads(value)
        except json.JSONDecodeError:
            value = ast.literal_eval(value)
    if not isinstance(value, (list, tuple)):
        raise ValueError('Expected a list of records')
    return value


def read_exports(root):
    records, seen = [], set()
    total_empty = 0
    for session, (_, xmin, xmax, pattern) in SESSIONS.items():
        for game in range(1, 5):
            matches = list(root.rglob(pattern.format(game)))
            if len(matches) != 1:
                raise ValueError(f'Expected exactly one {pattern.format(game)}; found {len(matches)}')
            path = matches[0]
            df = pd.read_csv(path) if path.suffix == '.csv' else pd.read_excel(path)
            columns = sorted(
                (c for c in df.columns if re.fullmatch(rf'guess4{game}\.\d+\.player\.samples', c)),
                key=lambda c: int(c.split('.')[1]))
            if not columns:
                raise ValueError(f'No expected sample columns in {path.name}')
            nrounds = nsamples = empty = 0
            for column in columns:
                prefix = column.removesuffix('.player.samples')
                rnd = int(prefix.split('.')[1])
                opponents = {}
                for a, b in sequence(df[f'{prefix}.subsession.paired_groups'].iloc[0]):
                    opponents[integer(a)] = integer(b)
                    opponents[integer(b)] = integer(a)
                for _, row in df.iterrows():
                    # Excel exports can include entirely unused participant rows.
                    if pd.isna(row['participant.id_in_session']):
                        continue
                    raw_samples = sequence(row[column])
                    if not raw_samples:
                        empty += 1
                        continue
                    pid = integer(row['participant.id_in_session'])
                    gid = integer(row[f'{prefix}.player.record_group_id'])
                    key = (session, pid, game, rnd)
                    if key in seen:
                        raise ValueError(f'Duplicate participant-round: {key}')
                    seen.add(key)
                    payoff = number(row.get(f'{prefix}.player.payoff_float'))
                    fallback = number(row.get(f'{prefix}.player.payoff'))
                    # Match the existing default preprocessing script's fallback.
                    if payoff in (None, 0) and fallback is not None:
                        payoff = fallback
                    won = number(row.get(f'{prefix}.group.is_win'))
                    if won not in (None, 0, 1):
                        raise ValueError(f'Unexpected win flag: {key}')
                    events = []
                    for step, sample in enumerate(raw_samples, 1):
                        if len(sample) != 3:
                            raise ValueError(f'Expected [value, x, timestamp]: {key}, step {step}')
                        value, x, time = sample
                        x, value = number(x), number(value)
                        if x is None or value is None or not xmin <= x <= xmax:
                            raise ValueError(f'Invalid sample values: {key}, step {step}')
                        timestamp = pd.Timestamp(time)
                        if pd.isna(timestamp) or timestamp.tzinfo is not None:
                            raise ValueError(f'Missing/timezone-aware timestamp: {key}, step {step}')
                        timestamp = timestamp.to_pydatetime()
                        if events and timestamp < events[-1][3]:
                            raise ValueError(f'Sample timestamps out of order: {key}')
                        events.append((step, x, value, timestamp))
                    records.append((key, (gid, opponents.get(gid), payoff,
                                         None if won is None else bool(won)), events))
                    nrounds += 1
                    nsamples += len(events)
            total_empty += empty
            print(f'{session:7} game {game}: {nrounds:4} rounds, {nsamples:5} samples; {empty} empty sequences')
    print(f'TOTAL: {len(records):,} rounds; {sum(len(r[2]) for r in records):,} samples')
    print(f'Empty sequences skipped: {total_empty}. One-sample rounds retained.')
    return records


def import_records(records, args):
    import psycopg
    password = getpass.getpass(f'PostgreSQL password for {args.user}: ')
    # One transaction: either the entire import commits or none of it does.
    with psycopg.connect(host=args.host, port=args.port, dbname=args.database,
                         user=args.user, password=password, connect_timeout=10) as conn:
        with conn.cursor() as cur:
            cur.execute(SCHEMA)
            # Serialize concurrent runs of this importer.
            cur.execute('SELECT pg_advisory_xact_lock(20260908)')
            for session, (date, xmin, xmax, _) in SESSIONS.items():
                cur.execute('INSERT INTO experiment_sessions VALUES (%s,%s,%s,%s) ON CONFLICT DO NOTHING',
                            (session, date, xmin, xmax))
                cur.execute('SELECT session_date::text, x_min, x_max FROM experiment_sessions WHERE session_id=%s', (session,))
                if cur.fetchone() != (date, xmin, xmax):
                    raise ValueError(f'Existing session metadata differs: {session}')
            added = unchanged = 0
            for key, metadata, events in records:
                cur.execute('''SELECT participant_round_id, group_id, opponent_group_id,
                               recorded_payoff, team_won FROM participant_rounds
                               WHERE session_id=%s AND participant_id=%s AND game_number=%s AND round_number=%s''', key)
                existing = cur.fetchone()
                if existing:
                    round_id = existing[0]
                    cur.execute('''SELECT step_number, x_value, observed_value, sampled_at
                                   FROM samples WHERE participant_round_id=%s ORDER BY step_number''', (round_id,))
                    if tuple(existing[1:]) != metadata or cur.fetchall() != events:
                        raise ValueError(f'Existing data differs for {key}; refusing to overwrite it.')
                    unchanged += 1
                    continue
                cur.execute('''INSERT INTO participant_rounds
                    (session_id, participant_id, game_number, round_number,
                     group_id, opponent_group_id, recorded_payoff, team_won)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s) RETURNING participant_round_id''', key + metadata)
                round_id = cur.fetchone()[0]
                cur.executemany('''INSERT INTO samples
                    (participant_round_id, step_number, x_value, observed_value, sampled_at)
                    VALUES (%s,%s,%s,%s,%s)''', [(round_id,) + e for e in events])
                added += 1
    print(f'COMMITTED: {added:,} new rounds; {unchanged:,} identical rounds already present.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--raw-dir', type=Path, default=Path(__file__).resolve().parent / 'data' / 'raw')
    parser.add_argument('--check-only', action='store_true', help='Validate files without connecting to PostgreSQL')
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', type=int, default=5432)
    parser.add_argument('--database', default='decision_lab')
    parser.add_argument('--user', default='postgres')
    args = parser.parse_args()
    try:
        records = read_exports(args.raw_dir)
        if args.check_only:
            print('Validation complete. No database changes made.')
        else:
            import_records(records, args)
    except Exception as exc:
        print(f'ERROR: {exc}')
        print('This run did not commit any database changes.')
        raise SystemExit(1)


if __name__ == '__main__':
    main()
