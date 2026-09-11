# .dockerignore

Limits Docker build context independently of Git tracking.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1-5 | Excludes Git history, local virtual environment and Python caches from the build context. |
| 6-7 | Excludes environment/secret files even when a developer has them locally. |
| 8-12 | Excludes raw data, model directories and serialized checkpoint extensions; use read-only runtime mounts instead. |
| 13-16 | Excludes archives and common image/PDF artifacts. Explicit Dockerfile COPY controls what actually enters the image. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1-5 | Excludes Git history, local virtual environment and Python caches from the build context. |
| 2 | 1-5 | Excludes Git history, local virtual environment and Python caches from the build context. |
| 3 | 1-5 | Excludes Git history, local virtual environment and Python caches from the build context. |
| 4 | 1-5 | Excludes Git history, local virtual environment and Python caches from the build context. |
| 5 | 1-5 | Excludes Git history, local virtual environment and Python caches from the build context. |
| 6 | 6-7 | Excludes environment/secret files even when a developer has them locally. |
| 7 | 6-7 | Excludes environment/secret files even when a developer has them locally. |
| 8 | 8-12 | Excludes raw data, model directories and serialized checkpoint extensions; use read-only runtime mounts instead. |
| 9 | 8-12 | Excludes raw data, model directories and serialized checkpoint extensions; use read-only runtime mounts instead. |
| 10 | 8-12 | Excludes raw data, model directories and serialized checkpoint extensions; use read-only runtime mounts instead. |
| 11 | 8-12 | Excludes raw data, model directories and serialized checkpoint extensions; use read-only runtime mounts instead. |
| 12 | 8-12 | Excludes raw data, model directories and serialized checkpoint extensions; use read-only runtime mounts instead. |
| 13 | 13-16 | Excludes archives and common image/PDF artifacts. Explicit Dockerfile COPY controls what actually enters the image. |
| 14 | 13-16 | Excludes archives and common image/PDF artifacts. Explicit Dockerfile COPY controls what actually enters the image. |
| 15 | 13-16 | Excludes archives and common image/PDF artifacts. Explicit Dockerfile COPY controls what actually enters the image. |
| 16 | 13-16 | Excludes archives and common image/PDF artifacts. Explicit Dockerfile COPY controls what actually enters the image. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  .git
   2  .venv
   3  __pycache__
   4  **/__pycache__
   5  *.pyc
   6  .env
   7  .env.*
   8  data
   9  models
  10  *.pkl
  11  *.pt
  12  *.pth
  13  *.zip
  14  *.png
  15  *.jpg
  16  *.pdf
```
