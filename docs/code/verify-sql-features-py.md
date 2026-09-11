# verify_sql_features.py

Checks full-dataset SQL reconstruction against the reference features and the outputs of the same original checkpoints.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Symbols

| Symbol | Lines |
|---|---|
| `main` | 14-60 |

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1-11 | Imports reference loaders, model architecture and full SQL reconstruction. Reference pickles are trusted and not hash-gated in this script. |
| 14-22 | Loads private cached sequences/weights and reconstructs SQL inputs in a consistent read-only repeatable-read snapshot. |
| 23-25 | Requires identical sequence identities and fold_map, rather than creating new validation splits. |
| 26-37 | Checks features and current coordinates for identical shape and absolute error <=1e-6, reporting the exact failing key/field/index. |
| 38-49 | Evaluates both cached and rebuilt sequences using each sequence's assigned original checkpoint in eval/inference mode. |
| 50-57 | Requires model-output error <=1e-5 and counts finite next-position and stop reference targets. These are parity counts, not accuracy metrics. |
| 58-60 | Reports reproduction status. The final wording is a historical migration gate, not a command to replace the current API again. |
| 63-66 | Runs main only as a script and exits nonzero on a failed comparison. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1-11 | Imports reference loaders, model architecture and full SQL reconstruction. Reference pickles are trusted and not hash-gated in this script. |
| 2 | 1-11 | Imports reference loaders, model architecture and full SQL reconstruction. Reference pickles are trusted and not hash-gated in this script. |
| 3 | 1-11 | Imports reference loaders, model architecture and full SQL reconstruction. Reference pickles are trusted and not hash-gated in this script. |
| 4 | 1-11 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 5 | 1-11 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 6 | 1-11 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 7 | 1-11 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 8 | 1-11 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 9 | 1-11 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 10 | 1-11 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 11 | 1-11 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 12 | 12 | Blank separator; no execution. |
| 13 | 13 | Blank separator; no execution. |
| 14 | 14-22 | Function declaration: this body runs when called, not at declaration time. |
| 15 | 14-22 | Loads private cached sequences/weights and reconstructs SQL inputs in a consistent read-only repeatable-read snapshot. |
| 16 | 14-22 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 17 | 14-22 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 18 | 14-22 | Loads private cached sequences/weights and reconstructs SQL inputs in a consistent read-only repeatable-read snapshot. |
| 19 | 14-22 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 20 | 14-22 | Loads private cached sequences/weights and reconstructs SQL inputs in a consistent read-only repeatable-read snapshot. |
| 21 | 14-22 | Loads private cached sequences/weights and reconstructs SQL inputs in a consistent read-only repeatable-read snapshot. |
| 22 | 14-22 | Loads private cached sequences/weights and reconstructs SQL inputs in a consistent read-only repeatable-read snapshot. |
| 23 | 23-25 | Requires identical sequence identities and fold_map, rather than creating new validation splits. |
| 24 | 23-25 | Conditional branch: determines which following statements run. |
| 25 | 23-25 | Failure path: interrupts normal execution with the stated exception. |
| 26 | 26-37 | Checks features and current coordinates for identical shape and absolute error <=1e-6, reporting the exact failing key/field/index. |
| 27 | 26-37 | Loop: repeats the following operations for the stated elements/condition. |
| 28 | 26-37 | Checks features and current coordinates for identical shape and absolute error <=1e-6, reporting the exact failing key/field/index. |
| 29 | 26-37 | Loop: repeats the following operations for the stated elements/condition. |
| 30 | 26-37 | Checks features and current coordinates for identical shape and absolute error <=1e-6, reporting the exact failing key/field/index. |
| 31 | 26-37 | Conditional branch: determines which following statements run. |
| 32 | 26-37 | Checks features and current coordinates for identical shape and absolute error <=1e-6, reporting the exact failing key/field/index. |
| 33 | 26-37 | Checks features and current coordinates for identical shape and absolute error <=1e-6, reporting the exact failing key/field/index. |
| 34 | 26-37 | Conditional branch: determines which following statements run. |
| 35 | 26-37 | Checks features and current coordinates for identical shape and absolute error <=1e-6, reporting the exact failing key/field/index. |
| 36 | 26-37 | Failure path: interrupts normal execution with the stated exception. |
| 37 | 26-37 | Checks features and current coordinates for identical shape and absolute error <=1e-6, reporting the exact failing key/field/index. |
| 38 | 38-49 | Evaluates both cached and rebuilt sequences using each sequence's assigned original checkpoint in eval/inference mode. |
| 39 | 38-49 | Evaluates both cached and rebuilt sequences using each sequence's assigned original checkpoint in eval/inference mode. |
| 40 | 38-49 | Evaluates both cached and rebuilt sequences using each sequence's assigned original checkpoint in eval/inference mode. |
| 41 | 38-49 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 42 | 38-49 | Loop: repeats the following operations for the stated elements/condition. |
| 43 | 38-49 | Evaluates both cached and rebuilt sequences using each sequence's assigned original checkpoint in eval/inference mode. |
| 44 | 38-49 | Loop: repeats the following operations for the stated elements/condition. |
| 45 | 38-49 | Conditional branch: determines which following statements run. |
| 46 | 38-49 | Evaluates both cached and rebuilt sequences using each sequence's assigned original checkpoint in eval/inference mode. |
| 47 | 38-49 | Loop: repeats the following operations for the stated elements/condition. |
| 48 | 38-49 | Evaluates both cached and rebuilt sequences using each sequence's assigned original checkpoint in eval/inference mode. |
| 49 | 38-49 | Evaluates both cached and rebuilt sequences using each sequence's assigned original checkpoint in eval/inference mode. |
| 50 | 50-57 | Loop: repeats the following operations for the stated elements/condition. |
| 51 | 50-57 | Requires model-output error <=1e-5 and counts finite next-position and stop reference targets. These are parity counts, not accuracy metrics. |
| 52 | 50-57 | Requires model-output error <=1e-5 and counts finite next-position and stop reference targets. These are parity counts, not accuracy metrics. |
| 53 | 50-57 | Conditional branch: determines which following statements run. |
| 54 | 50-57 | Requires model-output error <=1e-5 and counts finite next-position and stop reference targets. These are parity counts, not accuracy metrics. |
| 55 | 50-57 | Requires model-output error <=1e-5 and counts finite next-position and stop reference targets. These are parity counts, not accuracy metrics. |
| 56 | 50-57 | Requires model-output error <=1e-5 and counts finite next-position and stop reference targets. These are parity counts, not accuracy metrics. |
| 57 | 50-57 | Requires model-output error <=1e-5 and counts finite next-position and stop reference targets. These are parity counts, not accuracy metrics. |
| 58 | 58-60 | Reports reproduction status. The final wording is a historical migration gate, not a command to replace the current API again. |
| 59 | 58-60 | Reports reproduction status. The final wording is a historical migration gate, not a command to replace the current API again. |
| 60 | 58-60 | Reports reproduction status. The final wording is a historical migration gate, not a command to replace the current API again. |
| 61 | 61 | Blank separator; no execution. |
| 62 | 62 | Blank separator; no execution. |
| 63 | 63-66 | Conditional branch: determines which following statements run. |
| 64 | 63-66 | Exception-control block: separates normal work, error handling and cleanup. |
| 65 | 63-66 | Exception-control block: separates normal work, error handling and cleanup. |
| 66 | 63-66 | Runs main only as a script and exits nonzero on a failed comparison. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  """Verify PostgreSQL feature reconstruction before changing inference.
   2  Reads originals only as comparison references; never modifies the API or data.
   3  """
   4  from pathlib import Path
   5  import pickle
   6  import numpy as np
   7  import torch
   8  from psycopg import IsolationLevel
   9  from import_model_context import connect
  10  from sql_features import rebuild_from_database
  11  from verify_model import DeltaLSTM, key_for
  12  
  13  
  14  def main():
  15      folder=Path(__file__).resolve().parent/'models'
  16      with (folder/'preprocessed_sequences_delta_default.pkl').open('rb') as f:original=pickle.load(f)
  17      with (folder/'model_delta_default_weights.pkl').open('rb') as f:weights=pickle.load(f)
  18      print('Reading PostgreSQL and rebuilding features…',flush=True)
  19      with connect() as conn:
  20          conn.isolation_level=IsolationLevel.REPEATABLE_READ
  21          conn.read_only=True
  22          rebuilt,folds=rebuild_from_database(conn)
  23      refs={key_for(s):s for s in original['sequences']}
  24      if set(refs)!=set(rebuilt) or folds!=original['fold_map']:
  25          raise ValueError('Sequence identities or held-out fold assignments differ.')
  26      max_feature_difference=0.0
  27      for key,ref in refs.items():
  28          new=rebuilt[key]
  29          for field in ['features','current_x_norms','current_fx_norms']:
  30              a,b=ref[field],new[field]
  31              if a.shape!=b.shape:raise ValueError(f'Shape mismatch: {key}, {field}: {a.shape} vs {b.shape}')
  32              difference=float(np.max(np.abs(a-b)))
  33              max_feature_difference=max(max_feature_difference,difference)
  34              if not np.allclose(a,b,atol=1e-6,rtol=0):
  35                  index=np.unravel_index(np.argmax(np.abs(a-b)),a.shape)
  36                  raise ValueError(f'Feature mismatch: {key}, {field}, index {index}, difference {difference}')
  37      print(f'PASS: {len(refs):,} sequences and fold assignments match.',flush=True)
  38      print(f'Maximum feature/coordinate difference: {max_feature_difference:.8g}',flush=True)
  39      torch.set_num_threads(1)
  40      max_prediction_difference=0.0;position_count=stop_count=0
  41      with torch.inference_mode():
  42          for fold in range(5):
  43              model=DeltaLSTM();model.load_state_dict(weights[fold],strict=True);model.eval()
  44              for key,ref in refs.items():
  45                  if folds[key]!=fold:continue
  46                  outputs=[]
  47                  for seq in [ref,rebuilt[key]]:
  48                      x=torch.tensor(seq['features'],dtype=torch.float32).unsqueeze(0)
  49                      outputs.append(model(x,torch.tensor([x.shape[1]])))
  50                  for original_output,new_output in zip(*outputs):
  51                      difference=float((original_output-new_output).abs().max())
  52                      max_prediction_difference=max(max_prediction_difference,difference)
  53                      if difference>1e-5:raise ValueError(f'Model output differs: {key}, {difference}')
  54                  position_count+=int(np.isfinite(ref['targets_dx']).sum())
  55                  stop_count+=int(np.isfinite(ref['targets_stop']).sum())
  56              print(f'Fold {fold+1}/5 prediction comparison passed.',flush=True)
  57      print(f'Matched {position_count:,} next-position/value targets and {stop_count:,} stop targets.')
  58      print(f'Maximum model-output difference: {max_prediction_difference:.8g}')
  59      print('PASS: SQL-built inputs reproduce the original model behavior.')
  60      print('The running application is unchanged. These results are the gate for the next API update.')
  61  
  62  
  63  if __name__=='__main__':
  64      try:main()
  65      except Exception as exc:
  66          print(f'ERROR: {exc}');raise SystemExit(1)
```
