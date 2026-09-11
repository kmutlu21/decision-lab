# .github/workflows/ci.yml

Automates container builds and synthetic API checks on GitHub; it does not deploy to AWS.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1-5 | Names the workflow and triggers it on push, pull request or manual dispatch. |
| 6-7 | Gives the workflow token repository contents read access only. |
| 8-10 | Groups by workflow/ref and cancels older in-progress runs for that group. |
| 11-15 | Defines one Ubuntu job with a 30-minute execution limit. |
| 16-18 | Checks out repository code without persisting checkout credentials in the local Git configuration. |
| 19-20 | Validates the isolated CI Compose configuration before building. |
| 21-22 | Builds the application image from the checked-out source, not the already-running AWS image. |
| 23-24 | Checks installed Python dependency consistency; this does not execute the application tests. |
| 25-26 | Invokes the test container, which brings up dependencies and runs synthetic HTTP integration assertions. |
| 27-29 | Prints limited container logs if a prior step fails, aiding diagnosis. |
| 30-32 | Always removes the disposable CI stack and its volumes. The explicit CI compose file keeps this separate from the production named volume. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1-5 | Names the workflow and triggers it on push, pull request or manual dispatch. |
| 2 | 1-5 | Names the workflow and triggers it on push, pull request or manual dispatch. |
| 3 | 1-5 | Names the workflow and triggers it on push, pull request or manual dispatch. |
| 4 | 1-5 | Names the workflow and triggers it on push, pull request or manual dispatch. |
| 5 | 1-5 | Names the workflow and triggers it on push, pull request or manual dispatch. |
| 6 | 6-7 | Gives the workflow token repository contents read access only. |
| 7 | 6-7 | Gives the workflow token repository contents read access only. |
| 8 | 8-10 | Groups by workflow/ref and cancels older in-progress runs for that group. |
| 9 | 8-10 | Groups by workflow/ref and cancels older in-progress runs for that group. |
| 10 | 8-10 | Groups by workflow/ref and cancels older in-progress runs for that group. |
| 11 | 11-15 | Defines one Ubuntu job with a 30-minute execution limit. |
| 12 | 11-15 | Defines one Ubuntu job with a 30-minute execution limit. |
| 13 | 11-15 | Defines one Ubuntu job with a 30-minute execution limit. |
| 14 | 11-15 | Defines one Ubuntu job with a 30-minute execution limit. |
| 15 | 11-15 | Defines one Ubuntu job with a 30-minute execution limit. |
| 16 | 16-18 | Checks out repository code without persisting checkout credentials in the local Git configuration. |
| 17 | 16-18 | Checks out repository code without persisting checkout credentials in the local Git configuration. |
| 18 | 16-18 | Checks out repository code without persisting checkout credentials in the local Git configuration. |
| 19 | 19-20 | Validates the isolated CI Compose configuration before building. |
| 20 | 19-20 | Validates the isolated CI Compose configuration before building. |
| 21 | 21-22 | Builds the application image from the checked-out source, not the already-running AWS image. |
| 22 | 21-22 | Builds the application image from the checked-out source, not the already-running AWS image. |
| 23 | 23-24 | Checks installed Python dependency consistency; this does not execute the application tests. |
| 24 | 23-24 | Checks installed Python dependency consistency; this does not execute the application tests. |
| 25 | 25-26 | Invokes the test container, which brings up dependencies and runs synthetic HTTP integration assertions. |
| 26 | 25-26 | Invokes the test container, which brings up dependencies and runs synthetic HTTP integration assertions. |
| 27 | 27-29 | Prints limited container logs if a prior step fails, aiding diagnosis. |
| 28 | 27-29 | Prints limited container logs if a prior step fails, aiding diagnosis. |
| 29 | 27-29 | Prints limited container logs if a prior step fails, aiding diagnosis. |
| 30 | 30-32 | Always removes the disposable CI stack and its volumes. The explicit CI compose file keeps this separate from the production named volume. |
| 31 | 30-32 | Always removes the disposable CI stack and its volumes. The explicit CI compose file keeps this separate from the production named volume. |
| 32 | 30-32 | Always removes the disposable CI stack and its volumes. The explicit CI compose file keeps this separate from the production named volume. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  name: Container and API checks
   2  on:
   3    push:
   4    pull_request:
   5    workflow_dispatch:
   6  permissions:
   7    contents: read
   8  concurrency:
   9    group: ci-${{ github.workflow }}-${{ github.ref }}
  10    cancel-in-progress: true
  11  jobs:
  12    container-api:
  13      runs-on: ubuntu-24.04
  14      timeout-minutes: 30
  15      steps:
  16        - uses: actions/checkout@v6
  17          with:
  18            persist-credentials: false
  19        - name: Validate Compose configuration
  20          run: docker compose -f compose.ci.yaml config --quiet
  21        - name: Build application image
  22          run: docker compose -f compose.ci.yaml build api
  23        - name: Check installed dependencies
  24          run: docker run --rm decision-lab-api:ci python -m pip check
  25        - name: Exercise API with synthetic PostgreSQL records
  26          run: docker compose -f compose.ci.yaml run --rm tests
  27        - name: Show service logs on failure
  28          if: failure()
  29          run: docker compose -f compose.ci.yaml logs --no-color --tail 100
  30        - name: Remove disposable CI containers and volumes
  31          if: always()
  32          run: docker compose -f compose.ci.yaml down --volumes --remove-orphans
```
