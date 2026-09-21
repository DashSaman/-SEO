#!/usr/bin/env bash
set -euo pipefail
BACKUP_DIR="${1:?usage: phase2-restore-check.sh /opt/growth-os/backups/phase2-YYYYMMDD-HHMMSS}"
cd "$BACKUP_DIR"
sha256sum -c SHA256SUMS
pg_restore -l activepieces.dump >/dev/null
python3 - <<'PY'
from pathlib import Path
text = Path('activepieces.env').read_text()
for key in ('AP_ENCRYPTION_KEY=', 'AP_JWT_SECRET=', 'AP_POSTGRES_PASSWORD='):
    if key not in text:
        raise SystemExit('missing ' + key)
print('RESTORE_INPUTS_READABLE')
PY
