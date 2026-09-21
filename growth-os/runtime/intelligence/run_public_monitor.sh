#!/usr/bin/env bash
set -euo pipefail

REPO=/opt/growth-os/repo
STATE=/opt/growth-os/state/sites
LOCK=/opt/growth-os/state/public-monitor.lock

exec 9>"$LOCK"
flock -n 9 || { echo "PUBLIC_MONITOR_ALREADY_RUNNING"; exit 0; }

python3 "$REPO/growth-os/runtime/intelligence/public_baseline.py" \
  --site-id mytel --url https://mytel.one \
  --output-dir "$STATE/mytel/baselines"

python3 "$REPO/growth-os/runtime/intelligence/public_baseline.py" \
  --site-id tehnet --url https://tehnet.ir \
  --output-dir "$STATE/tehnet/baselines"

echo PUBLIC_MONITOR_OK
