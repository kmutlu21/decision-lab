> **Scope notice:** Historical migration note. PostgreSQL-built inference is already deployed. Do not follow the file replacement/restart steps again merely to install this documentation.

# Decision Lab: PostgreSQL inference API (v0.5)

Requires the successful verify_sql_features.py result from the previous update.

1. Stop the API with Ctrl+C.
2. Copy main.py, inference.py, replay.html, sql_runtime.py and
   verify_sql_runtime.py into decision-lab. Replace the first three.
   Keep feature_math.py, import_model_context.py, verify_model.py and the other
   project files. No new packages or database imports are needed.
3. Run:

```powershell
.\.venv\Scripts\python.exe verify_sql_runtime.py
```

Enter your PostgreSQL password. After PASS, restart:

```powershell
.\.venv\Scripts\python.exe main.py
```

Refresh http://127.0.0.1:8000/. The prediction status now says
"Inputs rebuilt from PostgreSQL history." /docs reports version 0.5.0.

## Request-time changes

/predict reads a consistent, read-only PostgreSQL snapshot. It selects the
requested own event, its own prefix, earlier teammate events in team games,
the stored opponent exports, prior recorded outcomes, objective normalization,
and original held-out fold. It retains the original opponent context-availability rule and uses only
opponent values through each event time within the feature builder.
Teammate observations at the exact cutoff timestamp are excluded to preserve
the original own-before-teammate tie rule. Multiple own observations at the same
time are limited by the requested step number.

No current-round payoff or winning outcome is used as an input. Only previous
available nonempty rounds provide the prior-outcome features. Missing prior
outcomes keep the original zero defaults. The feature definitions and stop
thresholds are unchanged.

The API no longer opens preprocessed_sequences_delta_default.pkl. That file
remains a reference for import/verification scripts. Runtime model weights
and the saved thresholds still come from the original weights/results files;
this is expected, since we are preserving the trained model. The inference
module verifies those artifacts' SHA256 hashes and loads them once per process.

This is historical held-out inference. Imported fold assignments remain
necessary. It is not yet a general endpoint for arbitrary new participants.
The UI caches requested predictions for a selected round; refresh/reselect
if the database changes. Missing one-sample fold assignments still produce
an available:false response with an explanation.

## Verification scope

The prior full-dataset SQL comparison covered all 1,086 sequences and all
model outputs. The new verifier checks the actual request-time prefix queries
at first, fourth (where available), and final own steps for one sequence in
each of the 12 session/game combinations. It checks reconstructed features,
predicted coordinates, stop probabilities, and stop/continue decisions.

Use the original cached reference only for verification; do not delete it.
If a comparison fails, retain the output and do not restart the new API yet.
Your committed main branch preserves the working earlier application.

