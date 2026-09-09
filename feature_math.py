"""Feature calculation extracted from the original default preprocessing.
The feature builder consumes event rows, an objective maximum and prior outcomes.
It does not load pickles, train models, or calculate future targets.
"""
import json
import numpy as np
import pandas as pd

GAMES={g:{'has_teammate':g in (2,4),'has_opponent':g in (3,4)} for g in range(1,5)}
TIME_CAP_S=120.0

def parse_opponent_timeline(opp_results_json):
    """
    Decode the opponent group's results_data JSON (stored as a string of
    {pid: [[fx, x, ts], ...]}) into a flat (timestamp, fx_raw) list sorted
    in time order. Used downstream to compute the opponent's running-best
    curve at any query timestamp via compute_opp_best_at_time.

    Returns [] for missing or malformed payloads — callers check len() to
    decide whether comp_gap should default to 0.
    """
    if opp_results_json is None: return []
    try: rd = json.loads(opp_results_json)
    except: return []
    opp = []
    for pid_str, samples in rd.items():
        for s in samples: opp.append((s[2], float(s[0])))
    opp.sort(key=lambda x: x[0])
    return opp


def compute_opp_best_at_time(opp_timeline, timestamp):
    """
    Linear scan to find the opponent's RUNNING-BEST fx as of `timestamp`.
    The timeline is presorted, so we can break out as soon as t > timestamp.
    Returns 0.0 if no opponent samples were observed by then (matches the
    way comp_gap is defined: opponent best is monotone-nondecreasing from 0).
    """
    best = 0.0
    for t, fx in opp_timeline:
        if t <= timestamp: best = max(best, fx)
        else: break
    return best



def build_sequences(raw_df, true_max_lookup, prior_outcome):
    sequences=[]
    for (session,game_num,rnd), round_df in raw_df.groupby(['session','game_num','round']):
        game_cfg = GAMES[game_num]
        x_min_val = round_df['x_domain_min'].iloc[0]
        x_max_val = round_df['x_domain_max'].iloc[0]
        domain_width = x_max_val - x_min_val
        true_max = true_max_lookup[(session,game_num,rnd)]
        has_teammate = game_cfg['has_teammate']
        has_opponent = game_cfg['has_opponent']
        for gid, group_df in round_df.groupby('record_group_id'):
            players = sorted(group_df['participant_id'].unique())
            # Parse opponent timeline ONCE per group; reused across both focal
            # players in the group (in team games) since they share an opponent.
            opp_timeline = []
            if has_opponent:
                opp_rd_row = group_df.dropna(subset=['opp_results_data'])
                if len(opp_rd_row) > 0:
                    opp_timeline = parse_opponent_timeline(opp_rd_row.iloc[0]['opp_results_data'])
            for target_pid in players:
                # Focal player's own samples (is_own=1) — these are the ones
                # whose deltas the network will be trained to predict.
                target_df = group_df[group_df['participant_id']==target_pid].sort_values('step')
                target_samples = [{'x':float(r['x']),'fx':float(r['fx']),'timestamp':r['timestamp'],'is_own':1,'pid':target_pid} for _,r in target_df.iterrows()]
                # Teammate's samples (is_own=0) only exist in G2/G4. The teammate
                # influences the focal player's running-best and spread-of-own
                # diagnostics, but the focal player's *targets* are computed
                # only against their own next event.
                mate_samples = []
                if has_teammate:
                    mate_df = group_df[group_df['participant_id']!=target_pid].sort_values('step')
                    mate_samples = [{'x':float(r['x']),'fx':float(r['fx']),'timestamp':r['timestamp'],'is_own':0,'pid':int(r['participant_id'])} for _,r in mate_df.iterrows()]
                # Merge the two streams and sort by timestamp. The (timestamp,
                # -is_own) tie-break ensures that when an own and teammate event
                # share a timestamp, the OWN event comes FIRST. This convention
                # is mirrored exactly in deploy_success_model.py and the rollout
                # simulators; if the order ever flips, deltas computed at tied
                # timestamps will silently disagree across pipelines.
                all_samples = target_samples + mate_samples
                all_samples.sort(key=lambda s: (s['timestamp'], -s['is_own']))
                # Need at least 2 own events to form a Δfx target between
                # consecutive own samples (i.e. one event with a "next own").
                if not target_samples: continue
                payoff = target_df['payoff'].iloc[0]
                is_win = target_df['is_win'].iloc[0]
    
                # Pull this round's prior outcome for this participant. (0, 0)
                # for round 1; the previous round's (is_win, payoff/200) otherwise.
                prior_won, prior_payoff_frac = prior_outcome.get(
                    (session, game_num, rnd, int(target_pid)), (0.0, 0.0))
    
                # round_start_ts is the timestamp of the FIRST event in the
                # round — used to derive elapsed_s and time_frac. We take the
                # earliest across all events in all_samples (own + teammate).
                all_ts = [pd.to_datetime(s['timestamp']) for s in all_samples]
                round_start_ts = min(all_ts)
    
                # Per-sequence accumulators.
                features = []
                current_x_norms = []
                current_fx_norms = []
                # Running-best in raw units (best_y) and its x location (best_x);
                # target_step_count tracks own samples only (for budget_frac);
                # target_budget is the unspent token count.
                best_y, best_x, target_step_count, target_budget = 0.0, None, 0, 200
                # Spreads use only OWN samples; teammate samples don't enter the
                # focal player's "exploration variance" estimate.
                own_x_values = []
                own_fx_values = []
    
                # Previous-event scalars used for delta features. We initialize
                # to None / 0 so the very first event's deltas are 0.
                prev_x_norm = None
                prev_fx_norm = None
                prev_comp_gap = 0.0
                prev_x_spread = 0.0
                prev_y_spread = 0.0
                prev_distance_to_best_x = 0.0
                prev_distance_to_best_y = 0.0
    
                # stagnation_steps counts the number of consecutive OWN events
                # without improvement; it advances ONLY on own no-improvement
                # events and resets to 0 whenever ANY event sets a new running
                # best (own or teammate). It is then converted to fractional
                # tokens (× 10 / 200) so that 0.05 means "the player has spent
                # one own sample's worth of budget without improving".
                stagnation_steps = 0
    
                for i, sample in enumerate(all_samples):
                    x_raw, fx_raw = sample['x'], sample['fx']
                    x_norm = (x_raw - x_min_val) / domain_width
                    fx_norm = fx_raw / true_max
                    # best_y_norm / best_x_norm reflect the running-best BEFORE
                    # this event lands. Used to compute improvement and the
                    # opponent gap; we update them after the feature row is built.
                    best_y_norm = best_y/true_max if best_y>0 else 0.0
                    best_x_norm = (best_x-x_min_val)/domain_width if best_x is not None else x_norm
    
                    # comp_gap: how far ahead the opponent is at this event time,
                    # normalized to f*. Positive when the opponent is ahead, zero
                    # if we lead and we don't have visibility.
                    if has_opponent and opp_timeline:
                        opp_best = compute_opp_best_at_time(opp_timeline, sample['timestamp'])
                        opp_best_y_norm = opp_best/true_max
                        comp_gap = opp_best_y_norm - max(best_y_norm, fx_norm)
                    else:
                        comp_gap = 0.0
    
                    # Budget advances on OWN events only (teammate samples are
                    # paid by the teammate's budget, not the focal player's).
                    if sample['is_own']==1:
                        target_step_count += 1
                        target_budget = 200 - target_step_count*10
                    budget_frac = target_budget/200
    
                    # Distance-to-best is computed against the AFTER-this-event
                    # running best so it captures the move toward/away from the
                    # current peak (including this very sample).
                    updated_best_y_norm = max(best_y_norm, fx_norm)
                    updated_best_x_norm = x_norm if fx_raw>best_y else best_x_norm
    
                    distance_to_best_x = abs(x_norm - updated_best_x_norm)
                    distance_to_best_y = abs(fx_norm - updated_best_y_norm)
                    # Improvement is computed against the BEFORE-event best so
                    # that a sample which sets a new best fires a positive value;
                    # otherwise it is exactly 0. (Strictly nonneg by max(0, ·).)
                    prev_best_y_norm = best_y_norm
                    improvement = max(0.0, fx_norm - prev_best_y_norm)
    
                    # Stagnation counter logic — see big comment above the loop.
                    if improvement > 0:
                        stagnation_steps = 0
                    elif sample['is_own'] == 1:
                        stagnation_steps += 1
                    stagnation_frac = stagnation_steps * 10 / 200
    
                    ts = pd.to_datetime(sample['timestamp'])
                    elapsed_s = (ts - round_start_ts).total_seconds()
                    time_frac = min(max(elapsed_s / TIME_CAP_S, 0.0), 1.0)
    
                    # Spreads use only own samples and require >= 2 events to
                    # be defined; std() of a single value is 0 anyway, but we
                    # gate explicitly to keep the contract crisp.
                    if sample['is_own'] == 1:
                        own_x_values.append(x_norm)
                        own_fx_values.append(fx_norm)
                    x_spread = float(np.std(own_x_values)) if len(own_x_values) >= 2 else 0.0
                    y_spread = float(np.std(own_fx_values)) if len(own_fx_values) >= 2 else 0.0
    
                    # All seven delta features below are PER-EVENT deltas (i.e.
                    # they compare against the previous event in the merged
                    # stream, not the previous own event).
                    delta_x = (x_norm - prev_x_norm) if prev_x_norm is not None else 0.0
                    delta_fx = (fx_norm - prev_fx_norm) if prev_fx_norm is not None else 0.0
                    delta_comp_gap = comp_gap - prev_comp_gap
                    delta_distance_to_best_x = distance_to_best_x - prev_distance_to_best_x
                    delta_distance_to_best_y = distance_to_best_y - prev_distance_to_best_y
                    delta_spread_x = x_spread - prev_x_spread
                    delta_spread_y = y_spread - prev_y_spread
    
                    # 14-feature row, ORDER MUST MATCH downstream model and
                    # deploy/rollout mirrors. See top-of-file FEATURE ORDERING.
                    features.append([
                        delta_x,                    # 0
                        delta_fx,                   # 1
                        sample['is_own'],           # 2
                        budget_frac,                # 3
                        delta_comp_gap,             # 4
                        delta_distance_to_best_x,   # 5
                        delta_distance_to_best_y,   # 6
                        improvement,                # 7
                        delta_spread_x,             # 8
                        delta_spread_y,             # 9
                        stagnation_frac,            # 10
                        time_frac,                  # 11
                        prior_won,                  # 12  NEW (constant within round)
                        prior_payoff_frac,          # 13  NEW (constant within round)
                    ])
    
                    # Snapshot absolute coords at every event. Downstream
                    # (model_delta_default.py) adds dx_pred to current_x_norms[t]
                    # to recover absolute predictions for paper figures.
                    current_x_norms.append(x_norm)
                    current_fx_norms.append(fx_norm)
    
                    # Roll the previous-event scalars forward.
                    prev_x_norm = x_norm
                    prev_fx_norm = fx_norm
                    prev_comp_gap = comp_gap
                    prev_distance_to_best_x = distance_to_best_x
                    prev_distance_to_best_y = distance_to_best_y
                    prev_x_spread = x_spread
                    prev_y_spread = y_spread
    
                    # Update the running-best AFTER all features that depend on
                    # the pre-event best have been computed.
                    if fx_raw>best_y: best_y=fx_raw; best_x=x_raw
    
                # Teammate id (only meaningful in G2/G4); -1 elsewhere. Useful
                # downstream for fold construction and for joining back to logs.
                mate_pid = mate_samples[0]['pid'] if has_teammate and mate_samples else -1
                sequences.append({
                    'meta': {'session':session,'game_num':game_num,'round':rnd,'participant_id':target_pid,
                             'record_group_id':int(gid),'teammate_id':mate_pid,
                             'opponent_group_id':int(group_df['opponent_group_id'].iloc[0]),
                             'payoff':payoff,'is_win':is_win,'n_target_samples':len(target_samples),
                             'prior_won':prior_won,'prior_payoff_frac':prior_payoff_frac},
                    'features': np.array(features, dtype=np.float32),
                    'current_x_norms': np.array(current_x_norms, dtype=np.float32),
                    'current_fx_norms': np.array(current_fx_norms, dtype=np.float32),
                })
    return sequences
