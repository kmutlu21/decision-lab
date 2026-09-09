"""Read only the selected historical prefix and rebuild its model inputs."""
import json
import numpy as np
import pandas as pd
from psycopg.rows import dict_row
from feature_math import build_sequences


class MissingRound(Exception):pass
class InvalidStep(Exception):pass


def make_prefix(rows, meta, key, after_step):
    """Pure feature assembly, also used by the parity checker."""
    if not rows:raise ValueError('No events in selected prefix.')
    frame=pd.DataFrame(rows)
    frame['timestamp']=frame['timestamp'].map(lambda t:t.isoformat(sep=' ') if not isinstance(t,str) else t)
    # Keep the exported context payload intact. The original feature loop
    # considers the context available when its timeline is nonempty, even
    # before its first observation. It uses only values with time <= each
    # event. Dropping later entries here would incorrectly turn that early
    # competitor gap into zero. Preserve that historical availability rule.
    priors={}
    for _,row in frame.drop_duplicates('participant_id').iterrows():
        priors[(key[0],key[1],key[2],int(row['participant_id']))]=(float(row['prior_won']),float(row['prior_payoff'])/200)
    candidates=build_sequences(frame,{key[:3]:float(meta['estimated_maximum'])},priors)
    sequence=next((s for s in candidates if int(s['meta']['participant_id'])==key[3]),None)
    if sequence is None:raise ValueError('Focal sequence missing.')
    own=np.flatnonzero(sequence['features'][:,2]>.5)
    if len(own)!=after_step or own[-1]!=len(sequence['features'])-1:
        raise ValueError('Prefix does not end at the requested own event.')
    return sequence


def load_prefix(conn,key,after_step):
    session,game,rnd,pid=key
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute('''
          SELECT r.participant_round_id,r.group_id,c.held_out_fold,c.source_cache_sha256,
                 f.estimated_maximum,e.x_min,e.x_max,s.sampled_at AS cutoff
          FROM participant_rounds r
          JOIN experiment_sessions e ON e.session_id=r.session_id
          LEFT JOIN model_context c ON c.participant_round_id=r.participant_round_id
          LEFT JOIN round_functions f ON f.session_id=r.session_id AND f.game_number=r.game_number AND f.round_number=r.round_number
          LEFT JOIN samples s ON s.participant_round_id=r.participant_round_id AND s.step_number=%s
          WHERE r.session_id=%s AND r.game_number=%s AND r.round_number=%s AND r.participant_id=%s
        ''',(after_step,session,game,rnd,pid))
        meta=cur.fetchone()
        if meta is None:raise MissingRound('Participant-round not found.')
        if meta['cutoff'] is None:raise InvalidStep('after_step exceeds the recorded sample count.')
        if meta['source_cache_sha256'] is None or meta['estimated_maximum'] is None:
            raise ValueError('Model context or objective maximum missing. Run the importers.')
        if meta['held_out_fold'] is None:return None,meta
        cur.execute('''
          SELECT r.session_id AS session,r.game_number AS game_num,r.round_number AS round,
                 r.participant_id,r.group_id AS record_group_id,COALESCE(r.opponent_group_id,-1) AS opponent_group_id,
                 0.0 AS payoff,0 AS is_win,e.x_min AS x_domain_min,e.x_max AS x_domain_max,
                 s.step_number AS step,s.x_value AS x,s.observed_value AS fx,s.sampled_at AS timestamp,
                 CASE WHEN s.step_number=1 THEN c.opponent_results_data ELSE NULL END AS opp_results_data,
                 COALESCE(prior.team_won,false)::integer AS prior_won,COALESCE(prior.recorded_payoff,0) AS prior_payoff
          FROM participant_rounds r
          JOIN samples s ON s.participant_round_id=r.participant_round_id
          JOIN experiment_sessions e ON e.session_id=r.session_id
          JOIN model_context c ON c.participant_round_id=r.participant_round_id
          LEFT JOIN LATERAL (
            SELECT p.team_won,p.recorded_payoff FROM participant_rounds p
            WHERE p.session_id=r.session_id AND p.game_number=r.game_number
              AND p.participant_id=r.participant_id AND p.round_number<r.round_number
            ORDER BY p.round_number DESC LIMIT 1
          ) prior ON true
          WHERE r.session_id=%s AND r.game_number=%s AND r.round_number=%s
            AND (r.participant_id=%s OR (%s AND r.group_id=%s))
            AND ((r.participant_id=%s AND s.step_number<=%s AND s.sampled_at<=%s)
                 OR (r.participant_id<>%s AND s.sampled_at<%s))
          ORDER BY r.participant_id,s.step_number
        ''',(session,game,rnd,pid,game in (2,4),meta['group_id'],pid,after_step,meta['cutoff'],pid,meta['cutoff']))
        rows=cur.fetchall()
    # Strict < for teammate cutoff implements the original own-before-mate
    # ordering when both sample timestamps are equal.
    return make_prefix(rows,meta,key,after_step),meta
