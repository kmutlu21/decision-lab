# Code walkthrough index

Source commit `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Read [the engineering guide](ENGINEERING_GUIDE.md) first.

All 28 executable, UI, dependency and configuration files are covered below, including 2192 physical lines. The line guides preserve original numbering; application code is unchanged.

| File | Purpose | Guide |
|---|---|---|
| `.dockerignore` | Limits Docker build context independently of Git tracking. | [16 lines](code/dockerignore.md) |
| `.github/workflows/ci.yml` | Automates container builds and synthetic API checks on GitHub; it does not deploy to AWS. | [32 lines](code/github-workflows-ci-yml.md) |
| `.gitignore` | Keeps local environments, credentials, research data, model files and downloaded packages out of new Git tracking. | [20 lines](code/gitignore.md) |
| `Dockerfile` | Builds the CPU application image; private data and models are supplied by mounts when a container runs. | [22 lines](code/Dockerfile.md) |
| `bootstrap_database.py` | Runs the three import stages in order inside the tools container; each stage has its own transaction. | [19 lines](code/bootstrap-database-py.md) |
| `ci/smoke_test.py` | Seeds an isolated synthetic PostgreSQL database and runs five HTTP integration tests without private data or trained weights. | [124 lines](code/ci-smoke-test-py.md) |
| `compose.ci.yaml` | Defines a separate disposable stack with synthetic data and no original checkpoints, avoiding the production database. | [44 lines](code/compose-ci-yaml.md) |
| `compose.yaml` | Defines the persistent local/AWS API and PostgreSQL services and an explicitly invoked import/verification service. | [72 lines](code/compose-yaml.md) |
| `deploy/Caddyfile` | Connects the public hostname to the API bound on the EC2 host. | [3 lines](code/deploy-Caddyfile.md) |
| `deploy/decision-lab-dns.service` | Defines a one-shot system service for the installed DNS updater. | [8 lines](code/deploy-decision-lab-dns-service.md) |
| `deploy/decision-lab-dns.timer` | Schedules the one-shot DNS update at boot and periodically afterward. | [10 lines](code/deploy-decision-lab-dns-timer.md) |
| `deploy/decision-lab-update-dns` | Updates Duck DNS from the server’s outward-facing IPv4 address without embedding the token in the repository. | [16 lines](code/deploy-decision-lab-update-dns.md) |
| `feature_math.py` | Implements the fixed 14-column event representation shared by offline parity checking and live inference. No training or future targets are created here. | [258 lines](code/feature-math-py.md) |
| `import_data.py` | Validates the 12 raw experiment exports and transactionally imports sessions, nonempty player-rounds and own sample events. | [219 lines](code/import-data-py.md) |
| `import_functions.py` | Imports each round’s objective family, parameters and numerical normalization maximum without altering observed samples. | [103 lines](code/import-functions-py.md) |
| `import_model_context.py` | Imports raw opponent exports and the original fold_map, keeping model lineage separate from sample data. | [96 lines](code/import-model-context-py.md) |
| `inference.py` | Loads fingerprinted original checkpoints and saved stopping thresholds once per process, then predicts from a SQL-built prefix. | [81 lines](code/inference-py.md) |
| `main.py` | Creates the FastAPI app, opens read-only database connections, exposes history and prediction endpoints, and registers the competition routes. | [222 lines](code/main-py.md) |
| `objectives.py` | One source of truth for the two mathematical landscapes and their normalization maximum. | [26 lines](code/objectives-py.md) |
| `replay.html` | Contains all production HTML, CSS and browser JavaScript. It requests historical JSON from FastAPI and draws SVG, without a frontend framework. | [199 lines](code/replay-html.md) |
| `replay_story.py` | Adds presentation-only routes for permitted own/teammate replay and final team outcomes, reusing existing SQL/normalization helpers. | [126 lines](code/replay-story-py.md) |
| `requirements.txt` | Pins the supplied Python environment. Not every listed package is a direct application dependency. | [32 lines](code/requirements-txt.md) |
| `setup_docker.py` | Checks local prerequisites and creates or preserves the separate Compose database password in ignored .env. | [28 lines](code/setup-docker-py.md) |
| `sql_features.py` | Rebuilds full historical sequences from PostgreSQL for parity verification. It is not the live /predict query path. | [62 lines](code/sql-features-py.md) |
| `sql_runtime.py` | Selects the exact request-time history visible at an own test and adapts it to the shared feature builder. | [80 lines](code/sql-runtime-py.md) |
| `verify_model.py` | Defines the deployed network architecture and separately verifies checkpoint outputs against the original saved validation arrays. | [160 lines](code/verify-model-py.md) |
| `verify_sql_features.py` | Checks full-dataset SQL reconstruction against the reference features and the outputs of the same original checkpoints. | [66 lines](code/verify-sql-features-py.md) |
| `verify_sql_runtime.py` | Checks representative prefixes through the actual request-time SQL loader and the production predictor. | [48 lines](code/verify-sql-runtime-py.md) |

## Other repository documents

| Original file | Role in this update |
|---|---|
| README.md | Replaced with an accurate portfolio-facing overview and guide links |
| `CI_SETUP.md` | Historical CI installation note. The workflow is already installed. Do not repeat the Copy/install steps on the current deployment. Use the current engineering guide for coverage; this snapshot does not test the competition endpoints or trained model in CI. |
| `DOCKER_SETUP.md` | Historical Docker setup note. The deployed service is already initialized and verified. For documentation-only changes, no rebuild or import is needed. Its copy/replace instructions describe an older update package. |
| `deploy/README.md` | Existing host operations guide. The configuration commands describe installed services outside the repository. Source-only review cannot verify their current live state; deployment validation below records prior checks. |
| `docs/sql-inference-migration-v0.5.md` | Historical migration note. PostgreSQL-built inference is already deployed. Do not follow the file replacement/restart steps again merely to install this documentation. |

The original archive contains 33 files. Every file is accounted for above. [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json) records source byte hashes, not runtime credential values.

## New documentation

- [Engineering guide](ENGINEERING_GUIDE.md): architecture, data/model contracts, request flow, setup and limits.
- [Review notes](REVIEW_NOTES.md): stale comments and future maintenance observations.
- [Learning exercises](LEARNING_EXERCISES.md): practical prompts with answers.
