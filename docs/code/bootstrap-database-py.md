# bootstrap_database.py

Runs the three import stages in order inside the tools container; each stage has its own transaction.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1-7 | Imports process tools and refuses to initialize without PGPASSWORD, preventing an interactive prompt inside the container. |
| 8-15 | Declares data → functions → model-context order. Explicitly forwards PG values as CLI arguments to import_data, whose connection defaults otherwise differ. |
| 16-19 | Uses the current interpreter for each subprocess and stops on a nonzero exit. Earlier stages remain committed if a later stage fails; idempotent reruns skip unchanged rows. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1-7 | Imports process tools and refuses to initialize without PGPASSWORD, preventing an interactive prompt inside the container. |
| 2 | 1-7 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 3 | 1-7 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 4 | 1-7 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 5 | 1-7 | Blank separator; no execution. |
| 6 | 1-7 | Conditional branch: determines which following statements run. |
| 7 | 1-7 | Failure path: interrupts normal execution with the stated exception. |
| 8 | 8-15 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 9 | 8-15 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 10 | 8-15 | Declares data → functions → model-context order. Explicitly forwards PG values as CLI arguments to import_data, whose connection defaults otherwise differ. |
| 11 | 8-15 | Declares data → functions → model-context order. Explicitly forwards PG values as CLI arguments to import_data, whose connection defaults otherwise differ. |
| 12 | 8-15 | Declares data → functions → model-context order. Explicitly forwards PG values as CLI arguments to import_data, whose connection defaults otherwise differ. |
| 13 | 8-15 | Declares data → functions → model-context order. Explicitly forwards PG values as CLI arguments to import_data, whose connection defaults otherwise differ. |
| 14 | 8-15 | Declares data → functions → model-context order. Explicitly forwards PG values as CLI arguments to import_data, whose connection defaults otherwise differ. |
| 15 | 8-15 | Closes the multiline expression or payload begun above. |
| 16 | 16-19 | Loop: repeats the following operations for the stated elements/condition. |
| 17 | 16-19 | Uses the current interpreter for each subprocess and stops on a nonzero exit. Earlier stages remain committed if a later stage fails; idempotent reruns skip unchanged rows. |
| 18 | 16-19 | Uses the current interpreter for each subprocess and stops on a nonzero exit. Earlier stages remain committed if a later stage fails; idempotent reruns skip unchanged rows. |
| 19 | 16-19 | Uses the current interpreter for each subprocess and stops on a nonzero exit. Earlier stages remain committed if a later stage fails; idempotent reruns skip unchanged rows. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  """Initialize the container database using the existing idempotent importers."""
   2  import os
   3  import subprocess
   4  import sys
   5  
   6  if not os.getenv('PGPASSWORD'):
   7      raise SystemExit('PGPASSWORD must be supplied by Docker Compose.')
   8  # Each importer commits independently. If a later stage fails, rerunning
   9  # resumes safely: identical earlier records are skipped, conflicts rejected.
  10  steps=[
  11   ['import_data.py','--host',os.getenv('PGHOST','db'),'--port',os.getenv('PGPORT','5432'),
  12    '--database',os.getenv('PGDATABASE','decision_lab'),'--user',os.getenv('PGUSER','postgres')],
  13   ['import_functions.py'],
  14   ['import_model_context.py'],
  15  ]
  16  for command in steps:
  17      print('\nRunning '+command[0],flush=True)
  18      subprocess.run([sys.executable,*command],check=True)
  19  print('\nContainer database initialized. Run the verification commands before starting the API.',flush=True)
```
