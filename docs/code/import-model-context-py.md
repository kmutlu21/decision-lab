# import_model_context.py

Imports raw opponent exports and the original fold_map, keeping model lineage separate from sample data.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Symbols

| Symbol | Lines |
|---|---|
| `connect` | 18-22 |
| `read_context` | 25-57 |
| `main` | 60-90 |

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1-15 | Imports session/parsing helpers and pins the exact reference-cache digest. No fold grouping or random split is performed here. |
| 18-22 | Connects using PG settings; prompts only if PGPASSWORD is absent. Verification scripts reuse this connection helper. |
| 25-33 | Reads the expected 12 files, finds round columns and prepares per-round parsing. |
| 34-42 | Maps group members and symmetric opponent pairings from the raw experiment export. |
| 43-49 | Skips unused/empty player histories and looks up the opposing group's rows. |
| 50-57 | In games 3/4, takes the first opposing member's nonempty results_data string and requires a JSON dictionary. Associates the payload with the focal sequence key. |
| 60-66 | Reads raw context and deserializes the cache only after the expected SHA256 matches; converts fold values to integers. |
| 67-74 | Creates model_context with one row per participant_round_id and nullable fold 0..4, then obtains the shared transaction lock. |
| 75-78 | Checks that raw and database round identities agree and that every saved fold has an imported database round. |
| 79-88 | Inserts missing context rows, skips identical rows and rejects conflicts. No fold means the nonempty round was excluded from the original model. |
| 89-90 | Reports inserted/unchanged context rows and how many rounds have saved fold assignments. |
| 93-96 | Runs the import only as a script; failure rolls back this stage and returns nonzero. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1-15 | Imports session/parsing helpers and pins the exact reference-cache digest. No fold grouping or random split is performed here. |
| 2 | 1-15 | Imports session/parsing helpers and pins the exact reference-cache digest. No fold grouping or random split is performed here. |
| 3 | 1-15 | Imports session/parsing helpers and pins the exact reference-cache digest. No fold grouping or random split is performed here. |
| 4 | 1-15 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 5 | 1-15 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 6 | 1-15 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 7 | 1-15 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 8 | 1-15 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 9 | 1-15 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 10 | 1-15 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 11 | 1-15 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 12 | 1-15 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 13 | 1-15 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 14 | 1-15 | Blank separator; no execution. |
| 15 | 1-15 | Imports session/parsing helpers and pins the exact reference-cache digest. No fold grouping or random split is performed here. |
| 16 | 16 | Blank separator; no execution. |
| 17 | 17 | Blank separator; no execution. |
| 18 | 18-22 | Function declaration: this body runs when called, not at declaration time. |
| 19 | 18-22 | Connects using PG settings; prompts only if PGPASSWORD is absent. Verification scripts reuse this connection helper. |
| 20 | 18-22 | Conditional branch: determines which following statements run. |
| 21 | 18-22 | Return: sends this result to the caller and ends this invocation. |
| 22 | 18-22 | Connects using PG settings; prompts only if PGPASSWORD is absent. Verification scripts reuse this connection helper. |
| 23 | 23 | Blank separator; no execution. |
| 24 | 24 | Blank separator; no execution. |
| 25 | 25-33 | Function declaration: this body runs when called, not at declaration time. |
| 26 | 25-33 | Reads the expected 12 files, finds round columns and prepares per-round parsing. |
| 27 | 25-33 | Loop: repeats the following operations for the stated elements/condition. |
| 28 | 25-33 | Loop: repeats the following operations for the stated elements/condition. |
| 29 | 25-33 | Reads the expected 12 files, finds round columns and prepares per-round parsing. |
| 30 | 25-33 | Conditional branch: determines which following statements run. |
| 31 | 25-33 | Reads the expected 12 files, finds round columns and prepares per-round parsing. |
| 32 | 25-33 | Reads the expected 12 files, finds round columns and prepares per-round parsing. |
| 33 | 25-33 | Loop: repeats the following operations for the stated elements/condition. |
| 34 | 34-42 | Maps group members and symmetric opponent pairings from the raw experiment export. |
| 35 | 34-42 | Maps group members and symmetric opponent pairings from the raw experiment export. |
| 36 | 34-42 | Loop: repeats the following operations for the stated elements/condition. |
| 37 | 34-42 | Maps group members and symmetric opponent pairings from the raw experiment export. |
| 38 | 34-42 | Conditional branch: determines which following statements run. |
| 39 | 34-42 | Maps group members and symmetric opponent pairings from the raw experiment export. |
| 40 | 34-42 | Loop: repeats the following operations for the stated elements/condition. |
| 41 | 34-42 | Maps group members and symmetric opponent pairings from the raw experiment export. |
| 42 | 34-42 | Loop: repeats the following operations for the stated elements/condition. |
| 43 | 43-49 | Conditional branch: determines which following statements run. |
| 44 | 43-49 | Skips unused/empty player histories and looks up the opposing group's rows. |
| 45 | 43-49 | Conditional branch: determines which following statements run. |
| 46 | 43-49 | Skips unused/empty player histories and looks up the opposing group's rows. |
| 47 | 43-49 | Skips unused/empty player histories and looks up the opposing group's rows. |
| 48 | 43-49 | Skips unused/empty player histories and looks up the opposing group's rows. |
| 49 | 43-49 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 50 | 50-57 | Conditional branch: determines which following statements run. |
| 51 | 50-57 | In games 3/4, takes the first opposing member's nonempty results_data string and requires a JSON dictionary. Associates the payload with the focal sequence key. |
| 52 | 50-57 | Conditional branch: determines which following statements run. |
| 53 | 50-57 | In games 3/4, takes the first opposing member's nonempty results_data string and requires a JSON dictionary. Associates the payload with the focal sequence key. |
| 54 | 50-57 | In games 3/4, takes the first opposing member's nonempty results_data string and requires a JSON dictionary. Associates the payload with the focal sequence key. |
| 55 | 50-57 | Conditional branch: determines which following statements run. |
| 56 | 50-57 | In games 3/4, takes the first opposing member's nonempty results_data string and requires a JSON dictionary. Associates the payload with the focal sequence key. |
| 57 | 50-57 | Return: sends this result to the caller and ends this invocation. |
| 58 | 58 | Blank separator; no execution. |
| 59 | 59 | Blank separator; no execution. |
| 60 | 60-66 | Function declaration: this body runs when called, not at declaration time. |
| 61 | 60-66 | Reads raw context and deserializes the cache only after the expected SHA256 matches; converts fold values to integers. |
| 62 | 60-66 | Reads raw context and deserializes the cache only after the expected SHA256 matches; converts fold values to integers. |
| 63 | 60-66 | Reads raw context and deserializes the cache only after the expected SHA256 matches; converts fold values to integers. |
| 64 | 60-66 | Conditional branch: determines which following statements run. |
| 65 | 60-66 | Reads raw context and deserializes the cache only after the expected SHA256 matches; converts fold values to integers. |
| 66 | 60-66 | Reads raw context and deserializes the cache only after the expected SHA256 matches; converts fold values to integers. |
| 67 | 67-74 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 68 | 67-74 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 69 | 67-74 | Creates model_context with one row per participant_round_id and nullable fold 0..4, then obtains the shared transaction lock. |
| 70 | 67-74 | Creates model_context with one row per participant_round_id and nullable fold 0..4, then obtains the shared transaction lock. |
| 71 | 67-74 | Creates model_context with one row per participant_round_id and nullable fold 0..4, then obtains the shared transaction lock. |
| 72 | 67-74 | Creates model_context with one row per participant_round_id and nullable fold 0..4, then obtains the shared transaction lock. |
| 73 | 67-74 | Creates model_context with one row per participant_round_id and nullable fold 0..4, then obtains the shared transaction lock. |
| 74 | 67-74 | Creates model_context with one row per participant_round_id and nullable fold 0..4, then obtains the shared transaction lock. |
| 75 | 75-78 | Checks that raw and database round identities agree and that every saved fold has an imported database round. |
| 76 | 75-78 | Checks that raw and database round identities agree and that every saved fold has an imported database round. |
| 77 | 75-78 | Conditional branch: determines which following statements run. |
| 78 | 75-78 | Conditional branch: determines which following statements run. |
| 79 | 79-88 | Inserts missing context rows, skips identical rows and rejects conflicts. No fold means the nonempty round was excluded from the original model. |
| 80 | 79-88 | Loop: repeats the following operations for the stated elements/condition. |
| 81 | 79-88 | Inserts missing context rows, skips identical rows and rejects conflicts. No fold means the nonempty round was excluded from the original model. |
| 82 | 79-88 | Inserts missing context rows, skips identical rows and rejects conflicts. No fold means the nonempty round was excluded from the original model. |
| 83 | 79-88 | Inserts missing context rows, skips identical rows and rejects conflicts. No fold means the nonempty round was excluded from the original model. |
| 84 | 79-88 | Conditional branch: determines which following statements run. |
| 85 | 79-88 | Conditional branch: determines which following statements run. |
| 86 | 79-88 | Inserts missing context rows, skips identical rows and rejects conflicts. No fold means the nonempty round was excluded from the original model. |
| 87 | 79-88 | Conditional branch: determines which following statements run. |
| 88 | 79-88 | Inserts missing context rows, skips identical rows and rejects conflicts. No fold means the nonempty round was excluded from the original model. |
| 89 | 89-90 | Reports inserted/unchanged context rows and how many rounds have saved fold assignments. |
| 90 | 89-90 | Reports inserted/unchanged context rows and how many rounds have saved fold assignments. |
| 91 | 91 | Blank separator; no execution. |
| 92 | 92 | Blank separator; no execution. |
| 93 | 93-96 | Conditional branch: determines which following statements run. |
| 94 | 93-96 | Exception-control block: separates normal work, error handling and cleanup. |
| 95 | 93-96 | Exception-control block: separates normal work, error handling and cleanup. |
| 96 | 93-96 | Runs the import only as a script; failure rolls back this stage and returns nonzero. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  """Import exported opponent context and original held-out fold assignments.
   2  Run after the existing data and function importers. Does not change samples.
   3  """
   4  import getpass
   5  import hashlib
   6  import json
   7  import os
   8  from pathlib import Path
   9  import pickle
  10  import re
  11  import pandas as pd
  12  import psycopg
  13  from import_data import SESSIONS, sequence, integer
  14  
  15  CACHE_HASH='4966ad1c64a736a74dee8feff0f47010a5f921654a26cf9a6836c70ce58f3f00'
  16  
  17  
  18  def connect():
  19      password=os.getenv('PGPASSWORD')
  20      if password is None: password=getpass.getpass('PostgreSQL password: ')
  21      return psycopg.connect(host=os.getenv('PGHOST','localhost'),port=os.getenv('PGPORT','5432'),
  22          dbname=os.getenv('PGDATABASE','decision_lab'),user=os.getenv('PGUSER','postgres'),password=password,connect_timeout=5)
  23  
  24  
  25  def read_context(root):
  26      records={}
  27      for session,(_,_,_,pattern) in SESSIONS.items():
  28          for game in range(1,5):
  29              files=list(root.rglob(pattern.format(game)))
  30              if len(files)!=1: raise ValueError(f'Expected one {pattern.format(game)}')
  31              df=pd.read_csv(files[0]) if files[0].suffix=='.csv' else pd.read_excel(files[0])
  32              rounds=sorted(int(c.split('.')[1]) for c in df if re.fullmatch(rf'guess4{game}\.\d+\.player.samples',c))
  33              for rnd in rounds:
  34                  pre=f'guess4{game}.{rnd}'
  35                  groups={}
  36                  for idx,row in df.iterrows():
  37                      gid=row[f'{pre}.player.record_group_id']
  38                      if pd.notna(gid): groups.setdefault(integer(gid),[]).append(idx)
  39                  opponents={}
  40                  for a,b in sequence(df[f'{pre}.subsession.paired_groups'].iloc[0]):
  41                      opponents[integer(a)]=integer(b);opponents[integer(b)]=integer(a)
  42                  for _,row in df.iterrows():
  43                      if pd.isna(row['participant.id_in_session']):continue
  44                      value=row[f'{pre}.player.samples']
  45                      if pd.isna(value) or not sequence(value):continue
  46                      pid=integer(row['participant.id_in_session']);gid=integer(row[f'{pre}.player.record_group_id'])
  47                      payload=None;col=f'{pre}.group.results_data'
  48                      indices=groups.get(opponents.get(gid),[])
  49                      # Match original preprocessing: first opponent group member.
  50                      if game in (3,4) and indices and col in df:
  51                          value=df.iloc[indices[0]][col]
  52                          if pd.notna(value) and str(value).strip() not in ('','{}'):
  53                              payload=str(value)
  54                              parsed=json.loads(payload)
  55                              if not isinstance(parsed,dict):raise ValueError('Invalid opponent payload')
  56                      records[(session,game,rnd,pid)]=payload
  57      return records
  58  
  59  
  60  def main():
  61      root=Path(__file__).resolve().parent
  62      records=read_context(root/'data'/'raw')
  63      raw=(root/'models'/'preprocessed_sequences_delta_default.pkl').read_bytes()
  64      if hashlib.sha256(raw).hexdigest()!=CACHE_HASH:raise ValueError('Feature cache differs from verified original.')
  65      dataset=pickle.loads(raw)
  66      folds={tuple(k):int(v) for k,v in dataset['fold_map'].items()}
  67      with connect() as conn:
  68          with conn.cursor() as cur:
  69              cur.execute('''CREATE TABLE IF NOT EXISTS model_context (
  70                participant_round_id BIGINT PRIMARY KEY REFERENCES participant_rounds(participant_round_id),
  71                opponent_results_data TEXT,
  72                held_out_fold INTEGER CHECK(held_out_fold BETWEEN 0 AND 4),
  73                source_cache_sha256 TEXT NOT NULL)''')
  74              cur.execute('SELECT pg_advisory_xact_lock(20260908)')
  75              cur.execute('SELECT session_id,game_number,round_number,participant_id,participant_round_id FROM participant_rounds')
  76              ids={tuple(row[:4]):row[4] for row in cur.fetchall()}
  77              if set(ids)!=set(records):raise ValueError('Imported participant-round identities differ from the raw files.')
  78              if not set(folds)<=set(ids):raise ValueError('Some model fold assignments have no database round.')
  79              added=unchanged=0
  80              for key,payload in records.items():
  81                  desired=(payload,folds.get(key),CACHE_HASH)
  82                  cur.execute('SELECT opponent_results_data,held_out_fold,source_cache_sha256 FROM model_context WHERE participant_round_id=%s',(ids[key],))
  83                  old=cur.fetchone()
  84                  if old is not None:
  85                      if old!=desired:raise ValueError(f'Conflicting existing context: {key}')
  86                      unchanged+=1
  87                  else:
  88                      cur.execute('INSERT INTO model_context VALUES (%s,%s,%s,%s)',(ids[key],)+desired);added+=1
  89      print(f'COMMITTED: {added} new context records; {unchanged} identical records already present.')
  90      print(f'{len(folds)} held-out fold assignments; {len(records)-len(folds)} rounds excluded from original model.')
  91  
  92  
  93  if __name__=='__main__':
  94      try:main()
  95      except Exception as exc:
  96          print(f'ERROR: {exc}\nNo changes committed by this run.');raise SystemExit(1)
```
