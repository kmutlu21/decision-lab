"""Read PostgreSQL events/context and build the original 14 model features.
No preprocessing pickle is read here. SQL stores fold metadata separately.
"""
import pandas as pd
from psycopg.rows import dict_row
from feature_math import build_sequences


def load_feature_inputs(conn):
    # One consistent snapshot is supplied by the caller. Preserve participant
    # then own-step ordering for the original stable merge/timestamp tie rules.
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute('''
          SELECT r.session_id AS session,r.game_number AS game_num,
                 r.round_number AS round,r.participant_id,r.group_id AS record_group_id,
                 COALESCE(r.opponent_group_id,-1) AS opponent_group_id,
                 COALESCE(r.recorded_payoff,0) AS payoff,
                 COALESCE(r.team_won,false)::integer AS is_win,
                 e.x_min AS x_domain_min,e.x_max AS x_domain_max,
                 s.step_number AS step,s.x_value AS x,s.observed_value AS fx,
                 s.sampled_at AS timestamp,
                 CASE WHEN s.step_number=1 THEN c.opponent_results_data ELSE NULL END AS opp_results_data,
                 c.source_cache_sha256,c.held_out_fold,
                 f.estimated_maximum
          FROM participant_rounds r
          JOIN samples s ON s.participant_round_id=r.participant_round_id
          JOIN experiment_sessions e ON e.session_id=r.session_id
          LEFT JOIN model_context c ON c.participant_round_id=r.participant_round_id
          LEFT JOIN round_functions f ON f.session_id=r.session_id
             AND f.game_number=r.game_number AND f.round_number=r.round_number
          ORDER BY r.session_id,r.game_number,r.round_number,r.participant_id,s.step_number
        ''')
        rows=cur.fetchall()
    if not rows:raise ValueError('No database samples found.')
    if any(r['source_cache_sha256'] is None or r['estimated_maximum'] is None for r in rows):
        raise ValueError('Missing model context or objective maximum. Run both context/function importers.')
    df=pd.DataFrame(rows)
    # Opponent exports use timestamp strings; use the same representation for
    # sample comparisons. Existing raw files have whole-second sample stamps.
    df['timestamp']=df['timestamp'].map(lambda t:t.isoformat(sep=' '))
    per_round=df.groupby(['session','game_num','round','participant_id'],sort=True)[['payoff','is_win']].first().reset_index()
    priors={}
    for (session,game,pid),group in per_round.groupby(['session','game_num','participant_id']):
        previous=(0.0,0.0)
        for _,row in group.sort_values('round').iterrows():
            priors[(session,int(game),int(row['round']),int(pid))]=previous
            previous=(float(row['is_win']),float(row['payoff'])/200)
    maxima={tuple(key):float(group['estimated_maximum'].iloc[0]) for key,group in df.groupby(['session','game_num','round'])}
    folds={}
    for key,group in df.groupby(['session','game_num','round','participant_id']):
        values=group['held_out_fold'].dropna().unique()
        if len(values)>1:raise ValueError(f'Conflicting folds: {key}')
        if len(values):folds[tuple(key)]=int(values[0])
    return df,maxima,priors,folds


def rebuild_from_database(conn):
    df,maxima,priors,folds=load_feature_inputs(conn)
    sequences=build_sequences(df,maxima,priors)
    by_key={ (s['meta']['session'],int(s['meta']['game_num']),int(s['meta']['round']),int(s['meta']['participant_id'])):s
             for s in sequences }
    return {key:by_key[key] for key in folds},folds
