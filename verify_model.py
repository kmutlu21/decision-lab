"""Reproduce the default LSTM's saved out-of-fold predictions on CPU.

Run: python verify_model.py
Reads the three original default-model pickle files in ./models.
Only use your trusted original research files: pickle is an executable format.
Does not import the training script, retrain, modify the API, or alter artifacts.
"""
import argparse
import hashlib
from pathlib import Path
import pickle

import numpy as np
import torch
from torch import nn
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence


class DeltaLSTM(nn.Module):
    """Architecture copied from model_delta_default.py, without training code."""
    def __init__(self, input_dim=14, hidden_dim=64, dropout=0.4):
        super().__init__()
        self.ln = nn.LayerNorm(input_dim)
        self.lstm = nn.LSTM(input_dim, hidden_dim, batch_first=True)
        self.drop = nn.Dropout(dropout)
        self.x_head = nn.Sequential(nn.Linear(hidden_dim, 32), nn.ReLU(), nn.Linear(32, 1), nn.Tanh())
        self.y_head = nn.Sequential(nn.Linear(hidden_dim, 32), nn.ReLU(), nn.Linear(32, 1), nn.Tanh())
        self.stop_head = nn.Sequential(nn.Linear(hidden_dim, 32), nn.ReLU(), nn.Linear(32, 1))

    def forward(self, x, lengths):
        x = self.ln(x)
        packed = pack_padded_sequence(x, lengths.cpu(), batch_first=True, enforce_sorted=False)
        output, _ = self.lstm(packed)
        hidden, _ = pad_packed_sequence(output, batch_first=True)
        hidden = self.drop(hidden)
        return (self.x_head(hidden).squeeze(-1), self.y_head(hidden).squeeze(-1),
                self.stop_head(hidden).squeeze(-1))


def key_for(sequence):
    meta = sequence['meta']
    return (meta['session'], int(meta['game_num']), int(meta['round']), int(meta['participant_id']))


def load_originals(folder):
    names = ['model_delta_default_weights.pkl', 'preprocessed_sequences_delta_default.pkl',
             'model_delta_default_results.pkl']
    objects = []
    for name in names:
        path = folder / name
        if not path.is_file():
            raise FileNotFoundError(f'Missing {path}. Put all three original files in models/.')
        raw = path.read_bytes()
        print(f'{name}: SHA256 {hashlib.sha256(raw).hexdigest()}')
        objects.append(pickle.loads(raw))
    return objects


def run(folder):
    torch.set_num_threads(1)
    weights, dataset, reference = load_originals(folder)
    sequences, fold_map = dataset['sequences'], dataset['fold_map']
    if len(weights) != 5 or reference['input_dim'] != 14 or reference['hidden_dim'] != 64:
        raise ValueError('Expected the five-fold, 14-input, 64-hidden default model.')
    keys = [key_for(s) for s in sequences]
    if len(set(keys)) != len(keys):
        raise ValueError('Duplicate sequence identities.')
    for seq in sequences:
        if key_for(seq) not in fold_map or fold_map[key_for(seq)] not in range(5):
            raise ValueError('Missing or invalid held-out fold assignment.')
        features = np.asarray(seq['features'])
        if features.ndim != 2 or features.shape[1] != 14 or not np.isfinite(features).all():
            raise ValueError('Invalid features in original cache.')
    print(f'Loaded {len(sequences):,} sequences; 14 input features; 5 fold models.')
    names = ['ax','px','ay','py','a_stop','p_stop','gn_x','gn_y','gn_stop',
             'step_idx_x','step_idx_y','step_idx_stop','round_x','round_stop',
             'prior_won_x','prior_payoff_x','prior_won_stop']
    reproduced = {name: [] for name in names}
    prefix_difference = 0.0
    # Preserve the exact fold-first, then original sequence order used in
    # the training script. The saved flat result arrays have no participant IDs.
    with torch.inference_mode():
        for fold in range(5):
            model = DeltaLSTM()
            model.load_state_dict(weights[fold], strict=True)
            model.eval()  # Turns off training dropout for deterministic inference.
            validation = [s for s in sequences if fold_map[key_for(s)] == fold]
            for seq_index, seq in enumerate(validation):
                features = torch.tensor(seq['features'], dtype=torch.float32).unsqueeze(0)
                length = features.shape[1]
                dx, dy, logits = model(features, torch.tensor([length]))
                # Check that truncating the input history does not change
                # predictions at that history's last step (one round per fold).
                if seq_index == 0:
                    for cut in sorted(set([1, max(1, length//2), length])):
                        prefix = model(features[:, :cut], torch.tensor([cut]))
                        for full, short in zip((dx,dy,logits),prefix):
                            prefix_difference = max(prefix_difference, float(torch.abs(full[0,cut-1]-short[0,-1])))
                dx,dy,logits = (v[0].numpy() for v in (dx,dy,logits))
                stop = 1.0 / (1.0 + np.exp(-logits))
                meta = seq['meta']
                own_index = 0
                for t in range(length):
                    if seq['features'][t,2] <= 0.5:
                        continue
                    if not np.isnan(seq['targets_dx'][t]):
                        reproduced['ax'].append(seq['current_x_norms'][t]+seq['targets_dx'][t])
                        reproduced['px'].append(seq['current_x_norms'][t]+dx[t])
                        reproduced['ay'].append(seq['current_fx_norms'][t]+seq['targets_dy'][t])
                        reproduced['py'].append(seq['current_fx_norms'][t]+dy[t])
                        for suffix in ['x','y']:
                            reproduced['gn_'+suffix].append(meta['game_num'])
                            reproduced['step_idx_'+suffix].append(own_index)
                        reproduced['round_x'].append(meta['round'])
                        reproduced['prior_won_x'].append(meta['prior_won'])
                        reproduced['prior_payoff_x'].append(meta['prior_payoff_frac'])
                    if not np.isnan(seq['targets_stop'][t]):
                        reproduced['a_stop'].append(seq['targets_stop'][t])
                        reproduced['p_stop'].append(stop[t])
                        reproduced['gn_stop'].append(meta['game_num'])
                        reproduced['step_idx_stop'].append(own_index)
                        reproduced['round_stop'].append(meta['round'])
                        reproduced['prior_won_stop'].append(meta['prior_won'])
                    own_index += 1
            print(f'Fold {fold+1}/5: {len(validation)} held-out sequences evaluated.')
    reproduced = {k:np.asarray(v) for k,v in reproduced.items()}
    failures = []
    for name, actual in reproduced.items():
        saved = np.asarray(reference['val'][name])
        if actual.shape != saved.shape:
            failures.append(f'{name}: shape {actual.shape} vs {saved.shape}')
            continue
        difference = float(np.max(np.abs(actual-saved))) if len(saved) else 0.0
        # Allow small CPU/version floating-point differences. This is on
        # normalized scales, so 1e-5 = 0.001 percentage points.
        if not np.allclose(actual, saved, atol=1e-5, rtol=0, equal_nan=False):
            failures.append(f'{name}: max absolute difference {difference:.8g}')
        if name in ('px','py','p_stop'):
            print(f'{name}: {len(actual):,} values; max absolute difference {difference:.8g}')
    print(f'Prefix/full-sequence maximum difference: {prefix_difference:.8g}')
    if prefix_difference > 1e-5:
        failures.append('Prefix/full-sequence prediction mismatch.')
    if failures:
        raise ValueError('Verification failed. Do not integrate yet.\n'+'\n'.join(failures))
    mask = reproduced['step_idx_x'] >= 3
    mae = np.abs(reproduced['ax'][mask]-reproduced['px'][mask]).mean()
    print(f'Next-position MAE after >=4 own samples: {mae:.8f} ({mae*100:.2f} percentage points).')
    print('PASS: saved predictions reproduced using the assigned held-out models.')
    print('No training or file changes performed. Next: connect verified inference to the API.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--models-dir',type=Path,default=Path(__file__).resolve().parent/'models')
    args = parser.parse_args()
    try:
        run(args.models_dir)
    except Exception as exc:
        print(f'ERROR: {exc}')
        raise SystemExit(1)
