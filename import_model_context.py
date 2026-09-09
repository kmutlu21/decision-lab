"""Import exported opponent context and original held-out fold assignments.
Run after the existing data and function importers. Does not change samples.
"""
import getpass
import hashlib
import json
import os
from pathlib import Path
import pickle
import re
import pandas as pd
import psycopg
from import_data import SESSIONS, sequence, integer

CACHE_HASH='4966ad1c64a736a74dee8feff0f47010a5f921654a26cf9a6836c70ce58f3f00'


def connect():
    password=os.getenv('PGPASSWORD')
    if password is None: password=getpass.getpass('PostgreSQL password: ')
    return psycopg.connect(host=os.getenv('PGHOST','localhost'),port=os.getenv('PGPORT','5432'),
        dbname=os.getenv('PGDATABASE','decision_lab'),user=os.getenv('PGUSER','postgres'),password=password,connect_timeout=5)


def read_context(root):
    records={}
    for session,(_,_,_,pattern) in SESSIONS.items():
        for game in range(1,5):
            files=list(root.rglob(pattern.format(game)))
            if len(files)!=1: raise ValueError(f'Expected one {pattern.format(game)}')
            df=pd.read_csv(files[0]) if files[0].suffix=='.csv' else pd.read_excel(files[0])
            rounds=sorted(int(c.split('.')[1]) for c in df if re.fullmatch(rf'guess4{game}\.\d+\.player.samples',c))
            for rnd in rounds:
                pre=f'guess4{game}.{rnd}'
                groups={}
                for idx,row in df.iterrows():
                    gid=row[f'{pre}.player.record_group_id']
                    if pd.notna(gid): groups.setdefault(integer(gid),[]).append(idx)
                opponents={}
                for a,b in sequence(df[f'{pre}.subsession.paired_groups'].iloc[0]):
                    opponents[integer(a)]=integer(b);opponents[integer(b)]=integer(a)
                for _,row in df.iterrows():
                    if pd.isna(row['participant.id_in_session']):continue
                    value=row[f'{pre}.player.samples']
                    if pd.isna(value) or not sequence(value):continue
                    pid=integer(row['participant.id_in_session']);gid=integer(row[f'{pre}.player.record_group_id'])
                    payload=None;col=f'{pre}.group.results_data'
                    indices=groups.get(opponents.get(gid),[])
                    # Match original preprocessing: first opponent group member.
                    if game in (3,4) and indices and col in df:
                        value=df.iloc[indices[0]][col]
                        if pd.notna(value) and str(value).strip() not in ('','{}'):
                            payload=str(value)
                            parsed=json.loads(payload)
                            if not isinstance(parsed,dict):raise ValueError('Invalid opponent payload')
                    records[(session,game,rnd,pid)]=payload
    return records


def main():
    root=Path(__file__).resolve().parent
    records=read_context(root/'data'/'raw')
    raw=(root/'models'/'preprocessed_sequences_delta_default.pkl').read_bytes()
    if hashlib.sha256(raw).hexdigest()!=CACHE_HASH:raise ValueError('Feature cache differs from verified original.')
    dataset=pickle.loads(raw)
    folds={tuple(k):int(v) for k,v in dataset['fold_map'].items()}
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute('''CREATE TABLE IF NOT EXISTS model_context (
              participant_round_id BIGINT PRIMARY KEY REFERENCES participant_rounds(participant_round_id),
              opponent_results_data TEXT,
              held_out_fold INTEGER CHECK(held_out_fold BETWEEN 0 AND 4),
              source_cache_sha256 TEXT NOT NULL)''')
            cur.execute('SELECT pg_advisory_xact_lock(20260908)')
            cur.execute('SELECT session_id,game_number,round_number,participant_id,participant_round_id FROM participant_rounds')
            ids={tuple(row[:4]):row[4] for row in cur.fetchall()}
            if set(ids)!=set(records):raise ValueError('Imported participant-round identities differ from the raw files.')
            if not set(folds)<=set(ids):raise ValueError('Some model fold assignments have no database round.')
            added=unchanged=0
            for key,payload in records.items():
                desired=(payload,folds.get(key),CACHE_HASH)
                cur.execute('SELECT opponent_results_data,held_out_fold,source_cache_sha256 FROM model_context WHERE participant_round_id=%s',(ids[key],))
                old=cur.fetchone()
                if old is not None:
                    if old!=desired:raise ValueError(f'Conflicting existing context: {key}')
                    unchanged+=1
                else:
                    cur.execute('INSERT INTO model_context VALUES (%s,%s,%s,%s)',(ids[key],)+desired);added+=1
    print(f'COMMITTED: {added} new context records; {unchanged} identical records already present.')
    print(f'{len(folds)} held-out fold assignments; {len(records)-len(folds)} rounds excluded from original model.')


if __name__=='__main__':
    try:main()
    except Exception as exc:
        print(f'ERROR: {exc}\nNo changes committed by this run.');raise SystemExit(1)
