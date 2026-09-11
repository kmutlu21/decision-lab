# Dockerfile

Builds the CPU application image; private data and models are supplied by mounts when a container runs.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1 | Uses the supplied Python 3.14 slim Debian Bookworm image tag. This source tag is not pinned to a digest. |
| 2-4 | Disables bytecode writes, buffers less Python output for logs and suppresses pip update notices. |
| 5 | Makes /app the working directory for subsequent image steps and the startup command. |
| 6-9 | Copies pinned requirements and installs CPU PyTorch from its wheel index before the remaining dependencies. && stops if the first installation fails. |
| 10 | Creates the unprivileged Linux account with UID 10001, which must be able to read mounted models. |
| 11-16 | Copies only named application/import/verification files into the image; private artifacts are intentionally absent. |
| 17 | Selects appuser for runtime commands. This is separate from PostgreSQL's application role, which remains postgres. |
| 18 | Documents the container port. EXPOSE alone does not publish it on the host or internet. |
| 19 | Launches Uvicorn, importing main:app, and listens on all container interfaces. Compose separately limits the host binding to loopback. |
| 21-22 | Adds competition route code as another image layer. COPY after CMD is valid; it does not execute after server startup or change the configured command. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1 | Uses the supplied Python 3.14 slim Debian Bookworm image tag. This source tag is not pinned to a digest. |
| 2 | 2-4 | Disables bytecode writes, buffers less Python output for logs and suppresses pip update notices. |
| 3 | 2-4 | Disables bytecode writes, buffers less Python output for logs and suppresses pip update notices. |
| 4 | 2-4 | Disables bytecode writes, buffers less Python output for logs and suppresses pip update notices. |
| 5 | 5 | Makes /app the working directory for subsequent image steps and the startup command. |
| 6 | 6-9 | Copies pinned requirements and installs CPU PyTorch from its wheel index before the remaining dependencies. && stops if the first installation fails. |
| 7 | 6-9 | Copies pinned requirements and installs CPU PyTorch from its wheel index before the remaining dependencies. && stops if the first installation fails. |
| 8 | 6-9 | Copies pinned requirements and installs CPU PyTorch from its wheel index before the remaining dependencies. && stops if the first installation fails. |
| 9 | 6-9 | Copies pinned requirements and installs CPU PyTorch from its wheel index before the remaining dependencies. && stops if the first installation fails. |
| 10 | 10 | Creates the unprivileged Linux account with UID 10001, which must be able to read mounted models. |
| 11 | 11-16 | Copies only named application/import/verification files into the image; private artifacts are intentionally absent. |
| 12 | 11-16 | Copies only named application/import/verification files into the image; private artifacts are intentionally absent. |
| 13 | 11-16 | Copies only named application/import/verification files into the image; private artifacts are intentionally absent. |
| 14 | 11-16 | Copies only named application/import/verification files into the image; private artifacts are intentionally absent. |
| 15 | 11-16 | Copies only named application/import/verification files into the image; private artifacts are intentionally absent. |
| 16 | 11-16 | Copies only named application/import/verification files into the image; private artifacts are intentionally absent. |
| 17 | 17 | Selects appuser for runtime commands. This is separate from PostgreSQL's application role, which remains postgres. |
| 18 | 18 | Documents the container port. EXPOSE alone does not publish it on the host or internet. |
| 19 | 19 | Launches Uvicorn, importing main:app, and listens on all container interfaces. Compose separately limits the host binding to loopback. |
| 20 | 20 | Blank separator; no execution. |
| 21 | 21-22 | Adds competition route code as another image layer. COPY after CMD is valid; it does not execute after server startup or change the configured command. |
| 22 | 21-22 | Adds competition route code as another image layer. COPY after CMD is valid; it does not execute after server startup or change the configured command. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  FROM python:3.14-slim-bookworm
   2  ENV PYTHONDONTWRITEBYTECODE=1 \
   3      PYTHONUNBUFFERED=1 \
   4      PIP_DISABLE_PIP_VERSION_CHECK=1
   5  WORKDIR /app
   6  # CPU-only PyTorch matches the verified Windows model runtime.
   7  COPY requirements.txt ./requirements.txt
   8  RUN python -m pip install --no-cache-dir torch==2.14.0+cpu --index-url https://download.pytorch.org/whl/cpu \
   9      && python -m pip install --no-cache-dir -r requirements.txt
  10  RUN useradd --create-home --uid 10001 appuser
  11  # Explicit source list: research data, credentials and model artifacts are
  12  # provided at runtime, not stored in image layers.
  13  COPY main.py inference.py replay.html objectives.py verify_model.py ./
  14  COPY import_data.py import_functions.py import_model_context.py ./
  15  COPY feature_math.py sql_features.py sql_runtime.py ./
  16  COPY verify_sql_features.py verify_sql_runtime.py bootstrap_database.py ./
  17  USER appuser
  18  EXPOSE 8000
  19  CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
  20  
  21  # Read-only competition presentation routes
  22  COPY replay_story.py ./
```
