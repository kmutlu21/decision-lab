# compose.yaml

Defines the persistent local/AWS API and PostgreSQL services and an explicitly invoked import/verification service.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1 | Sets the project name used for container, network and volume naming. |
| 3-5 | Defines a reusable YAML anchor for the application image and build directory. |
| 6-11 | Passes database connection settings to Python. Resolves the password from environment/.env and fails configuration if it is missing or empty. |
| 12-14 | Requires initial database health before starting a dependent service. This is not ongoing automatic failover. |
| 16-19 | Starts the database service using the supplied PostgreSQL 18 tag and restarts it unless deliberately stopped. |
| 20-23 | Sets first-initialization database/user/password. Changing these variables does not automatically rewrite an existing database's credentials. |
| 24-26 | Keeps PostgreSQL data in a named volume independent of API image rebuilds. |
| 27-32 | Runs pg_isready every 5 seconds with a 10-second startup allowance and up to 20 failing probes. |
| 34-38 | Starts the API with inherited app settings and exposes port 8000 only on host 127.0.0.1. Caddy reaches it from that host. |
| 39-45 | Mounts the existing models folder read-only and rejects a missing host path rather than creating an empty directory. Linux file permissions still apply. |
| 46-51 | Probes /health inside the API container. Healthy proves basic database connection, not inference readiness. |
| 53-56 | Defines the tools-profile init service with bootstrap_database.py instead of the API command; it inherits database settings and health dependency. |
| 57-69 | Mounts raw files and models read-only for import/verification jobs. This is why init can import data while the API needs no raw-file mount. |
| 71-72 | Declares the persistent database volume. Removing it deletes the stored database; it is not an expendable image cache. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1 | Sets the project name used for container, network and volume naming. |
| 2 | 2 | Blank separator; no execution. |
| 3 | 3-5 | Defines a reusable YAML anchor for the application image and build directory. |
| 4 | 3-5 | Defines a reusable YAML anchor for the application image and build directory. |
| 5 | 3-5 | Defines a reusable YAML anchor for the application image and build directory. |
| 6 | 6-11 | Passes database connection settings to Python. Resolves the password from environment/.env and fails configuration if it is missing or empty. |
| 7 | 6-11 | Passes database connection settings to Python. Resolves the password from environment/.env and fails configuration if it is missing or empty. |
| 8 | 6-11 | Passes database connection settings to Python. Resolves the password from environment/.env and fails configuration if it is missing or empty. |
| 9 | 6-11 | Passes database connection settings to Python. Resolves the password from environment/.env and fails configuration if it is missing or empty. |
| 10 | 6-11 | Passes database connection settings to Python. Resolves the password from environment/.env and fails configuration if it is missing or empty. |
| 11 | 6-11 | Passes database connection settings to Python. Resolves the password from environment/.env and fails configuration if it is missing or empty. |
| 12 | 12-14 | Requires initial database health before starting a dependent service. This is not ongoing automatic failover. |
| 13 | 12-14 | Requires initial database health before starting a dependent service. This is not ongoing automatic failover. |
| 14 | 12-14 | Requires initial database health before starting a dependent service. This is not ongoing automatic failover. |
| 15 | 15 | Blank separator; no execution. |
| 16 | 16-19 | Starts the database service using the supplied PostgreSQL 18 tag and restarts it unless deliberately stopped. |
| 17 | 16-19 | Starts the database service using the supplied PostgreSQL 18 tag and restarts it unless deliberately stopped. |
| 18 | 16-19 | Starts the database service using the supplied PostgreSQL 18 tag and restarts it unless deliberately stopped. |
| 19 | 16-19 | Starts the database service using the supplied PostgreSQL 18 tag and restarts it unless deliberately stopped. |
| 20 | 20-23 | Sets first-initialization database/user/password. Changing these variables does not automatically rewrite an existing database's credentials. |
| 21 | 20-23 | Sets first-initialization database/user/password. Changing these variables does not automatically rewrite an existing database's credentials. |
| 22 | 20-23 | Sets first-initialization database/user/password. Changing these variables does not automatically rewrite an existing database's credentials. |
| 23 | 20-23 | Sets first-initialization database/user/password. Changing these variables does not automatically rewrite an existing database's credentials. |
| 24 | 24-26 | Keeps PostgreSQL data in a named volume independent of API image rebuilds. |
| 25 | 24-26 | Keeps PostgreSQL data in a named volume independent of API image rebuilds. |
| 26 | 24-26 | Keeps PostgreSQL data in a named volume independent of API image rebuilds. |
| 27 | 27-32 | Runs pg_isready every 5 seconds with a 10-second startup allowance and up to 20 failing probes. |
| 28 | 27-32 | Runs pg_isready every 5 seconds with a 10-second startup allowance and up to 20 failing probes. |
| 29 | 27-32 | Runs pg_isready every 5 seconds with a 10-second startup allowance and up to 20 failing probes. |
| 30 | 27-32 | Runs pg_isready every 5 seconds with a 10-second startup allowance and up to 20 failing probes. |
| 31 | 27-32 | Runs pg_isready every 5 seconds with a 10-second startup allowance and up to 20 failing probes. |
| 32 | 27-32 | Runs pg_isready every 5 seconds with a 10-second startup allowance and up to 20 failing probes. |
| 33 | 33 | Blank separator; no execution. |
| 34 | 34-38 | Starts the API with inherited app settings and exposes port 8000 only on host 127.0.0.1. Caddy reaches it from that host. |
| 35 | 34-38 | Starts the API with inherited app settings and exposes port 8000 only on host 127.0.0.1. Caddy reaches it from that host. |
| 36 | 34-38 | Starts the API with inherited app settings and exposes port 8000 only on host 127.0.0.1. Caddy reaches it from that host. |
| 37 | 34-38 | Starts the API with inherited app settings and exposes port 8000 only on host 127.0.0.1. Caddy reaches it from that host. |
| 38 | 34-38 | Starts the API with inherited app settings and exposes port 8000 only on host 127.0.0.1. Caddy reaches it from that host. |
| 39 | 39-45 | Mounts the existing models folder read-only and rejects a missing host path rather than creating an empty directory. Linux file permissions still apply. |
| 40 | 39-45 | Mounts the existing models folder read-only and rejects a missing host path rather than creating an empty directory. Linux file permissions still apply. |
| 41 | 39-45 | Mounts the existing models folder read-only and rejects a missing host path rather than creating an empty directory. Linux file permissions still apply. |
| 42 | 39-45 | Mounts the existing models folder read-only and rejects a missing host path rather than creating an empty directory. Linux file permissions still apply. |
| 43 | 39-45 | Mounts the existing models folder read-only and rejects a missing host path rather than creating an empty directory. Linux file permissions still apply. |
| 44 | 39-45 | Mounts the existing models folder read-only and rejects a missing host path rather than creating an empty directory. Linux file permissions still apply. |
| 45 | 39-45 | Mounts the existing models folder read-only and rejects a missing host path rather than creating an empty directory. Linux file permissions still apply. |
| 46 | 46-51 | Probes /health inside the API container. Healthy proves basic database connection, not inference readiness. |
| 47 | 46-51 | Probes /health inside the API container. Healthy proves basic database connection, not inference readiness. |
| 48 | 46-51 | Probes /health inside the API container. Healthy proves basic database connection, not inference readiness. |
| 49 | 46-51 | Probes /health inside the API container. Healthy proves basic database connection, not inference readiness. |
| 50 | 46-51 | Probes /health inside the API container. Healthy proves basic database connection, not inference readiness. |
| 51 | 46-51 | Probes /health inside the API container. Healthy proves basic database connection, not inference readiness. |
| 52 | 52 | Blank separator; no execution. |
| 53 | 53-56 | Defines the tools-profile init service with bootstrap_database.py instead of the API command; it inherits database settings and health dependency. |
| 54 | 53-56 | Defines the tools-profile init service with bootstrap_database.py instead of the API command; it inherits database settings and health dependency. |
| 55 | 53-56 | Defines the tools-profile init service with bootstrap_database.py instead of the API command; it inherits database settings and health dependency. |
| 56 | 53-56 | Defines the tools-profile init service with bootstrap_database.py instead of the API command; it inherits database settings and health dependency. |
| 57 | 57-69 | Mounts raw files and models read-only for import/verification jobs. This is why init can import data while the API needs no raw-file mount. |
| 58 | 57-69 | Mounts raw files and models read-only for import/verification jobs. This is why init can import data while the API needs no raw-file mount. |
| 59 | 57-69 | Mounts raw files and models read-only for import/verification jobs. This is why init can import data while the API needs no raw-file mount. |
| 60 | 57-69 | Mounts raw files and models read-only for import/verification jobs. This is why init can import data while the API needs no raw-file mount. |
| 61 | 57-69 | Mounts raw files and models read-only for import/verification jobs. This is why init can import data while the API needs no raw-file mount. |
| 62 | 57-69 | Mounts raw files and models read-only for import/verification jobs. This is why init can import data while the API needs no raw-file mount. |
| 63 | 57-69 | Mounts raw files and models read-only for import/verification jobs. This is why init can import data while the API needs no raw-file mount. |
| 64 | 57-69 | Mounts raw files and models read-only for import/verification jobs. This is why init can import data while the API needs no raw-file mount. |
| 65 | 57-69 | Mounts raw files and models read-only for import/verification jobs. This is why init can import data while the API needs no raw-file mount. |
| 66 | 57-69 | Mounts raw files and models read-only for import/verification jobs. This is why init can import data while the API needs no raw-file mount. |
| 67 | 57-69 | Mounts raw files and models read-only for import/verification jobs. This is why init can import data while the API needs no raw-file mount. |
| 68 | 57-69 | Mounts raw files and models read-only for import/verification jobs. This is why init can import data while the API needs no raw-file mount. |
| 69 | 57-69 | Mounts raw files and models read-only for import/verification jobs. This is why init can import data while the API needs no raw-file mount. |
| 70 | 70 | Blank separator; no execution. |
| 71 | 71-72 | Declares the persistent database volume. Removing it deletes the stored database; it is not an expendable image cache. |
| 72 | 71-72 | Declares the persistent database volume. Removing it deletes the stored database; it is not an expendable image cache. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  name: decision-lab
   2  
   3  x-app: &app
   4    image: decision-lab-api:local
   5    build: .
   6    environment:
   7      PGHOST: db
   8      PGPORT: "5432"
   9      PGDATABASE: decision_lab
  10      PGUSER: postgres
  11      PGPASSWORD: ${DECISION_LAB_DB_PASSWORD:?Run setup_docker.py first}
  12    depends_on:
  13      db:
  14        condition: service_healthy
  15  
  16  services:
  17    db:
  18      restart: unless-stopped
  19      image: postgres:18-bookworm
  20      environment:
  21        POSTGRES_DB: decision_lab
  22        POSTGRES_USER: postgres
  23        POSTGRES_PASSWORD: ${DECISION_LAB_DB_PASSWORD:?Run setup_docker.py first}
  24      volumes:
  25        # PostgreSQL 18 stores versioned data beneath this parent directory.
  26        - postgres_data:/var/lib/postgresql
  27      healthcheck:
  28        test: ["CMD-SHELL", "pg_isready -U postgres -d decision_lab"]
  29        interval: 5s
  30        timeout: 5s
  31        retries: 20
  32        start_period: 10s
  33  
  34    api:
  35      restart: unless-stopped
  36      <<: *app
  37      ports:
  38        - "127.0.0.1:8000:8000"
  39      volumes:
  40        - type: bind
  41          source: ./models
  42          target: /app/models
  43          read_only: true
  44          bind:
  45            create_host_path: false
  46      healthcheck:
  47        test: ["CMD", "python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=4)"]
  48        interval: 10s
  49        timeout: 5s
  50        retries: 5
  51        start_period: 20s
  52  
  53    init:
  54      <<: *app
  55      profiles: ["tools"]
  56      command: ["python", "bootstrap_database.py"]
  57      volumes:
  58        - type: bind
  59          source: ./data/raw
  60          target: /app/data/raw
  61          read_only: true
  62          bind:
  63            create_host_path: false
  64        - type: bind
  65          source: ./models
  66          target: /app/models
  67          read_only: true
  68          bind:
  69            create_host_path: false
  70  
  71  volumes:
  72    postgres_data:
```
