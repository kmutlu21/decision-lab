# verify_sql_runtime.py

Checks representative prefixes through the actual request-time SQL loader and the production predictor.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Symbols

| Symbol | Lines |
|---|---|
| `main` | 13-43 |

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1-10 | Imports reference data, SQL prefix construction and HistoricalPredictor. torch is imported but not directly used here. |
| 13-21 | Loads the reference and fingerprint-checked predictor, then selects the first reference sequence for each session/game combination. |
| 22-27 | Uses a read-only repeatable-read snapshot and unique first/fourth/final own-step cutoffs per selected sequence. |
| 28-32 | Maps own-step count into the merged reference prefix and requires reconstructed feature parity at tolerance 1e-6. |
| 33-38 | Runs the same predictor on SQL and reference prefixes, compares x/y/stop to 1e-5 and requires identical thresholded actions. |
| 39-43 | Reports prefix count and worst prediction difference. The familiar 36 count is observed for this dataset, not a hard-coded assertion in the script. |
| 46-48 | Runs the check as a CLI and returns nonzero on any failure. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1-10 | Imports reference data, SQL prefix construction and HistoricalPredictor. torch is imported but not directly used here. |
| 2 | 1-10 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 3 | 1-10 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 4 | 1-10 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 5 | 1-10 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 6 | 1-10 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 7 | 1-10 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 8 | 1-10 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 9 | 1-10 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 10 | 1-10 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 11 | 11 | Blank separator; no execution. |
| 12 | 12 | Blank separator; no execution. |
| 13 | 13-21 | Function declaration: this body runs when called, not at declaration time. |
| 14 | 13-21 | Loads the reference and fingerprint-checked predictor, then selects the first reference sequence for each session/game combination. |
| 15 | 13-21 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 16 | 13-21 | Loads the reference and fingerprint-checked predictor, then selects the first reference sequence for each session/game combination. |
| 17 | 13-21 | Loads the reference and fingerprint-checked predictor, then selects the first reference sequence for each session/game combination. |
| 18 | 13-21 | Loop: repeats the following operations for the stated elements/condition. |
| 19 | 13-21 | Loads the reference and fingerprint-checked predictor, then selects the first reference sequence for each session/game combination. |
| 20 | 13-21 | Loads the reference and fingerprint-checked predictor, then selects the first reference sequence for each session/game combination. |
| 21 | 13-21 | Loads the reference and fingerprint-checked predictor, then selects the first reference sequence for each session/game combination. |
| 22 | 22-27 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 23 | 22-27 | Uses a read-only repeatable-read snapshot and unique first/fourth/final own-step cutoffs per selected sequence. |
| 24 | 22-27 | Loop: repeats the following operations for the stated elements/condition. |
| 25 | 22-27 | Uses a read-only repeatable-read snapshot and unique first/fourth/final own-step cutoffs per selected sequence. |
| 26 | 22-27 | Loop: repeats the following operations for the stated elements/condition. |
| 27 | 22-27 | Uses a read-only repeatable-read snapshot and unique first/fourth/final own-step cutoffs per selected sequence. |
| 28 | 28-32 | Maps own-step count into the merged reference prefix and requires reconstructed feature parity at tolerance 1e-6. |
| 29 | 28-32 | Conditional branch: determines which following statements run. |
| 30 | 28-32 | Failure path: interrupts normal execution with the stated exception. |
| 31 | 28-32 | Maps own-step count into the merged reference prefix and requires reconstructed feature parity at tolerance 1e-6. |
| 32 | 28-32 | Maps own-step count into the merged reference prefix and requires reconstructed feature parity at tolerance 1e-6. |
| 33 | 33-38 | Runs the same predictor on SQL and reference prefixes, compares x/y/stop to 1e-5 and requires identical thresholded actions. |
| 34 | 33-38 | Loop: repeats the following operations for the stated elements/condition. |
| 35 | 33-38 | Runs the same predictor on SQL and reference prefixes, compares x/y/stop to 1e-5 and requires identical thresholded actions. |
| 36 | 33-38 | Conditional branch: determines which following statements run. |
| 37 | 33-38 | Conditional branch: determines which following statements run. |
| 38 | 33-38 | Failure path: interrupts normal execution with the stated exception. |
| 39 | 39-43 | Reports prefix count and worst prediction difference. The familiar 36 count is observed for this dataset, not a hard-coded assertion in the script. |
| 40 | 39-43 | Reports prefix count and worst prediction difference. The familiar 36 count is observed for this dataset, not a hard-coded assertion in the script. |
| 41 | 39-43 | Reports prefix count and worst prediction difference. The familiar 36 count is observed for this dataset, not a hard-coded assertion in the script. |
| 42 | 39-43 | Reports prefix count and worst prediction difference. The familiar 36 count is observed for this dataset, not a hard-coded assertion in the script. |
| 43 | 39-43 | Reports prefix count and worst prediction difference. The familiar 36 count is observed for this dataset, not a hard-coded assertion in the script. |
| 44 | 44 | Blank separator; no execution. |
| 45 | 45 | Blank separator; no execution. |
| 46 | 46-48 | Conditional branch: determines which following statements run. |
| 47 | 46-48 | Exception-control block: separates normal work, error handling and cleanup. |
| 48 | 46-48 | Exception-control block: separates normal work, error handling and cleanup. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  """Check the request-time SQL prefix path on every session/game before restart."""
   2  from pathlib import Path
   3  import pickle
   4  import numpy as np
   5  import torch
   6  from psycopg import IsolationLevel
   7  from import_model_context import connect
   8  from sql_runtime import load_prefix
   9  from inference import HistoricalPredictor
  10  from verify_model import key_for
  11  
  12  
  13  def main():
  14      folder=Path(__file__).resolve().parent/'models'
  15      with (folder/'preprocessed_sequences_delta_default.pkl').open('rb') as f:reference=pickle.load(f)
  16      predictor=HistoricalPredictor(folder)
  17      selected={}
  18      for seq in reference['sequences']:
  19          key=key_for(seq)
  20          selected.setdefault(key[:2],seq)
  21      count=0;worst=0.0
  22      with connect() as conn:
  23          conn.isolation_level=IsolationLevel.REPEATABLE_READ;conn.read_only=True
  24          for seq in selected.values():
  25              key=key_for(seq);own=np.flatnonzero(seq['features'][:,2]>.5)
  26              for step in sorted({1,min(4,len(own)),len(own)}):
  27                  new,meta=load_prefix(conn,key,step)
  28                  expected=seq['features'][:own[step-1]+1]
  29                  if new is None or new['features'].shape!=expected.shape or not np.allclose(new['features'],expected,atol=1e-6,rtol=0):
  30                      raise ValueError(f'Prefix feature mismatch at {key}, step {step}')
  31                  actual=predictor.predict(key,step,new,meta)
  32                  reference_prefix={'features':expected,'current_x_norms':seq['current_x_norms'][:len(expected)],'current_fx_norms':seq['current_fx_norms'][:len(expected)]}
  33                  saved_input_prediction=predictor.predict(key,step,reference_prefix,meta)
  34                  for field in ['predicted_position_fraction','predicted_quality_fraction','stop_probability']:
  35                      difference=abs(actual[field]-saved_input_prediction[field]);worst=max(worst,difference)
  36                      if difference>1e-5:raise ValueError(f'Prediction mismatch: {key}, {field}')
  37                  if actual['predicted_action']!=saved_input_prediction['predicted_action']:
  38                      raise ValueError(f'Classification mismatch: {key}, step {step}')
  39                  count+=1
  40              print(f'{key[0]} game {key[1]}: request-time prefix checks passed.',flush=True)
  41      print(f'PASS: {count} SQL prefix predictions across {len(selected)} session/game combinations.')
  42      print(f'Maximum prediction difference: {worst:.8g}')
  43      print('Ready to restart the API with PostgreSQL-built inputs.')
  44  
  45  
  46  if __name__=='__main__':
  47      try:main()
  48      except Exception as exc:print(f'ERROR: {exc}');raise SystemExit(1)
```
