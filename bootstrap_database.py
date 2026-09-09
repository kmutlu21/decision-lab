"""Initialize the container database using the existing idempotent importers."""
import os
import subprocess
import sys

if not os.getenv('PGPASSWORD'):
    raise SystemExit('PGPASSWORD must be supplied by Docker Compose.')
# Each importer commits independently. If a later stage fails, rerunning
# resumes safely: identical earlier records are skipped, conflicts rejected.
steps=[
 ['import_data.py','--host',os.getenv('PGHOST','db'),'--port',os.getenv('PGPORT','5432'),
  '--database',os.getenv('PGDATABASE','decision_lab'),'--user',os.getenv('PGUSER','postgres')],
 ['import_functions.py'],
 ['import_model_context.py'],
]
for command in steps:
    print('\nRunning '+command[0],flush=True)
    subprocess.run([sys.executable,*command],check=True)
print('\nContainer database initialized. Run the verification commands before starting the API.',flush=True)
