#!/usr/bin/env bash
set -euo pipefail
umask 077
STAMP="$(date +%Y%m%d-%H%M%S)"
DEST="/opt/growth-os/backups/phase2-${STAMP}"
mkdir -p "$DEST"

docker exec growthos-postgres pg_dump -U postgres -d activepieces -Fc > "$DEST/activepieces.dump"
cp /opt/stacks/activepieces/.env "$DEST/activepieces.env"
sha256sum "$DEST/activepieces.dump" "$DEST/activepieces.env" > "$DEST/SHA256SUMS"

test -s "$DEST/activepieces.dump"
test -s "$DEST/activepieces.env"
echo "$DEST"
