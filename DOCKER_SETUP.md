# Run Decision Lab with Docker

Copy this package into the existing project root, replacing import_data.py. It adds environment-based password support while retaining the interactive password prompt for local use. Keep existing source files, requirements.txt, data/raw, and models.

Docker builds a Linux image containing Python and the application dependencies. Compose starts PostgreSQL and the API together. The database uses its own persistent volume; the existing Windows PostgreSQL database is unchanged. Model files and initialization data are mounted read-only.

## Prepare and build (PowerShell in project root)

```powershell
.\.venv\Scripts\python.exe setup_docker.py
docker compose config --quiet
docker compose build api
```

Stop if a command fails. The setup script generates a separate database password in the Git-ignored .env file. Keep that file: changing its password later does not change the password already initialized in PostgreSQL. The build uses the existing requirements.txt and installs the CPU PyTorch package first. If dependency installation fails, retain the build error for diagnosis.

## Initialize and verify

```powershell
docker compose run --rm init
docker compose run --rm init python verify_sql_features.py
docker compose run --rm init python verify_sql_runtime.py
```

Initialization imports raw observations, objective functions, and model context into the container database. Identical records are skipped on reruns. Verification checks feature reconstruction and model outputs in the Linux runtime. Stop and investigate any verification failure before continuing.

## Start the application

Stop any local Uvicorn process using port 8000 first (Ctrl+C in its terminal).

```powershell
docker compose up -d api
docker compose ps
```

Open http://localhost:8000 and check the replay and model predictions. The API port is bound to this computer only. PostgreSQL does not publish a host port. The API health check tests its /health endpoint; model parity is checked by the separate verification commands above.

## Everyday commands

```powershell
docker compose logs --tail 80 api
docker compose stop
docker compose up -d api
```

After source changes, rebuild with docker compose build api, then recreate the API with docker compose up -d api. Data persists in the named PostgreSQL volume when containers stop.

This package has been checked for Python syntax and compatibility with the supplied source interfaces. Image building and container integration still need to be verified on your computer.
