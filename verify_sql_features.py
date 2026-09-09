"""Verify PostgreSQL feature reconstruction before changing inference.
Reads originals only as comparison references; never modifies the API or data.
"""
from pathlib import Path
import pickle
import numpy as np
import torch
from psycopg import IsolationLevel
from import_model_context import connect
from sql_features import rebuild_from_database
from verify_model import DeltaLSTM, key_for


def main():
    folder=Path(__file__).resolve().parent/'models'
    with (folder/'preprocessed_sequences_delta_default.pkl').open('rb') as f:original=pickle.load(f)
    with (folder/'model_delta_default_weights.pkl').open('rb') as f:weights=pickle.load(f)
    print('Reading PostgreSQL and rebuilding features…',flush=True)
    with connect() as conn:
        conn.isolation_level=IsolationLevel.REPEATABLE_READ
        conn.read_only=True
        rebuilt,folds=rebuild_from_database(conn)
    refs={key_for(s):s for s in original['sequences']}
    if set(refs)!=set(rebuilt) or folds!=original['fold_map']:
        raise ValueError('Sequence identities or held-out fold assignments differ.')
    max_feature_difference=0.0
    for key,ref in refs.items():
        new=rebuilt[key]
        for field in ['features','current_x_norms','current_fx_norms']:
            a,b=ref[field],new[field]
            if a.shape!=b.shape:raise ValueError(f'Shape mismatch: {key}, {field}: {a.shape} vs {b.shape}')
            difference=float(np.max(np.abs(a-b)))
            max_feature_difference=max(max_feature_difference,difference)
            if not np.allclose(a,b,atol=1e-6,rtol=0):
                index=np.unravel_index(np.argmax(np.abs(a-b)),a.shape)
                raise ValueError(f'Feature mismatch: {key}, {field}, index {index}, difference {difference}')
    print(f'PASS: {len(refs):,} sequences and fold assignments match.',flush=True)
    print(f'Maximum feature/coordinate difference: {max_feature_difference:.8g}',flush=True)
    torch.set_num_threads(1)
    max_prediction_difference=0.0;position_count=stop_count=0
    with torch.inference_mode():
        for fold in range(5):
            model=DeltaLSTM();model.load_state_dict(weights[fold],strict=True);model.eval()
            for key,ref in refs.items():
                if folds[key]!=fold:continue
                outputs=[]
                for seq in [ref,rebuilt[key]]:
                    x=torch.tensor(seq['features'],dtype=torch.float32).unsqueeze(0)
                    outputs.append(model(x,torch.tensor([x.shape[1]])))
                for original_output,new_output in zip(*outputs):
                    difference=float((original_output-new_output).abs().max())
                    max_prediction_difference=max(max_prediction_difference,difference)
                    if difference>1e-5:raise ValueError(f'Model output differs: {key}, {difference}')
                position_count+=int(np.isfinite(ref['targets_dx']).sum())
                stop_count+=int(np.isfinite(ref['targets_stop']).sum())
            print(f'Fold {fold+1}/5 prediction comparison passed.',flush=True)
    print(f'Matched {position_count:,} next-position/value targets and {stop_count:,} stop targets.')
    print(f'Maximum model-output difference: {max_prediction_difference:.8g}')
    print('PASS: SQL-built inputs reproduce the original model behavior.')
    print('The running application is unchanged. These results are the gate for the next API update.')


if __name__=='__main__':
    try:main()
    except Exception as exc:
        print(f'ERROR: {exc}');raise SystemExit(1)
