# Growth OS Phase 2 Core Platform Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deploy the first persistent 24/7 Growth OS control plane on the verified Ubuntu 24.04 WSL2 host, with Activepieces Community Edition, PostgreSQL, Redis, Uptime Kuma, Dockge, backups, localhost-only management ports, and Windows-to-WSL autostart.

**Architecture:** Docker Compose stacks live under `/opt/stacks`; the checked-out documentation/runtime repository lives at `/opt/growth-os/repo`; backups and host state live under `/opt/growth-os`. Activepieces provides orchestration, PostgreSQL durable state, Redis job queue, one worker with concurrency 1, Uptime Kuma service monitoring, and Dockge a beginner-friendly Compose UI. Phase 2 never modifies MyTel or Tehran Network production sites.

**Tech Stack:** Ubuntu 24.04 on WSL2, Docker Engine 29.8.1, Docker Compose v5.5.1, Activepieces Community Edition `ghcr.io/activepieces/activepieces:0.86.3`, `pgvector/pgvector:0.8.0-pg14`, `redis:7.0.7`, `louislam/uptime-kuma:2`, `louislam/dockge:1`, PowerShell Scheduled Tasks.

**Spec:** `docs/superpowers/specs/2026-09-21-growth-os-autonomous-content-video-reporting-design.md`

## Global Constraints

- Owner workflow is review-only for ordinary operations.
- Paid generative APIs remain disabled by default.
- Phase 2 performs no production-site changes.
- MyTel and Tehran Network credentials, queues, logs, reports, and state remain isolated.
- No raw secret value is committed to GitHub.
- Persistent services use Docker Compose and `restart: unless-stopped`.
- Management UIs bind to `127.0.0.1` only during the pilot.
- Activepieces Community Edition only; no enterprise-only dependency.
- `AP_WORKER_CONCURRENCY=1`.
- Existing WSL cap remains 20 GB RAM, 12 processors, 8 GB swap.
- Every completed step and deviation is recorded in `AGENT.md`.
- Operator docs remain bilingual FA/EN.

## Review Focus

1. **WSL starts but Docker does not** — autostart test must prove Docker becomes active without manual intervention.
2. **Port collision on 8080/3001/5001** — preflight aborts before deployment if a selected port is already in use.
3. **Secret generation failure** — Activepieces deployment aborts if encryption key, JWT secret, or PostgreSQL password is empty.
4. **Worker cannot reach app** — worker uses `AP_FRONTEND_URL=http://app`; smoke test must prove worker stays running.
5. **Backup exists but is unusable** — backup must be non-zero, checksum-valid, and readable by `pg_restore -l`.

---

## File Structure

Repository files created in this phase:

```text
growth-os/runtime/core/
  README-FA.md
  README-EN.md
  activepieces.compose.yaml
  uptime-kuma.compose.yaml
  dockge.compose.yaml
  phase2-smoke.sh
  phase2-backup.sh
  phase2-restore-check.sh
  windows-autostart.ps1
  LICENSE-LEDGER.md

growth-os/operations/
  PHASE2-RUNBOOK-FA.md
  PHASE2-RUNBOOK-EN.md

AGENT.md
```

Live host layout:

```text
/opt/growth-os/repo/                 # read-only working clone of growth-os-bootstrap branch
/opt/growth-os/backups/
/opt/growth-os/logs/
/opt/growth-os/state/

/opt/stacks/activepieces/
  compose.yaml
  .env
  cache/

/opt/stacks/uptime-kuma/
  compose.yaml

/opt/stacks/dockge/
  compose.yaml
  data/
```

Repository templates contain no secrets. `/opt/stacks/activepieces/.env` is host-only and never committed.

---

### Task 1: Phase 2 host preflight, canonical repo clone, and runtime directories

**Files:**
- Create: `growth-os/runtime/core/README-FA.md`
- Create: `growth-os/runtime/core/README-EN.md`
- Modify: `AGENT.md`

**Interfaces:**
- Consumes: verified Phase 1 WSL2 + Docker baseline.
- Produces: canonical repo clone at `/opt/growth-os/repo`, runtime directories, and verified free ports.

- [ ] **Step 1: Verify host identity and Docker state**

Run inside Ubuntu:

```bash
whoami
id
free -h
nproc
docker --version
docker compose version
systemctl is-active docker
```

Expected: `amirreza`; about 19 GiB RAM; `nproc` = 12; Docker 29.8.1; Compose v5.5.1; Docker `active`.

- [ ] **Step 2: Verify required ports are unused**

```bash
for p in 8080 3001 5001; do
  if ss -ltn "sport = :$p" | grep -q LISTEN; then
    echo "PORT_IN_USE:$p"
    exit 1
  else
    echo "PORT_FREE:$p"
  fi
done
```

Expected exactly three `PORT_FREE` lines.

- [ ] **Step 3: Create runtime directories**

```bash
sudo mkdir -p /opt/growth-os/backups /opt/growth-os/logs /opt/growth-os/state
sudo mkdir -p /opt/stacks/activepieces /opt/stacks/uptime-kuma /opt/stacks/dockge
sudo chown -R amirreza:amirreza /opt/growth-os /opt/stacks
chmod 750 /opt/growth-os /opt/growth-os/backups /opt/growth-os/logs /opt/growth-os/state /opt/stacks
```

- [ ] **Step 4: Clone the working branch to the canonical host path**

```bash
if [ -e /opt/growth-os/repo ]; then
  echo REPO_PATH_ALREADY_EXISTS
  exit 1
fi

git clone --branch growth-os-bootstrap --single-branch https://github.com/DashSaman/-SEO.git /opt/growth-os/repo
```

Expected: checkout of `growth-os-bootstrap` succeeds without requiring credentials because the repository is public.

- [ ] **Step 5: Verify branch and ownership**

```bash
git -C /opt/growth-os/repo branch --show-current
stat -c '%U:%G %a %n' /opt/growth-os /opt/stacks
```

Expected branch `growth-os-bootstrap`; owner `amirreza:amirreza`.

- [ ] **Step 6: Create bilingual host-layout docs and record evidence**

Create `growth-os/runtime/core/README-FA.md` and `README-EN.md` with the exact runtime paths, local ports, backup path, and rule that `.env` never enters Git. Update `AGENT.md` with actual preflight output.

Commit those repository changes through the connected GitHub integration with commit message:

```text
docs: record Phase 2 host preflight
```

Then refresh the host clone:

```bash
git -C /opt/growth-os/repo pull --ff-only
```

---

### Task 2: Activepieces Community Edition stack

**Files:**
- Create: `growth-os/runtime/core/activepieces.compose.yaml`
- Create live host file: `/opt/stacks/activepieces/compose.yaml`
- Create live host secret file: `/opt/stacks/activepieces/.env`
- Modify: `AGENT.md`

**Interfaces:**
- Consumes: Task 1 runtime directories and free port 8080.
- Produces: app on `127.0.0.1:8080`, one worker, PostgreSQL, Redis.

- [ ] **Step 1: Write the sanitized Compose template**

Create `growth-os/runtime/core/activepieces.compose.yaml`:

```yaml
services:
  app:
    image: ghcr.io/activepieces/activepieces:0.86.3
    container_name: growthos-activepieces-app
    restart: unless-stopped
    ports:
      - "127.0.0.1:8080:80"
    depends_on:
      postgres:
        condition: service_started
      redis:
        condition: service_started
    env_file: .env
    environment:
      AP_CONTAINER_TYPE: APP
    volumes:
      - ./cache:/usr/src/app/cache
    networks:
      - activepieces

  worker:
    image: ghcr.io/activepieces/activepieces:0.86.3
    container_name: growthos-activepieces-worker
    restart: unless-stopped
    depends_on:
      - app
    env_file: .env
    environment:
      AP_CONTAINER_TYPE: WORKER
      AP_FRONTEND_URL: http://app
      AP_WORKER_CONCURRENCY: "1"
      AP_EXECUTION_MODE: SANDBOX_CODE_ONLY
    volumes:
      - ./cache:/usr/src/app/cache
    networks:
      - activepieces

  postgres:
    image: pgvector/pgvector:0.8.0-pg14
    container_name: growthos-postgres
    restart: unless-stopped
    env_file: .env
    environment:
      POSTGRES_DB: ${AP_POSTGRES_DATABASE}
      POSTGRES_USER: ${AP_POSTGRES_USERNAME}
      POSTGRES_PASSWORD: ${AP_POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - activepieces

  redis:
    image: redis:7.0.7
    container_name: growthos-redis
    restart: unless-stopped
    command: ["redis-server", "--appendonly", "yes"]
    volumes:
      - redis_data:/data
    networks:
      - activepieces

volumes:
  postgres_data:
  redis_data:

networks:
  activepieces:
```

- [ ] **Step 2: Commit the sanitized template and refresh the host clone**

Commit message:

```text
feat: add Activepieces core stack template
```

Then:

```bash
git -C /opt/growth-os/repo pull --ff-only
cp /opt/growth-os/repo/growth-os/runtime/core/activepieces.compose.yaml /opt/stacks/activepieces/compose.yaml
mkdir -p /opt/stacks/activepieces/cache
```

- [ ] **Step 3: Generate host-only secrets**

```bash
sudo apt install -y openssl
cd /opt/stacks/activepieces
AP_ENCRYPTION_KEY="$(openssl rand -hex 16)"
AP_JWT_SECRET="$(openssl rand -hex 32)"
AP_POSTGRES_PASSWORD="$(openssl rand -base64 36 | tr -d '\n/+=' | cut -c1-32)"
cat > .env <<EOF
AP_ENVIRONMENT=prod
AP_FRONTEND_URL=http://localhost:8080
AP_POSTGRES_DATABASE=activepieces
AP_POSTGRES_HOST=postgres
AP_POSTGRES_PORT=5432
AP_POSTGRES_USERNAME=postgres
AP_POSTGRES_PASSWORD=${AP_POSTGRES_PASSWORD}
AP_REDIS_HOST=redis
AP_REDIS_PORT=6379
AP_ENCRYPTION_KEY=${AP_ENCRYPTION_KEY}
AP_JWT_SECRET=${AP_JWT_SECRET}
AP_EXECUTION_MODE=SANDBOX_CODE_ONLY
AP_WORKER_CONCURRENCY=1
AP_TELEMETRY_ENABLED=false
AP_TRIGGER_DEFAULT_POLL_INTERVAL=5
AP_FLOW_TIMEOUT_SECONDS=600
EOF
chmod 600 .env
```

- [ ] **Step 4: Verify secrets without printing values**

```bash
python3 - <<'PY'
from pathlib import Path
required = {'AP_ENCRYPTION_KEY','AP_JWT_SECRET','AP_POSTGRES_PASSWORD'}
vals = {}
for line in Path('/opt/stacks/activepieces/.env').read_text().splitlines():
    if '=' in line:
        k, v = line.split('=', 1)
        vals[k] = v
missing = [k for k in required if not vals.get(k)]
if missing:
    raise SystemExit('EMPTY_SECRET:' + ','.join(sorted(missing)))
print('SECRETS_OK')
PY
```

Expected: `SECRETS_OK`.

- [ ] **Step 5: Validate Compose**

```bash
cd /opt/stacks/activepieces
docker compose config >/dev/null && echo COMPOSE_OK
```

Expected: `COMPOSE_OK`.

- [ ] **Step 6: Start Activepieces**

```bash
docker compose -p activepieces up -d
```

- [ ] **Step 7: Wait for health and verify every component**

```bash
for i in $(seq 1 60); do
  if curl -fsS http://localhost:8080/api/v1/health >/dev/null; then
    echo ACTIVEPIECES_HEALTH_OK
    break
  fi
  sleep 2
  if [ "$i" -eq 60 ]; then
    docker compose -p activepieces ps
    docker logs --tail 100 growthos-activepieces-app
    exit 1
  fi
done

docker exec growthos-postgres pg_isready -U postgres -d activepieces
test "$(docker exec growthos-redis redis-cli ping)" = "PONG"
test "$(docker inspect -f '{{.State.Status}}' growthos-activepieces-worker)" = "running"
docker compose -p activepieces ps
```

Expected: health OK, PostgreSQL accepting connections, Redis PONG, worker running.

- [ ] **Step 8: Record runtime evidence**

Update `AGENT.md` with actual image IDs/digests from:

```bash
docker inspect --format='{{.Config.Image}} {{.Image}}' growthos-activepieces-app growthos-postgres growthos-redis
```

Commit message:

```text
chore: record Activepieces runtime verification
```

---

### Task 3: Uptime Kuma monitoring stack

**Files:**
- Create: `growth-os/runtime/core/uptime-kuma.compose.yaml`
- Create live host file: `/opt/stacks/uptime-kuma/compose.yaml`
- Modify: `AGENT.md`

**Interfaces:**
- Consumes: Docker Compose and free port 3001.
- Produces: Uptime Kuma on `127.0.0.1:3001`.

- [ ] **Step 1: Create the template**

```yaml
services:
  uptime-kuma:
    image: louislam/uptime-kuma:2
    container_name: growthos-uptime-kuma
    restart: unless-stopped
    ports:
      - "127.0.0.1:3001:3001"
    volumes:
      - uptime_kuma_data:/app/data

volumes:
  uptime_kuma_data:
```

- [ ] **Step 2: Commit and refresh host clone**

Commit message:

```text
feat: add Uptime Kuma monitoring stack
```

Then:

```bash
git -C /opt/growth-os/repo pull --ff-only
cp /opt/growth-os/repo/growth-os/runtime/core/uptime-kuma.compose.yaml /opt/stacks/uptime-kuma/compose.yaml
cd /opt/stacks/uptime-kuma
docker compose config >/dev/null && echo COMPOSE_OK
```

- [ ] **Step 3: Start and wait for HTTP response**

```bash
docker compose -p uptime-kuma up -d
for i in $(seq 1 60); do
  if curl -fsS http://localhost:3001/ >/dev/null; then
    echo UPTIME_KUMA_HTTP_OK
    break
  fi
  sleep 2
  if [ "$i" -eq 60 ]; then
    docker logs --tail 100 growthos-uptime-kuma
    exit 1
  fi
done
```

Expected: `UPTIME_KUMA_HTTP_OK`.

- [ ] **Step 4: Record image digest**

```bash
docker inspect --format='{{.Config.Image}} {{.Image}}' growthos-uptime-kuma
```

Write result to `AGENT.md` and commit message:

```text
chore: record Uptime Kuma runtime verification
```

---

### Task 4: Dockge local Compose management UI

**Files:**
- Create: `growth-os/runtime/core/dockge.compose.yaml`
- Create live host file: `/opt/stacks/dockge/compose.yaml`
- Modify: `AGENT.md`

**Interfaces:**
- Consumes: `/opt/stacks`, Docker socket, free port 5001.
- Produces: Dockge on `127.0.0.1:5001`.

- [ ] **Step 1: Verify operator numeric UID/GID**

```bash
id -u amirreza
id -g amirreza
```

Expected on this host: `1000` and `1000`. If output differs, do not start Dockge; record the actual values and generate the Compose file with those actual numbers before proceeding.

- [ ] **Step 2: Create the template for the verified 1000/1000 host**

```yaml
services:
  dockge:
    image: louislam/dockge:1
    container_name: growthos-dockge
    restart: unless-stopped
    ports:
      - "127.0.0.1:5001:5001"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ./data:/app/data
      - /opt/stacks:/opt/stacks
    environment:
      DOCKGE_STACKS_DIR: /opt/stacks
      PUID: "1000"
      PGID: "1000"
```

- [ ] **Step 3: Commit, refresh, validate and start**

Commit message:

```text
feat: add local Dockge stack manager
```

Then:

```bash
git -C /opt/growth-os/repo pull --ff-only
cp /opt/growth-os/repo/growth-os/runtime/core/dockge.compose.yaml /opt/stacks/dockge/compose.yaml
mkdir -p /opt/stacks/dockge/data
cd /opt/stacks/dockge
docker compose config >/dev/null && echo COMPOSE_OK
docker compose -p dockge up -d
```

- [ ] **Step 4: Wait for Dockge UI**

```bash
for i in $(seq 1 60); do
  if curl -fsS http://localhost:5001/ >/dev/null; then
    echo DOCKGE_HTTP_OK
    break
  fi
  sleep 2
  if [ "$i" -eq 60 ]; then
    docker logs --tail 100 growthos-dockge
    exit 1
  fi
done
```

Expected: `DOCKGE_HTTP_OK`.

- [ ] **Step 5: Record security boundary and image digest**

```bash
docker inspect --format='{{.Config.Image}} {{.Image}}' growthos-dockge
```

`AGENT.md` must state that Dockge has root-equivalent capability through `/var/run/docker.sock` and is intentionally localhost-only. Commit message:

```text
chore: record Dockge runtime verification
```

---

### Task 5: Unified Phase 2 smoke test

**Files:**
- Create: `growth-os/runtime/core/phase2-smoke.sh`
- Modify: `AGENT.md`

**Interfaces:**
- Consumes: all Phase 2 containers.
- Produces: one deterministic PASS/FAIL command used after every restart.

- [ ] **Step 1: Create the smoke test**

```bash
#!/usr/bin/env bash
set -euo pipefail

pass() { printf 'PASS %s\n' "$1"; }
fail() { printf 'FAIL %s\n' "$1" >&2; exit 1; }

systemctl is-active --quiet docker && pass docker-active || fail docker-active

docker inspect -f '{{.State.Running}}' growthos-activepieces-app | grep -qx true && pass activepieces-app || fail activepieces-app
docker inspect -f '{{.State.Running}}' growthos-activepieces-worker | grep -qx true && pass activepieces-worker || fail activepieces-worker
docker inspect -f '{{.State.Running}}' growthos-postgres | grep -qx true && pass postgres-container || fail postgres-container
docker inspect -f '{{.State.Running}}' growthos-redis | grep -qx true && pass redis-container || fail redis-container
docker inspect -f '{{.State.Running}}' growthos-uptime-kuma | grep -qx true && pass uptime-kuma || fail uptime-kuma
docker inspect -f '{{.State.Running}}' growthos-dockge | grep -qx true && pass dockge || fail dockge

curl -fsS http://localhost:8080/api/v1/health >/dev/null && pass activepieces-health || fail activepieces-health
docker exec growthos-postgres pg_isready -U postgres -d activepieces >/dev/null && pass postgres-ready || fail postgres-ready
test "$(docker exec growthos-redis redis-cli ping)" = "PONG" && pass redis-ping || fail redis-ping
curl -fsS http://localhost:3001/ >/dev/null && pass kuma-http || fail kuma-http
curl -fsS http://localhost:5001/ >/dev/null && pass dockge-http || fail dockge-http

for p in 8080 3001 5001; do
  ss -ltn "sport = :$p" | grep -q LISTEN || fail "port-$p"
done
pass expected-ports

echo PHASE2_SMOKE_OK
```

- [ ] **Step 2: Commit and execute**

Commit message:

```text
test: add Phase 2 smoke verification
```

Then:

```bash
git -C /opt/growth-os/repo pull --ff-only
chmod +x /opt/growth-os/repo/growth-os/runtime/core/phase2-smoke.sh
/opt/growth-os/repo/growth-os/runtime/core/phase2-smoke.sh
```

Expected final line: `PHASE2_SMOKE_OK`.

- [ ] **Step 3: Record smoke result**

Update `AGENT.md` with complete PASS list and commit message:

```text
chore: record Phase 2 smoke result
```

---

### Task 6: Backup and restore-input verification

**Files:**
- Create: `growth-os/runtime/core/phase2-backup.sh`
- Create: `growth-os/runtime/core/phase2-restore-check.sh`
- Modify: `AGENT.md`

**Interfaces:**
- Consumes: Activepieces PostgreSQL and host `.env`.
- Produces: timestamped dump, protected secret-config copy, checksums, and non-destructive restore-readability test.

- [ ] **Step 1: Create backup script**

```bash
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
```

- [ ] **Step 2: Create restore-input verification script**

```bash
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
```

- [ ] **Step 3: Commit scripts**

Commit message:

```text
feat: add Phase 2 backup verification
```

- [ ] **Step 4: Refresh host clone and run**

```bash
git -C /opt/growth-os/repo pull --ff-only
sudo apt install -y postgresql-client
chmod +x /opt/growth-os/repo/growth-os/runtime/core/phase2-backup.sh
chmod +x /opt/growth-os/repo/growth-os/runtime/core/phase2-restore-check.sh
BACKUP_DIR="$(/opt/growth-os/repo/growth-os/runtime/core/phase2-backup.sh)"
/opt/growth-os/repo/growth-os/runtime/core/phase2-restore-check.sh "$BACKUP_DIR"
```

Expected final line: `RESTORE_INPUTS_READABLE`.

- [ ] **Step 5: Record exact backup evidence**

```bash
find "$BACKUP_DIR" -maxdepth 1 -type f -printf '%f %s bytes\n'
cat "$BACKUP_DIR/SHA256SUMS"
```

Record file sizes and hashes in `AGENT.md`; never commit backup files or secret values. Commit message:

```text
chore: record Phase 2 backup evidence
```

---

### Task 7: Windows autostart and plugged-in no-sleep policy

**Files:**
- Create: `growth-os/runtime/core/windows-autostart.ps1`
- Modify: `AGENT.md`

**Interfaces:**
- Consumes: Windows 11 host and `Ubuntu-24.04` distro.
- Produces: WSL launch at user logon and no automatic sleep while AC powered.

- [ ] **Step 1: Create PowerShell setup script**

```powershell
$ErrorActionPreference = 'Stop'

powercfg /change standby-timeout-ac 0

$Action = New-ScheduledTaskAction -Execute 'wsl.exe' -Argument '-d Ubuntu-24.04 --exec /bin/true'
$Trigger = New-ScheduledTaskTrigger -AtLogOn
$Settings = New-ScheduledTaskSettingsSet -StartWhenAvailable
$Principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType Interactive -RunLevel Highest

Register-ScheduledTask `
  -TaskName 'GrowthOS-Start-WSL' `
  -Action $Action `
  -Trigger $Trigger `
  -Settings $Settings `
  -Principal $Principal `
  -Description 'Start Ubuntu WSL for Growth OS services at user logon' `
  -Force

Get-ScheduledTask -TaskName 'GrowthOS-Start-WSL' | Select-Object TaskName, State
```

- [ ] **Step 2: Commit script**

Commit message:

```text
feat: add Growth OS Windows autostart
```

- [ ] **Step 3: Run in Administrator PowerShell**

Use the script content from the repository after it has been committed. Expected scheduled task name: `GrowthOS-Start-WSL`.

- [ ] **Step 4: Test without reboot**

```powershell
Start-ScheduledTask -TaskName 'GrowthOS-Start-WSL'
Start-Sleep -Seconds 8
wsl -d Ubuntu-24.04 -- systemctl is-active docker
```

Expected: `active`.

- [ ] **Step 5: Run full smoke test from Windows through WSL**

```powershell
wsl -d Ubuntu-24.04 -- bash -lc '/opt/growth-os/repo/growth-os/runtime/core/phase2-smoke.sh'
```

Expected final line: `PHASE2_SMOKE_OK`.

- [ ] **Step 6: Record evidence**

Update `AGENT.md` with scheduled-task state and smoke result. Commit message:

```text
chore: record Windows autostart verification
```

---

### Task 8: License ledger and bilingual operations runbook

**Files:**
- Create: `growth-os/runtime/core/LICENSE-LEDGER.md`
- Create: `growth-os/operations/PHASE2-RUNBOOK-FA.md`
- Create: `growth-os/operations/PHASE2-RUNBOOK-EN.md`
- Modify: `AGENT.md`

**Interfaces:**
- Consumes: actual deployed images and verified official licensing sources.
- Produces: commercialization due-diligence record and recovery guide.

- [ ] **Step 1: Populate exact license ledger**

Record at minimum:

```text
Activepieces Community Edition core — MIT; enterprise directories separately commercial.
Uptime Kuma — MIT.
Dockge — MIT.
pgvector — PostgreSQL License.
Redis 7.0.7 — BSD-3-Clause, because Redis 7.2.x and prior remain BSDv3.
Docker/Moby/Compose — record the exact upstream license for the installed engine/CLI/compose components.
```

Every row contains: component, image/tag, image digest, license, official source, commercial-use note, redistribution/SaaS note, verification date.

- [ ] **Step 2: Write bilingual operational runbooks**

Both runbooks include these exact commands:

```bash
cd /opt/stacks/activepieces && docker compose -p activepieces ps
cd /opt/stacks/uptime-kuma && docker compose -p uptime-kuma ps
cd /opt/stacks/dockge && docker compose -p dockge ps

docker logs --tail 100 growthos-activepieces-app
docker logs --tail 100 growthos-activepieces-worker
docker logs --tail 100 growthos-postgres
docker logs --tail 100 growthos-redis

/opt/growth-os/repo/growth-os/runtime/core/phase2-smoke.sh
/opt/growth-os/repo/growth-os/runtime/core/phase2-backup.sh
```

They also explain Windows access URLs:

```text
http://localhost:8080
http://localhost:3001
http://localhost:5001
```

- [ ] **Step 3: Commit documentation**

Commit message:

```text
docs: add Phase 2 license and operations runbooks
```

---

### Task 9: Phase 2 cold-start resilience and completion gate

**Files:**
- Modify: `AGENT.md`

**Interfaces:**
- Consumes: all Phase 2 services, smoke test, backup scripts, Windows autostart.
- Produces: verified Phase 2 completion and handoff to Phase 3 Local AI.

- [ ] **Step 1: Take a fresh verified backup**

```bash
BACKUP_DIR="$(/opt/growth-os/repo/growth-os/runtime/core/phase2-backup.sh)"
/opt/growth-os/repo/growth-os/runtime/core/phase2-restore-check.sh "$BACKUP_DIR"
```

Expected: checksum PASS and `RESTORE_INPUTS_READABLE`.

- [ ] **Step 2: Cold-stop WSL**

Inside Ubuntu:

```bash
exit
```

Then in Windows PowerShell:

```powershell
wsl --shutdown
wsl -d Ubuntu-24.04 --exec /bin/true
Start-Sleep -Seconds 10
```

- [ ] **Step 3: Run full smoke test after cold start**

```powershell
wsl -d Ubuntu-24.04 -- bash -lc '/opt/growth-os/repo/growth-os/runtime/core/phase2-smoke.sh'
```

Expected final line: `PHASE2_SMOKE_OK`.

- [ ] **Step 4: Verify all local UIs from Windows browser**

Open:

```text
http://localhost:8080
http://localhost:3001
http://localhost:5001
```

Expected: Activepieces, Uptime Kuma and Dockge load.

- [ ] **Step 5: Close Phase 2 in `AGENT.md`**

Set:

```text
STATUS: PHASE2 COMPLETE + PHASE3 READY
CURRENT_PHASE: Phase 3 — Local AI Layer
CURRENT_TASK: P3-AI-01 — Local model runtime and GPU job scheduler
```

Record actual image digests, smoke result, backup verification, license ledger commit, and any deviations.

Commit message:

```text
chore: close Phase 2 core platform
```

---

## Phase 2 Completion Criteria

```text
[ ] Activepieces app reachable on localhost:8080
[ ] Activepieces worker running at concurrency 1
[ ] PostgreSQL ready
[ ] Redis returns PONG
[ ] Uptime Kuma reachable on localhost:3001
[ ] Dockge reachable on localhost:5001
[ ] Management UIs remain localhost-only
[ ] phase2-smoke.sh returns PHASE2_SMOKE_OK
[ ] Backup dump and secret-config copy pass checksum/readability verification
[ ] WSL cold start returns all services without manual startup
[ ] Windows GrowthOS-Start-WSL scheduled task exists
[ ] AC sleep is disabled for 24/7 pilot operation
[ ] License ledger complete
[ ] FA/EN runbooks complete
[ ] AGENT.md records every action and deviation
```

## Sources Used for the Plan

- Activepieces official self-host docs: Docker Compose with PostgreSQL and Redis; Docker Compose v2; WSL2 on Windows; `/api/v1/health` verification.
- Activepieces official architecture docs: PostgreSQL durable state and Redis/BullMQ queue.
- Activepieces worker docs: concurrency 1 and `SANDBOX_CODE_ONLY` production guidance.
- Activepieces license docs: Community Edition core MIT; enterprise directories/features separately commercial.
- Uptime Kuma official docs: Docker Compose deployment and localhost-only port binding supported; MIT license.
- Dockge official docs: `/opt/stacks`, port 5001, Docker socket mount; MIT license.
- Redis license record: Redis 7.2.x and earlier remain BSDv3; pinned image is 7.0.7.
- pgvector official license: PostgreSQL License.
