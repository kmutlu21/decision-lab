# sql_runtime.py

Selects the exact request-time history visible at an own test and adapts it to the shared feature builder.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Symbols

| Symbol | Lines |
|---|---|
| `MissingRound` | 9-9 |
| `InvalidStep` | 10-10 |
| `make_prefix` | 13-32 |
| `load_prefix` | 35-80 |

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1-10 | Imports dataframe/SQL tools and defines missing-round and invalid-step exceptions consumed by main.py. json is unused in this file. |
| 13-17 | Converts returned SQL dictionaries to a DataFrame and timestamps to strings matching the research exports. |
| 18-22 | Explains why the whole stored opponent payload is retained. Only scores at/before each event are used, but nonempty-payload availability is a preserved historical caveat. |
| 23-26 | Builds previous-outcome lookup entries for participants in the prefix, dividing previous payoff by 200, and calls feature_math.build_sequences. |
| 27-32 | Selects the focal participant sequence and asserts exactly after_step own events with the final merged event being the requested own sample. |
| 35-46 | Looks up focal metadata and the requested own timestamp. LEFT JOIN permits informative missing-context/invalid-step errors rather than silently losing the record. |
| 47-52 | Distinguishes absent round, nonexistent step, absent import metadata and excluded model round. No held-out fold means replay is possible but prediction unavailable. |
| 53-60 | Selects normalized-feature source columns. Current payoff and is_win are explicit zero placeholders, not current-round outcome inputs. Opponent JSON appears only on step 1. |
| 61-64 | Joins samples, session bounds and model context for each included participant. |
| 65-70 | A lateral subquery gets that participant's latest earlier imported round within the same session/game. This is previous nonempty history, not necessarily round_number minus one. |
| 71-76 | Includes own rows only through the chosen step and timestamp. Includes teammate rows only in games 2/4 and strictly BEFORE the cutoff; never reads opponent x as a feature. |
| 77-80 | Returns rows and rebuilds features. The strict teammate timestamp rule preserves own-before-teammate ties; the caller establishes the transaction isolation level. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1-10 | Imports dataframe/SQL tools and defines missing-round and invalid-step exceptions consumed by main.py. json is unused in this file. |
| 2 | 1-10 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 3 | 1-10 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 4 | 1-10 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 5 | 1-10 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 6 | 1-10 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 7 | 1-10 | Blank separator; no execution. |
| 8 | 1-10 | Blank separator; no execution. |
| 9 | 1-10 | Class declaration: groups the following methods into a reusable type. |
| 10 | 1-10 | Class declaration: groups the following methods into a reusable type. |
| 11 | 11 | Blank separator; no execution. |
| 12 | 12 | Blank separator; no execution. |
| 13 | 13-17 | Function declaration: this body runs when called, not at declaration time. |
| 14 | 13-17 | Converts returned SQL dictionaries to a DataFrame and timestamps to strings matching the research exports. |
| 15 | 13-17 | Conditional branch: determines which following statements run. |
| 16 | 13-17 | Converts returned SQL dictionaries to a DataFrame and timestamps to strings matching the research exports. |
| 17 | 13-17 | Converts returned SQL dictionaries to a DataFrame and timestamps to strings matching the research exports. |
| 18 | 18-22 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 19 | 18-22 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 20 | 18-22 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 21 | 18-22 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 22 | 18-22 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 23 | 23-26 | Builds previous-outcome lookup entries for participants in the prefix, dividing previous payoff by 200, and calls feature_math.build_sequences. |
| 24 | 23-26 | Loop: repeats the following operations for the stated elements/condition. |
| 25 | 23-26 | Builds previous-outcome lookup entries for participants in the prefix, dividing previous payoff by 200, and calls feature_math.build_sequences. |
| 26 | 23-26 | Builds previous-outcome lookup entries for participants in the prefix, dividing previous payoff by 200, and calls feature_math.build_sequences. |
| 27 | 27-32 | Selects the focal participant sequence and asserts exactly after_step own events with the final merged event being the requested own sample. |
| 28 | 27-32 | Conditional branch: determines which following statements run. |
| 29 | 27-32 | Selects the focal participant sequence and asserts exactly after_step own events with the final merged event being the requested own sample. |
| 30 | 27-32 | Conditional branch: determines which following statements run. |
| 31 | 27-32 | Failure path: interrupts normal execution with the stated exception. |
| 32 | 27-32 | Return: sends this result to the caller and ends this invocation. |
| 33 | 33 | Blank separator; no execution. |
| 34 | 34 | Blank separator; no execution. |
| 35 | 35-46 | Function declaration: this body runs when called, not at declaration time. |
| 36 | 35-46 | Looks up focal metadata and the requested own timestamp. LEFT JOIN permits informative missing-context/invalid-step errors rather than silently losing the record. |
| 37 | 35-46 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 38 | 35-46 | Looks up focal metadata and the requested own timestamp. LEFT JOIN permits informative missing-context/invalid-step errors rather than silently losing the record. |
| 39 | 35-46 | Looks up focal metadata and the requested own timestamp. LEFT JOIN permits informative missing-context/invalid-step errors rather than silently losing the record. |
| 40 | 35-46 | Looks up focal metadata and the requested own timestamp. LEFT JOIN permits informative missing-context/invalid-step errors rather than silently losing the record. |
| 41 | 35-46 | Looks up focal metadata and the requested own timestamp. LEFT JOIN permits informative missing-context/invalid-step errors rather than silently losing the record. |
| 42 | 35-46 | Looks up focal metadata and the requested own timestamp. LEFT JOIN permits informative missing-context/invalid-step errors rather than silently losing the record. |
| 43 | 35-46 | Looks up focal metadata and the requested own timestamp. LEFT JOIN permits informative missing-context/invalid-step errors rather than silently losing the record. |
| 44 | 35-46 | Looks up focal metadata and the requested own timestamp. LEFT JOIN permits informative missing-context/invalid-step errors rather than silently losing the record. |
| 45 | 35-46 | Looks up focal metadata and the requested own timestamp. LEFT JOIN permits informative missing-context/invalid-step errors rather than silently losing the record. |
| 46 | 35-46 | Looks up focal metadata and the requested own timestamp. LEFT JOIN permits informative missing-context/invalid-step errors rather than silently losing the record. |
| 47 | 47-52 | Distinguishes absent round, nonexistent step, absent import metadata and excluded model round. No held-out fold means replay is possible but prediction unavailable. |
| 48 | 47-52 | Distinguishes absent round, nonexistent step, absent import metadata and excluded model round. No held-out fold means replay is possible but prediction unavailable. |
| 49 | 47-52 | Conditional branch: determines which following statements run. |
| 50 | 47-52 | Conditional branch: determines which following statements run. |
| 51 | 47-52 | Conditional branch: determines which following statements run. |
| 52 | 47-52 | Failure path: interrupts normal execution with the stated exception. |
| 53 | 53-60 | Conditional branch: determines which following statements run. |
| 54 | 53-60 | Selects normalized-feature source columns. Current payoff and is_win are explicit zero placeholders, not current-round outcome inputs. Opponent JSON appears only on step 1. |
| 55 | 53-60 | Selects normalized-feature source columns. Current payoff and is_win are explicit zero placeholders, not current-round outcome inputs. Opponent JSON appears only on step 1. |
| 56 | 53-60 | Selects normalized-feature source columns. Current payoff and is_win are explicit zero placeholders, not current-round outcome inputs. Opponent JSON appears only on step 1. |
| 57 | 53-60 | Selects normalized-feature source columns. Current payoff and is_win are explicit zero placeholders, not current-round outcome inputs. Opponent JSON appears only on step 1. |
| 58 | 53-60 | Selects normalized-feature source columns. Current payoff and is_win are explicit zero placeholders, not current-round outcome inputs. Opponent JSON appears only on step 1. |
| 59 | 53-60 | Selects normalized-feature source columns. Current payoff and is_win are explicit zero placeholders, not current-round outcome inputs. Opponent JSON appears only on step 1. |
| 60 | 53-60 | Selects normalized-feature source columns. Current payoff and is_win are explicit zero placeholders, not current-round outcome inputs. Opponent JSON appears only on step 1. |
| 61 | 61-64 | Joins samples, session bounds and model context for each included participant. |
| 62 | 61-64 | Joins samples, session bounds and model context for each included participant. |
| 63 | 61-64 | Joins samples, session bounds and model context for each included participant. |
| 64 | 61-64 | Joins samples, session bounds and model context for each included participant. |
| 65 | 65-70 | A lateral subquery gets that participant's latest earlier imported round within the same session/game. This is previous nonempty history, not necessarily round_number minus one. |
| 66 | 65-70 | A lateral subquery gets that participant's latest earlier imported round within the same session/game. This is previous nonempty history, not necessarily round_number minus one. |
| 67 | 65-70 | A lateral subquery gets that participant's latest earlier imported round within the same session/game. This is previous nonempty history, not necessarily round_number minus one. |
| 68 | 65-70 | A lateral subquery gets that participant's latest earlier imported round within the same session/game. This is previous nonempty history, not necessarily round_number minus one. |
| 69 | 65-70 | A lateral subquery gets that participant's latest earlier imported round within the same session/game. This is previous nonempty history, not necessarily round_number minus one. |
| 70 | 65-70 | A lateral subquery gets that participant's latest earlier imported round within the same session/game. This is previous nonempty history, not necessarily round_number minus one. |
| 71 | 71-76 | Includes own rows only through the chosen step and timestamp. Includes teammate rows only in games 2/4 and strictly BEFORE the cutoff; never reads opponent x as a feature. |
| 72 | 71-76 | Includes own rows only through the chosen step and timestamp. Includes teammate rows only in games 2/4 and strictly BEFORE the cutoff; never reads opponent x as a feature. |
| 73 | 71-76 | Includes own rows only through the chosen step and timestamp. Includes teammate rows only in games 2/4 and strictly BEFORE the cutoff; never reads opponent x as a feature. |
| 74 | 71-76 | Includes own rows only through the chosen step and timestamp. Includes teammate rows only in games 2/4 and strictly BEFORE the cutoff; never reads opponent x as a feature. |
| 75 | 71-76 | Includes own rows only through the chosen step and timestamp. Includes teammate rows only in games 2/4 and strictly BEFORE the cutoff; never reads opponent x as a feature. |
| 76 | 71-76 | Includes own rows only through the chosen step and timestamp. Includes teammate rows only in games 2/4 and strictly BEFORE the cutoff; never reads opponent x as a feature. |
| 77 | 77-80 | Returns rows and rebuilds features. The strict teammate timestamp rule preserves own-before-teammate ties; the caller establishes the transaction isolation level. |
| 78 | 77-80 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 79 | 77-80 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 80 | 77-80 | Return: sends this result to the caller and ends this invocation. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  """Read only the selected historical prefix and rebuild its model inputs."""
   2  import json
   3  import numpy as np
   4  import pandas as pd
   5  from psycopg.rows import dict_row
   6  from feature_math import build_sequences
   7  
   8  
   9  class MissingRound(Exception):pass
  10  class InvalidStep(Exception):pass
  11  
  12  
  13  def make_prefix(rows, meta, key, after_step):
  14      """Pure feature assembly, also used by the parity checker."""
  15      if not rows:raise ValueError('No events in selected prefix.')
  16      frame=pd.DataFrame(rows)
  17      frame['timestamp']=frame['timestamp'].map(lambda t:t.isoformat(sep=' ') if not isinstance(t,str) else t)
  18      # Keep the exported context payload intact. The original feature loop
  19      # considers the context available when its timeline is nonempty, even
  20      # before its first observation. It uses only values with time <= each
  21      # event. Dropping later entries here would incorrectly turn that early
  22      # competitor gap into zero. Preserve that historical availability rule.
  23      priors={}
  24      for _,row in frame.drop_duplicates('participant_id').iterrows():
  25          priors[(key[0],key[1],key[2],int(row['participant_id']))]=(float(row['prior_won']),float(row['prior_payoff'])/200)
  26      candidates=build_sequences(frame,{key[:3]:float(meta['estimated_maximum'])},priors)
  27      sequence=next((s for s in candidates if int(s['meta']['participant_id'])==key[3]),None)
  28      if sequence is None:raise ValueError('Focal sequence missing.')
  29      own=np.flatnonzero(sequence['features'][:,2]>.5)
  30      if len(own)!=after_step or own[-1]!=len(sequence['features'])-1:
  31          raise ValueError('Prefix does not end at the requested own event.')
  32      return sequence
  33  
  34  
  35  def load_prefix(conn,key,after_step):
  36      session,game,rnd,pid=key
  37      with conn.cursor(row_factory=dict_row) as cur:
  38          cur.execute('''
  39            SELECT r.participant_round_id,r.group_id,c.held_out_fold,c.source_cache_sha256,
  40                   f.estimated_maximum,e.x_min,e.x_max,s.sampled_at AS cutoff
  41            FROM participant_rounds r
  42            JOIN experiment_sessions e ON e.session_id=r.session_id
  43            LEFT JOIN model_context c ON c.participant_round_id=r.participant_round_id
  44            LEFT JOIN round_functions f ON f.session_id=r.session_id AND f.game_number=r.game_number AND f.round_number=r.round_number
  45            LEFT JOIN samples s ON s.participant_round_id=r.participant_round_id AND s.step_number=%s
  46            WHERE r.session_id=%s AND r.game_number=%s AND r.round_number=%s AND r.participant_id=%s
  47          ''',(after_step,session,game,rnd,pid))
  48          meta=cur.fetchone()
  49          if meta is None:raise MissingRound('Participant-round not found.')
  50          if meta['cutoff'] is None:raise InvalidStep('after_step exceeds the recorded sample count.')
  51          if meta['source_cache_sha256'] is None or meta['estimated_maximum'] is None:
  52              raise ValueError('Model context or objective maximum missing. Run the importers.')
  53          if meta['held_out_fold'] is None:return None,meta
  54          cur.execute('''
  55            SELECT r.session_id AS session,r.game_number AS game_num,r.round_number AS round,
  56                   r.participant_id,r.group_id AS record_group_id,COALESCE(r.opponent_group_id,-1) AS opponent_group_id,
  57                   0.0 AS payoff,0 AS is_win,e.x_min AS x_domain_min,e.x_max AS x_domain_max,
  58                   s.step_number AS step,s.x_value AS x,s.observed_value AS fx,s.sampled_at AS timestamp,
  59                   CASE WHEN s.step_number=1 THEN c.opponent_results_data ELSE NULL END AS opp_results_data,
  60                   COALESCE(prior.team_won,false)::integer AS prior_won,COALESCE(prior.recorded_payoff,0) AS prior_payoff
  61            FROM participant_rounds r
  62            JOIN samples s ON s.participant_round_id=r.participant_round_id
  63            JOIN experiment_sessions e ON e.session_id=r.session_id
  64            JOIN model_context c ON c.participant_round_id=r.participant_round_id
  65            LEFT JOIN LATERAL (
  66              SELECT p.team_won,p.recorded_payoff FROM participant_rounds p
  67              WHERE p.session_id=r.session_id AND p.game_number=r.game_number
  68                AND p.participant_id=r.participant_id AND p.round_number<r.round_number
  69              ORDER BY p.round_number DESC LIMIT 1
  70            ) prior ON true
  71            WHERE r.session_id=%s AND r.game_number=%s AND r.round_number=%s
  72              AND (r.participant_id=%s OR (%s AND r.group_id=%s))
  73              AND ((r.participant_id=%s AND s.step_number<=%s AND s.sampled_at<=%s)
  74                   OR (r.participant_id<>%s AND s.sampled_at<%s))
  75            ORDER BY r.participant_id,s.step_number
  76          ''',(session,game,rnd,pid,game in (2,4),meta['group_id'],pid,after_step,meta['cutoff'],pid,meta['cutoff']))
  77          rows=cur.fetchall()
  78      # Strict < for teammate cutoff implements the original own-before-mate
  79      # ordering when both sample timestamps are equal.
  80      return make_prefix(rows,meta,key,after_step),meta
```
