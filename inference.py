"""CPU inference over verified historical feature prefixes.

Features are rebuilt from a PostgreSQL event prefix for each request.
The original preprocessing cache is not opened at runtime. Target arrays
are never used to make predictions. All checkpoints remain in eval mode.
"""
from pathlib import Path
import hashlib
import pickle
from threading import Lock

import numpy as np
import torch
from verify_model import DeltaLSTM

EXPECTED = {
 'model_delta_default_results.pkl': 'ab2797f96ae186fc581137e3dce74342dfc0fa2f5cb10d3e6a3cc81748c35a38',
 'model_delta_default_weights.pkl': 'e1e2433a8b18ae0018aaa5095a3c5ab393061cd74f1c9c6cabc83ae6579dd8ca',
}


class HistoricalPredictor:
    def __init__(self, folder):
        artifacts = {}
        for name, digest in EXPECTED.items():
            raw = (folder / name).read_bytes()
            if hashlib.sha256(raw).hexdigest() != digest:
                raise ValueError(f'{name} differs from the verified original. Re-verify artifacts before changing the model version.')
            artifacts[name] = pickle.loads(raw)
        results = artifacts['model_delta_default_results.pkl']
        self.stop_thresholds = {int(game):float(value) for game,value in results['game_thresholds'].items()}
        self.models = []
        torch.set_num_threads(1)
        for weights in artifacts['model_delta_default_weights.pkl']:
            model = DeltaLSTM()
            model.load_state_dict(weights, strict=True)
            model.eval()
            self.models.append(model)

    def predict(self, key, after_step, seq, meta):
        if seq is None:
            return {'available':False, 'reason':'This round was excluded from the original model (fewer than two own samples).'}
        t = len(seq['features'])-1
        features = torch.tensor(seq['features'], dtype=torch.float32).unsqueeze(0)
        fold = int(meta['held_out_fold'])
        with torch.inference_mode():
            dx,dy,logits = self.models[fold](features,torch.tensor([t+1]))
            # Preserve float32 addition from the original scoring procedure.
            x = float(np.float32(seq['current_x_norms'][t]) + np.float32(dx[0,-1].item()))
            y = float(np.float32(seq['current_fx_norms'][t]) + np.float32(dy[0,-1].item()))
            stop = float(torch.sigmoid(logits[0,-1]))
        threshold = self.stop_thresholds[key[1]]
        n = meta
        return {
            'available':True, 'after_step':after_step, 'held_out_fold':fold+1,
            'predicted_position_fraction':x, 'predicted_quality_fraction':y,
            'predicted_x_value':n['x_min']+x*(n['x_max']-n['x_min']),
            'predicted_objective_value':y*n['estimated_maximum'],
            'stop_score':stop,  # Retained for API compatibility.
            'stop_probability':stop,
            'stop_threshold':threshold,
            'predicted_action':'stop' if stop >= threshold else 'continue',
            'threshold_source':'saved per-game F1-maximizing out-of-fold threshold',
            'position_outside_domain':not 0 <= x <= 1,
            'context_events':t+1,
            'model_version':'default-14-features-original-oof-v1',
            'input_source':'PostgreSQL event prefix; features computed at request time',
            'interpretation':'Next sample conditional on continuing; stopping probability is uncalibrated; predicted stop covers both submission and timeout.',
        }


_predictor = None
_lock = Lock()


def get_predictor():
    global _predictor
    with _lock:
        if _predictor is None:
            _predictor = HistoricalPredictor(Path(__file__).resolve().parent/'models')
        return _predictor
