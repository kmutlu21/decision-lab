"""HTTP integration checks against an isolated, disposable PostgreSQL database.

Run through compose.ci.yaml. Never point this script at a research database.
No original participant records or model checkpoints are required.
"""
import json
import math
import os
import sys
import unittest
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import urlopen

# This file is mounted outside /app in the built application image.
sys.path.insert(0, str(Path('/app')))
import psycopg
from psycopg.types.json import Jsonb
from import_data import SCHEMA as DATA_SCHEMA
from import_functions import SCHEMA as FUNCTION_SCHEMA


def seed():
    if os.environ.get('PGDATABASE') != 'decision_lab_ci':
        raise RuntimeError('Synthetic fixtures require the isolated decision_lab_ci database.')
    with psycopg.connect() as conn:
        conn.execute(DATA_SCHEMA)
        conn.execute(FUNCTION_SCHEMA)
        # Refuse to mix fixtures with any existing records; do not delete data.
        if conn.execute('SELECT COUNT(*) FROM experiment_sessions').fetchone()[0]:
            raise RuntimeError('CI database must be empty. Recreate the isolated CI stack.')
        for session, date, low, high, family in [
            ('feb18', '2026-02-18', 0, 100, 'gaussian'),
            ('march6', '2025-03-06', -20, 20, 'cauchy'),
        ]:
            conn.execute('INSERT INTO experiment_sessions VALUES (%s,%s,%s,%s)',
                         (session, date, low, high))
            rid = conn.execute('''INSERT INTO participant_rounds
                (session_id, participant_id, game_number, round_number)
                VALUES (%s,1,1,1) RETURNING participant_round_id''', (session,)).fetchone()[0]
            # Both analytical functions peak at 10 at the design-space midpoint.
            center = (low + high) / 2
            params = {}
            for i in range(1, 4):
                params[f'a_{i}'] = 10 if i == 1 else 0
                params[f'b_{i}'] = .01 if family == 'gaussian' else center
                params[f'c_{i}'] = center if family == 'gaussian' else 1
            conn.execute('INSERT INTO round_functions VALUES (%s,1,1,%s,%s,10,%s)',
                         (session, family, Jsonb(params), 'synthetic_analytic_maximum'))
            # Middle observation is best; final observation must not leak into a prefix.
            for step, fraction, seconds in [(1, .25, 0), (2, .5, 8), (3, .75, 20)]:
                x = low + fraction * (high-low)
                value = 10*math.exp(-.01*(x-center)**2) if family == 'gaussian' else 10/((x-center)**2+1)
                conn.execute('''INSERT INTO samples
                    (participant_round_id,step_number,x_value,observed_value,sampled_at)
                    VALUES (%s,%s,%s,%s,TIMESTAMP '2026-01-01 12:00:00' + %s * INTERVAL '1 second')''',
                    (rid, step, x, value, seconds))


def request(path):
    try:
        with urlopen(os.environ.get('API_URL', 'http://api:8000') + path, timeout=10) as response:
            return response.status, response.read().decode()
    except HTTPError as error:
        with error:
            return error.code, error.read().decode()


class ApiChecks(unittest.TestCase):
    def get_json(self, path, status=200):
        code, body = request(path)
        self.assertEqual(code, status, body)
        return json.loads(body)

    def test_health_and_home(self):
        self.assertEqual(self.get_json('/health')['database'], 'connected')
        code, body = request('/')
        self.assertEqual(code, 200)
        self.assertIn('<html', body.lower())

    def test_session_counts_and_rounds(self):
        sessions = self.get_json('/sessions')
        self.assertEqual({s['session_id'] for s in sessions}, {'feb18', 'march6'})
        for row in sessions:
            self.assertEqual(row['participant_rounds'], 1)
            self.assertEqual(row['samples'], 3)
        rounds = self.get_json('/rounds?session_id=feb18&game_number=1')
        self.assertEqual(rounds, [{'participant_id': 1, 'round_number': 1, 'sample_count': 3}])

    def test_prefix_normalization_and_running_best(self):
        for session in ['feb18', 'march6']:
            with self.subTest(session=session):
                query = f'/samples?session_id={session}&game_number=1&participant_id=1&round_number=1'
                prefix = self.get_json(query + '&through_step=2')['samples']
                self.assertEqual([p['step_number'] for p in prefix], [1, 2])
                self.assertEqual([p['position_fraction'] for p in prefix], [.25, .5])
                self.assertEqual([p['seconds_since_first_sample'] for p in prefix], [0, 8])
                self.assertAlmostEqual(prefix[-1]['quality_fraction'], 1)
                full = self.get_json(query)['samples']
                self.assertLess(full[-1]['quality_fraction'], 1)
                self.assertAlmostEqual(full[-1]['best_quality_fraction_so_far'], 1)
                self.assertEqual(full[-1]['seconds_since_first_sample'], 20)

    def test_both_objective_families(self):
        for session, low, high in [('feb18', 0, 100), ('march6', -20, 20)]:
            with self.subTest(session=session):
                curve = self.get_json(f'/landscape?session_id={session}&game_number=1&round_number=1&points=51')['curve']
                self.assertEqual(len(curve), 51)
                self.assertEqual(curve[0]['x_value'], low)
                self.assertEqual(curve[-1]['x_value'], high)
                self.assertAlmostEqual(curve[25]['quality_fraction'], 1)

    def test_invalid_and_missing_requests(self):
        for path in ['/rounds?session_id=invalid&game_number=1',
                     '/rounds?session_id=feb18&game_number=5',
                     '/samples?session_id=feb18&game_number=1&participant_id=1&round_number=1&through_step=0']:
            self.get_json(path, 422)
        self.get_json('/samples?session_id=feb18&game_number=1&participant_id=999&round_number=1', 404)
        self.get_json('/landscape?session_id=feb18&game_number=1&round_number=999', 404)


if __name__ == '__main__':
    seed()
    unittest.main(verbosity=2)
