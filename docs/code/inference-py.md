# inference.py

Loads fingerprinted original checkpoints and saved stopping thresholds once per process, then predicts from a SQL-built prefix.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Symbols

| Symbol | Lines |
|---|---|
| `HistoricalPredictor` | 22-69 |
| `__init__` | 23-38 |
| `predict` | 40-69 |
| `get_predictor` | 76-81 |

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1-14 | Imports the network architecture from verify_model. Its __main__ guard prevents the verification job running during an import. |
| 16-19 | Pins the exact SHA256 digests of the weights and results artifacts. These are integrity references, not credentials. |
| 22-29 | For each expected artifact, reads bytes and validates the digest BEFORE pickle deserialization. Changed bytes require deliberate reverification. |
| 30-31 | Extracts per-game stopping cutoffs from saved results. This code does not optimize F1 or recalibrate probabilities. |
| 32-38 | Creates all five CPU networks, sets a single PyTorch compute thread, loads parameters strictly and disables training dropout with eval(). |
| 40-45 | Returns an unavailable result for a missing fold; otherwise converts the full observed prefix into float32 shape [1, T, 14]. SQL is responsible for prefix validity. |
| 46-51 | Runs only the assigned zero-based held-out fold, not a five-model ensemble. Adds predicted deltas to current coordinates using float32 and applies sigmoid to the stop logit. |
| 52-53 | Selects the threshold using game number, which is key[1]. Metadata supplies bounds and objective maximum. |
| 54-60 | Returns normalized predictions and conversions to original units. The y head remains in the API for compatibility but is not drawn by the current UI. |
| 61-65 | Uses probability >= threshold for STOP. Records the saved threshold origin and flags, rather than clips, out-of-domain x predictions. |
| 66-69 | Labels model/input versions and interpretation. The sigmoid score is uncalibrated; sequence ending combines submission and timeout. |
| 72-81 | A lock protects lazy creation of a process-local singleton. Later calls reuse models; multiple Uvicorn processes would each keep their own copy. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1-14 | Imports the network architecture from verify_model. Its __main__ guard prevents the verification job running during an import. |
| 2 | 1-14 | Blank separator; no execution. |
| 3 | 1-14 | Imports the network architecture from verify_model. Its __main__ guard prevents the verification job running during an import. |
| 4 | 1-14 | Imports the network architecture from verify_model. Its __main__ guard prevents the verification job running during an import. |
| 5 | 1-14 | Imports the network architecture from verify_model. Its __main__ guard prevents the verification job running during an import. |
| 6 | 1-14 | Imports the network architecture from verify_model. Its __main__ guard prevents the verification job running during an import. |
| 7 | 1-14 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 8 | 1-14 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 9 | 1-14 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 10 | 1-14 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 11 | 1-14 | Blank separator; no execution. |
| 12 | 1-14 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 13 | 1-14 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 14 | 1-14 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 15 | 15 | Blank separator; no execution. |
| 16 | 16-19 | Pins the exact SHA256 digests of the weights and results artifacts. These are integrity references, not credentials. |
| 17 | 16-19 | Pins the exact SHA256 digests of the weights and results artifacts. These are integrity references, not credentials. |
| 18 | 16-19 | Pins the exact SHA256 digests of the weights and results artifacts. These are integrity references, not credentials. |
| 19 | 16-19 | Closes the multiline expression or payload begun above. |
| 20 | 20 | Blank separator; no execution. |
| 21 | 21 | Blank separator; no execution. |
| 22 | 22-29 | Class declaration: groups the following methods into a reusable type. |
| 23 | 22-29 | Function declaration: this body runs when called, not at declaration time. |
| 24 | 22-29 | For each expected artifact, reads bytes and validates the digest BEFORE pickle deserialization. Changed bytes require deliberate reverification. |
| 25 | 22-29 | Loop: repeats the following operations for the stated elements/condition. |
| 26 | 22-29 | For each expected artifact, reads bytes and validates the digest BEFORE pickle deserialization. Changed bytes require deliberate reverification. |
| 27 | 22-29 | Conditional branch: determines which following statements run. |
| 28 | 22-29 | Failure path: interrupts normal execution with the stated exception. |
| 29 | 22-29 | For each expected artifact, reads bytes and validates the digest BEFORE pickle deserialization. Changed bytes require deliberate reverification. |
| 30 | 30-31 | Extracts per-game stopping cutoffs from saved results. This code does not optimize F1 or recalibrate probabilities. |
| 31 | 30-31 | Extracts per-game stopping cutoffs from saved results. This code does not optimize F1 or recalibrate probabilities. |
| 32 | 32-38 | Creates all five CPU networks, sets a single PyTorch compute thread, loads parameters strictly and disables training dropout with eval(). |
| 33 | 32-38 | Creates all five CPU networks, sets a single PyTorch compute thread, loads parameters strictly and disables training dropout with eval(). |
| 34 | 32-38 | Loop: repeats the following operations for the stated elements/condition. |
| 35 | 32-38 | Creates all five CPU networks, sets a single PyTorch compute thread, loads parameters strictly and disables training dropout with eval(). |
| 36 | 32-38 | Creates all five CPU networks, sets a single PyTorch compute thread, loads parameters strictly and disables training dropout with eval(). |
| 37 | 32-38 | Creates all five CPU networks, sets a single PyTorch compute thread, loads parameters strictly and disables training dropout with eval(). |
| 38 | 32-38 | Creates all five CPU networks, sets a single PyTorch compute thread, loads parameters strictly and disables training dropout with eval(). |
| 39 | 39 | Blank separator; no execution. |
| 40 | 40-45 | Function declaration: this body runs when called, not at declaration time. |
| 41 | 40-45 | Conditional branch: determines which following statements run. |
| 42 | 40-45 | Return: sends this result to the caller and ends this invocation. |
| 43 | 40-45 | Returns an unavailable result for a missing fold; otherwise converts the full observed prefix into float32 shape [1, T, 14]. SQL is responsible for prefix validity. |
| 44 | 40-45 | Returns an unavailable result for a missing fold; otherwise converts the full observed prefix into float32 shape [1, T, 14]. SQL is responsible for prefix validity. |
| 45 | 40-45 | Returns an unavailable result for a missing fold; otherwise converts the full observed prefix into float32 shape [1, T, 14]. SQL is responsible for prefix validity. |
| 46 | 46-51 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 47 | 46-51 | Runs only the assigned zero-based held-out fold, not a five-model ensemble. Adds predicted deltas to current coordinates using float32 and applies sigmoid to the stop logit. |
| 48 | 46-51 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 49 | 46-51 | Runs only the assigned zero-based held-out fold, not a five-model ensemble. Adds predicted deltas to current coordinates using float32 and applies sigmoid to the stop logit. |
| 50 | 46-51 | Runs only the assigned zero-based held-out fold, not a five-model ensemble. Adds predicted deltas to current coordinates using float32 and applies sigmoid to the stop logit. |
| 51 | 46-51 | Runs only the assigned zero-based held-out fold, not a five-model ensemble. Adds predicted deltas to current coordinates using float32 and applies sigmoid to the stop logit. |
| 52 | 52-53 | Selects the threshold using game number, which is key[1]. Metadata supplies bounds and objective maximum. |
| 53 | 52-53 | Selects the threshold using game number, which is key[1]. Metadata supplies bounds and objective maximum. |
| 54 | 54-60 | Return: sends this result to the caller and ends this invocation. |
| 55 | 54-60 | Returns normalized predictions and conversions to original units. The y head remains in the API for compatibility but is not drawn by the current UI. |
| 56 | 54-60 | Returns normalized predictions and conversions to original units. The y head remains in the API for compatibility but is not drawn by the current UI. |
| 57 | 54-60 | Returns normalized predictions and conversions to original units. The y head remains in the API for compatibility but is not drawn by the current UI. |
| 58 | 54-60 | Returns normalized predictions and conversions to original units. The y head remains in the API for compatibility but is not drawn by the current UI. |
| 59 | 54-60 | Returns normalized predictions and conversions to original units. The y head remains in the API for compatibility but is not drawn by the current UI. |
| 60 | 54-60 | Returns normalized predictions and conversions to original units. The y head remains in the API for compatibility but is not drawn by the current UI. |
| 61 | 61-65 | Uses probability >= threshold for STOP. Records the saved threshold origin and flags, rather than clips, out-of-domain x predictions. |
| 62 | 61-65 | Uses probability >= threshold for STOP. Records the saved threshold origin and flags, rather than clips, out-of-domain x predictions. |
| 63 | 61-65 | Uses probability >= threshold for STOP. Records the saved threshold origin and flags, rather than clips, out-of-domain x predictions. |
| 64 | 61-65 | Uses probability >= threshold for STOP. Records the saved threshold origin and flags, rather than clips, out-of-domain x predictions. |
| 65 | 61-65 | Uses probability >= threshold for STOP. Records the saved threshold origin and flags, rather than clips, out-of-domain x predictions. |
| 66 | 66-69 | Labels model/input versions and interpretation. The sigmoid score is uncalibrated; sequence ending combines submission and timeout. |
| 67 | 66-69 | Labels model/input versions and interpretation. The sigmoid score is uncalibrated; sequence ending combines submission and timeout. |
| 68 | 66-69 | Labels model/input versions and interpretation. The sigmoid score is uncalibrated; sequence ending combines submission and timeout. |
| 69 | 66-69 | Closes the multiline expression or payload begun above. |
| 70 | 70 | Blank separator; no execution. |
| 71 | 71 | Blank separator; no execution. |
| 72 | 72-81 | A lock protects lazy creation of a process-local singleton. Later calls reuse models; multiple Uvicorn processes would each keep their own copy. |
| 73 | 72-81 | A lock protects lazy creation of a process-local singleton. Later calls reuse models; multiple Uvicorn processes would each keep their own copy. |
| 74 | 72-81 | Blank separator; no execution. |
| 75 | 72-81 | Blank separator; no execution. |
| 76 | 72-81 | Function declaration: this body runs when called, not at declaration time. |
| 77 | 72-81 | A lock protects lazy creation of a process-local singleton. Later calls reuse models; multiple Uvicorn processes would each keep their own copy. |
| 78 | 72-81 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 79 | 72-81 | Conditional branch: determines which following statements run. |
| 80 | 72-81 | A lock protects lazy creation of a process-local singleton. Later calls reuse models; multiple Uvicorn processes would each keep their own copy. |
| 81 | 72-81 | Return: sends this result to the caller and ends this invocation. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  """CPU inference over verified historical feature prefixes.
   2  
   3  Features are rebuilt from a PostgreSQL event prefix for each request.
   4  The original preprocessing cache is not opened at runtime. Target arrays
   5  are never used to make predictions. All checkpoints remain in eval mode.
   6  """
   7  from pathlib import Path
   8  import hashlib
   9  import pickle
  10  from threading import Lock
  11  
  12  import numpy as np
  13  import torch
  14  from verify_model import DeltaLSTM
  15  
  16  EXPECTED = {
  17   'model_delta_default_results.pkl': 'ab2797f96ae186fc581137e3dce74342dfc0fa2f5cb10d3e6a3cc81748c35a38',
  18   'model_delta_default_weights.pkl': 'e1e2433a8b18ae0018aaa5095a3c5ab393061cd74f1c9c6cabc83ae6579dd8ca',
  19  }
  20  
  21  
  22  class HistoricalPredictor:
  23      def __init__(self, folder):
  24          artifacts = {}
  25          for name, digest in EXPECTED.items():
  26              raw = (folder / name).read_bytes()
  27              if hashlib.sha256(raw).hexdigest() != digest:
  28                  raise ValueError(f'{name} differs from the verified original. Re-verify artifacts before changing the model version.')
  29              artifacts[name] = pickle.loads(raw)
  30          results = artifacts['model_delta_default_results.pkl']
  31          self.stop_thresholds = {int(game):float(value) for game,value in results['game_thresholds'].items()}
  32          self.models = []
  33          torch.set_num_threads(1)
  34          for weights in artifacts['model_delta_default_weights.pkl']:
  35              model = DeltaLSTM()
  36              model.load_state_dict(weights, strict=True)
  37              model.eval()
  38              self.models.append(model)
  39  
  40      def predict(self, key, after_step, seq, meta):
  41          if seq is None:
  42              return {'available':False, 'reason':'This round was excluded from the original model (fewer than two own samples).'}
  43          t = len(seq['features'])-1
  44          features = torch.tensor(seq['features'], dtype=torch.float32).unsqueeze(0)
  45          fold = int(meta['held_out_fold'])
  46          with torch.inference_mode():
  47              dx,dy,logits = self.models[fold](features,torch.tensor([t+1]))
  48              # Preserve float32 addition from the original scoring procedure.
  49              x = float(np.float32(seq['current_x_norms'][t]) + np.float32(dx[0,-1].item()))
  50              y = float(np.float32(seq['current_fx_norms'][t]) + np.float32(dy[0,-1].item()))
  51              stop = float(torch.sigmoid(logits[0,-1]))
  52          threshold = self.stop_thresholds[key[1]]
  53          n = meta
  54          return {
  55              'available':True, 'after_step':after_step, 'held_out_fold':fold+1,
  56              'predicted_position_fraction':x, 'predicted_quality_fraction':y,
  57              'predicted_x_value':n['x_min']+x*(n['x_max']-n['x_min']),
  58              'predicted_objective_value':y*n['estimated_maximum'],
  59              'stop_score':stop,  # Retained for API compatibility.
  60              'stop_probability':stop,
  61              'stop_threshold':threshold,
  62              'predicted_action':'stop' if stop >= threshold else 'continue',
  63              'threshold_source':'saved per-game F1-maximizing out-of-fold threshold',
  64              'position_outside_domain':not 0 <= x <= 1,
  65              'context_events':t+1,
  66              'model_version':'default-14-features-original-oof-v1',
  67              'input_source':'PostgreSQL event prefix; features computed at request time',
  68              'interpretation':'Next sample conditional on continuing; stopping probability is uncalibrated; predicted stop covers both submission and timeout.',
  69          }
  70  
  71  
  72  _predictor = None
  73  _lock = Lock()
  74  
  75  
  76  def get_predictor():
  77      global _predictor
  78      with _lock:
  79          if _predictor is None:
  80              _predictor = HistoricalPredictor(Path(__file__).resolve().parent/'models')
  81          return _predictor
```
