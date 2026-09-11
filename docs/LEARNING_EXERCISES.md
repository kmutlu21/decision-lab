# Learn the repository by tracing behavior

These are reading exercises, not required changes or a new test suite. Follow the code index for numbered source.

## 1. What happens when I click Show model comparison?

**Trace:** replay.html → togglePrediction → render → loadPrediction → GET /predict → main.predict → sql_runtime.load_prefix → feature_math.build_sequences → HistoricalPredictor.predict.

**Answer:** the browser requests a historical prefix for the action currently being compared. It does not send arbitrary new samples or ask the server to train a model. All five checkpoints may be loaded on first inference, but only the assigned fold produces that sequence's prediction.

## 2. Does model.predict receive x, y, remaining budget and time directly?

**Answer:** it receives an ordered [1,T,14] float32 feature tensor. Features include x/y changes, own/mate flag, remaining budget fraction and elapsed fraction, plus other statistics/priors. Absolute current coordinates are held separately so delta outputs can be added back. It does not receive true round time remaining.

## 3. Why is a teammate test at the exact cutoff second excluded?

**Answer:** the original sort puts the focal own event first on exact ties. The prefix ends at that own event, so a same-second teammate event would occur after the endpoint in that ordering. SQL uses strict < for teammate timestamps and <= for own timestamps, with an additional own-step bound.

## 4. Why can a model say STOP while a predicted x is displayed?

**Answer:** separate heads predict whether the player stops and where the next sample would be conditional on continuation. At a revealed actual next sample, the browser labels actual action CONTINUE and may show the model's incorrect STOP classification alongside its conditional x estimate. Those outputs are not a recommended joint policy.

## 5. Why are one-sample rounds in the replay but unavailable for inference?

**Answer:** the raw importer preserves nonempty data. Model availability depends on the saved fold_map from the original training dataset. Runtime feature code can assemble a one-event prefix, but an excluded round has no assigned original model for held-out reproduction.

## 6. Can I change 200 to 300 to support a different game?

**Answer:** not as a display-only change across the whole app. Budget normalization, prior payoff scaling and stagnation scaling assume 200 in multiple modules; saved weights were trained on that representation. A new ruleset requires deliberate data/model-contract work and evaluation. Formatting payoff to zero decimals, by contrast, changes only presentation.

## 7. Where would a database password live?

**Answer:** Compose receives DECISION_LAB_DB_PASSWORD from local environment/.env and supplies it to the container as PGPASSWORD. It is not in the image source. SQL connection code reads that environment. The Duck DNS token is a different secret stored in a protected host file. Neither belongs in a screenshot or commit.

## 8. Why did /health pass before the model was loaded?

**Answer:** it only calls fetch('SELECT 1'). The predictor singleton is lazy and first loads/checks model artifacts during a prediction. A healthy database/API does not establish that the weights exist or that predictions are accurate.

## 9. Does CI test the updated competition results?

**Answer:** no. The source CI suite tests home, health, counts, samples, landscapes and invalid requests. Its database contains no model_context or real checkpoint. The separate replay verifier previously used during deployment is absent from this archive.

## 10. If I change a reference title, must I import the data again?

**Answer:** no. A replay.html change requires a new API image/container under the current explicit-copy Dockerfile. The data volume is separate. A README-only change needs neither an API rebuild nor a database import.

## 11. Is the error bracket a confidence interval?

**Answer:** no. It connects one predicted x to one observed x. For prediction .35 and actual .50, the error is 15 percentage points of domain width. No uncertainty interval is estimated by that display.

## 12. How can I explain what is still missing?

**Answer:** original fold/training evidence is outside this repo; no successful decision-support policy is deployed; threshold tuning is not an independent test; there is no continuous new-data feed or retraining/drift pipeline. These limitations define the scope of the portfolio contribution without taking away from the SQL, inference, testing and deployment work.
