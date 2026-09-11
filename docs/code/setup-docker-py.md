# setup_docker.py

Checks local prerequisites and creates or preserves the separate Compose database password in ignored .env.

Source: `d0afd0c367f72354259d0661a76a0119fb4ed8b2`. Numbers refer to the original physical lines, including comments and blanks.

[Back to index](../CODE_INDEX.md)

## Reading blocks

These notes explain the purpose of each logical block. The next section maps each physical line to its block and shows the source.

| Lines | Explanation |
|---|---|
| 1-9 | Locates the project root and enumerates source/private-artifact prerequisites. This older list does not include replay_story.py, though the current Dockerfile requires it. |
| 10-12 | Reports missing required files or raw-data directory before creating configuration. It checks directory existence, not readability of every raw file. |
| 13-16 | Uses git check-ignore to ensure .env is excluded before writing a secret. Any nonzero result stops setup. |
| 17-21 | If .env already contains a DECISION_LAB_DB_PASSWORD assignment, preserves it. It does not validate that an existing value is nonempty or correct for an existing database. |
| 22-27 | Otherwise appends or creates a 24-random-byte hex password without printing it. Existing other settings survive. |
| 28 | Explains that this container password is separate from the Windows PostgreSQL installation. Changing .env later does not itself rotate the database password. |

## Every physical line

The short line note is read together with its linked block explanation above. Long compound HTML/JavaScript lines remain intact to preserve traceability.

| Line | Block | Line note |
|---|---|---|
| 1 | 1-9 | Locates the project root and enumerates source/private-artifact prerequisites. This older list does not include replay_story.py, though the current Dockerfile requires it. |
| 2 | 1-9 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 3 | 1-9 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 4 | 1-9 | Blank separator; no execution. |
| 5 | 1-9 | Locates the project root and enumerates source/private-artifact prerequisites. This older list does not include replay_story.py, though the current Dockerfile requires it. |
| 6 | 1-9 | Locates the project root and enumerates source/private-artifact prerequisites. This older list does not include replay_story.py, though the current Dockerfile requires it. |
| 7 | 1-9 | Locates the project root and enumerates source/private-artifact prerequisites. This older list does not include replay_story.py, though the current Dockerfile requires it. |
| 8 | 1-9 | Locates the project root and enumerates source/private-artifact prerequisites. This older list does not include replay_story.py, though the current Dockerfile requires it. |
| 9 | 1-9 | Locates the project root and enumerates source/private-artifact prerequisites. This older list does not include replay_story.py, though the current Dockerfile requires it. |
| 10 | 10-12 | Reports missing required files or raw-data directory before creating configuration. It checks directory existence, not readability of every raw file. |
| 11 | 10-12 | Conditional branch: determines which following statements run. |
| 12 | 10-12 | Conditional branch: determines which following statements run. |
| 13 | 13-16 | Source comment; explanatory text, not executed. See the block note for corrections where applicable. |
| 14 | 13-16 | Import: makes these names available; guarded CLI entry points do not run merely because they are imported. |
| 15 | 13-16 | Uses git check-ignore to ensure .env is excluded before writing a secret. Any nonzero result stops setup. |
| 16 | 13-16 | Conditional branch: determines which following statements run. |
| 17 | 17-21 | If .env already contains a DECISION_LAB_DB_PASSWORD assignment, preserves it. It does not validate that an existing value is nonempty or correct for an existing database. |
| 18 | 17-21 | Conditional branch: determines which following statements run. |
| 19 | 17-21 | If .env already contains a DECISION_LAB_DB_PASSWORD assignment, preserves it. It does not validate that an existing value is nonempty or correct for an existing database. |
| 20 | 17-21 | Conditional branch: determines which following statements run. |
| 21 | 17-21 | If .env already contains a DECISION_LAB_DB_PASSWORD assignment, preserves it. It does not validate that an existing value is nonempty or correct for an existing database. |
| 22 | 22-27 | Conditional branch: determines which following statements run. |
| 23 | 22-27 | Context manager: establishes resource scope and guarantees cleanup on exit. |
| 24 | 22-27 | Otherwise appends or creates a 24-random-byte hex password without printing it. Existing other settings survive. |
| 25 | 22-27 | Conditional branch: determines which following statements run. |
| 26 | 22-27 | Otherwise appends or creates a 24-random-byte hex password without printing it. Existing other settings survive. |
| 27 | 22-27 | Otherwise appends or creates a 24-random-byte hex password without printing it. Existing other settings survive. |
| 28 | 28 | Explains that this container password is separate from the Windows PostgreSQL installation. Changing .env later does not itself rotate the database password. |

## Numbered source

The embedded font payload is abbreviated for readability only; the original file is unmodified and fingerprinted in SOURCE_MANIFEST.json.

```text
   1  """Prepare local Compose settings without printing or replacing a password."""
   2  from pathlib import Path
   3  import secrets
   4  
   5  root=Path(__file__).resolve().parent
   6  required=['requirements.txt','main.py','inference.py','replay.html','objectives.py','verify_model.py',
   7   'import_data.py','import_functions.py','import_model_context.py','feature_math.py','sql_features.py',
   8   'sql_runtime.py','verify_sql_features.py','verify_sql_runtime.py','bootstrap_database.py']
   9  required += ['models/'+n for n in ['model_delta_default_weights.pkl','model_delta_default_results.pkl','preprocessed_sequences_delta_default.pkl']]
  10  missing=[name for name in required if not (root/name).is_file()]
  11  if not (root/'data'/'raw').is_dir():missing.append('data/raw/')
  12  if missing:raise SystemExit('Missing required files:\n'+'\n'.join(missing))
  13  # Confirm the secret file is excluded from Git before creating it.
  14  import subprocess
  15  check=subprocess.run(['git','check-ignore','--quiet','--no-index','.env'],cwd=root)
  16  if check.returncode!=0:raise SystemExit('Add .env to .gitignore before running this script.')
  17  path=root/'.env'
  18  if path.exists():
  19      text=path.read_text(encoding='utf-8-sig')
  20      if any(line.strip().startswith('DECISION_LAB_DB_PASSWORD=') for line in text.splitlines()):
  21          print('Existing Docker database password retained.')
  22      else:
  23          with path.open('a',encoding='utf-8') as f:f.write('\nDECISION_LAB_DB_PASSWORD='+secrets.token_hex(24)+'\n')
  24          print('Docker database password added to .env; existing settings retained.')
  25  else:
  26      path.write_text('DECISION_LAB_DB_PASSWORD='+secrets.token_hex(24)+'\n',encoding='utf-8')
  27      print('Local .env created with a generated Docker database password.')
  28  print('Setup complete. The password is separate from your Windows PostgreSQL password.')
```
