"""CPU inference over verified historical feature prefixes.

This first integration uses the original feature cache. It does not yet build
14-feature sequences from SQL or accept new experimental data. Target arrays
are never used to make predictions. All checkpoints remain in eval mode.
"""
from pathlib import Path
import hashlib
import pickle
from threading import Lock

import numpy as np
import torch
from verify_model import DeltaLSTM, key_for

EXPECTED = {
 'model_delta_default_results.pkl': 'ab2797f96ae186fc581137e3dce74342dfc0fa2f5cb10d3e6a3cc81748c35a38',
 'model_delta_default_weights.pkl': 'e1e2433a8b18ae0018aaa5095a3c5ab393061cd74f1c9c6cabc83ae6579dd8ca',
 'preprocessed_sequences_delta_default.pkl': '4966ad1c64a736a74dee8feff0f47010a5f921654a26cf9a6836c70ce58f3f00',
}


class HistoricalPredictor:
    def __init__(self, folder):
        artifacts = {}
        for name, digest in EXPECTED.items():
            raw = (folder / name).read_bytes()
            if hashlib.sha256(raw).hexdigest() != digest:
                raise ValueError(f'{name} differs from the verified original. Re-verify artifacts before changing the model version.')
            artifacts[name] = pickle.loads(raw)
        dataset = artifacts['preprocessed_sequences_delta_default.pkl']
        self.sequences = {key_for(s):s for s in dataset['sequences']}
        self.fold_map = dataset['fold_map']
        results = artifacts['model_delta_default_results.pkl']
        self.stop_thresholds = {int(game):float(value) for game,value in results['game_thresholds'].items()}
        self.models = []
        torch.set_num_threads(1)
        for weights in artifacts['model_delta_default_weights.pkl']:
            model = DeltaLSTM()
            model.load_state_dict(weights, strict=True)
            model.eval()
            self.models.append(model)

    def predict(self, key, after_step, observed):
        seq = self.sequences.get(key)
        if seq is None:
            return {'available':False, 'reason':'This participant-round is absent from the original model cache (one-sample rounds were excluded).'}
        own = np.flatnonzero(seq['features'][:,2] > 0.5)
        if not 1 <= after_step <= len(own):
            raise ValueError('Requested step is outside the cached own-sample sequence.')
        if len(observed['samples']) != after_step:
            raise ValueError('Requested step is outside the recorded database sequence.')
        # Refuse to overlay a cached research trajectory on different SQL data.
        # At this stage the shared context still comes from the original cache.
        actual_x = np.array([r['position_fraction'] for r in observed['samples']])
        actual_y = np.array([r['quality_fraction'] for r in observed['samples']])
        if not (np.allclose(actual_x, seq['current_x_norms'][own[:after_step]], atol=1e-5, rtol=0)
                and np.allclose(actual_y, seq['current_fx_norms'][own[:after_step]], atol=1e-5, rtol=0)):
            raise ValueError('Database sample history differs from the verified model inputs.')
        t = int(own[after_step-1])
        features = torch.tensor(seq['features'][:t+1], dtype=torch.float32).unsqueeze(0)
        fold = int(self.fold_map[key])
        with torch.inference_mode():
            dx,dy,logits = self.models[fold](features,torch.tensor([t+1]))
            # Preserve float32 addition from the original scoring procedure.
            x = float(np.float32(seq['current_x_norms'][t]) + np.float32(dx[0,-1].item()))
            y = float(np.float32(seq['current_fx_norms'][t]) + np.float32(dy[0,-1].item()))
            stop = float(torch.sigmoid(logits[0,-1]))
        threshold = self.stop_thresholds[key[1]]
        n = observed['normalization']
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
            'input_source':'verified original historical feature prefix',
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
