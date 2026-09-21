# Growth OS Phase 2 Core Platform Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deploy the first persistent 24/7 Growth OS control plane on the verified Ubuntu 24.04 WSL2 host, with Activepieces Community Edition, PostgreSQL, Redis, Uptime Kuma, Dockge, backups, local-only management ports, and Windows-to-WSL autostart.

**Architecture:** Docker Compose stacks live under `/opt/stacks` and persistent Growth OS operational data lives under `/opt/growth-os`. Activepieces is the workflow engine with a dedicated app container, one worker at concurrency 1, PostgreSQL as durable state, and Redis as the queue. Uptime Kuma monitors service health; Dockge provides a beginner-friendly Compose UI but is exposed only on localhost because its Docker socket mount is privileged. Phase 2 does not modify MyTel or Tehran Network production sites.

**Tech Stack:** Ubuntu 24.04 on WSL2, Docker Engine 29.8.1, Docker Compose v5.5.1, Activepieces Community Edition pinned to `ghcr.io/activepieces/activepieces:0.86.3`, `pgvector/pgvector:0.8.0-pg14`, `redis:7.0.7`, `louislam/uptime-kuma:2`, `louislam/dockge:1`, PowerShell Scheduled Tasks.

**Spec:** `docs/superpowers/specs/2026-09-21-growth-os-autonomous-content-video-reporting-design.md`

## Global Constraints

- The owner operates in review-only mode for routine Growth OS work; Phase 2 must not introduce a manual approval requirement for ordinary runtime operations.
- Paid generative APIs remain disabled by default.
- No production-site change is permitted in Phase 2.
- MyTel and Tehran Network credentials, queues, logs, reports, and state remain logically isolated.
- No raw secret value is committed to GitHub.
- Every persistent service uses Docker Compose and `restart: unless-stopped`.
- Management UIs bind to `127.0.0.1` only during the local pilot.
- Activepieces Community Edition core is used; enterprise-only features are not required by this plan.
- `AP_WORKER_CONCURRENCY=1` to reduce OOM blast radius and match Activepieces production guidance.
- The WSL host remains capped by the already-verified `.wslconfig`: 20 GB RAM, 12 processors, 8 GB swap.
- All operator-facing documentation remains bilingual FA/EN and every completed task is recorded in `AGENT.md`.

## Review Focus

1. **WSL starts but Docker does not** — the Windows autostart task must start the distro, and the smoke test must prove Docker becomes active without manual intervention.
2. **Port collision on 8080/3001/5001** — preflight must fail before deployment if any selected localhost port is already listening.
3. **Activepieces secret generation failure** — deployment must abort if encryption key, JWT secret, or PostgreSQL password is empty.
4. **Activepieces worker cannot reach app** — worker must use `AP_FRONTEND_URL=http://app` internally and smoke test must confirm worker container remains healthy/running.
5. **Backup succeeds syntactically but is unusable** — backup task must create a non-zero SQL dump, verify it contains a PostgreSQL dump header, and record SHA256.

---

## File Structure

The implementation creates or modifies these repository files:

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

The live host uses these runtime paths:

```text
/opt/stacks/activepieces/
  compose.yaml
  .env

/opt/stacks/uptime-kuma/
  compose.yaml

/opt/stacks/dockge/
  compose.yaml
  data/

/opt/growth-os/
  backups/
  logs/
  state/
```

Repository compose files are sanitized templates with no secret values. The live `/opt/stacks/activepieces/.env` is generated on the host and is never committed.

---

### Task 1: Phase 2 host preflight and runtime directories

**Files:**
- Create: `growth-os/runtime/core/README-FA.md`
- Create: `growth-os/runtime/core/README-EN.md`
- Modify: `AGENT.md`

**Interfaces:**
- Consumes: verified Phase 1 WSL2 + Docker baseline.
- Produces: `/opt/stacks`, `/opt/growth-os/{backups,logs,state}` owned by `amirreza`, and a recorded port/resource preflight.

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

Expected: user `amirreza`; memory about 19 GiB; `nproc` = 12; Docker 29.8.1; Compose v5.5.1; Docker state `active`.

- [ ] **Step 2: Verify required ports are unused**

Run:

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

Expected:

```text
PORT_FREE:8080
PORT_FREE:3001
PORT_FREE:5001
```

- [ ] **Step 3: Create runtime directories with controlled ownership**

Run:

```bash
sudo mkdir -p /opt/stacks/activepieces /opt/stacks/uptime-kuma /opt/stacks/dockge
sudo mkdir -p /opt/growth-os/backups /opt/growth-os/logs /opt/growth-os/state
sudo chown -R amirreza:amirreza /opt/stacks /opt/growth-os
chmod 750 /opt/stacks /opt/growth-os /opt/growth-os/backups /opt/growth-os/logs /opt/growth-os/state
```

- [ ] **Step 4: Verify ownership**

Run:

```bash
stat -c '%U:%G %a %n' /opt/stacks /opt/growth-os /opt/growth-os/backups
```

Expected owner/group `amirreza:amirreza` and mode `750`.

- [ ] **Step 5: Document the preflight and commit**

Update `AGENT.md` with actual outputs and create FA/EN runtime-readme files explaining ports and runtime paths.

Commit:

```bash
git add AGENT.md growth-os/runtime/core/README-FA.md growth-os/runtime/core/README-EN.md
git commit -m "docs: record Phase 2 host preflight"
```

---

### Task 2: Activepieces Community Edition stack

**Files:**
- Create: `growth-os/runtime/core/activepieces.compose.yaml`
- Create live host file: `/opt/stacks/activepieces/compose.yaml`
- Create live secret file: `/opt/stacks/activepieces/.env` (never commit)
- Modify: `AGENT.md`

**Interfaces:**
- Consumes: `/opt/stacks/activepieces`, Docker Compose, ports verified free.
- Produces: Activepieces app on `127.0.0.1:8080`, one worker at concurrency 1, PostgreSQL, Redis.

- [ ] **Step 1: Write the sanitized Compose template**

Create `growth-os/runtime/core/activepieces.compose.yaml` with exactly:

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

- [ ] **Step 2: Copy the Compose template to the live stack directory**

Run:

```bash
cp growth-os/runtime/core/activepieces.compose.yaml /opt/stacks/activepieces/compose.yaml
mkdir -p /opt/stacks/activepieces/cache
```

- [ ] **Step 3: Generate host-only secrets**

Run:

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

- [ ] **Step 4: Verify secrets are non-empty without printing their values**

Run:

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

- [ ] **Step 5: Validate Compose before starting**

Run:

```bash
cd /opt/stacks/activepieces
docker compose config >/dev/null && echo COMPOSE_OK
```

Expected: `COMPOSE_OK`.

- [ ] **Step 6: Start Activepieces**

Run:

```bash
docker compose -p activepieces up -d
```

- [ ] **Step 7: Verify app, database, Redis and worker**

Run:

```bash
docker compose -p activepieces ps
curl -fsS http://localhost:8080/api/v1/health

docker exec growthos-postgres pg_isready -U postgres -d activepieces
docker exec growthos-redis redis-cli ping

docker inspect -f '{{.State.Status}}' growthos-activepieces-worker
```

Expected: all four containers running; health endpoint succeeds; PostgreSQL accepts connections; Redis returns `PONG`; worker status is `running`.

- [ ] **Step 8: Pin evidence in the ledger and commit the sanitized template only**

Commit:

```bash
git add growth-os/runtime/core/activepieces.compose.yaml AGENT.md
git commit -m "feat: add Activepieces core stack template"
```

Do not add `/opt/stacks/activepieces/.env` to Git.

---

### Task 3: Uptime Kuma monitoring stack

**Files:**
- Create: `growth-os/runtime/core/uptime-kuma.compose.yaml`
- Create live host file: `/opt/stacks/uptime-kuma/compose.yaml`
- Modify: `AGENT.md`

**Interfaces:**
- Consumes: Docker Compose and free port 3001.
- Produces: Uptime Kuma on `127.0.0.1:3001` with persistent storage.

- [ ] **Step 1: Write the Compose template**

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

- [ ] **Step 2: Copy and validate**

Run:

```bash
cp growth-os/runtime/core/uptime-kuma.compose.yaml /opt/stacks/uptime-kuma/compose.yaml
cd /opt/stacks/uptime-kuma
docker compose config >/dev/null && echo COMPOSE_OK
```

- [ ] **Step 3: Start and test**

Run:

```bash
docker compose -p uptime-kuma up -d
curl -fsSI http://localhost:3001/ | head -n 1
```

Expected HTTP response line beginning with `HTTP/1.1 200` or an equivalent successful 2xx response.

- [ ] **Step 4: Commit**

```bash
git add growth-os/runtime/core/uptime-kuma.compose.yaml AGENT.md
git commit -m "feat: add Uptime Kuma monitoring stack"
```

---

### Task 4: Dockge local Compose management UI

**Files:**
- Create: `growth-os/runtime/core/dockge.compose.yaml`
- Create live host file: `/opt/stacks/dockge/compose.yaml`
- Modify: `AGENT.md`

**Interfaces:**
- Consumes: `/opt/stacks`, Docker socket, port 5001.
- Produces: Dockge UI on `127.0.0.1:5001` able to discover stacks in `/opt/stacks`.

- [ ] **Step 1: Write Compose template**

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

- [ ] **Step 2: Verify current UID/GID before start**

Run:

```bash
id -u amirreza
id -g amirreza
```

Expected both values `1000`. If either differs, edit the live Compose to the actual numeric values before startup and record the difference in `AGENT.md`.

- [ ] **Step 3: Start and verify**

Run:

```bash
cp growth-os/runtime/core/dockge.compose.yaml /opt/stacks/dockge/compose.yaml
mkdir -p /opt/stacks/dockge/data
cd /opt/stacks/dockge
docker compose config >/dev/null && echo COMPOSE_OK
docker compose -p dockge up -d
curl -fsSI http://localhost:5001/ | head -n 1
```

Expected successful 2xx/3xx HTTP response.

- [ ] **Step 4: Record Docker-socket security note and commit**

`AGENT.md` must state that Dockge is root-equivalent through `/var/run/docker.sock` and remains localhost-only during the pilot.

Commit:

```bash
git add growth-os/runtime/core/dockge.compose.yaml AGENT.md
git commit -m "feat: add local Dockge stack manager"
```

---

### Task 5: Phase 2 smoke-test script

**Files:**
- Create: `growth-os/runtime/core/phase2-smoke.sh`
- Modify: `AGENT.md`

**Interfaces:**
- Consumes: all Phase 2 containers.
- Produces: single PASS/FAIL verification used after every restart and before later phases.

- [ ] **Step 1: Create the smoke test**

Create `growth-os/runtime/core/phase2-smoke.sh`:

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

echo PHASE2_SMOKE_OK
```

- [ ] **Step 2: Make executable and run**

```bash
chmod +x growth-os/runtime/core/phase2-smoke.sh
./growth-os/runtime/core/phase2-smoke.sh
```

Expected final line: `PHASE2_SMOKE_OK`.

- [ ] **Step 3: Add port-collision regression check**

Run:

```bash
for p in 8080 3001 5001; do ss -ltn "sport = :$p" | grep -q LISTEN || exit 1; done
echo EXPECTED_PORTS_LISTENING
```

Expected: `EXPECTED_PORTS_LISTENING`.

- [ ] **Step 4: Commit**

```bash
git add growth-os/runtime/core/phase2-smoke.sh AGENT.md
git commit -m "test: add Phase 2 smoke verification"
```

---

### Task 6: Backup and restore-validation scripts

**Files:**
- Create: `growth-os/runtime/core/phase2-backup.sh`
- Create: `growth-os/runtime/core/phase2-restore-check.sh`
- Modify: `AGENT.md`

**Interfaces:**
- Consumes: Activepieces PostgreSQL and live `.env`.
- Produces: timestamped PostgreSQL dump, encrypted-secret configuration copy, SHA256 manifest, and a non-destructive restore-readability test.

- [ ] **Step 1: Create database/config backup script**

Create `growth-os/runtime/core/phase2-backup.sh`:

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

- [ ] **Step 2: Create non-destructive restore-readability check**

Create `growth-os/runtime/core/phase2-restore-check.sh`:

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

- [ ] **Step 3: Install client utility and run backup**

```bash
sudo apt install -y postgresql-client
chmod +x growth-os/runtime/core/phase2-backup.sh growth-os/runtime/core/phase2-restore-check.sh
BACKUP_DIR="$(./growth-os/runtime/core/phase2-backup.sh)"
./growth-os/runtime/core/phase2-restore-check.sh "$BACKUP_DIR"
```

Expected: checksum verification succeeds and final line `RESTORE_INPUTS_READABLE`.

- [ ] **Step 4: Commit scripts, never the backup data**

```bash
git add growth-os/runtime/core/phase2-backup.sh growth-os/runtime/core/phase2-restore-check.sh AGENT.md
git commit -m "feat: add Phase 2 backup verification"
```

---

### Task 7: Windows autostart and plugged-in no-sleep policy

**Files:**
- Create: `growth-os/runtime/core/windows-autostart.ps1`
- Modify: `AGENT.md`

**Interfaces:**
- Consumes: Windows 11 host, Ubuntu-24.04 distro, systemd-enabled Docker.
- Produces: WSL launch at user logon and no automatic sleep while AC-powered.

- [ ] **Step 1: Create PowerShell setup script**

Create `growth-os/runtime/core/windows-autostart.ps1`:

```powershell
$ErrorActionPreference = 'Stop'

powercfg /change standby-timeout-ac 0

$Action = New-ScheduledTaskAction -Execute 'wsl.exe' -Argument '-d Ubuntu-24.04 --exec /bin/true'
$Trigger = New-ScheduledTaskTrigger -AtLogOn
$Settings = New-ScheduledTaskSettingsSet -StartWhenAvailable
Register-ScheduledTask -TaskName 'GrowthOS-Start-WSL' -Action $Action -Trigger $Trigger -Settings $Settings -Description 'Start Ubuntu WSL for Growth OS services at user logon' -Force

Get-ScheduledTask -TaskName 'GrowthOS-Start-WSL' | Select-Object TaskName, State
```

- [ ] **Step 2: Run from Administrator PowerShell**

Run from Windows, using the Windows-accessible path to the checked-out repository or copy/paste the script content into an elevated PowerShell session.

Expected task exists as `GrowthOS-Start-WSL`.

- [ ] **Step 3: Test scheduled task without reboot**

Run:

```powershell
Start-ScheduledTask -TaskName 'GrowthOS-Start-WSL'
Start-Sleep -Seconds 8
wsl -d Ubuntu-24.04 -- systemctl is-active docker
```

Expected: `active`.

- [ ] **Step 4: Re-run Phase 2 smoke test from WSL**

```powershell
wsl -d Ubuntu-24.04 -- bash -lc 'cd /path/to/repo && ./growth-os/runtime/core/phase2-smoke.sh'
```

During implementation, replace `/path/to/repo` with the actual repository path discovered on the host and record that exact path in `AGENT.md`.

- [ ] **Step 5: Commit**

```bash
git add growth-os/runtime/core/windows-autostart.ps1 AGENT.md
git commit -m "feat: add Growth OS Windows autostart"
```

---

### Task 8: License ledger and bilingual operations runbook

**Files:**
- Create: `growth-os/runtime/core/LICENSE-LEDGER.md`
- Create: `growth-os/operations/PHASE2-RUNBOOK-FA.md`
- Create: `growth-os/operations/PHASE2-RUNBOOK-EN.md`
- Modify: `AGENT.md`

**Interfaces:**
- Consumes: verified Phase 2 service versions and official license sources.
- Produces: commercial-product due-diligence record and operator recovery guide.

- [ ] **Step 1: Record exact Phase 2 components and license boundaries**

`LICENSE-LEDGER.md` must record at minimum:

```text
Activepieces Community Edition — core MIT; enterprise directories separately commercial; deployed CE features only.
Uptime Kuma — verify repository license at implementation time and record commit/tag.
Dockge — verify repository license at implementation time and record commit/tag.
PostgreSQL/pgvector image — record PostgreSQL + pgvector upstream licenses.
Redis image — record the exact Redis 7.0.7 license applicable to the pinned image.
Docker Engine/Compose — record upstream licensing and redistribution note.
```

Each row must include: component, pinned version/image, license, official source, commercial-use note, redistribution/SaaS note, date verified.

- [ ] **Step 2: Write FA/EN runbooks**

Both runbooks must contain exact commands for:

```bash
# Status
cd /opt/stacks/activepieces && docker compose -p activepieces ps
cd /opt/stacks/uptime-kuma && docker compose -p uptime-kuma ps
cd /opt/stacks/dockge && docker compose -p dockge ps

# Logs
docker logs --tail 100 growthos-activepieces-app
docker logs --tail 100 growthos-activepieces-worker
docker logs --tail 100 growthos-postgres
docker logs --tail 100 growthos-redis

# Restart
docker restart growthos-activepieces-app growthos-activepieces-worker

# Smoke test
./growth-os/runtime/core/phase2-smoke.sh

# Backup
./growth-os/runtime/core/phase2-backup.sh
```

The runbook must also explain how to reach `http://localhost:8080`, `http://localhost:3001`, and `http://localhost:5001` from Windows.

- [ ] **Step 3: Commit**

```bash
git add growth-os/runtime/core/LICENSE-LEDGER.md growth-os/operations/PHASE2-RUNBOOK-FA.md growth-os/operations/PHASE2-RUNBOOK-EN.md AGENT.md
git commit -m "docs: add Phase 2 license and operations runbooks"
```

---

### Task 9: Phase 2 restart resilience and completion gate

**Files:**
- Modify: `AGENT.md`

**Interfaces:**
- Consumes: all Phase 2 services, backup scripts, Windows autostart.
- Produces: verified Phase 2 completion and a safe handoff to Phase 3 Local AI.

- [ ] **Step 1: Take a fresh verified Phase 2 backup**

Run:

```bash
cd <actual-repo-path>
BACKUP_DIR="$(./growth-os/runtime/core/phase2-backup.sh)"
./growth-os/runtime/core/phase2-restore-check.sh "$BACKUP_DIR"
```

Record backup directory, file sizes and SHA256 in `AGENT.md` without committing secret files.

- [ ] **Step 2: Perform full WSL shutdown test**

From Ubuntu:

```bash
exit
```

From Windows PowerShell:

```powershell
wsl --shutdown
wsl -d Ubuntu-24.04 --exec /bin/true
Start-Sleep -Seconds 10
```

- [ ] **Step 3: Run full smoke test after cold WSL start**

From Ubuntu:

```bash
cd <actual-repo-path>
./growth-os/runtime/core/phase2-smoke.sh
```

Expected final line: `PHASE2_SMOKE_OK`.

- [ ] **Step 4: Verify local management endpoints from Windows**

In Windows browser open:

```text
http://localhost:8080
http://localhost:3001
http://localhost:5001
```

Expected: Activepieces, Uptime Kuma, Dockge UIs load.

- [ ] **Step 5: Close Phase 2 in the ledger**

Update `AGENT.md`:

```text
STATUS: PHASE2 COMPLETE + PHASE3 READY
CURRENT_PHASE: Phase 3 — Local AI Layer
CURRENT_TASK: P3-AI-01 — Local model runtime and GPU job scheduler
```

Record all actual image versions, smoke result, backup verification and any deviations from this plan.

- [ ] **Step 6: Commit completion evidence**

```bash
git add AGENT.md
git commit -m "chore: close Phase 2 core platform"
```

---

## Phase 2 Completion Criteria

Phase 2 is complete only when all of the following are true:

```text
[ ] Activepieces app reachable on localhost:8080
[ ] Activepieces worker running with concurrency 1
[ ] PostgreSQL ready
[ ] Redis PONG
[ ] Uptime Kuma reachable on localhost:3001
[ ] Dockge reachable on localhost:5001
[ ] No management UI exposed beyond localhost during pilot
[ ] Smoke test returns PHASE2_SMOKE_OK
[ ] Backup dump + secret config copy pass checksum/readability verification
[ ] WSL cold-start returns Docker and all services without manual startup
[ ] Windows logon task exists
[ ] AC sleep is disabled for 24/7 pilot operation
[ ] License ledger updated
[ ] FA/EN runbooks updated
[ ] AGENT.md records every action and deviation
```

## Source Notes Used for This Plan

- Activepieces official self-host documentation currently recommends Docker Compose with PostgreSQL and Redis, Docker Compose v2, WSL2 on Windows, and health verification at `/api/v1/health`.
- Activepieces official architecture documentation identifies PostgreSQL as durable application state and Redis/BullMQ as the job queue.
- Activepieces official worker guidance recommends `AP_WORKER_CONCURRENCY=1` and `SANDBOX_CODE_ONLY` for production-style isolation.
- Activepieces Community Edition core is MIT-licensed; enterprise directories/features are separately licensed.
- Uptime Kuma official documentation supports Docker Compose and localhost-only port binding.
- Dockge official documentation uses `/opt/stacks`, port 5001, and a Docker socket mount; the socket is therefore treated as privileged and localhost-only in this pilot.
