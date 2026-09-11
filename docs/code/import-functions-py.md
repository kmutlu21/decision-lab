# import_functions.py

Imports each round’s objective family, parameters and numerical normalization maximum without altering observed samples.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Symbols

| Symbol | Lines |
|---|---|
| `read_functions` | 30-58 |
| `main` | 61-99 |

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1-16 | Imports data-reading/validation tools, session filename conventions and the shared objective evaluator's maximum estimator. |
| 18-27 | Defines round_functions keyed by session/game/round, with a constrained family, JSONB parameter map and positive maximum. |
| 30-40 | Reads each expected export and assigns March to cauchy, February to gaussian; discovers numeric round columns. |
| 41-50 | Extracts all nine a_i/b_i/c_i coefficients. All populated group rows must agree and contain finite values. |
| 51-55 | Requires positive Cauchy denominators, estimates the round maximum and records the method identifier with the parameters. |
| 56-58 | Reports validated function counts and returns records. This phase has no database writes. |
| 61-69 | Parses raw-dir/check-only, reads functions and exits early for validation-only use. |
| 70-78 | Gets the password, connects using PG environment settings, creates schema and obtains the shared importer lock. |
| 79-83 | Verifies existing session metadata matches the raw-file conventions before inserting any function data. |
| 84-91 | Checks existing function rows for exact equality and rejects a conflicting family, parameters, maximum or method. |
| 92-99 | Wraps parameters as Jsonb, inserts missing rows and commits only on successful completion; errors exit nonzero. |
| 102-103 | Guards script execution so other modules can import SCHEMA without launching an import job. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1-16 | Imports data-reading/validation tools, session filename conventions and the shared objective evaluator's maximum estimator. |
| 2 | 1-16 | Imports data-reading/validation tools, session filename conventions and the shared objective evaluator's maximum estimator. |
| 3 | 1-16 | Imports data-reading/validation tools, session filename conventions and the shared objective evaluator's maximum estimator. |
| 4 | 1-16 | Imports data-reading/validation tools, session filename conventions and the shared objective evaluator's maximum estimator. |
| 5 | 1-16 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 6 | 1-16 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 7 | 1-16 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 8 | 1-16 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 9 | 1-16 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 10 | 1-16 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 11 | 1-16 | Blank separator; no execution. |
| 12 | 1-16 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 13 | 1-16 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 14 | 1-16 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 15 | 1-16 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 16 | 1-16 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 17 | 17 | Blank separator; no execution. |
| 18 | 18-27 | Defines round_functions keyed by session/game/round, with a constrained family, JSONB parameter map and positive maximum. |
| 19 | 18-27 | Defines round_functions keyed by session/game/round, with a constrained family, JSONB parameter map and positive maximum. |
| 20 | 18-27 | Defines round_functions keyed by session/game/round, with a constrained family, JSONB parameter map and positive maximum. |
| 21 | 18-27 | Defines round_functions keyed by session/game/round, with a constrained family, JSONB parameter map and positive maximum. |
| 22 | 18-27 | Defines round_functions keyed by session/game/round, with a constrained family, JSONB parameter map and positive maximum. |
| 23 | 18-27 | Defines round_functions keyed by session/game/round, with a constrained family, JSONB parameter map and positive maximum. |
| 24 | 18-27 | Defines round_functions keyed by session/game/round, with a constrained family, JSONB parameter map and positive maximum. |
| 25 | 18-27 | Defines round_functions keyed by session/game/round, with a constrained family, JSONB parameter map and positive maximum. |
| 26 | 18-27 | Defines round_functions keyed by session/game/round, with a constrained family, JSONB parameter map and positive maximum. |
| 27 | 18-27 | Defines round_functions keyed by session/game/round, with a constrained family, JSONB parameter map and positive maximum. |
| 28 | 28 | Blank separator; no execution. |
| 29 | 29 | Blank separator; no execution. |
| 30 | 30-40 | Function declaration: this body runs when called, not at declaration time. |
| 31 | 30-40 | Reads each expected export and assigns March to cauchy, February to gaussian; discovers numeric round columns. |
| 32 | 30-40 | Loop: repeats the following operations for the stated elements/condition. |
| 33 | 30-40 | Reads each expected export and assigns March to cauchy, February to gaussian; discovers numeric round columns. |
| 34 | 30-40 | Loop: repeats the following operations for the stated elements/condition. |
| 35 | 30-40 | Reads each expected export and assigns March to cauchy, February to gaussian; discovers numeric round columns. |
| 36 | 30-40 | Conditional branch: determines which following statements run. |
| 37 | 30-40 | Failure path: interrupts normal execution with the stated exception. |
| 38 | 30-40 | Reads each expected export and assigns March to cauchy, February to gaussian; discovers numeric round columns. |
| 39 | 30-40 | Reads each expected export and assigns March to cauchy, February to gaussian; discovers numeric round columns. |
| 40 | 30-40 | Reads each expected export and assigns March to cauchy, February to gaussian; discovers numeric round columns. |
| 41 | 41-50 | Conditional branch: determines which following statements run. |
| 42 | 41-50 | Failure path: interrupts normal execution with the stated exception. |
| 43 | 41-50 | Loop: repeats the following operations for the stated elements/condition. |
| 44 | 41-50 | Extracts all nine a_i/b_i/c_i coefficients. All populated group rows must agree and contain finite values. |
| 45 | 41-50 | Extracts all nine a_i/b_i/c_i coefficients. All populated group rows must agree and contain finite values. |
| 46 | 41-50 | Extracts all nine a_i/b_i/c_i coefficients. All populated group rows must agree and contain finite values. |
| 47 | 41-50 | Conditional branch: determines which following statements run. |
| 48 | 41-50 | Failure path: interrupts normal execution with the stated exception. |
| 49 | 41-50 | Extracts all nine a_i/b_i/c_i coefficients. All populated group rows must agree and contain finite values. |
| 50 | 41-50 | Conditional branch: determines which following statements run. |
| 51 | 51-55 | Failure path: interrupts normal execution with the stated exception. |
| 52 | 51-55 | Conditional branch: determines which following statements run. |
| 53 | 51-55 | Failure path: interrupts normal execution with the stated exception. |
| 54 | 51-55 | Requires positive Cauchy denominators, estimates the round maximum and records the method identifier with the parameters. |
| 55 | 51-55 | Requires positive Cauchy denominators, estimates the round maximum and records the method identifier with the parameters. |
| 56 | 56-58 | Reports validated function counts and returns records. This phase has no database writes. |
| 57 | 56-58 | Reports validated function counts and returns records. This phase has no database writes. |
| 58 | 56-58 | Return: sends this result to the caller and ends this invocation. |
| 59 | 59 | Blank separator; no execution. |
| 60 | 60 | Blank separator; no execution. |
| 61 | 61-69 | Function declaration: this body runs when called, not at declaration time. |
| 62 | 61-69 | Parses raw-dir/check-only, reads functions and exits early for validation-only use. |
| 63 | 61-69 | Parses raw-dir/check-only, reads functions and exits early for validation-only use. |
| 64 | 61-69 | Parses raw-dir/check-only, reads functions and exits early for validation-only use. |
| 65 | 61-69 | Parses raw-dir/check-only, reads functions and exits early for validation-only use. |
| 66 | 61-69 | Exception-control block: separates normal work, error handling and cleanup. |
| 67 | 61-69 | Parses raw-dir/check-only, reads functions and exits early for validation-only use. |
| 68 | 61-69 | Conditional branch: determines which following statements run. |
| 69 | 61-69 | Parses raw-dir/check-only, reads functions and exits early for validation-only use. |
| 70 | 70-78 | Gets the password, connects using PG environment settings, creates schema and obtains the shared importer lock. |
| 71 | 70-78 | Conditional branch: determines which following statements run. |
| 72 | 70-78 | Gets the password, connects using PG environment settings, creates schema and obtains the shared importer lock. |
| 73 | 70-78 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 74 | 70-78 | Gets the password, connects using PG environment settings, creates schema and obtains the shared importer lock. |
| 75 | 70-78 | Gets the password, connects using PG environment settings, creates schema and obtains the shared importer lock. |
| 76 | 70-78 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 77 | 70-78 | Gets the password, connects using PG environment settings, creates schema and obtains the shared importer lock. |
| 78 | 70-78 | Gets the password, connects using PG environment settings, creates schema and obtains the shared importer lock. |
| 79 | 79-83 | Loop: repeats the following operations for the stated elements/condition. |
| 80 | 79-83 | Verifies existing session metadata matches the raw-file conventions before inserting any function data. |
| 81 | 79-83 | Conditional branch: determines which following statements run. |
| 82 | 79-83 | Failure path: interrupts normal execution with the stated exception. |
| 83 | 79-83 | Verifies existing session metadata matches the raw-file conventions before inserting any function data. |
| 84 | 84-91 | Loop: repeats the following operations for the stated elements/condition. |
| 85 | 84-91 | Checks existing function rows for exact equality and rejects a conflicting family, parameters, maximum or method. |
| 86 | 84-91 | Checks existing function rows for exact equality and rejects a conflicting family, parameters, maximum or method. |
| 87 | 84-91 | Checks existing function rows for exact equality and rejects a conflicting family, parameters, maximum or method. |
| 88 | 84-91 | Conditional branch: determines which following statements run. |
| 89 | 84-91 | Conditional branch: determines which following statements run. |
| 90 | 84-91 | Failure path: interrupts normal execution with the stated exception. |
| 91 | 84-91 | Checks existing function rows for exact equality and rejects a conflicting family, parameters, maximum or method. |
| 92 | 92-99 | Conditional branch: determines which following statements run. |
| 93 | 92-99 | Wraps parameters as Jsonb, inserts missing rows and commits only on successful completion; errors exit nonzero. |
| 94 | 92-99 | Wraps parameters as Jsonb, inserts missing rows and commits only on successful completion; errors exit nonzero. |
| 95 | 92-99 | Wraps parameters as Jsonb, inserts missing rows and commits only on successful completion; errors exit nonzero. |
| 96 | 92-99 | Wraps parameters as Jsonb, inserts missing rows and commits only on successful completion; errors exit nonzero. |
| 97 | 92-99 | Exception-control block: separates normal work, error handling and cleanup. |
| 98 | 92-99 | Wraps parameters as Jsonb, inserts missing rows and commits only on successful completion; errors exit nonzero. |
| 99 | 92-99 | Failure path: interrupts normal execution with the stated exception. |
| 100 | 100 | Blank separator; no execution. |
| 101 | 101 | Blank separator; no execution. |
| 102 | 102-103 | Conditional branch: determines which following statements run. |
| 103 | 102-103 | Guards script execution so other modules can import SCHEMA without launching an import job. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  """Add objective parameters to the existing decision_lab database.
   2  Run python import_functions.py [--check-only]. Uses existing import_data.py.
   3  Raw samples and existing participant-rounds are never modified.
   4  """
   5  import argparse
   6  import getpass
   7  import math
   8  import os
   9  from pathlib import Path
  10  import re
  11  
  12  import pandas as pd
  13  import psycopg
  14  from psycopg.types.json import Jsonb
  15  from import_data import SESSIONS
  16  from objectives import estimate_maximum, MAXIMUM_METHOD
  17  
  18  SCHEMA = '''CREATE TABLE IF NOT EXISTS round_functions (
  19   session_id TEXT NOT NULL REFERENCES experiment_sessions(session_id),
  20   game_number INTEGER NOT NULL CHECK (game_number BETWEEN 1 AND 4),
  21   round_number INTEGER NOT NULL CHECK (round_number > 0),
  22   function_family TEXT NOT NULL CHECK (function_family IN ('gaussian','cauchy')),
  23   parameters JSONB NOT NULL,
  24   estimated_maximum DOUBLE PRECISION NOT NULL CHECK (estimated_maximum > 0),
  25   maximum_method TEXT NOT NULL,
  26   PRIMARY KEY(session_id, game_number, round_number)
  27  )'''
  28  
  29  
  30  def read_functions(root):
  31      functions = []
  32      for session, (_, xmin, xmax, pattern) in SESSIONS.items():
  33          family = 'cauchy' if session == 'march6' else 'gaussian'
  34          for game in range(1, 5):
  35              matches = list(root.rglob(pattern.format(game)))
  36              if len(matches) != 1:
  37                  raise ValueError(f'Expected one {pattern.format(game)}; found {len(matches)}')
  38              path = matches[0]
  39              df = pd.read_csv(path) if path.suffix == '.csv' else pd.read_excel(path)
  40              rounds = sorted(int(c.split('.')[1]) for c in df if re.fullmatch(rf'guess4{game}\.\d+\.player.samples', c))
  41              if not rounds:
  42                  raise ValueError(f'No round columns: {path.name}')
  43              for rnd in rounds:
  44                  prefix = f'guess4{game}.{rnd}.group.'
  45                  names = [f'{letter}_{i}' for letter in 'abc' for i in range(1, 4)]
  46                  values = df[[prefix + name for name in names]].dropna(how='all')
  47                  if values.empty or values.isna().any().any() or len(values.drop_duplicates()) != 1:
  48                      raise ValueError(f'Missing/conflicting function parameters: {session}/{game}/{rnd}')
  49                  params = dict(zip(names, map(float, values.iloc[0])))
  50                  if not all(math.isfinite(v) for v in params.values()):
  51                      raise ValueError('Nonfinite objective parameters')
  52                  if family == 'cauchy' and any(params[f'c_{i}'] <= 0 for i in range(1,4)):
  53                      raise ValueError('Cauchy denominator must be positive')
  54                  maximum = estimate_maximum(family, params, xmin, xmax)
  55                  functions.append((session, game, rnd, family, params, maximum, MAXIMUM_METHOD))
  56              print(f'{session} game {game}: {len(rounds)} functions validated')
  57      print(f'TOTAL: {len(functions)} round functions')
  58      return functions
  59  
  60  
  61  def main():
  62      parser = argparse.ArgumentParser(description=__doc__)
  63      parser.add_argument('--raw-dir', type=Path, default=Path(__file__).resolve().parent / 'data' / 'raw')
  64      parser.add_argument('--check-only', action='store_true')
  65      args = parser.parse_args()
  66      try:
  67          records = read_functions(args.raw_dir)
  68          if args.check_only:
  69              return
  70          password = os.getenv('PGPASSWORD')
  71          if password is None:
  72              password = getpass.getpass('PostgreSQL password: ')
  73          with psycopg.connect(host=os.getenv('PGHOST','localhost'), port=os.getenv('PGPORT','5432'),
  74                               dbname=os.getenv('PGDATABASE','decision_lab'), user=os.getenv('PGUSER','postgres'),
  75                               password=password, connect_timeout=5) as conn:
  76              with conn.cursor() as cur:
  77                  cur.execute(SCHEMA)
  78                  cur.execute('SELECT pg_advisory_xact_lock(20260908)')
  79                  for session, (date, xmin, xmax, _) in SESSIONS.items():
  80                      cur.execute('SELECT session_date::text, x_min, x_max FROM experiment_sessions WHERE session_id=%s', (session,))
  81                      if cur.fetchone() != (date, xmin, xmax):
  82                          raise ValueError(f'Session metadata missing/different: {session}. Check the original import.')
  83                  added = unchanged = 0
  84                  for record in records:
  85                      cur.execute('''SELECT function_family, parameters, estimated_maximum, maximum_method
  86                                     FROM round_functions WHERE session_id=%s AND game_number=%s AND round_number=%s''', record[:3])
  87                      existing = cur.fetchone()
  88                      if existing:
  89                          if existing != record[3:]:
  90                              raise ValueError(f'Existing function differs: {record[:3]}; refusing to overwrite.')
  91                          unchanged += 1
  92                      else:
  93                          cur.execute('INSERT INTO round_functions VALUES (%s,%s,%s,%s,%s,%s,%s)',
  94                                      record[:4] + (Jsonb(record[4]),) + record[5:])
  95                          added += 1
  96          print(f'COMMITTED: {added} new round functions; {unchanged} identical functions already present.')
  97      except Exception as exc:
  98          print(f'ERROR: {exc}\nThis run did not commit any database changes.')
  99          raise SystemExit(1)
 100  
 101  
 102  if __name__ == '__main__':
 103      main()
```
