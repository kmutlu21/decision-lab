# ci/smoke_test.py

Seeds an isolated synthetic PostgreSQL database and runs five HTTP integration tests without private data or trained weights.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Symbols

| Symbol | Lines |
|---|---|
| `seed` | 23-57 |
| `request` | 60-66 |
| `ApiChecks` | 69-119 |
| `get_json` | 70-73 |
| `test_health_and_home` | 75-79 |
| `test_session_counts_and_rounds` | 81-88 |
| `test_prefix_normalization_and_running_best` | 90-102 |
| `test_both_objective_families` | 104-111 |
| `test_invalid_and_missing_requests` | 113-119 |

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1-20 | Imports standard HTTP/unittest tools, exposes /app on Python's path and imports only the two schema definitions, not importer execution. |
| 23-31 | Requires the CI database name, creates schema and refuses to seed if sessions already exist. No research data is deleted to make room. |
| 32-40 | Creates one synthetic player-round each for February and March with their different domains and objective families. |
| 41-49 | Creates simple functions with a known midpoint maximum of 10, making normalization checks analytically testable. |
| 50-57 | Inserts three known own samples at 0, 8 and 20 seconds. The middle sample is best, letting the test distinguish current from running best. |
| 60-66 | Makes an HTTP request, returns status/body for successes and HTTP errors, and closes both response types correctly. |
| 69-73 | Defines a unittest suite with a helper that checks status before decoding JSON. |
| 75-79 | Checks database health and that the home response contains HTML. It does not execute browser JavaScript. |
| 81-88 | Checks session counts and the participant-round menu against the fixture identities. |
| 90-102 | Checks own-prefix truncation, normalized positions, relative time and retention of the earlier best after a poorer final observation. |
| 104-111 | Checks both curve families across their exact domains and verifies the midpoint's known normalized maximum. |
| 113-119 | Checks validation errors (422) and missing historical records/functions (404). |
| 122-124 | Seeds first, then runs unittest. There are no /predict, /replay-story or /replay-results tests in this snapshot. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1-20 | Imports standard HTTP/unittest tools, exposes /app on Python's path and imports only the two schema definitions, not importer execution. |
| 2 | 1-20 | Blank separator; no execution. |
| 3 | 1-20 | Imports standard HTTP/unittest tools, exposes /app on Python's path and imports only the two schema definitions, not importer execution. |
| 4 | 1-20 | Imports standard HTTP/unittest tools, exposes /app on Python's path and imports only the two schema definitions, not importer execution. |
| 5 | 1-20 | Imports standard HTTP/unittest tools, exposes /app on Python's path and imports only the two schema definitions, not importer execution. |
| 6 | 1-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 7 | 1-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 8 | 1-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 9 | 1-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 10 | 1-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 11 | 1-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 12 | 1-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 13 | 1-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 14 | 1-20 | Blank separator; no execution. |
| 15 | 1-20 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 16 | 1-20 | Imports standard HTTP/unittest tools, exposes /app on Python's path and imports only the two schema definitions, not importer execution. |
| 17 | 1-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 18 | 1-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 19 | 1-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 20 | 1-20 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 21 | 21 | Blank separator; no execution. |
| 22 | 22 | Blank separator; no execution. |
| 23 | 23-31 | Function declaration: this body runs when called, not at declaration time. |
| 24 | 23-31 | Conditional branch: determines which following statements run. |
| 25 | 23-31 | Failure path: interrupts normal execution with the stated exception. |
| 26 | 23-31 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 27 | 23-31 | Requires the CI database name, creates schema and refuses to seed if sessions already exist. No research data is deleted to make room. |
| 28 | 23-31 | Requires the CI database name, creates schema and refuses to seed if sessions already exist. No research data is deleted to make room. |
| 29 | 23-31 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 30 | 23-31 | Conditional branch: determines which following statements run. |
| 31 | 23-31 | Failure path: interrupts normal execution with the stated exception. |
| 32 | 32-40 | Loop: repeats the following operations for the stated elements/condition. |
| 33 | 32-40 | Creates one synthetic player-round each for February and March with their different domains and objective families. |
| 34 | 32-40 | Creates one synthetic player-round each for February and March with their different domains and objective families. |
| 35 | 32-40 | Creates one synthetic player-round each for February and March with their different domains and objective families. |
| 36 | 32-40 | Creates one synthetic player-round each for February and March with their different domains and objective families. |
| 37 | 32-40 | Creates one synthetic player-round each for February and March with their different domains and objective families. |
| 38 | 32-40 | Creates one synthetic player-round each for February and March with their different domains and objective families. |
| 39 | 32-40 | Creates one synthetic player-round each for February and March with their different domains and objective families. |
| 40 | 32-40 | Creates one synthetic player-round each for February and March with their different domains and objective families. |
| 41 | 41-49 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 42 | 41-49 | Creates simple functions with a known midpoint maximum of 10, making normalization checks analytically testable. |
| 43 | 41-49 | Creates simple functions with a known midpoint maximum of 10, making normalization checks analytically testable. |
| 44 | 41-49 | Loop: repeats the following operations for the stated elements/condition. |
| 45 | 41-49 | Creates simple functions with a known midpoint maximum of 10, making normalization checks analytically testable. |
| 46 | 41-49 | Creates simple functions with a known midpoint maximum of 10, making normalization checks analytically testable. |
| 47 | 41-49 | Creates simple functions with a known midpoint maximum of 10, making normalization checks analytically testable. |
| 48 | 41-49 | Creates simple functions with a known midpoint maximum of 10, making normalization checks analytically testable. |
| 49 | 41-49 | Creates simple functions with a known midpoint maximum of 10, making normalization checks analytically testable. |
| 50 | 50-57 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 51 | 50-57 | Loop: repeats the following operations for the stated elements/condition. |
| 52 | 50-57 | Inserts three known own samples at 0, 8 and 20 seconds. The middle sample is best, letting the test distinguish current from running best. |
| 53 | 50-57 | Inserts three known own samples at 0, 8 and 20 seconds. The middle sample is best, letting the test distinguish current from running best. |
| 54 | 50-57 | Inserts three known own samples at 0, 8 and 20 seconds. The middle sample is best, letting the test distinguish current from running best. |
| 55 | 50-57 | Inserts three known own samples at 0, 8 and 20 seconds. The middle sample is best, letting the test distinguish current from running best. |
| 56 | 50-57 | Inserts three known own samples at 0, 8 and 20 seconds. The middle sample is best, letting the test distinguish current from running best. |
| 57 | 50-57 | Inserts three known own samples at 0, 8 and 20 seconds. The middle sample is best, letting the test distinguish current from running best. |
| 58 | 58 | Blank separator; no execution. |
| 59 | 59 | Blank separator; no execution. |
| 60 | 60-66 | Function declaration: this body runs when called, not at declaration time. |
| 61 | 60-66 | Exception-control block: separates normal work, error handling and cleanup. |
| 62 | 60-66 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 63 | 60-66 | Return: sends this result to the caller and ends this invocation. |
| 64 | 60-66 | Exception-control block: separates normal work, error handling and cleanup. |
| 65 | 60-66 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 66 | 60-66 | Return: sends this result to the caller and ends this invocation. |
| 67 | 67 | Blank separator; no execution. |
| 68 | 68 | Blank separator; no execution. |
| 69 | 69-73 | Class declaration: groups the following methods into a reusable type. |
| 70 | 69-73 | Function declaration: this body runs when called, not at declaration time. |
| 71 | 69-73 | Defines a unittest suite with a helper that checks status before decoding JSON. |
| 72 | 69-73 | Defines a unittest suite with a helper that checks status before decoding JSON. |
| 73 | 69-73 | Return: sends this result to the caller and ends this invocation. |
| 74 | 74 | Blank separator; no execution. |
| 75 | 75-79 | Function declaration: this body runs when called, not at declaration time. |
| 76 | 75-79 | Checks database health and that the home response contains HTML. It does not execute browser JavaScript. |
| 77 | 75-79 | Checks database health and that the home response contains HTML. It does not execute browser JavaScript. |
| 78 | 75-79 | Checks database health and that the home response contains HTML. It does not execute browser JavaScript. |
| 79 | 75-79 | Checks database health and that the home response contains HTML. It does not execute browser JavaScript. |
| 80 | 80 | Blank separator; no execution. |
| 81 | 81-88 | Function declaration: this body runs when called, not at declaration time. |
| 82 | 81-88 | Checks session counts and the participant-round menu against the fixture identities. |
| 83 | 81-88 | Checks session counts and the participant-round menu against the fixture identities. |
| 84 | 81-88 | Loop: repeats the following operations for the stated elements/condition. |
| 85 | 81-88 | Checks session counts and the participant-round menu against the fixture identities. |
| 86 | 81-88 | Checks session counts and the participant-round menu against the fixture identities. |
| 87 | 81-88 | Checks session counts and the participant-round menu against the fixture identities. |
| 88 | 81-88 | Checks session counts and the participant-round menu against the fixture identities. |
| 89 | 89 | Blank separator; no execution. |
| 90 | 90-102 | Function declaration: this body runs when called, not at declaration time. |
| 91 | 90-102 | Loop: repeats the following operations for the stated elements/condition. |
| 92 | 90-102 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 93 | 90-102 | Checks own-prefix truncation, normalized positions, relative time and retention of the earlier best after a poorer final observation. |
| 94 | 90-102 | Checks own-prefix truncation, normalized positions, relative time and retention of the earlier best after a poorer final observation. |
| 95 | 90-102 | Checks own-prefix truncation, normalized positions, relative time and retention of the earlier best after a poorer final observation. |
| 96 | 90-102 | Checks own-prefix truncation, normalized positions, relative time and retention of the earlier best after a poorer final observation. |
| 97 | 90-102 | Checks own-prefix truncation, normalized positions, relative time and retention of the earlier best after a poorer final observation. |
| 98 | 90-102 | Checks own-prefix truncation, normalized positions, relative time and retention of the earlier best after a poorer final observation. |
| 99 | 90-102 | Checks own-prefix truncation, normalized positions, relative time and retention of the earlier best after a poorer final observation. |
| 100 | 90-102 | Checks own-prefix truncation, normalized positions, relative time and retention of the earlier best after a poorer final observation. |
| 101 | 90-102 | Checks own-prefix truncation, normalized positions, relative time and retention of the earlier best after a poorer final observation. |
| 102 | 90-102 | Checks own-prefix truncation, normalized positions, relative time and retention of the earlier best after a poorer final observation. |
| 103 | 103 | Blank separator; no execution. |
| 104 | 104-111 | Function declaration: this body runs when called, not at declaration time. |
| 105 | 104-111 | Loop: repeats the following operations for the stated elements/condition. |
| 106 | 104-111 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 107 | 104-111 | Checks both curve families across their exact domains and verifies the midpoint's known normalized maximum. |
| 108 | 104-111 | Checks both curve families across their exact domains and verifies the midpoint's known normalized maximum. |
| 109 | 104-111 | Checks both curve families across their exact domains and verifies the midpoint's known normalized maximum. |
| 110 | 104-111 | Checks both curve families across their exact domains and verifies the midpoint's known normalized maximum. |
| 111 | 104-111 | Checks both curve families across their exact domains and verifies the midpoint's known normalized maximum. |
| 112 | 112 | Blank separator; no execution. |
| 113 | 113-119 | Function declaration: this body runs when called, not at declaration time. |
| 114 | 113-119 | Loop: repeats the following operations for the stated elements/condition. |
| 115 | 113-119 | Checks validation errors (422) and missing historical records/functions (404). |
| 116 | 113-119 | Checks validation errors (422) and missing historical records/functions (404). |
| 117 | 113-119 | Checks validation errors (422) and missing historical records/functions (404). |
| 118 | 113-119 | Checks validation errors (422) and missing historical records/functions (404). |
| 119 | 113-119 | Checks validation errors (422) and missing historical records/functions (404). |
| 120 | 120 | Blank separator; no execution. |
| 121 | 121 | Blank separator; no execution. |
| 122 | 122-124 | Conditional branch: determines which following statements run. |
| 123 | 122-124 | Seeds first, then runs unittest. There are no /predict, /replay-story or /replay-results tests in this snapshot. |
| 124 | 122-124 | Seeds first, then runs unittest. There are no /predict, /replay-story or /replay-results tests in this snapshot. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  """HTTP integration checks against an isolated, disposable PostgreSQL database.
   2  
   3  Run through compose.ci.yaml. Never point this script at a research database.
   4  No original participant records or model checkpoints are required.
   5  """
   6  import json
   7  import math
   8  import os
   9  import sys
  10  import unittest
  11  from pathlib import Path
  12  from urllib.error import HTTPError
  13  from urllib.request import urlopen
  14  
  15  # This file is mounted outside /app in the built application image.
  16  sys.path.insert(0, str(Path('/app')))
  17  import psycopg
  18  from psycopg.types.json import Jsonb
  19  from import_data import SCHEMA as DATA_SCHEMA
  20  from import_functions import SCHEMA as FUNCTION_SCHEMA
  21  
  22  
  23  def seed():
  24      if os.environ.get('PGDATABASE') != 'decision_lab_ci':
  25          raise RuntimeError('Synthetic fixtures require the isolated decision_lab_ci database.')
  26      with psycopg.connect() as conn:
  27          conn.execute(DATA_SCHEMA)
  28          conn.execute(FUNCTION_SCHEMA)
  29          # Refuse to mix fixtures with any existing records; do not delete data.
  30          if conn.execute('SELECT COUNT(*) FROM experiment_sessions').fetchone()[0]:
  31              raise RuntimeError('CI database must be empty. Recreate the isolated CI stack.')
  32          for session, date, low, high, family in [
  33              ('feb18', '2026-02-18', 0, 100, 'gaussian'),
  34              ('march6', '2025-03-06', -20, 20, 'cauchy'),
  35          ]:
  36              conn.execute('INSERT INTO experiment_sessions VALUES (%s,%s,%s,%s)',
  37                           (session, date, low, high))
  38              rid = conn.execute('''INSERT INTO participant_rounds
  39                  (session_id, participant_id, game_number, round_number)
  40                  VALUES (%s,1,1,1) RETURNING participant_round_id''', (session,)).fetchone()[0]
  41              # Both analytical functions peak at 10 at the design-space midpoint.
  42              center = (low + high) / 2
  43              params = {}
  44              for i in range(1, 4):
  45                  params[f'a_{i}'] = 10 if i == 1 else 0
  46                  params[f'b_{i}'] = .01 if family == 'gaussian' else center
  47                  params[f'c_{i}'] = center if family == 'gaussian' else 1
  48              conn.execute('INSERT INTO round_functions VALUES (%s,1,1,%s,%s,10,%s)',
  49                           (session, family, Jsonb(params), 'synthetic_analytic_maximum'))
  50              # Middle observation is best; final observation must not leak into a prefix.
  51              for step, fraction, seconds in [(1, .25, 0), (2, .5, 8), (3, .75, 20)]:
  52                  x = low + fraction * (high-low)
  53                  value = 10*math.exp(-.01*(x-center)**2) if family == 'gaussian' else 10/((x-center)**2+1)
  54                  conn.execute('''INSERT INTO samples
  55                      (participant_round_id,step_number,x_value,observed_value,sampled_at)
  56                      VALUES (%s,%s,%s,%s,TIMESTAMP '2026-01-01 12:00:00' + %s * INTERVAL '1 second')''',
  57                      (rid, step, x, value, seconds))
  58  
  59  
  60  def request(path):
  61      try:
  62          with urlopen(os.environ.get('API_URL', 'http://api:8000') + path, timeout=10) as response:
  63              return response.status, response.read().decode()
  64      except HTTPError as error:
  65          with error:
  66              return error.code, error.read().decode()
  67  
  68  
  69  class ApiChecks(unittest.TestCase):
  70      def get_json(self, path, status=200):
  71          code, body = request(path)
  72          self.assertEqual(code, status, body)
  73          return json.loads(body)
  74  
  75      def test_health_and_home(self):
  76          self.assertEqual(self.get_json('/health')['database'], 'connected')
  77          code, body = request('/')
  78          self.assertEqual(code, 200)
  79          self.assertIn('<html', body.lower())
  80  
  81      def test_session_counts_and_rounds(self):
  82          sessions = self.get_json('/sessions')
  83          self.assertEqual({s['session_id'] for s in sessions}, {'feb18', 'march6'})
  84          for row in sessions:
  85              self.assertEqual(row['participant_rounds'], 1)
  86              self.assertEqual(row['samples'], 3)
  87          rounds = self.get_json('/rounds?session_id=feb18&game_number=1')
  88          self.assertEqual(rounds, [{'participant_id': 1, 'round_number': 1, 'sample_count': 3}])
  89  
  90      def test_prefix_normalization_and_running_best(self):
  91          for session in ['feb18', 'march6']:
  92              with self.subTest(session=session):
  93                  query = f'/samples?session_id={session}&game_number=1&participant_id=1&round_number=1'
  94                  prefix = self.get_json(query + '&through_step=2')['samples']
  95                  self.assertEqual([p['step_number'] for p in prefix], [1, 2])
  96                  self.assertEqual([p['position_fraction'] for p in prefix], [.25, .5])
  97                  self.assertEqual([p['seconds_since_first_sample'] for p in prefix], [0, 8])
  98                  self.assertAlmostEqual(prefix[-1]['quality_fraction'], 1)
  99                  full = self.get_json(query)['samples']
 100                  self.assertLess(full[-1]['quality_fraction'], 1)
 101                  self.assertAlmostEqual(full[-1]['best_quality_fraction_so_far'], 1)
 102                  self.assertEqual(full[-1]['seconds_since_first_sample'], 20)
 103  
 104      def test_both_objective_families(self):
 105          for session, low, high in [('feb18', 0, 100), ('march6', -20, 20)]:
 106              with self.subTest(session=session):
 107                  curve = self.get_json(f'/landscape?session_id={session}&game_number=1&round_number=1&points=51')['curve']
 108                  self.assertEqual(len(curve), 51)
 109                  self.assertEqual(curve[0]['x_value'], low)
 110                  self.assertEqual(curve[-1]['x_value'], high)
 111                  self.assertAlmostEqual(curve[25]['quality_fraction'], 1)
 112  
 113      def test_invalid_and_missing_requests(self):
 114          for path in ['/rounds?session_id=invalid&game_number=1',
 115                       '/rounds?session_id=feb18&game_number=5',
 116                       '/samples?session_id=feb18&game_number=1&participant_id=1&round_number=1&through_step=0']:
 117              self.get_json(path, 422)
 118          self.get_json('/samples?session_id=feb18&game_number=1&participant_id=999&round_number=1', 404)
 119          self.get_json('/landscape?session_id=feb18&game_number=1&round_number=999', 404)
 120  
 121  
 122  if __name__ == '__main__':
 123      seed()
 124      unittest.main(verbosity=2)
```
