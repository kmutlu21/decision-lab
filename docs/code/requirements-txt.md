# requirements.txt

Pins the supplied Python environment. Not every listed package is a direct application dependency.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1 | Dependency supporting annotation/documentation metadata in the API stack; not directly imported by project code. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 2 | Constraint metadata used by the validation dependency stack; not directly imported. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 3 | Async concurrency support in the web stack; the application uses it indirectly. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 4 | CLI parsing dependency used by tooling such as Uvicorn, not this project’s argparse-based scripts. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 5 | Excel XML support associated with openpyxl. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 6 | Creates endpoints, validates query parameters and exposes OpenAPI documentation in main/replay_story. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 7 | File-locking dependency; not the PostgreSQL advisory lock used by importers. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 8 | Filesystem abstraction dependency; this project reads its files through pathlib/pandas, without a custom fsspec pipeline. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 9 | HTTP/1.1 protocol support for the server dependency stack. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 10 | Internationalized domain-name support in dependencies. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 11 | Template engine dependency; replay.html is served directly, not rendered with Jinja templates. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 12 | Safe-string dependency commonly accompanying Jinja2; not used directly here. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 13 | Arbitrary-precision arithmetic dependency; project objective calculations use NumPy/SciPy instead. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 14 | Graph library dependency; no graph algorithm or fold construction using it exists in this snapshot. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 15 | Array math, float32 conversion, normalization, feature statistics and parity comparisons. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 16 | Excel .xlsx reader engine used by pandas for March exports. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 17 | Raw CSV/Excel reading, timestamp conversion, grouping and feature DataFrame assembly. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 18 | PostgreSQL Python interface: parameterized queries, transactions, dict rows and JSONB adapters. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 19 | Binary implementation package paired with psycopg. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 20 | FastAPI request/response validation dependency. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 21 | Compiled core of the Pydantic validation stack. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 22 | Date parsing support in the dataframe dependency stack. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 23 | Provides minimize_scalar for objective maximum estimation. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 24 | Python packaging dependency retained in the supplied environment snapshot. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 25 | Compatibility utility dependency, not directly imported by project scripts. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 26 | Underlying web framework supplying response/ASGI functionality to FastAPI. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 27 | Symbolic mathematics dependency; the objective equations here are explicitly coded numerically. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 28 | CPU PyTorch network architecture, checkpoint loading and inference. Docker installs this CPU build from the PyTorch index. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 29 | Type introspection support in the validation stack. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 30 | Typing backports/extensions used by dependencies. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 31 | Timezone database dependency. Stored sample timestamps here intentionally have no timezone. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 32 | ASGI server that hosts main:app inside the API container. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1 | Dependency supporting annotation/documentation metadata in the API stack; not directly imported by project code. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 2 | 2 | Constraint metadata used by the validation dependency stack; not directly imported. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 3 | 3 | Async concurrency support in the web stack; the application uses it indirectly. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 4 | 4 | CLI parsing dependency used by tooling such as Uvicorn, not this project’s argparse-based scripts. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 5 | 5 | Excel XML support associated with openpyxl. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 6 | 6 | Creates endpoints, validates query parameters and exposes OpenAPI documentation in main/replay_story. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 7 | 7 | File-locking dependency; not the PostgreSQL advisory lock used by importers. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 8 | 8 | Filesystem abstraction dependency; this project reads its files through pathlib/pandas, without a custom fsspec pipeline. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 9 | 9 | HTTP/1.1 protocol support for the server dependency stack. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 10 | 10 | Internationalized domain-name support in dependencies. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 11 | 11 | Template engine dependency; replay.html is served directly, not rendered with Jinja templates. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 12 | 12 | Safe-string dependency commonly accompanying Jinja2; not used directly here. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 13 | 13 | Arbitrary-precision arithmetic dependency; project objective calculations use NumPy/SciPy instead. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 14 | 14 | Graph library dependency; no graph algorithm or fold construction using it exists in this snapshot. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 15 | 15 | Array math, float32 conversion, normalization, feature statistics and parity comparisons. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 16 | 16 | Excel .xlsx reader engine used by pandas for March exports. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 17 | 17 | Raw CSV/Excel reading, timestamp conversion, grouping and feature DataFrame assembly. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 18 | 18 | PostgreSQL Python interface: parameterized queries, transactions, dict rows and JSONB adapters. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 19 | 19 | Binary implementation package paired with psycopg. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 20 | 20 | FastAPI request/response validation dependency. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 21 | 21 | Compiled core of the Pydantic validation stack. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 22 | 22 | Date parsing support in the dataframe dependency stack. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 23 | 23 | Provides minimize_scalar for objective maximum estimation. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 24 | 24 | Python packaging dependency retained in the supplied environment snapshot. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 25 | 25 | Compatibility utility dependency, not directly imported by project scripts. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 26 | 26 | Underlying web framework supplying response/ASGI functionality to FastAPI. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 27 | 27 | Symbolic mathematics dependency; the objective equations here are explicitly coded numerically. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 28 | 28 | CPU PyTorch network architecture, checkpoint loading and inference. Docker installs this CPU build from the PyTorch index. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 29 | 29 | Type introspection support in the validation stack. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 30 | 30 | Typing backports/extensions used by dependencies. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 31 | 31 | Timezone database dependency. Stored sample timestamps here intentionally have no timezone. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |
| 32 | 32 | ASGI server that hosts main:app inside the API container. The exact supplied version is pinned by ==; this guide does not upgrade or independently verify package availability. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  annotated-doc==0.0.5
   2  annotated-types==0.8.0
   3  anyio==4.15.1
   4  click==8.5.0
   5  et_xmlfile==2.0.0
   6  fastapi==0.141.1
   7  filelock==3.32.3
   8  fsspec==2026.7.0
   9  h11==0.16.0
  10  idna==3.19
  11  Jinja2==3.1.6
  12  MarkupSafe==3.0.3
  13  mpmath==1.3.0
  14  networkx==3.6.1
  15  numpy==2.5.3
  16  openpyxl==3.1.5
  17  pandas==3.0.5
  18  psycopg==3.3.5
  19  psycopg-binary==3.3.5
  20  pydantic==2.13.5
  21  pydantic_core==2.46.5
  22  python-dateutil==2.9.0.post0
  23  scipy==1.18.1
  24  setuptools==78.1.0
  25  six==1.17.0
  26  starlette==1.6.0
  27  sympy==1.14.0
  28  torch==2.14.0+cpu
  29  typing-inspection==0.4.4
  30  typing_extensions==4.16.0
  31  tzdata==2026.3
  32  uvicorn==0.52.4
```
