# sql_features.py

Rebuilds full historical sequences from PostgreSQL for parity verification. It is not the live /predict query path.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Symbols

| Symbol | Lines |
|---|---|
| `load_feature_inputs` | 9-54 |
| `rebuild_from_database` | 57-62 |

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1-6 | Imports the common feature builder so full reconstruction and request-time inference use identical feature mathematics. |
| 9-22 | Selects all stored own events with normalized-domain metadata, context and fold assignments. Here current outcomes are available as metadata for building prior-round lookups. |
| 23-32 | Joins the five database tables and orders rows consistently. Missing context/functions survive LEFT JOIN so validation can detect them. |
| 33-40 | Rejects empty or incomplete input, builds a DataFrame and formats timestamps like the original exports. |
| 41-47 | Builds one outcome per player-round, then shifts outcomes forward within each participant/session/game. First available rounds get zero priors. |
| 48-54 | Builds maximum and fold dictionaries and rejects conflicting nonnull folds for the same identity. Returns tabular input and metadata. |
| 57-62 | Builds every available sequence, indexes it by canonical key, and returns only keys with original held-out assignments plus the fold map. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1-6 | Imports the common feature builder so full reconstruction and request-time inference use identical feature mathematics. |
| 2 | 1-6 | Imports the common feature builder so full reconstruction and request-time inference use identical feature mathematics. |
| 3 | 1-6 | Imports the common feature builder so full reconstruction and request-time inference use identical feature mathematics. |
| 4 | 1-6 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 5 | 1-6 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 6 | 1-6 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 7 | 7 | Blank separator; no execution. |
| 8 | 8 | Blank separator; no execution. |
| 9 | 9-22 | Function declaration: this body runs when called, not at declaration time. |
| 10 | 9-22 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 11 | 9-22 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 12 | 9-22 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 13 | 9-22 | Selects all stored own events with normalized-domain metadata, context and fold assignments. Here current outcomes are available as metadata for building prior-round lookups. |
| 14 | 9-22 | Selects all stored own events with normalized-domain metadata, context and fold assignments. Here current outcomes are available as metadata for building prior-round lookups. |
| 15 | 9-22 | Selects all stored own events with normalized-domain metadata, context and fold assignments. Here current outcomes are available as metadata for building prior-round lookups. |
| 16 | 9-22 | Selects all stored own events with normalized-domain metadata, context and fold assignments. Here current outcomes are available as metadata for building prior-round lookups. |
| 17 | 9-22 | Selects all stored own events with normalized-domain metadata, context and fold assignments. Here current outcomes are available as metadata for building prior-round lookups. |
| 18 | 9-22 | Selects all stored own events with normalized-domain metadata, context and fold assignments. Here current outcomes are available as metadata for building prior-round lookups. |
| 19 | 9-22 | Selects all stored own events with normalized-domain metadata, context and fold assignments. Here current outcomes are available as metadata for building prior-round lookups. |
| 20 | 9-22 | Selects all stored own events with normalized-domain metadata, context and fold assignments. Here current outcomes are available as metadata for building prior-round lookups. |
| 21 | 9-22 | Selects all stored own events with normalized-domain metadata, context and fold assignments. Here current outcomes are available as metadata for building prior-round lookups. |
| 22 | 9-22 | Selects all stored own events with normalized-domain metadata, context and fold assignments. Here current outcomes are available as metadata for building prior-round lookups. |
| 23 | 23-32 | Joins the five database tables and orders rows consistently. Missing context/functions survive LEFT JOIN so validation can detect them. |
| 24 | 23-32 | Joins the five database tables and orders rows consistently. Missing context/functions survive LEFT JOIN so validation can detect them. |
| 25 | 23-32 | Joins the five database tables and orders rows consistently. Missing context/functions survive LEFT JOIN so validation can detect them. |
| 26 | 23-32 | Joins the five database tables and orders rows consistently. Missing context/functions survive LEFT JOIN so validation can detect them. |
| 27 | 23-32 | Joins the five database tables and orders rows consistently. Missing context/functions survive LEFT JOIN so validation can detect them. |
| 28 | 23-32 | Joins the five database tables and orders rows consistently. Missing context/functions survive LEFT JOIN so validation can detect them. |
| 29 | 23-32 | Joins the five database tables and orders rows consistently. Missing context/functions survive LEFT JOIN so validation can detect them. |
| 30 | 23-32 | Joins the five database tables and orders rows consistently. Missing context/functions survive LEFT JOIN so validation can detect them. |
| 31 | 23-32 | Joins the five database tables and orders rows consistently. Missing context/functions survive LEFT JOIN so validation can detect them. |
| 32 | 23-32 | Closes the multiline expression or payload begun above. |
| 33 | 33-40 | Rejects empty or incomplete input, builds a DataFrame and formats timestamps like the original exports. |
| 34 | 33-40 | Conditional branch: determines which following statements run. |
| 35 | 33-40 | Conditional branch: determines which following statements run. |
| 36 | 33-40 | Failure path: interrupts normal execution with the stated exception. |
| 37 | 33-40 | Rejects empty or incomplete input, builds a DataFrame and formats timestamps like the original exports. |
| 38 | 33-40 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 39 | 33-40 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 40 | 33-40 | Rejects empty or incomplete input, builds a DataFrame and formats timestamps like the original exports. |
| 41 | 41-47 | Builds one outcome per player-round, then shifts outcomes forward within each participant/session/game. First available rounds get zero priors. |
| 42 | 41-47 | Builds one outcome per player-round, then shifts outcomes forward within each participant/session/game. First available rounds get zero priors. |
| 43 | 41-47 | Loop: repeats the following operations for the stated elements/condition. |
| 44 | 41-47 | Builds one outcome per player-round, then shifts outcomes forward within each participant/session/game. First available rounds get zero priors. |
| 45 | 41-47 | Loop: repeats the following operations for the stated elements/condition. |
| 46 | 41-47 | Builds one outcome per player-round, then shifts outcomes forward within each participant/session/game. First available rounds get zero priors. |
| 47 | 41-47 | Builds one outcome per player-round, then shifts outcomes forward within each participant/session/game. First available rounds get zero priors. |
| 48 | 48-54 | Builds maximum and fold dictionaries and rejects conflicting nonnull folds for the same identity. Returns tabular input and metadata. |
| 49 | 48-54 | Builds maximum and fold dictionaries and rejects conflicting nonnull folds for the same identity. Returns tabular input and metadata. |
| 50 | 48-54 | Loop: repeats the following operations for the stated elements/condition. |
| 51 | 48-54 | Builds maximum and fold dictionaries and rejects conflicting nonnull folds for the same identity. Returns tabular input and metadata. |
| 52 | 48-54 | Conditional branch: determines which following statements run. |
| 53 | 48-54 | Conditional branch: determines which following statements run. |
| 54 | 48-54 | Return: sends this result to the caller and ends this invocation. |
| 55 | 55 | Blank separator; no execution. |
| 56 | 56 | Blank separator; no execution. |
| 57 | 57-62 | Function declaration: this body runs when called, not at declaration time. |
| 58 | 57-62 | Builds every available sequence, indexes it by canonical key, and returns only keys with original held-out assignments plus the fold map. |
| 59 | 57-62 | Builds every available sequence, indexes it by canonical key, and returns only keys with original held-out assignments plus the fold map. |
| 60 | 57-62 | Builds every available sequence, indexes it by canonical key, and returns only keys with original held-out assignments plus the fold map. |
| 61 | 57-62 | Loop: repeats the following operations for the stated elements/condition. |
| 62 | 57-62 | Return: sends this result to the caller and ends this invocation. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  """Read PostgreSQL events/context and build the original 14 model features.
   2  No preprocessing pickle is read here. SQL stores fold metadata separately.
   3  """
   4  import pandas as pd
   5  from psycopg.rows import dict_row
   6  from feature_math import build_sequences
   7  
   8  
   9  def load_feature_inputs(conn):
  10      # One consistent snapshot is supplied by the caller. Preserve participant
  11      # then own-step ordering for the original stable merge/timestamp tie rules.
  12      with conn.cursor(row_factory=dict_row) as cur:
  13          cur.execute('''
  14            SELECT r.session_id AS session,r.game_number AS game_num,
  15                   r.round_number AS round,r.participant_id,r.group_id AS record_group_id,
  16                   COALESCE(r.opponent_group_id,-1) AS opponent_group_id,
  17                   COALESCE(r.recorded_payoff,0) AS payoff,
  18                   COALESCE(r.team_won,false)::integer AS is_win,
  19                   e.x_min AS x_domain_min,e.x_max AS x_domain_max,
  20                   s.step_number AS step,s.x_value AS x,s.observed_value AS fx,
  21                   s.sampled_at AS timestamp,
  22                   CASE WHEN s.step_number=1 THEN c.opponent_results_data ELSE NULL END AS opp_results_data,
  23                   c.source_cache_sha256,c.held_out_fold,
  24                   f.estimated_maximum
  25            FROM participant_rounds r
  26            JOIN samples s ON s.participant_round_id=r.participant_round_id
  27            JOIN experiment_sessions e ON e.session_id=r.session_id
  28            LEFT JOIN model_context c ON c.participant_round_id=r.participant_round_id
  29            LEFT JOIN round_functions f ON f.session_id=r.session_id
  30               AND f.game_number=r.game_number AND f.round_number=r.round_number
  31            ORDER BY r.session_id,r.game_number,r.round_number,r.participant_id,s.step_number
  32          ''')
  33          rows=cur.fetchall()
  34      if not rows:raise ValueError('No database samples found.')
  35      if any(r['source_cache_sha256'] is None or r['estimated_maximum'] is None for r in rows):
  36          raise ValueError('Missing model context or objective maximum. Run both context/function importers.')
  37      df=pd.DataFrame(rows)
  38      # Opponent exports use timestamp strings; use the same representation for
  39      # sample comparisons. Existing raw files have whole-second sample stamps.
  40      df['timestamp']=df['timestamp'].map(lambda t:t.isoformat(sep=' '))
  41      per_round=df.groupby(['session','game_num','round','participant_id'],sort=True)[['payoff','is_win']].first().reset_index()
  42      priors={}
  43      for (session,game,pid),group in per_round.groupby(['session','game_num','participant_id']):
  44          previous=(0.0,0.0)
  45          for _,row in group.sort_values('round').iterrows():
  46              priors[(session,int(game),int(row['round']),int(pid))]=previous
  47              previous=(float(row['is_win']),float(row['payoff'])/200)
  48      maxima={tuple(key):float(group['estimated_maximum'].iloc[0]) for key,group in df.groupby(['session','game_num','round'])}
  49      folds={}
  50      for key,group in df.groupby(['session','game_num','round','participant_id']):
  51          values=group['held_out_fold'].dropna().unique()
  52          if len(values)>1:raise ValueError(f'Conflicting folds: {key}')
  53          if len(values):folds[tuple(key)]=int(values[0])
  54      return df,maxima,priors,folds
  55  
  56  
  57  def rebuild_from_database(conn):
  58      df,maxima,priors,folds=load_feature_inputs(conn)
  59      sequences=build_sequences(df,maxima,priors)
  60      by_key={ (s['meta']['session'],int(s['meta']['game_num']),int(s['meta']['round']),int(s['meta']['participant_id'])):s
  61               for s in sequences }
  62      return {key:by_key[key] for key in folds},folds
```
