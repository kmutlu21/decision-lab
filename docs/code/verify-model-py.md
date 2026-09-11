# verify_model.py

Defines the deployed network architecture and separately verifies checkpoint outputs against the original saved validation arrays.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Symbols

| Symbol | Lines |
|---|---|
| `DeltaLSTM` | 19-37 |
| `__init__` | 21-28 |
| `forward` | 30-37 |
| `key_for` | 40-42 |
| `load_originals` | 45-56 |
| `run` | 59-149 |

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1-16 | Imports CPU inference and packed-sequence tools. The original artifact loader trusts supplied pickles; unlike runtime inference it prints hashes rather than enforcing pinned digests. |
| 19-28 | Builds LayerNorm(14), a single unidirectional 64-hidden LSTM, dropout 0.4 and separate 64→32→1 heads. x/y end in tanh; stopping ends in a raw logit. |
| 30-37 | Normalizes each event, packs variable-length sequences, runs the LSTM, unpacks, applies dropout and returns three [batch,time] arrays. eval mode makes dropout inactive. |
| 40-42 | Defines the canonical key as (session, game, round, participant). This differs from import_data's insertion-key field order. |
| 45-56 | Loads weights, cached sequences and saved results from models/, reporting SHA256. Pickle must be trusted; merely printing its hash does not validate it. |
| 59-72 | Checks five checkpoints, expected model dimensions, unique identities, valid fold assignments and finite [T,14] cached inputs. |
| 73-79 | Prepares arrays in the saved results' schema and a prefix-parity accumulator. Flat results lack identities, so ordering must be reproduced exactly. |
| 80-89 | Loops fold first, then original sequence order, selects held-out sequences, loads the correct checkpoint and evaluates the full sequence. |
| 90-97 | On the first sequence per fold, checks short/mid/full prefix endpoints against full-sequence outputs to catch future-context dependence. |
| 98-104 | Converts outputs to NumPy and ignores teammate output rows; own_index is zero-based. |
| 105-114 | For valid delta targets, reconstructs actual/predicted x and y and records scenario, own-step and prior-outcome metadata in matched order. |
| 115-124 | Collects stop labels/probabilities on valid own events, including terminal labels; advances own_index and reports fold counts. |
| 125-140 | Checks every rebuilt array's shape and absolute tolerance 1e-5 against saved results; also checks sampled prefix parity. Zero relative tolerance makes the criterion explicit. |
| 141-149 | Fails on any mismatch. Reports x MAE where zero-based own_index >=3, meaning prediction made AFTER own test 4 or later. This is not identical to the UI's first test-4 comparison from a test-3 prefix. |
| 152-160 | Provides a models-dir CLI and a nonzero error exit. Importing DeltaLSTM does not execute this verification block. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1-16 | Imports CPU inference and packed-sequence tools. The original artifact loader trusts supplied pickles; unlike runtime inference it prints hashes rather than enforcing pinned digests. |
| 2 | 1-16 | Blank separator; no execution. |
| 3 | 1-16 | Imports CPU inference and packed-sequence tools. The original artifact loader trusts supplied pickles; unlike runtime inference it prints hashes rather than enforcing pinned digests. |
| 4 | 1-16 | Imports CPU inference and packed-sequence tools. The original artifact loader trusts supplied pickles; unlike runtime inference it prints hashes rather than enforcing pinned digests. |
| 5 | 1-16 | Imports CPU inference and packed-sequence tools. The original artifact loader trusts supplied pickles; unlike runtime inference it prints hashes rather than enforcing pinned digests. |
| 6 | 1-16 | Imports CPU inference and packed-sequence tools. The original artifact loader trusts supplied pickles; unlike runtime inference it prints hashes rather than enforcing pinned digests. |
| 7 | 1-16 | Imports CPU inference and packed-sequence tools. The original artifact loader trusts supplied pickles; unlike runtime inference it prints hashes rather than enforcing pinned digests. |
| 8 | 1-16 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 9 | 1-16 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 10 | 1-16 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 11 | 1-16 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 12 | 1-16 | Blank separator; no execution. |
| 13 | 1-16 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 14 | 1-16 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 15 | 1-16 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 16 | 1-16 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 17 | 17 | Blank separator; no execution. |
| 18 | 18 | Blank separator; no execution. |
| 19 | 19-28 | Class declaration: groups the following methods into a reusable type. |
| 20 | 19-28 | Builds LayerNorm(14), a single unidirectional 64-hidden LSTM, dropout 0.4 and separate 64→32→1 heads. x/y end in tanh; stopping ends in a raw logit. |
| 21 | 19-28 | Function declaration: this body runs when called, not at declaration time. |
| 22 | 19-28 | Builds LayerNorm(14), a single unidirectional 64-hidden LSTM, dropout 0.4 and separate 64→32→1 heads. x/y end in tanh; stopping ends in a raw logit. |
| 23 | 19-28 | Builds LayerNorm(14), a single unidirectional 64-hidden LSTM, dropout 0.4 and separate 64→32→1 heads. x/y end in tanh; stopping ends in a raw logit. |
| 24 | 19-28 | Builds LayerNorm(14), a single unidirectional 64-hidden LSTM, dropout 0.4 and separate 64→32→1 heads. x/y end in tanh; stopping ends in a raw logit. |
| 25 | 19-28 | Builds LayerNorm(14), a single unidirectional 64-hidden LSTM, dropout 0.4 and separate 64→32→1 heads. x/y end in tanh; stopping ends in a raw logit. |
| 26 | 19-28 | Builds LayerNorm(14), a single unidirectional 64-hidden LSTM, dropout 0.4 and separate 64→32→1 heads. x/y end in tanh; stopping ends in a raw logit. |
| 27 | 19-28 | Builds LayerNorm(14), a single unidirectional 64-hidden LSTM, dropout 0.4 and separate 64→32→1 heads. x/y end in tanh; stopping ends in a raw logit. |
| 28 | 19-28 | Builds LayerNorm(14), a single unidirectional 64-hidden LSTM, dropout 0.4 and separate 64→32→1 heads. x/y end in tanh; stopping ends in a raw logit. |
| 29 | 29 | Blank separator; no execution. |
| 30 | 30-37 | Function declaration: this body runs when called, not at declaration time. |
| 31 | 30-37 | Normalizes each event, packs variable-length sequences, runs the LSTM, unpacks, applies dropout and returns three [batch,time] arrays. eval mode makes dropout inactive. |
| 32 | 30-37 | Normalizes each event, packs variable-length sequences, runs the LSTM, unpacks, applies dropout and returns three [batch,time] arrays. eval mode makes dropout inactive. |
| 33 | 30-37 | Normalizes each event, packs variable-length sequences, runs the LSTM, unpacks, applies dropout and returns three [batch,time] arrays. eval mode makes dropout inactive. |
| 34 | 30-37 | Normalizes each event, packs variable-length sequences, runs the LSTM, unpacks, applies dropout and returns three [batch,time] arrays. eval mode makes dropout inactive. |
| 35 | 30-37 | Normalizes each event, packs variable-length sequences, runs the LSTM, unpacks, applies dropout and returns three [batch,time] arrays. eval mode makes dropout inactive. |
| 36 | 30-37 | Return: sends this result to the caller and ends this invocation. |
| 37 | 30-37 | Normalizes each event, packs variable-length sequences, runs the LSTM, unpacks, applies dropout and returns three [batch,time] arrays. eval mode makes dropout inactive. |
| 38 | 38 | Blank separator; no execution. |
| 39 | 39 | Blank separator; no execution. |
| 40 | 40-42 | Function declaration: this body runs when called, not at declaration time. |
| 41 | 40-42 | Defines the canonical key as (session, game, round, participant). This differs from import_data's insertion-key field order. |
| 42 | 40-42 | Return: sends this result to the caller and ends this invocation. |
| 43 | 43 | Blank separator; no execution. |
| 44 | 44 | Blank separator; no execution. |
| 45 | 45-56 | Function declaration: this body runs when called, not at declaration time. |
| 46 | 45-56 | Loads weights, cached sequences and saved results from models/, reporting SHA256. Pickle must be trusted; merely printing its hash does not validate it. |
| 47 | 45-56 | Loads weights, cached sequences and saved results from models/, reporting SHA256. Pickle must be trusted; merely printing its hash does not validate it. |
| 48 | 45-56 | Loads weights, cached sequences and saved results from models/, reporting SHA256. Pickle must be trusted; merely printing its hash does not validate it. |
| 49 | 45-56 | Loop: repeats the following operations for the stated elements/condition. |
| 50 | 45-56 | Loads weights, cached sequences and saved results from models/, reporting SHA256. Pickle must be trusted; merely printing its hash does not validate it. |
| 51 | 45-56 | Conditional branch: determines which following statements run. |
| 52 | 45-56 | Failure path: interrupts normal execution with the stated exception. |
| 53 | 45-56 | Loads weights, cached sequences and saved results from models/, reporting SHA256. Pickle must be trusted; merely printing its hash does not validate it. |
| 54 | 45-56 | Loads weights, cached sequences and saved results from models/, reporting SHA256. Pickle must be trusted; merely printing its hash does not validate it. |
| 55 | 45-56 | Loads weights, cached sequences and saved results from models/, reporting SHA256. Pickle must be trusted; merely printing its hash does not validate it. |
| 56 | 45-56 | Return: sends this result to the caller and ends this invocation. |
| 57 | 57 | Blank separator; no execution. |
| 58 | 58 | Blank separator; no execution. |
| 59 | 59-72 | Function declaration: this body runs when called, not at declaration time. |
| 60 | 59-72 | Checks five checkpoints, expected model dimensions, unique identities, valid fold assignments and finite [T,14] cached inputs. |
| 61 | 59-72 | Checks five checkpoints, expected model dimensions, unique identities, valid fold assignments and finite [T,14] cached inputs. |
| 62 | 59-72 | Checks five checkpoints, expected model dimensions, unique identities, valid fold assignments and finite [T,14] cached inputs. |
| 63 | 59-72 | Conditional branch: determines which following statements run. |
| 64 | 59-72 | Failure path: interrupts normal execution with the stated exception. |
| 65 | 59-72 | Checks five checkpoints, expected model dimensions, unique identities, valid fold assignments and finite [T,14] cached inputs. |
| 66 | 59-72 | Conditional branch: determines which following statements run. |
| 67 | 59-72 | Failure path: interrupts normal execution with the stated exception. |
| 68 | 59-72 | Loop: repeats the following operations for the stated elements/condition. |
| 69 | 59-72 | Conditional branch: determines which following statements run. |
| 70 | 59-72 | Failure path: interrupts normal execution with the stated exception. |
| 71 | 59-72 | Checks five checkpoints, expected model dimensions, unique identities, valid fold assignments and finite [T,14] cached inputs. |
| 72 | 59-72 | Conditional branch: determines which following statements run. |
| 73 | 73-79 | Failure path: interrupts normal execution with the stated exception. |
| 74 | 73-79 | Prepares arrays in the saved results' schema and a prefix-parity accumulator. Flat results lack identities, so ordering must be reproduced exactly. |
| 75 | 73-79 | Prepares arrays in the saved results' schema and a prefix-parity accumulator. Flat results lack identities, so ordering must be reproduced exactly. |
| 76 | 73-79 | Prepares arrays in the saved results' schema and a prefix-parity accumulator. Flat results lack identities, so ordering must be reproduced exactly. |
| 77 | 73-79 | Prepares arrays in the saved results' schema and a prefix-parity accumulator. Flat results lack identities, so ordering must be reproduced exactly. |
| 78 | 73-79 | Prepares arrays in the saved results' schema and a prefix-parity accumulator. Flat results lack identities, so ordering must be reproduced exactly. |
| 79 | 73-79 | Prepares arrays in the saved results' schema and a prefix-parity accumulator. Flat results lack identities, so ordering must be reproduced exactly. |
| 80 | 80-89 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 81 | 80-89 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 82 | 80-89 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 83 | 80-89 | Loop: repeats the following operations for the stated elements/condition. |
| 84 | 80-89 | Loops fold first, then original sequence order, selects held-out sequences, loads the correct checkpoint and evaluates the full sequence. |
| 85 | 80-89 | Loops fold first, then original sequence order, selects held-out sequences, loads the correct checkpoint and evaluates the full sequence. |
| 86 | 80-89 | Loops fold first, then original sequence order, selects held-out sequences, loads the correct checkpoint and evaluates the full sequence. |
| 87 | 80-89 | Loops fold first, then original sequence order, selects held-out sequences, loads the correct checkpoint and evaluates the full sequence. |
| 88 | 80-89 | Loop: repeats the following operations for the stated elements/condition. |
| 89 | 80-89 | Loops fold first, then original sequence order, selects held-out sequences, loads the correct checkpoint and evaluates the full sequence. |
| 90 | 90-97 | On the first sequence per fold, checks short/mid/full prefix endpoints against full-sequence outputs to catch future-context dependence. |
| 91 | 90-97 | On the first sequence per fold, checks short/mid/full prefix endpoints against full-sequence outputs to catch future-context dependence. |
| 92 | 90-97 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 93 | 90-97 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 94 | 90-97 | Conditional branch: determines which following statements run. |
| 95 | 90-97 | Loop: repeats the following operations for the stated elements/condition. |
| 96 | 90-97 | On the first sequence per fold, checks short/mid/full prefix endpoints against full-sequence outputs to catch future-context dependence. |
| 97 | 90-97 | Loop: repeats the following operations for the stated elements/condition. |
| 98 | 98-104 | Converts outputs to NumPy and ignores teammate output rows; own_index is zero-based. |
| 99 | 98-104 | Converts outputs to NumPy and ignores teammate output rows; own_index is zero-based. |
| 100 | 98-104 | Converts outputs to NumPy and ignores teammate output rows; own_index is zero-based. |
| 101 | 98-104 | Converts outputs to NumPy and ignores teammate output rows; own_index is zero-based. |
| 102 | 98-104 | Converts outputs to NumPy and ignores teammate output rows; own_index is zero-based. |
| 103 | 98-104 | Loop: repeats the following operations for the stated elements/condition. |
| 104 | 98-104 | Conditional branch: determines which following statements run. |
| 105 | 105-114 | For valid delta targets, reconstructs actual/predicted x and y and records scenario, own-step and prior-outcome metadata in matched order. |
| 106 | 105-114 | Conditional branch: determines which following statements run. |
| 107 | 105-114 | For valid delta targets, reconstructs actual/predicted x and y and records scenario, own-step and prior-outcome metadata in matched order. |
| 108 | 105-114 | For valid delta targets, reconstructs actual/predicted x and y and records scenario, own-step and prior-outcome metadata in matched order. |
| 109 | 105-114 | For valid delta targets, reconstructs actual/predicted x and y and records scenario, own-step and prior-outcome metadata in matched order. |
| 110 | 105-114 | For valid delta targets, reconstructs actual/predicted x and y and records scenario, own-step and prior-outcome metadata in matched order. |
| 111 | 105-114 | Loop: repeats the following operations for the stated elements/condition. |
| 112 | 105-114 | For valid delta targets, reconstructs actual/predicted x and y and records scenario, own-step and prior-outcome metadata in matched order. |
| 113 | 105-114 | For valid delta targets, reconstructs actual/predicted x and y and records scenario, own-step and prior-outcome metadata in matched order. |
| 114 | 105-114 | For valid delta targets, reconstructs actual/predicted x and y and records scenario, own-step and prior-outcome metadata in matched order. |
| 115 | 115-124 | Collects stop labels/probabilities on valid own events, including terminal labels; advances own_index and reports fold counts. |
| 116 | 115-124 | Collects stop labels/probabilities on valid own events, including terminal labels; advances own_index and reports fold counts. |
| 117 | 115-124 | Conditional branch: determines which following statements run. |
| 118 | 115-124 | Collects stop labels/probabilities on valid own events, including terminal labels; advances own_index and reports fold counts. |
| 119 | 115-124 | Collects stop labels/probabilities on valid own events, including terminal labels; advances own_index and reports fold counts. |
| 120 | 115-124 | Collects stop labels/probabilities on valid own events, including terminal labels; advances own_index and reports fold counts. |
| 121 | 115-124 | Collects stop labels/probabilities on valid own events, including terminal labels; advances own_index and reports fold counts. |
| 122 | 115-124 | Collects stop labels/probabilities on valid own events, including terminal labels; advances own_index and reports fold counts. |
| 123 | 115-124 | Collects stop labels/probabilities on valid own events, including terminal labels; advances own_index and reports fold counts. |
| 124 | 115-124 | Collects stop labels/probabilities on valid own events, including terminal labels; advances own_index and reports fold counts. |
| 125 | 125-140 | Checks every rebuilt array's shape and absolute tolerance 1e-5 against saved results; also checks sampled prefix parity. Zero relative tolerance makes the criterion explicit. |
| 126 | 125-140 | Checks every rebuilt array's shape and absolute tolerance 1e-5 against saved results; also checks sampled prefix parity. Zero relative tolerance makes the criterion explicit. |
| 127 | 125-140 | Checks every rebuilt array's shape and absolute tolerance 1e-5 against saved results; also checks sampled prefix parity. Zero relative tolerance makes the criterion explicit. |
| 128 | 125-140 | Loop: repeats the following operations for the stated elements/condition. |
| 129 | 125-140 | Checks every rebuilt array's shape and absolute tolerance 1e-5 against saved results; also checks sampled prefix parity. Zero relative tolerance makes the criterion explicit. |
| 130 | 125-140 | Conditional branch: determines which following statements run. |
| 131 | 125-140 | Checks every rebuilt array's shape and absolute tolerance 1e-5 against saved results; also checks sampled prefix parity. Zero relative tolerance makes the criterion explicit. |
| 132 | 125-140 | Checks every rebuilt array's shape and absolute tolerance 1e-5 against saved results; also checks sampled prefix parity. Zero relative tolerance makes the criterion explicit. |
| 133 | 125-140 | Checks every rebuilt array's shape and absolute tolerance 1e-5 against saved results; also checks sampled prefix parity. Zero relative tolerance makes the criterion explicit. |
| 134 | 125-140 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 135 | 125-140 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 136 | 125-140 | Conditional branch: determines which following statements run. |
| 137 | 125-140 | Checks every rebuilt array's shape and absolute tolerance 1e-5 against saved results; also checks sampled prefix parity. Zero relative tolerance makes the criterion explicit. |
| 138 | 125-140 | Conditional branch: determines which following statements run. |
| 139 | 125-140 | Checks every rebuilt array's shape and absolute tolerance 1e-5 against saved results; also checks sampled prefix parity. Zero relative tolerance makes the criterion explicit. |
| 140 | 125-140 | Checks every rebuilt array's shape and absolute tolerance 1e-5 against saved results; also checks sampled prefix parity. Zero relative tolerance makes the criterion explicit. |
| 141 | 141-149 | Conditional branch: determines which following statements run. |
| 142 | 141-149 | Fails on any mismatch. Reports x MAE where zero-based own_index >=3, meaning prediction made AFTER own test 4 or later. This is not identical to the UI's first test-4 comparison from a test-3 prefix. |
| 143 | 141-149 | Conditional branch: determines which following statements run. |
| 144 | 141-149 | Failure path: interrupts normal execution with the stated exception. |
| 145 | 141-149 | Fails on any mismatch. Reports x MAE where zero-based own_index >=3, meaning prediction made AFTER own test 4 or later. This is not identical to the UI's first test-4 comparison from a test-3 prefix. |
| 146 | 141-149 | Fails on any mismatch. Reports x MAE where zero-based own_index >=3, meaning prediction made AFTER own test 4 or later. This is not identical to the UI's first test-4 comparison from a test-3 prefix. |
| 147 | 141-149 | Fails on any mismatch. Reports x MAE where zero-based own_index >=3, meaning prediction made AFTER own test 4 or later. This is not identical to the UI's first test-4 comparison from a test-3 prefix. |
| 148 | 141-149 | Fails on any mismatch. Reports x MAE where zero-based own_index >=3, meaning prediction made AFTER own test 4 or later. This is not identical to the UI's first test-4 comparison from a test-3 prefix. |
| 149 | 141-149 | Fails on any mismatch. Reports x MAE where zero-based own_index >=3, meaning prediction made AFTER own test 4 or later. This is not identical to the UI's first test-4 comparison from a test-3 prefix. |
| 150 | 150 | Blank separator; no execution. |
| 151 | 151 | Blank separator; no execution. |
| 152 | 152-160 | Conditional branch: determines which following statements run. |
| 153 | 152-160 | Provides a models-dir CLI and a nonzero error exit. Importing DeltaLSTM does not execute this verification block. |
| 154 | 152-160 | Provides a models-dir CLI and a nonzero error exit. Importing DeltaLSTM does not execute this verification block. |
| 155 | 152-160 | Provides a models-dir CLI and a nonzero error exit. Importing DeltaLSTM does not execute this verification block. |
| 156 | 152-160 | Exception-control block: separates normal work, error handling and cleanup. |
| 157 | 152-160 | Provides a models-dir CLI and a nonzero error exit. Importing DeltaLSTM does not execute this verification block. |
| 158 | 152-160 | Exception-control block: separates normal work, error handling and cleanup. |
| 159 | 152-160 | Provides a models-dir CLI and a nonzero error exit. Importing DeltaLSTM does not execute this verification block. |
| 160 | 152-160 | Failure path: interrupts normal execution with the stated exception. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  """Reproduce the default LSTM's saved out-of-fold predictions on CPU.
   2  
   3  Run: python verify_model.py
   4  Reads the three original default-model pickle files in ./models.
   5  Only use your trusted original research files: pickle is an executable format.
   6  Does not import the training script, retrain, modify the API, or alter artifacts.
   7  """
   8  import argparse
   9  import hashlib
  10  from pathlib import Path
  11  import pickle
  12  
  13  import numpy as np
  14  import torch
  15  from torch import nn
  16  from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence
  17  
  18  
  19  class DeltaLSTM(nn.Module):
  20      """Architecture copied from model_delta_default.py, without training code."""
  21      def __init__(self, input_dim=14, hidden_dim=64, dropout=0.4):
  22          super().__init__()
  23          self.ln = nn.LayerNorm(input_dim)
  24          self.lstm = nn.LSTM(input_dim, hidden_dim, batch_first=True)
  25          self.drop = nn.Dropout(dropout)
  26          self.x_head = nn.Sequential(nn.Linear(hidden_dim, 32), nn.ReLU(), nn.Linear(32, 1), nn.Tanh())
  27          self.y_head = nn.Sequential(nn.Linear(hidden_dim, 32), nn.ReLU(), nn.Linear(32, 1), nn.Tanh())
  28          self.stop_head = nn.Sequential(nn.Linear(hidden_dim, 32), nn.ReLU(), nn.Linear(32, 1))
  29  
  30      def forward(self, x, lengths):
  31          x = self.ln(x)
  32          packed = pack_padded_sequence(x, lengths.cpu(), batch_first=True, enforce_sorted=False)
  33          output, _ = self.lstm(packed)
  34          hidden, _ = pad_packed_sequence(output, batch_first=True)
  35          hidden = self.drop(hidden)
  36          return (self.x_head(hidden).squeeze(-1), self.y_head(hidden).squeeze(-1),
  37                  self.stop_head(hidden).squeeze(-1))
  38  
  39  
  40  def key_for(sequence):
  41      meta = sequence['meta']
  42      return (meta['session'], int(meta['game_num']), int(meta['round']), int(meta['participant_id']))
  43  
  44  
  45  def load_originals(folder):
  46      names = ['model_delta_default_weights.pkl', 'preprocessed_sequences_delta_default.pkl',
  47               'model_delta_default_results.pkl']
  48      objects = []
  49      for name in names:
  50          path = folder / name
  51          if not path.is_file():
  52              raise FileNotFoundError(f'Missing {path}. Put all three original files in models/.')
  53          raw = path.read_bytes()
  54          print(f'{name}: SHA256 {hashlib.sha256(raw).hexdigest()}')
  55          objects.append(pickle.loads(raw))
  56      return objects
  57  
  58  
  59  def run(folder):
  60      torch.set_num_threads(1)
  61      weights, dataset, reference = load_originals(folder)
  62      sequences, fold_map = dataset['sequences'], dataset['fold_map']
  63      if len(weights) != 5 or reference['input_dim'] != 14 or reference['hidden_dim'] != 64:
  64          raise ValueError('Expected the five-fold, 14-input, 64-hidden default model.')
  65      keys = [key_for(s) for s in sequences]
  66      if len(set(keys)) != len(keys):
  67          raise ValueError('Duplicate sequence identities.')
  68      for seq in sequences:
  69          if key_for(seq) not in fold_map or fold_map[key_for(seq)] not in range(5):
  70              raise ValueError('Missing or invalid held-out fold assignment.')
  71          features = np.asarray(seq['features'])
  72          if features.ndim != 2 or features.shape[1] != 14 or not np.isfinite(features).all():
  73              raise ValueError('Invalid features in original cache.')
  74      print(f'Loaded {len(sequences):,} sequences; 14 input features; 5 fold models.')
  75      names = ['ax','px','ay','py','a_stop','p_stop','gn_x','gn_y','gn_stop',
  76               'step_idx_x','step_idx_y','step_idx_stop','round_x','round_stop',
  77               'prior_won_x','prior_payoff_x','prior_won_stop']
  78      reproduced = {name: [] for name in names}
  79      prefix_difference = 0.0
  80      # Preserve the exact fold-first, then original sequence order used in
  81      # the training script. The saved flat result arrays have no participant IDs.
  82      with torch.inference_mode():
  83          for fold in range(5):
  84              model = DeltaLSTM()
  85              model.load_state_dict(weights[fold], strict=True)
  86              model.eval()  # Turns off training dropout for deterministic inference.
  87              validation = [s for s in sequences if fold_map[key_for(s)] == fold]
  88              for seq_index, seq in enumerate(validation):
  89                  features = torch.tensor(seq['features'], dtype=torch.float32).unsqueeze(0)
  90                  length = features.shape[1]
  91                  dx, dy, logits = model(features, torch.tensor([length]))
  92                  # Check that truncating the input history does not change
  93                  # predictions at that history's last step (one round per fold).
  94                  if seq_index == 0:
  95                      for cut in sorted(set([1, max(1, length//2), length])):
  96                          prefix = model(features[:, :cut], torch.tensor([cut]))
  97                          for full, short in zip((dx,dy,logits),prefix):
  98                              prefix_difference = max(prefix_difference, float(torch.abs(full[0,cut-1]-short[0,-1])))
  99                  dx,dy,logits = (v[0].numpy() for v in (dx,dy,logits))
 100                  stop = 1.0 / (1.0 + np.exp(-logits))
 101                  meta = seq['meta']
 102                  own_index = 0
 103                  for t in range(length):
 104                      if seq['features'][t,2] <= 0.5:
 105                          continue
 106                      if not np.isnan(seq['targets_dx'][t]):
 107                          reproduced['ax'].append(seq['current_x_norms'][t]+seq['targets_dx'][t])
 108                          reproduced['px'].append(seq['current_x_norms'][t]+dx[t])
 109                          reproduced['ay'].append(seq['current_fx_norms'][t]+seq['targets_dy'][t])
 110                          reproduced['py'].append(seq['current_fx_norms'][t]+dy[t])
 111                          for suffix in ['x','y']:
 112                              reproduced['gn_'+suffix].append(meta['game_num'])
 113                              reproduced['step_idx_'+suffix].append(own_index)
 114                          reproduced['round_x'].append(meta['round'])
 115                          reproduced['prior_won_x'].append(meta['prior_won'])
 116                          reproduced['prior_payoff_x'].append(meta['prior_payoff_frac'])
 117                      if not np.isnan(seq['targets_stop'][t]):
 118                          reproduced['a_stop'].append(seq['targets_stop'][t])
 119                          reproduced['p_stop'].append(stop[t])
 120                          reproduced['gn_stop'].append(meta['game_num'])
 121                          reproduced['step_idx_stop'].append(own_index)
 122                          reproduced['round_stop'].append(meta['round'])
 123                          reproduced['prior_won_stop'].append(meta['prior_won'])
 124                      own_index += 1
 125              print(f'Fold {fold+1}/5: {len(validation)} held-out sequences evaluated.')
 126      reproduced = {k:np.asarray(v) for k,v in reproduced.items()}
 127      failures = []
 128      for name, actual in reproduced.items():
 129          saved = np.asarray(reference['val'][name])
 130          if actual.shape != saved.shape:
 131              failures.append(f'{name}: shape {actual.shape} vs {saved.shape}')
 132              continue
 133          difference = float(np.max(np.abs(actual-saved))) if len(saved) else 0.0
 134          # Allow small CPU/version floating-point differences. This is on
 135          # normalized scales, so 1e-5 = 0.001 percentage points.
 136          if not np.allclose(actual, saved, atol=1e-5, rtol=0, equal_nan=False):
 137              failures.append(f'{name}: max absolute difference {difference:.8g}')
 138          if name in ('px','py','p_stop'):
 139              print(f'{name}: {len(actual):,} values; max absolute difference {difference:.8g}')
 140      print(f'Prefix/full-sequence maximum difference: {prefix_difference:.8g}')
 141      if prefix_difference > 1e-5:
 142          failures.append('Prefix/full-sequence prediction mismatch.')
 143      if failures:
 144          raise ValueError('Verification failed. Do not integrate yet.\n'+'\n'.join(failures))
 145      mask = reproduced['step_idx_x'] >= 3
 146      mae = np.abs(reproduced['ax'][mask]-reproduced['px'][mask]).mean()
 147      print(f'Next-position MAE after >=4 own samples: {mae:.8f} ({mae*100:.2f} percentage points).')
 148      print('PASS: saved predictions reproduced using the assigned held-out models.')
 149      print('No training or file changes performed. Next: connect verified inference to the API.')
 150  
 151  
 152  if __name__ == '__main__':
 153      parser = argparse.ArgumentParser(description=__doc__)
 154      parser.add_argument('--models-dir',type=Path,default=Path(__file__).resolve().parent/'models')
 155      args = parser.parse_args()
 156      try:
 157          run(args.models_dir)
 158      except Exception as exc:
 159          print(f'ERROR: {exc}')
 160          raise SystemExit(1)
```
