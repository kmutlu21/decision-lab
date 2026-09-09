# GitHub Actions: container and API checks

Copy .github/, ci/, and compose.ci.yaml into the existing project root. No changes to requirements.txt or Dockerfile are needed. These files depend on the Docker setup and SQL API files already developed on feature/sql-model-inputs.

The workflow runs on pushes, pull requests, and manual dispatch. It builds the existing Docker image, runs pip check, and exercises the actual HTTP API against PostgreSQL 18 using synthetic data. No research files, trained models, GitHub secrets, or cloud account are needed. The checkout step uses the official actions/checkout action: https://github.com/actions/checkout.

Checks cover the home page, database health, session and round counts, replay prefix truncation, running best, elapsed time, February/March normalization, both objective families, and invalid/missing requests. They do not test trained model predictions or prove model quality. Keep using verify_sql_features.py and verify_sql_runtime.py locally for parity with the private research artifacts.

## Install and push (PowerShell in your project)

```powershell
git add .github/workflows/ci.yml ci/smoke_test.py compose.ci.yaml CI_SETUP.md
git diff --cached --stat
git commit -m "Add container build and synthetic API integration checks"
git push
```

The Docker setup must also be committed and pushed. Open the repository's Actions tab and select Container and API checks. The initial image build can take several minutes. If a run fails, open the failed step and share its error. This workflow checks code; it does not publish an image or deploy the application.

## Optional local execution

```powershell
docker compose -f compose.ci.yaml build api
docker compose -f compose.ci.yaml run --rm tests
docker compose -f compose.ci.yaml down --volumes --remove-orphans
```

Always include -f compose.ci.yaml for these commands. This separate stack has no published ports and does not use your main app's database, .env, datasets, or model files. Cleanup removes only the disposable CI stack and its volumes. Fixtures require an empty database and refuse to overwrite existing records; clean up before rerunning locally.

## Validation status

Python syntax and Compose/workflow YAML structure were checked before delivery. The CI integration run must still execute on your Docker host or GitHub runner; a passing build alone does not establish that these tests pass. Dependencies are retained exactly as supplied in your successfully built requirements.txt. The first GitHub run verifies availability and installation in a clean runner.
