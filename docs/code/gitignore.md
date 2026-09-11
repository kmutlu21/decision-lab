# .gitignore

Keeps local environments, credentials, research data, model files and downloaded packages out of new Git tracking.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1-6 | Ignores virtual environments, bytecode and pytest cache. These rules do not untrack files already committed. |
| 7-10 | Ignores .env and its variants, with an explicit exception permitting a nonsecret .env.example template. |
| 12-17 | Ignores raw/data folders and serialized model artifacts. The deployed app still requires authorized private copies outside Git. |
| 19-20 | Ignores downloaded ZIP update packages so they are not accidentally committed as application source. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1-6 | Ignores virtual environments, bytecode and pytest cache. These rules do not untrack files already committed. |
| 2 | 1-6 | Ignores virtual environments, bytecode and pytest cache. These rules do not untrack files already committed. |
| 3 | 1-6 | Ignores virtual environments, bytecode and pytest cache. These rules do not untrack files already committed. |
| 4 | 1-6 | Ignores virtual environments, bytecode and pytest cache. These rules do not untrack files already committed. |
| 5 | 1-6 | Ignores virtual environments, bytecode and pytest cache. These rules do not untrack files already committed. |
| 6 | 1-6 | Blank separator; no execution. |
| 7 | 7-10 | Ignores .env and its variants, with an explicit exception permitting a nonsecret .env.example template. |
| 8 | 7-10 | Ignores .env and its variants, with an explicit exception permitting a nonsecret .env.example template. |
| 9 | 7-10 | Ignores .env and its variants, with an explicit exception permitting a nonsecret .env.example template. |
| 10 | 7-10 | Ignores .env and its variants, with an explicit exception permitting a nonsecret .env.example template. |
| 11 | 11 | Blank separator; no execution. |
| 12 | 12-17 | Ignores raw/data folders and serialized model artifacts. The deployed app still requires authorized private copies outside Git. |
| 13 | 12-17 | Ignores raw/data folders and serialized model artifacts. The deployed app still requires authorized private copies outside Git. |
| 14 | 12-17 | Ignores raw/data folders and serialized model artifacts. The deployed app still requires authorized private copies outside Git. |
| 15 | 12-17 | Ignores raw/data folders and serialized model artifacts. The deployed app still requires authorized private copies outside Git. |
| 16 | 12-17 | Ignores raw/data folders and serialized model artifacts. The deployed app still requires authorized private copies outside Git. |
| 17 | 12-17 | Ignores raw/data folders and serialized model artifacts. The deployed app still requires authorized private copies outside Git. |
| 18 | 18 | Blank separator; no execution. |
| 19 | 19-20 | Ignores downloaded ZIP update packages so they are not accidentally committed as application source. |
| 20 | 19-20 | Ignores downloaded ZIP update packages so they are not accidentally committed as application source. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  # Python environment and generated files
   2  .venv/
   3  __pycache__/
   4  *.py[cod]
   5  .pytest_cache/
   6  
   7  # Credentials and local settings
   8  .env
   9  .env.*
  10  !.env.example
  11  
  12  # Research data and model artifacts
  13  data/
  14  models/
  15  *.pkl
  16  *.pt
  17  *.pth
  18  
  19  # Downloaded update archives
  20  *.zip
```
