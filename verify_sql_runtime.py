"""Check the request-time SQL prefix path on every session/game before restart."""
from pathlib import Path
import pickle
import numpy as np
import torch
from psycopg import IsolationLevel
from import_model_context import connect
from sql_runtime import load_prefix
from inference import HistoricalPredictor
from verify_model import key_for


def main():
    folder=Path(__file__).resolve().parent/'models'
    with (folder/'preprocessed_sequences_delta_default.pkl').open('rb') as f:reference=pickle.load(f)
    predictor=HistoricalPredictor(folder)
    selected={}
    for seq in reference['sequences']:
        key=key_for(seq)
        selected.setdefault(key[:2],seq)
    count=0;worst=0.0
    with connect() as conn:
        conn.isolation_level=IsolationLevel.REPEATABLE_READ;conn.read_only=True
        for seq in selected.values():
            key=key_for(seq);own=np.flatnonzero(seq['features'][:,2]>.5)
            for step in sorted({1,min(4,len(own)),len(own)}):
                new,meta=load_prefix(conn,key,step)
                expected=seq['features'][:own[step-1]+1]
                if new is None or new['features'].shape!=expected.shape or not np.allclose(new['features'],expected,atol=1e-6,rtol=0):
                    raise ValueError(f'Prefix feature mismatch at {key}, step {step}')
                actual=predictor.predict(key,step,new,meta)
                reference_prefix={'features':expected,'current_x_norms':seq['current_x_norms'][:len(expected)],'current_fx_norms':seq['current_fx_norms'][:len(expected)]}
                saved_input_prediction=predictor.predict(key,step,reference_prefix,meta)
                for field in ['predicted_position_fraction','predicted_quality_fraction','stop_probability']:
                    difference=abs(actual[field]-saved_input_prediction[field]);worst=max(worst,difference)
                    if difference>1e-5:raise ValueError(f'Prediction mismatch: {key}, {field}')
                if actual['predicted_action']!=saved_input_prediction['predicted_action']:
                    raise ValueError(f'Classification mismatch: {key}, step {step}')
                count+=1
            print(f'{key[0]} game {key[1]}: request-time prefix checks passed.',flush=True)
    print(f'PASS: {count} SQL prefix predictions across {len(selected)} session/game combinations.')
    print(f'Maximum prediction difference: {worst:.8g}')
    print('Ready to restart the API with PostgreSQL-built inputs.')


if __name__=='__main__':
    try:main()
    except Exception as exc:print(f'ERROR: {exc}');raise SystemExit(1)
