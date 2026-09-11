# compose.ci.yaml

Defines a separate disposable stack with synthetic data and no original checkpoints, avoiding the production database.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1-9 | Uses a distinct project/database and an intentionally disposable test password. No production secret variable is referenced. |
| 10-14 | Waits for PostgreSQL readiness with short CI polling intervals. |
| 15-23 | Builds the same application sources under a CI image name; a YAML anchor captures the synthetic database settings. |
| 24-32 | Starts the API after database readiness and checks its health. No ports are published to the host. |
| 33-41 | Creates an explicitly invoked tests service inheriting the synthetic connection settings and pointing HTTP requests to the api service. |
| 42-44 | Mounts ci/ read-only and runs smoke_test.py. It seeds schema/data before its HTTP assertions; there is no model mount. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1-9 | Uses a distinct project/database and an intentionally disposable test password. No production secret variable is referenced. |
| 2 | 1-9 | Uses a distinct project/database and an intentionally disposable test password. No production secret variable is referenced. |
| 3 | 1-9 | Uses a distinct project/database and an intentionally disposable test password. No production secret variable is referenced. |
| 4 | 1-9 | Uses a distinct project/database and an intentionally disposable test password. No production secret variable is referenced. |
| 5 | 1-9 | Uses a distinct project/database and an intentionally disposable test password. No production secret variable is referenced. |
| 6 | 1-9 | Uses a distinct project/database and an intentionally disposable test password. No production secret variable is referenced. |
| 7 | 1-9 | Uses a distinct project/database and an intentionally disposable test password. No production secret variable is referenced. |
| 8 | 1-9 | Uses a distinct project/database and an intentionally disposable test password. No production secret variable is referenced. |
| 9 | 1-9 | Uses a distinct project/database and an intentionally disposable test password. No production secret variable is referenced. |
| 10 | 10-14 | Waits for PostgreSQL readiness with short CI polling intervals. |
| 11 | 10-14 | Waits for PostgreSQL readiness with short CI polling intervals. |
| 12 | 10-14 | Waits for PostgreSQL readiness with short CI polling intervals. |
| 13 | 10-14 | Waits for PostgreSQL readiness with short CI polling intervals. |
| 14 | 10-14 | Waits for PostgreSQL readiness with short CI polling intervals. |
| 15 | 15-23 | Builds the same application sources under a CI image name; a YAML anchor captures the synthetic database settings. |
| 16 | 15-23 | Builds the same application sources under a CI image name; a YAML anchor captures the synthetic database settings. |
| 17 | 15-23 | Builds the same application sources under a CI image name; a YAML anchor captures the synthetic database settings. |
| 18 | 15-23 | Builds the same application sources under a CI image name; a YAML anchor captures the synthetic database settings. |
| 19 | 15-23 | Builds the same application sources under a CI image name; a YAML anchor captures the synthetic database settings. |
| 20 | 15-23 | Builds the same application sources under a CI image name; a YAML anchor captures the synthetic database settings. |
| 21 | 15-23 | Builds the same application sources under a CI image name; a YAML anchor captures the synthetic database settings. |
| 22 | 15-23 | Builds the same application sources under a CI image name; a YAML anchor captures the synthetic database settings. |
| 23 | 15-23 | Builds the same application sources under a CI image name; a YAML anchor captures the synthetic database settings. |
| 24 | 24-32 | Starts the API after database readiness and checks its health. No ports are published to the host. |
| 25 | 24-32 | Starts the API after database readiness and checks its health. No ports are published to the host. |
| 26 | 24-32 | Starts the API after database readiness and checks its health. No ports are published to the host. |
| 27 | 24-32 | Starts the API after database readiness and checks its health. No ports are published to the host. |
| 28 | 24-32 | Starts the API after database readiness and checks its health. No ports are published to the host. |
| 29 | 24-32 | Starts the API after database readiness and checks its health. No ports are published to the host. |
| 30 | 24-32 | Starts the API after database readiness and checks its health. No ports are published to the host. |
| 31 | 24-32 | Starts the API after database readiness and checks its health. No ports are published to the host. |
| 32 | 24-32 | Starts the API after database readiness and checks its health. No ports are published to the host. |
| 33 | 33-41 | Creates an explicitly invoked tests service inheriting the synthetic connection settings and pointing HTTP requests to the api service. |
| 34 | 33-41 | Creates an explicitly invoked tests service inheriting the synthetic connection settings and pointing HTTP requests to the api service. |
| 35 | 33-41 | Creates an explicitly invoked tests service inheriting the synthetic connection settings and pointing HTTP requests to the api service. |
| 36 | 33-41 | Creates an explicitly invoked tests service inheriting the synthetic connection settings and pointing HTTP requests to the api service. |
| 37 | 33-41 | Creates an explicitly invoked tests service inheriting the synthetic connection settings and pointing HTTP requests to the api service. |
| 38 | 33-41 | Creates an explicitly invoked tests service inheriting the synthetic connection settings and pointing HTTP requests to the api service. |
| 39 | 33-41 | Creates an explicitly invoked tests service inheriting the synthetic connection settings and pointing HTTP requests to the api service. |
| 40 | 33-41 | Creates an explicitly invoked tests service inheriting the synthetic connection settings and pointing HTTP requests to the api service. |
| 41 | 33-41 | Creates an explicitly invoked tests service inheriting the synthetic connection settings and pointing HTTP requests to the api service. |
| 42 | 42-44 | Mounts ci/ read-only and runs smoke_test.py. It seeds schema/data before its HTTP assertions; there is no model mount. |
| 43 | 42-44 | Mounts ci/ read-only and runs smoke_test.py. It seeds schema/data before its HTTP assertions; there is no model mount. |
| 44 | 42-44 | Mounts ci/ read-only and runs smoke_test.py. It seeds schema/data before its HTTP assertions; there is no model mount. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  # Isolated synthetic-data stack; does not use .env, models, or research data.
   2  name: decision-lab-ci
   3  services:
   4    db:
   5      image: postgres:18-bookworm
   6      environment:
   7        POSTGRES_DB: decision_lab_ci
   8        POSTGRES_USER: postgres
   9        POSTGRES_PASSWORD: ci-only-disposable
  10      healthcheck:
  11        test: ["CMD-SHELL", "pg_isready -U postgres -d decision_lab_ci"]
  12        interval: 2s
  13        timeout: 5s
  14        retries: 30
  15    api:
  16      image: decision-lab-api:ci
  17      build: .
  18      environment: &database
  19        PGHOST: db
  20        PGPORT: "5432"
  21        PGDATABASE: decision_lab_ci
  22        PGUSER: postgres
  23        PGPASSWORD: ci-only-disposable
  24      depends_on:
  25        db:
  26          condition: service_healthy
  27      healthcheck:
  28        test: ["CMD", "python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=4)"]
  29        interval: 2s
  30        timeout: 5s
  31        retries: 30
  32        start_period: 10s
  33    tests:
  34      image: decision-lab-api:ci
  35      environment:
  36        <<: *database
  37        API_URL: http://api:8000
  38      profiles: ["tools"]
  39      depends_on:
  40        api:
  41          condition: service_healthy
  42      volumes:
  43        - ./ci:/ci:ro
  44      command: ["python", "/ci/smoke_test.py"]
```
