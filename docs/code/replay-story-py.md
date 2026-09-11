# replay_story.py

Adds presentation-only routes for permitted own/teammate replay and final team outcomes, reusing existing SQL/normalization helpers.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Symbols

| Symbol | Lines |
|---|---|
| `as_time` | 16-17 |
| `assemble_story` | 20-60 |
| `assemble_results` | 63-85 |
| `register_replay_routes` | 88-126 |
| `focal_for` | 89-95 |
| `story` | 98-113 |
| `results` | 116-126 |

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1-13 | Defines API validation types and display rules of 200 initial tokens and 10 per test. Recorded payoff is read rather than recomputed. |
| 16-17 | Accepts an existing datetime or parses an ISO timestamp string, allowing pure assembly functions to work with SQL rows or fixtures. |
| 20-26 | Documents the historical replay boundary: later events are sent for playback, so this route is not an access-controlled live game. |
| 27-31 | Filters to focal own events and same-team events only in games 2/4; sorts time first, focal player first on ties, then participant/step. |
| 32-42 | Parses scores from opponent payload only in games 3/4. It ignores opponent x; malformed supported cases yield an unavailable score timeline. |
| 43-48 | Finds first own timestamp and walks permitted events, collecting rival scores available at/before each event time. |
| 49-56 | Returns event role/identity, relative display time, normalized x/y and observed competitor best. A pre-first-own teammate event can have negative display seconds. |
| 57-60 | Returns rules and data-availability flags. With no observed rival scores, display uses None, unlike the model's zero-initialized score convention. |
| 63-70 | For each of the two recorded groups, gathers members and only infers a group win value from consistent nonmissing recorded flags. |
| 71-79 | Computes each player's spent/remaining tokens from sample count, normalizes their own best and returns recorded payoff unchanged. |
| 80-85 | Reports both teams, whether each has two imported players and whether exactly one team won. Missing rosters/outcome flags are explicit. |
| 88-95 | Registers closures using injected app/fetch/get_function. Resolves the focal participant-round or raises 404. |
| 97-106 | The story endpoint selects only own and permitted same-group events from SQL. |
| 107-113 | Optionally fetches opponent context and combines the rows with function normalization through assemble_story. |
| 115-126 | The results endpoint aggregates counts and best values for both groups and calls assemble_results. These queries use separate fetch connections, not one shared snapshot. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1-13 | Defines API validation types and display rules of 200 initial tokens and 10 per test. Recorded payoff is read rather than recomputed. |
| 2 | 1-13 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 3 | 1-13 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 4 | 1-13 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 5 | 1-13 | Blank separator; no execution. |
| 6 | 1-13 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 7 | 1-13 | Blank separator; no execution. |
| 8 | 1-13 | Defines API validation types and display rules of 200 initial tokens and 10 per test. Recorded payoff is read rather than recomputed. |
| 9 | 1-13 | Defines API validation types and display rules of 200 initial tokens and 10 per test. Recorded payoff is read rather than recomputed. |
| 10 | 1-13 | Defines API validation types and display rules of 200 initial tokens and 10 per test. Recorded payoff is read rather than recomputed. |
| 11 | 1-13 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 12 | 1-13 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 13 | 1-13 | Defines API validation types and display rules of 200 initial tokens and 10 per test. Recorded payoff is read rather than recomputed. |
| 14 | 14 | Blank separator; no execution. |
| 15 | 15 | Blank separator; no execution. |
| 16 | 16-17 | Function declaration: this body runs when called, not at declaration time. |
| 17 | 16-17 | Return: sends this result to the caller and ends this invocation. |
| 18 | 18 | Blank separator; no execution. |
| 19 | 19 | Blank separator; no execution. |
| 20 | 20-26 | Function declaration: this body runs when called, not at declaration time. |
| 21 | 20-26 | Documents the historical replay boundary: later events are sent for playback, so this route is not an access-controlled live game. |
| 22 | 20-26 | Blank separator; no execution. |
| 23 | 20-26 | Documents the historical replay boundary: later events are sent for playback, so this route is not an access-controlled live game. |
| 24 | 20-26 | Documents the historical replay boundary: later events are sent for playback, so this route is not an access-controlled live game. |
| 25 | 20-26 | Loop: repeats the following operations for the stated elements/condition. |
| 26 | 20-26 | Documents the historical replay boundary: later events are sent for playback, so this route is not an access-controlled live game. |
| 27 | 27-31 | Filters to focal own events and same-team events only in games 2/4; sorts time first, focal player first on ties, then participant/step. |
| 28 | 27-31 | Filters to focal own events and same-team events only in games 2/4; sorts time first, focal player first on ties, then participant/step. |
| 29 | 27-31 | Filters to focal own events and same-team events only in games 2/4; sorts time first, focal player first on ties, then participant/step. |
| 30 | 27-31 | Filters to focal own events and same-team events only in games 2/4; sorts time first, focal player first on ties, then participant/step. |
| 31 | 27-31 | Filters to focal own events and same-team events only in games 2/4; sorts time first, focal player first on ties, then participant/step. |
| 32 | 32-42 | Parses scores from opponent payload only in games 3/4. It ignores opponent x; malformed supported cases yield an unavailable score timeline. |
| 33 | 32-42 | Parses scores from opponent payload only in games 3/4. It ignores opponent x; malformed supported cases yield an unavailable score timeline. |
| 34 | 32-42 | Parses scores from opponent payload only in games 3/4. It ignores opponent x; malformed supported cases yield an unavailable score timeline. |
| 35 | 32-42 | Conditional branch: determines which following statements run. |
| 36 | 32-42 | Exception-control block: separates normal work, error handling and cleanup. |
| 37 | 32-42 | Parses scores from opponent payload only in games 3/4. It ignores opponent x; malformed supported cases yield an unavailable score timeline. |
| 38 | 32-42 | Parses scores from opponent payload only in games 3/4. It ignores opponent x; malformed supported cases yield an unavailable score timeline. |
| 39 | 32-42 | Loop: repeats the following operations for the stated elements/condition. |
| 40 | 32-42 | Parses scores from opponent payload only in games 3/4. It ignores opponent x; malformed supported cases yield an unavailable score timeline. |
| 41 | 32-42 | Exception-control block: separates normal work, error handling and cleanup. |
| 42 | 32-42 | Parses scores from opponent payload only in games 3/4. It ignores opponent x; malformed supported cases yield an unavailable score timeline. |
| 43 | 43-48 | Finds first own timestamp and walks permitted events, collecting rival scores available at/before each event time. |
| 44 | 43-48 | Finds first own timestamp and walks permitted events, collecting rival scores available at/before each event time. |
| 45 | 43-48 | Loop: repeats the following operations for the stated elements/condition. |
| 46 | 43-48 | Finds first own timestamp and walks permitted events, collecting rival scores available at/before each event time. |
| 47 | 43-48 | Finds first own timestamp and walks permitted events, collecting rival scores available at/before each event time. |
| 48 | 43-48 | Finds first own timestamp and walks permitted events, collecting rival scores available at/before each event time. |
| 49 | 49-56 | Returns event role/identity, relative display time, normalized x/y and observed competitor best. A pre-first-own teammate event can have negative display seconds. |
| 50 | 49-56 | Returns event role/identity, relative display time, normalized x/y and observed competitor best. A pre-first-own teammate event can have negative display seconds. |
| 51 | 49-56 | Returns event role/identity, relative display time, normalized x/y and observed competitor best. A pre-first-own teammate event can have negative display seconds. |
| 52 | 49-56 | Returns event role/identity, relative display time, normalized x/y and observed competitor best. A pre-first-own teammate event can have negative display seconds. |
| 53 | 49-56 | Returns event role/identity, relative display time, normalized x/y and observed competitor best. A pre-first-own teammate event can have negative display seconds. |
| 54 | 49-56 | Returns event role/identity, relative display time, normalized x/y and observed competitor best. A pre-first-own teammate event can have negative display seconds. |
| 55 | 49-56 | Returns event role/identity, relative display time, normalized x/y and observed competitor best. A pre-first-own teammate event can have negative display seconds. |
| 56 | 49-56 | Returns event role/identity, relative display time, normalized x/y and observed competitor best. A pre-first-own teammate event can have negative display seconds. |
| 57 | 57-60 | Return: sends this result to the caller and ends this invocation. |
| 58 | 57-60 | Returns rules and data-availability flags. With no observed rival scores, display uses None, unlike the model's zero-initialized score convention. |
| 59 | 57-60 | Returns rules and data-availability flags. With no observed rival scores, display uses None, unlike the model's zero-initialized score convention. |
| 60 | 57-60 | Returns rules and data-availability flags. With no observed rival scores, display uses None, unlike the model's zero-initialized score convention. |
| 61 | 61 | Blank separator; no execution. |
| 62 | 62 | Blank separator; no execution. |
| 63 | 63-70 | Function declaration: this body runs when called, not at declaration time. |
| 64 | 63-70 | For each of the two recorded groups, gathers members and only infers a group win value from consistent nonmissing recorded flags. |
| 65 | 63-70 | For each of the two recorded groups, gathers members and only infers a group win value from consistent nonmissing recorded flags. |
| 66 | 63-70 | Loop: repeats the following operations for the stated elements/condition. |
| 67 | 63-70 | For each of the two recorded groups, gathers members and only infers a group win value from consistent nonmissing recorded flags. |
| 68 | 63-70 | For each of the two recorded groups, gathers members and only infers a group win value from consistent nonmissing recorded flags. |
| 69 | 63-70 | For each of the two recorded groups, gathers members and only infers a group win value from consistent nonmissing recorded flags. |
| 70 | 63-70 | For each of the two recorded groups, gathers members and only infers a group win value from consistent nonmissing recorded flags. |
| 71 | 71-79 | Computes each player's spent/remaining tokens from sample count, normalizes their own best and returns recorded payoff unchanged. |
| 72 | 71-79 | Loop: repeats the following operations for the stated elements/condition. |
| 73 | 71-79 | Computes each player's spent/remaining tokens from sample count, normalizes their own best and returns recorded payoff unchanged. |
| 74 | 71-79 | Computes each player's spent/remaining tokens from sample count, normalizes their own best and returns recorded payoff unchanged. |
| 75 | 71-79 | Computes each player's spent/remaining tokens from sample count, normalizes their own best and returns recorded payoff unchanged. |
| 76 | 71-79 | Computes each player's spent/remaining tokens from sample count, normalizes their own best and returns recorded payoff unchanged. |
| 77 | 71-79 | Computes each player's spent/remaining tokens from sample count, normalizes their own best and returns recorded payoff unchanged. |
| 78 | 71-79 | Computes each player's spent/remaining tokens from sample count, normalizes their own best and returns recorded payoff unchanged. |
| 79 | 71-79 | Computes each player's spent/remaining tokens from sample count, normalizes their own best and returns recorded payoff unchanged. |
| 80 | 80-85 | Reports both teams, whether each has two imported players and whether exactly one team won. Missing rosters/outcome flags are explicit. |
| 81 | 80-85 | Reports both teams, whether each has two imported players and whether exactly one team won. Missing rosters/outcome flags are explicit. |
| 82 | 80-85 | Reports both teams, whether each has two imported players and whether exactly one team won. Missing rosters/outcome flags are explicit. |
| 83 | 80-85 | Reports both teams, whether each has two imported players and whether exactly one team won. Missing rosters/outcome flags are explicit. |
| 84 | 80-85 | Return: sends this result to the caller and ends this invocation. |
| 85 | 80-85 | Reports both teams, whether each has two imported players and whether exactly one team won. Missing rosters/outcome flags are explicit. |
| 86 | 86 | Blank separator; no execution. |
| 87 | 87 | Blank separator; no execution. |
| 88 | 88-95 | Function declaration: this body runs when called, not at declaration time. |
| 89 | 88-95 | Function declaration: this body runs when called, not at declaration time. |
| 90 | 88-95 | Registers closures using injected app/fetch/get_function. Resolves the focal participant-round or raises 404. |
| 91 | 88-95 | Registers closures using injected app/fetch/get_function. Resolves the focal participant-round or raises 404. |
| 92 | 88-95 | Registers closures using injected app/fetch/get_function. Resolves the focal participant-round or raises 404. |
| 93 | 88-95 | Conditional branch: determines which following statements run. |
| 94 | 88-95 | Failure path: interrupts normal execution with the stated exception. |
| 95 | 88-95 | Return: sends this result to the caller and ends this invocation. |
| 96 | 96 | Blank separator; no execution. |
| 97 | 97-106 | Decorator: attaches registration/metadata to the following function. |
| 98 | 97-106 | Function declaration: this body runs when called, not at declaration time. |
| 99 | 97-106 | The story endpoint selects only own and permitted same-group events from SQL. |
| 100 | 97-106 | The story endpoint selects only own and permitted same-group events from SQL. |
| 101 | 97-106 | The story endpoint selects only own and permitted same-group events from SQL. |
| 102 | 97-106 | The story endpoint selects only own and permitted same-group events from SQL. |
| 103 | 97-106 | The story endpoint selects only own and permitted same-group events from SQL. |
| 104 | 97-106 | The story endpoint selects only own and permitted same-group events from SQL. |
| 105 | 97-106 | The story endpoint selects only own and permitted same-group events from SQL. |
| 106 | 97-106 | The story endpoint selects only own and permitted same-group events from SQL. |
| 107 | 107-113 | Optionally fetches opponent context and combines the rows with function normalization through assemble_story. |
| 108 | 107-113 | Conditional branch: determines which following statements run. |
| 109 | 107-113 | Optionally fetches opponent context and combines the rows with function normalization through assemble_story. |
| 110 | 107-113 | Optionally fetches opponent context and combines the rows with function normalization through assemble_story. |
| 111 | 107-113 | Optionally fetches opponent context and combines the rows with function normalization through assemble_story. |
| 112 | 107-113 | Return: sends this result to the caller and ends this invocation. |
| 113 | 107-113 | Optionally fetches opponent context and combines the rows with function normalization through assemble_story. |
| 114 | 114 | Blank separator; no execution. |
| 115 | 115-126 | Decorator: attaches registration/metadata to the following function. |
| 116 | 115-126 | Function declaration: this body runs when called, not at declaration time. |
| 117 | 115-126 | The results endpoint aggregates counts and best values for both groups and calls assemble_results. These queries use separate fetch connections, not one shared snapshot. |
| 118 | 115-126 | The results endpoint aggregates counts and best values for both groups and calls assemble_results. These queries use separate fetch connections, not one shared snapshot. |
| 119 | 115-126 | The results endpoint aggregates counts and best values for both groups and calls assemble_results. These queries use separate fetch connections, not one shared snapshot. |
| 120 | 115-126 | The results endpoint aggregates counts and best values for both groups and calls assemble_results. These queries use separate fetch connections, not one shared snapshot. |
| 121 | 115-126 | The results endpoint aggregates counts and best values for both groups and calls assemble_results. These queries use separate fetch connections, not one shared snapshot. |
| 122 | 115-126 | The results endpoint aggregates counts and best values for both groups and calls assemble_results. These queries use separate fetch connections, not one shared snapshot. |
| 123 | 115-126 | The results endpoint aggregates counts and best values for both groups and calls assemble_results. These queries use separate fetch connections, not one shared snapshot. |
| 124 | 115-126 | The results endpoint aggregates counts and best values for both groups and calls assemble_results. These queries use separate fetch connections, not one shared snapshot. |
| 125 | 115-126 | The results endpoint aggregates counts and best values for both groups and calls assemble_results. These queries use separate fetch connections, not one shared snapshot. |
| 126 | 115-126 | Return: sends this result to the caller and ends this invocation. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  """Read-only presentation routes. Does not change model inputs or artifacts."""
   2  import json
   3  from datetime import datetime
   4  from typing import Annotated, Literal
   5  
   6  from fastapi import HTTPException, Query
   7  
   8  Session = Literal['feb18', 'feb20', 'march6']
   9  Positive = Annotated[int, Query(ge=1)]
  10  Game = Annotated[int, Query(ge=1, le=4)]
  11  # Both recorded experimental versions use these costs. Payoffs are read,
  12  # never recalculated from a formula that could differ between sessions.
  13  RULES = {s: {'initial_tokens': 200, 'sample_cost': 10} for s in ('feb18', 'feb20', 'march6')}
  14  
  15  
  16  def as_time(value):
  17      return datetime.fromisoformat(value) if isinstance(value, str) else value
  18  
  19  
  20  def assemble_story(rows, focal, function, session_id, game_number, opponent_payload):
  21      """Return the permitted replay timeline, without rival locations or outcomes.
  22  
  23      Own events precede teammate events at identical timestamps, matching the
  24      original model's strict teammate cutoff. Historical future events are sent
  25      for playback, as in /samples; this is not an access-controlled live game.
  26      Opponent performance comes from the same saved export used by inference.
  27      """
  28      pid = focal['participant_id']
  29      eligible = [r for r in rows if r['participant_id'] == pid or
  30                  (game_number in (2, 4) and r['group_id'] == focal['group_id'])]
  31      eligible.sort(key=lambda r: (as_time(r['sampled_at']), r['participant_id'] != pid,
  32                                   r['participant_id'], r['step_number']))
  33      rivals = []
  34      payload_ok = False
  35      if game_number in (3, 4) and opponent_payload:
  36          try:
  37              payload = json.loads(opponent_payload)
  38              rivals = sorted((as_time(s[2]), float(s[0]))
  39                              for values in payload.values() for s in values)
  40              payload_ok = True
  41          except (ValueError, TypeError, KeyError, AttributeError, IndexError):
  42              rivals = []
  43      first_own = min(as_time(r['sampled_at']) for r in eligible if r['participant_id'] == pid)
  44      events = []
  45      for r in eligible:
  46          t = as_time(r['sampled_at'])
  47          observed_rivals = [score for stamp, score in rivals if stamp <= t]
  48          events.append({
  49              'participant_id': r['participant_id'], 'step_number': r['step_number'],
  50              'role': 'own' if r['participant_id'] == pid else 'teammate',
  51              'sampled_at': t.isoformat(),
  52              'seconds_since_first_own_sample': (t - first_own).total_seconds(),
  53              'position_fraction': (r['x_value'] - function['x_min']) / (function['x_max'] - function['x_min']),
  54              'quality_fraction': r['observed_value'] / function['estimated_maximum'],
  55              'opponent_best_quality': max(observed_rivals) / function['estimated_maximum'] if observed_rivals else None,
  56          })
  57      return {'events': events, 'rules': RULES[session_id],
  58              'opponent_scores_available': payload_ok,
  59              'teammate_record_available': any(r['role'] == 'teammate' for r in events),
  60              'perspective': 'Historical replay with scenario-limited sharing; performance uses analyst normalization.'}
  61  
  62  
  63  def assemble_results(rows, focal, function, session_id):
  64      rules = RULES[session_id]
  65      teams = []
  66      for group, label in ((focal['group_id'], 'Selected team'),
  67                           (focal['opponent_group_id'], 'Opposing team')):
  68          members = [r for r in rows if group is not None and r['group_id'] == group]
  69          flags = {bool(r['team_won']) for r in members if r['team_won'] is not None}
  70          won = next(iter(flags)) if len(flags) == 1 and all(r['team_won'] is not None for r in members) else None
  71          players = []
  72          for r in members:
  73              used = r['sample_count'] * rules['sample_cost']
  74              players.append({'participant_id': r['participant_id'],
  75                              'selected': r['participant_id'] == focal['participant_id'],
  76                              'samples': r['sample_count'], 'tokens_spent': used,
  77                              'tokens_remaining': rules['initial_tokens'] - used,
  78                              'best_quality': r['best_value'] / function['estimated_maximum'],
  79                              'recorded_payoff': r['recorded_payoff']})
  80          teams.append({'label': label, 'group_id': group, 'won': won, 'players': players})
  81      complete = all(len(t['players']) == 2 for t in teams)
  82      flags = [t['won'] for t in teams]
  83      consistent = complete and None not in flags and flags.count(True) == 1
  84      return {'teams': teams, 'complete': complete, 'outcome_consistent': consistent,
  85              'note': 'Final recorded outcomes. Remaining tokens and final payoff are different quantities. Empty rounds were not imported.'}
  86  
  87  
  88  def register_replay_routes(app, fetch, get_function):
  89      def focal_for(session, game, pid, rnd):
  90          records = fetch('''SELECT participant_round_id, participant_id, group_id, opponent_group_id
  91                             FROM participant_rounds WHERE session_id=%s AND game_number=%s
  92                             AND participant_id=%s AND round_number=%s''', (session, game, pid, rnd))
  93          if not records:
  94              raise HTTPException(404, 'Recorded player-round not found.')
  95          return records[0]
  96  
  97      @app.get('/replay-story')
  98      def story(session_id: Session, game_number: Game, participant_id: Positive, round_number: Positive):
  99          focal = focal_for(session_id, game_number, participant_id, round_number)
 100          rows = fetch('''SELECT r.participant_id, r.group_id, s.step_number,
 101                                s.x_value, s.observed_value, s.sampled_at
 102                         FROM participant_rounds r JOIN samples s USING (participant_round_id)
 103                         WHERE r.session_id=%s AND r.game_number=%s AND r.round_number=%s
 104                           AND (r.participant_id=%s OR (%s AND r.group_id=%s))''',
 105                       (session_id, game_number, round_number, participant_id,
 106                        game_number in (2, 4), focal['group_id']))
 107          payload = None
 108          if game_number in (3, 4):
 109              context = fetch('SELECT opponent_results_data FROM model_context WHERE participant_round_id=%s',
 110                              (focal['participant_round_id'],))
 111              payload = context[0]['opponent_results_data'] if context else None
 112          return assemble_story(rows, focal, get_function(session_id, game_number, round_number),
 113                                session_id, game_number, payload)
 114  
 115      @app.get('/replay-results')
 116      def results(session_id: Session, game_number: Game, participant_id: Positive, round_number: Positive):
 117          focal = focal_for(session_id, game_number, participant_id, round_number)
 118          rows = fetch('''SELECT r.participant_id, r.group_id, r.team_won, r.recorded_payoff,
 119                                COUNT(s.sample_id) AS sample_count, MAX(s.observed_value) AS best_value
 120                         FROM participant_rounds r JOIN samples s USING (participant_round_id)
 121                         WHERE r.session_id=%s AND r.game_number=%s AND r.round_number=%s
 122                           AND (r.group_id=%s OR r.group_id=%s)
 123                         GROUP BY r.participant_round_id, r.participant_id, r.group_id, r.team_won, r.recorded_payoff
 124                         ORDER BY r.participant_id''',
 125                       (session_id, game_number, round_number, focal['group_id'], focal['opponent_group_id']))
 126          return assemble_results(rows, focal, get_function(session_id, game_number, round_number), session_id)
```
