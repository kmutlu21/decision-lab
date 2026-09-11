"""Read-only presentation routes. Does not change model inputs or artifacts."""
import json
from datetime import datetime
from typing import Annotated, Literal

from fastapi import HTTPException, Query

Session = Literal['feb18', 'feb20', 'march6']
Positive = Annotated[int, Query(ge=1)]
Game = Annotated[int, Query(ge=1, le=4)]
# Both recorded experimental versions use these costs. Payoffs are read,
# never recalculated from a formula that could differ between sessions.
RULES = {s: {'initial_tokens': 200, 'sample_cost': 10} for s in ('feb18', 'feb20', 'march6')}


def as_time(value):
    return datetime.fromisoformat(value) if isinstance(value, str) else value


def assemble_story(rows, focal, function, session_id, game_number, opponent_payload):
    """Return the permitted replay timeline, without rival locations or outcomes.

    Own events precede teammate events at identical timestamps, matching the
    original model's strict teammate cutoff. Historical future events are sent
    for playback, as in /samples; this is not an access-controlled live game.
    Opponent performance comes from the same saved export used by inference.
    """
    pid = focal['participant_id']
    eligible = [r for r in rows if r['participant_id'] == pid or
                (game_number in (2, 4) and r['group_id'] == focal['group_id'])]
    eligible.sort(key=lambda r: (as_time(r['sampled_at']), r['participant_id'] != pid,
                                 r['participant_id'], r['step_number']))
    rivals = []
    payload_ok = False
    if game_number in (3, 4) and opponent_payload:
        try:
            payload = json.loads(opponent_payload)
            rivals = sorted((as_time(s[2]), float(s[0]))
                            for values in payload.values() for s in values)
            payload_ok = True
        except (ValueError, TypeError, KeyError, AttributeError, IndexError):
            rivals = []
    first_own = min(as_time(r['sampled_at']) for r in eligible if r['participant_id'] == pid)
    events = []
    for r in eligible:
        t = as_time(r['sampled_at'])
        observed_rivals = [score for stamp, score in rivals if stamp <= t]
        events.append({
            'participant_id': r['participant_id'], 'step_number': r['step_number'],
            'role': 'own' if r['participant_id'] == pid else 'teammate',
            'sampled_at': t.isoformat(),
            'seconds_since_first_own_sample': (t - first_own).total_seconds(),
            'position_fraction': (r['x_value'] - function['x_min']) / (function['x_max'] - function['x_min']),
            'quality_fraction': r['observed_value'] / function['estimated_maximum'],
            'opponent_best_quality': max(observed_rivals) / function['estimated_maximum'] if observed_rivals else None,
        })
    return {'events': events, 'rules': RULES[session_id],
            'opponent_scores_available': payload_ok,
            'teammate_record_available': any(r['role'] == 'teammate' for r in events),
            'perspective': 'Historical replay with scenario-limited sharing; performance uses analyst normalization.'}


def assemble_results(rows, focal, function, session_id):
    rules = RULES[session_id]
    teams = []
    for group, label in ((focal['group_id'], 'Selected team'),
                         (focal['opponent_group_id'], 'Opposing team')):
        members = [r for r in rows if group is not None and r['group_id'] == group]
        flags = {bool(r['team_won']) for r in members if r['team_won'] is not None}
        won = next(iter(flags)) if len(flags) == 1 and all(r['team_won'] is not None for r in members) else None
        players = []
        for r in members:
            used = r['sample_count'] * rules['sample_cost']
            players.append({'participant_id': r['participant_id'],
                            'selected': r['participant_id'] == focal['participant_id'],
                            'samples': r['sample_count'], 'tokens_spent': used,
                            'tokens_remaining': rules['initial_tokens'] - used,
                            'best_quality': r['best_value'] / function['estimated_maximum'],
                            'recorded_payoff': r['recorded_payoff']})
        teams.append({'label': label, 'group_id': group, 'won': won, 'players': players})
    complete = all(len(t['players']) == 2 for t in teams)
    flags = [t['won'] for t in teams]
    consistent = complete and None not in flags and flags.count(True) == 1
    return {'teams': teams, 'complete': complete, 'outcome_consistent': consistent,
            'note': 'Final recorded outcomes. Remaining tokens and final payoff are different quantities. Empty rounds were not imported.'}


def register_replay_routes(app, fetch, get_function):
    def focal_for(session, game, pid, rnd):
        records = fetch('''SELECT participant_round_id, participant_id, group_id, opponent_group_id
                           FROM participant_rounds WHERE session_id=%s AND game_number=%s
                           AND participant_id=%s AND round_number=%s''', (session, game, pid, rnd))
        if not records:
            raise HTTPException(404, 'Recorded player-round not found.')
        return records[0]

    @app.get('/replay-story')
    def story(session_id: Session, game_number: Game, participant_id: Positive, round_number: Positive):
        focal = focal_for(session_id, game_number, participant_id, round_number)
        rows = fetch('''SELECT r.participant_id, r.group_id, s.step_number,
                              s.x_value, s.observed_value, s.sampled_at
                       FROM participant_rounds r JOIN samples s USING (participant_round_id)
                       WHERE r.session_id=%s AND r.game_number=%s AND r.round_number=%s
                         AND (r.participant_id=%s OR (%s AND r.group_id=%s))''',
                     (session_id, game_number, round_number, participant_id,
                      game_number in (2, 4), focal['group_id']))
        payload = None
        if game_number in (3, 4):
            context = fetch('SELECT opponent_results_data FROM model_context WHERE participant_round_id=%s',
                            (focal['participant_round_id'],))
            payload = context[0]['opponent_results_data'] if context else None
        return assemble_story(rows, focal, get_function(session_id, game_number, round_number),
                              session_id, game_number, payload)

    @app.get('/replay-results')
    def results(session_id: Session, game_number: Game, participant_id: Positive, round_number: Positive):
        focal = focal_for(session_id, game_number, participant_id, round_number)
        rows = fetch('''SELECT r.participant_id, r.group_id, r.team_won, r.recorded_payoff,
                              COUNT(s.sample_id) AS sample_count, MAX(s.observed_value) AS best_value
                       FROM participant_rounds r JOIN samples s USING (participant_round_id)
                       WHERE r.session_id=%s AND r.game_number=%s AND r.round_number=%s
                         AND (r.group_id=%s OR r.group_id=%s)
                       GROUP BY r.participant_round_id, r.participant_id, r.group_id, r.team_won, r.recorded_payoff
                       ORDER BY r.participant_id''',
                     (session_id, game_number, round_number, focal['group_id'], focal['opponent_group_id']))
        return assemble_results(rows, focal, get_function(session_id, game_number, round_number), session_id)
