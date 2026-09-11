# Review notes and limitations

Source: d0afd0c367f72354259d0661a76a0119fb4ed8b2. These findings explain existing behavior; no runtime code was changed to address them.

## Documentation corrections included

| Previous wording or implication | What this source does |
|---|---|
| Original units are available in the UI | Current UI presents normalized values; raw values still exist in API fields |
| Graph shows only own samples | Games 2/4 also show teammate samples; games 3/4 show rival best scores |
| Model time starts at first own sample | feature_math starts at earliest merged own/teammate event; display time starts at first own |
| Competition gap is zero when leading | The formula permits a negative gap |
| Feature builder needs two own events | Current runtime builder accepts one; missing saved fold excludes the original one-sample rounds |
| Teammates influence own spread | They influence visible best, but spread uses only own observations |
| A fresh train/test design exists in this repo | Original folds and checkpoints are imported, not reconstructed or trained |
| CI proves the model and new replay work | CI covers five synthetic HTTP tests and does not call /predict or the two competition endpoints |
| The 10.40 pp error uses the exact visible comparison subset | Verifier forecasts after own test 4 onward; UI starts with the forecast after own test 3 for actual test 4 |
| A green /health proves inference is ready | It only executes SELECT 1; checkpoint loading is lazy on prediction |
| Deployment files in Git are the active host files | Installed copies under /etc and /usr/local/bin must be managed separately |

## Scientific boundaries worth preserving

1. Original group-aware fold construction is outside the archive. The runtime respects saved assignment, but cannot prove how those assignments were created.
2. Saved F1-maximizing game thresholds are reused. Evaluating thresholded results on the same observations used to choose cutoffs is not an independent evaluation.
3. Objective-maximum scaling uses full analyst knowledge. Availability of this quantity in a future live recommendation system needs an explicit decision.
4. The feature builder retains a nonempty-opponent-timeline availability convention. Future scores are filtered by time, but timeline existence is known from the full export.
5. Stopping combines voluntary submission with timeout. It does not measure only deliberate commitment.
6. The displayed model learns observed behavior; the unsuccessful success-conditioning work is not deployed. Predictive accuracy alone does not show improved decision quality.
7. The displayed star comes from sampled curve points and the stored maximum is numerically estimated; neither is a proof of the exact global optimum.

## Maintainability observations, not changes made

- `DeltaLSTM` lives in a verifier that production imports. A future refactor could move it to a dedicated architecture module, with parity checks protecting behavior.
- `replay.html` mixes dense one-line CSS/JavaScript and several generations of style overrides. It retains unused legend-control styles, an always-true marker filter and hidden score panels. The annotation follows original physical lines so references remain stable; a later formatting-only change would require a new line map.
- `setup_docker.py` has an older required-file list and does not check replay_story.py. Docker's explicit COPY still fails if it is missing. An existing password assignment is retained even if it is empty.
- The connection role is postgres. Request transactions are read-only, but a dedicated least-privilege database role and connection pooling are not configured.
- Presentation endpoints perform several separately connected reads. With static data this is generally consistent; concurrent future imports could make a combined story/result read span different database states. /predict already uses a repeatable-read transaction.
- Model digest checks are enforced in production and on context-cache import, but several general verification loaders trust pickles without enforcing those constants. Hash logging alone is not validation.
- Input parser checks are purpose-specific. For example, parse_opponent_timeline catches JSON parsing errors but not every unexpected nested data shape; no arbitrary external dataset support is implied.
- `source_cache_sha256` identifies context provenance; runtime checks its presence, not equality to a pinned constant on every request. Administrative database changes are outside the reference-parity guarantee.
- API docs still report version 0.5.0. Newer UI code was appended without changing that version string.
- Dependencies are pinned by version, but Python/PostgreSQL base image tags are not digest-pinned in source. The guide preserves the versions actually supplied, without claiming future availability.
- GitHub Actions builds/tests but has no image registry publishing or EC2 deployment job. Health probes and logs are not model-drift monitoring.
- Empty player-rounds are not in participant_rounds. Outcome cards therefore flag incomplete rosters instead of inventing missing players.
- The prior 12-combination replay verifier is not in the uploaded repository. Its previously reported local pass is distinguished from the checked-in CI tests.

## Verification for this documentation delivery

The authoring process reads the source archive, parses Python syntax for symbol mapping and associates every physical source/configuration line with commentary. A SHA256 manifest records the reviewed bytes. Documentation links, coverage and archive contents are checked. No model is retrained, no research pickle is deserialized, no SQL import is performed and no AWS setting changes.

Application execution and browser rendering were not rerun as part of this documentation task. Previously reported test/deployment passes are explicitly identified as prior evidence. The standalone HTML guide is a reading aid, not another hosted application.
