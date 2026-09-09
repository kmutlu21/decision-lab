"""Prepare local Compose settings without printing or replacing a password."""
from pathlib import Path
import secrets

root=Path(__file__).resolve().parent
required=['requirements.txt','main.py','inference.py','replay.html','objectives.py','verify_model.py',
 'import_data.py','import_functions.py','import_model_context.py','feature_math.py','sql_features.py',
 'sql_runtime.py','verify_sql_features.py','verify_sql_runtime.py','bootstrap_database.py']
required += ['models/'+n for n in ['model_delta_default_weights.pkl','model_delta_default_results.pkl','preprocessed_sequences_delta_default.pkl']]
missing=[name for name in required if not (root/name).is_file()]
if not (root/'data'/'raw').is_dir():missing.append('data/raw/')
if missing:raise SystemExit('Missing required files:\n'+'\n'.join(missing))
# Confirm the secret file is excluded from Git before creating it.
import subprocess
check=subprocess.run(['git','check-ignore','--quiet','--no-index','.env'],cwd=root)
if check.returncode!=0:raise SystemExit('Add .env to .gitignore before running this script.')
path=root/'.env'
if path.exists():
    text=path.read_text(encoding='utf-8-sig')
    if any(line.strip().startswith('DECISION_LAB_DB_PASSWORD=') for line in text.splitlines()):
        print('Existing Docker database password retained.')
    else:
        with path.open('a',encoding='utf-8') as f:f.write('\nDECISION_LAB_DB_PASSWORD='+secrets.token_hex(24)+'\n')
        print('Docker database password added to .env; existing settings retained.')
else:
    path.write_text('DECISION_LAB_DB_PASSWORD='+secrets.token_hex(24)+'\n',encoding='utf-8')
    print('Local .env created with a generated Docker database password.')
print('Setup complete. The password is separate from your Windows PostgreSQL password.')
