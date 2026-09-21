# AGENT.md — Growth OS Execution Ledger

PROJECT: Growth OS
STATUS: PHASE2 COMPLETE + PHASE3 READY
CURRENT_PHASE: Phase 3 — Local AI Layer
CURRENT_TASK: P3-AI-00 — Prepare the local-AI implementation plan
EXACT_NEXT_TASK: Create and review the Phase 3 Native implementation plan for local text/model routing, GPU job scheduling and resource-safe AI workers before installing AI services on `Amirreza-Pc`.

## State rules
- [x] Never repeat a verified completed task unless verification later fails or an intentional upgrade is approved.
- [x] Never mark a task complete merely because an action ran; verify first.
- [x] Record failures and fixes, not only successes.
- [x] Never store credentials or secret values in this repository.
- [x] Every production-impacting change in later phases requires rollback notes and live verification.
- [x] Keep MyTel and Tehran Network site-specific state isolated.
- [x] Explain every operator step for a beginner and preserve reusable FA/EN runbooks.
- [x] Keep visual diagrams/checklists for major operator phases.
- [x] Treat content creation, media repurposing, social publishing, analytics feedback and website optimization as one integrated Growth OS loop.
- [x] Treat revenue and competitive opportunity discovery as a first-class product function, not only SEO reporting.
- [x] Owner workflow is review-only for routine content/video/publishing operations; the system should execute normal low-risk work autonomously and report results.
- [x] Every site must maintain its own Repo-side operational reports and its own Telegram reporting channel/destination.

## Phase 0 — Repository Foundation
- [x] P0-01 Inventory and freeze pre-bootstrap corpus
- [x] P0-02 Move existing SEO corpus to `SEO-REFERENCE-V1/`
- [x] P0-03 Create bilingual root docs and canonical execution ledger
- [x] P0-04 Create Growth OS documentation skeleton
- [x] P0-05 Validate tree, links, and secret hygiene
- [~] P0-06 Bootstrap PR opened and reviewed; merge to `main` still requires owner approval

## Phase 1 — Windows / WSL2 Foundation
- [x] P1-WSL-01 Preflight Windows / WSL / GPU
- [x] P1-WSL-02 Install WSL package + VirtualMachinePlatform and reboot
- [x] P1-WSL-03 Install Ubuntu 24.04 distribution
- [x] P1-WSL-04 Create Linux user/password
- [x] P1-WSL-05 Verify Ubuntu runs on WSL VERSION 2
- [x] P1-WSL-06 Verify RTX 3070 is visible inside Ubuntu
- [x] P1-WSL-07 Update Ubuntu packages
- [x] P1-WSL-08 Configure WSL resource limits
- [x] P1-WSL-09 Verify systemd
- [x] P1-WSL-10 Install Docker Engine + Compose
- [x] P1-WSL-11 Verify Docker and WSL restart/autostart behavior
- [x] P1-WSL-12 Create Phase 1 backup/baseline record

## Phase 2 — Core Platform
- [x] P2-CORE-01 Host preflight, local ports, runtime directories and canonical repo clone
- [x] P2-CORE-02 Activepieces + PostgreSQL + Redis
- [x] P2-CORE-03 Uptime Kuma monitoring
- [x] P2-CORE-04 Dockge local Compose management
- [x] P2-CORE-05 Unified smoke test
- [x] P2-CORE-06 Backup + restore-input verification
- [x] P2-CORE-07 Windows/WSL autostart + AC no-sleep validation
- [x] P2-CORE-08 License ledger + bilingual operations runbook
- [x] P2-CORE-09 Cold-start verification and baseline closeout

## Later phases
- [ ] Phase 3 — AI Layer
- [ ] Phase 4 — SEO + Revenue Intelligence
- [ ] Phase 5 — Agent Execution
- [ ] Phase 6 — Intelligence Feeds / Competitors / Trends
- [ ] Phase 7 — Content + Social Automation
- [ ] Phase 8 — Pilots
- [ ] Phase 9 — Productization

## Phase timing / site-work boundary
- Phases 0–3 prepare the controlled runtime and AI infrastructure; they do not modify production sites.
- Phase 4 begins real data ingestion/auditing for MyTel and Tehran Network and starts building the Revenue Opportunity queue.
- Phase 5 enables controlled Agent-driven code/content changes through branch/PR/QA gates.
- Phase 6 expands continuous competitor, trend and market-signal discovery.
- Phase 7 adds integrated content generation, media repurposing, editorial scheduling and multi-channel social publishing with measurement feedback.
- Phase 8 validates the full 24/7 pilot loop and measured business/SEO outcomes.

## Unified Growth OS product requirement
The target system is not only an SEO monitor. The production goal is a single orchestration layer that can:
- continuously ingest GSC, GA4, crawl, ranking, server/log, competitor, trend, lead and social-performance signals;
- detect and prioritize technical, search, content, conversion, product, offer and market opportunities;
- score opportunities by revenue potential, commercial intent, demand, speed, confidence, effort and risk;
- generate or improve website pages, articles, FAQs, schema, internal links and commercial copy;
- repurpose approved content into platform-specific social assets instead of blindly duplicating the same text everywhere;
- automatically generate scripts, storyboards, characters/visuals, local voice, subtitles, short-form video edits and platform-specific renders without routine owner editing;
- schedule and publish through official APIs/connectors where available;
- measure website/search/social and business outcomes and feed results back into the next planning cycle;
- use approval tiers so low-risk work can become automated while destructive/high-impact changes stay gated;
- write per-site action/result reports to both the relevant repository and Telegram reporting channel;
- keep a full action/cost/result history for later multi-site commercialization.

Canonical design docs:
- `growth-os/architecture/CONTENT-SOCIAL-AUTOPILOT-FA.md`
- `growth-os/architecture/CONTENT-SOCIAL-AUTOPILOT-EN.md`
- `growth-os/architecture/REVENUE-OPPORTUNITY-ENGINE-FA.md`
- `growth-os/architecture/REVENUE-OPPORTUNITY-ENGINE-EN.md`
- `docs/superpowers/specs/2026-09-21-growth-os-autonomous-content-video-reporting-design.md`
- `docs/superpowers/plans/2026-09-21-growth-os-phase2-core-platform.md`

## Verified Phase 0 summary
- P0-01 VERIFIED: baseline commit `dabb9794095897a86bc1c5ed7a2ed9d3fb0e264f`; 52 SEO files inventoried.
- P0-02 VERIFIED: `SEO-REFERENCE-V1/` tree SHA equals the original baseline tree SHA, proving 52/52 content identity.
- P0-03 VERIFIED: root `README.md`, `README.fa.md`, and canonical `AGENT.md` created.
- P0-04 VERIFIED: Growth OS documentation skeleton and isolated MyTel/Tehran Network docs created.
- P0-05 VERIFIED: tree/navigation/secret-hygiene checks passed.
- P0-06 REVIEWED_AWAITING_MERGE_APPROVAL: PR #1 is open; do not merge without explicit owner approval.

## Phase 1 run log

### P1-WSL-01 — Initial preflight
STATUS: VERIFIED_COMPLETE
DATE: 2026-09-21
RESULT: WSL not installed initially; Windows detected NVIDIA GeForce RTX 3070 Laptop GPU with 8192 MiB VRAM; Windows NVIDIA driver 616.92; CUDA UMD 13.4.
DECISION: Use WSL2 + Ubuntu 24.04 LTS, not VMware/Ubuntu Desktop.

### P1-WSL-02A — Normal WSL install attempt
STATUS: FAILED_RECORDED
COMMAND: `wsl --install -d Ubuntu-24.04`
RESULT: `Internal server error (500)` while downloading WSL 2.7.14.
INCIDENT: `growth-os/troubleshooting/INC-WSL2-0001-HTTP-500.md`

### P1-WSL-02B — Web-download workaround
STATUS: VERIFIED_COMPLETE
COMMAND: `wsl --install --web-download -d Ubuntu-24.04`
RESULT: WSL 2.7.14 installed; `VirtualMachinePlatform` enabled; Windows rebooted as requested.

### P1-WSL-02C — Post-reboot verification
STATUS: VERIFIED_COMPLETE
RESULT: `Default Version: 2`; WSL2 engine responds; online distro list includes `Ubuntu-24.04`; WSL1 warning is irrelevant to this project.

### P1-WSL-03 — Ubuntu 24.04 distribution installation
STATUS: VERIFIED_COMPLETE
COMMAND: `wsl --install --web-download -d Ubuntu-24.04`
RESULT: Ubuntu 24.04 LTS downloaded, installed, and launched successfully.

### P1-WSL-04 — Linux account creation
STATUS: VERIFIED_COMPLETE
RESULT: Linux username `amirreza` created; password setup succeeded; secret value was not shared or stored.

### P1-WSL-05 — Verify WSL version
STATUS: VERIFIED_COMPLETE
RESULT: `wsl --list --verbose` reports `Ubuntu-24.04` as `Running`, `VERSION 2`.

### P1-WSL-06 — Verify NVIDIA GPU inside Ubuntu
STATUS: VERIFIED_COMPLETE
RESULT: Ubuntu `nvidia-smi` sees NVIDIA GeForce RTX 3070 with 8192 MiB VRAM; GPU compute visibility is working.

### P1-WSL-07A — Refresh Ubuntu package metadata
STATUS: VERIFIED_COMPLETE
COMMAND: `sudo apt update`
RESULT: Ubuntu Noble package indexes downloaded successfully; 35.1 MB fetched; 25 packages reported as upgradable.

### P1-WSL-07B — Upgrade Ubuntu packages
STATUS: VERIFIED_COMPLETE
DATE: 2026-09-21
COMMAND: `sudo apt upgrade -y`
RESULT: 25 packages upgraded; package triggers completed and shell prompt returned without visible fatal error.

### P1-WSL-08 — Configure and verify WSL resource limits
STATUS: VERIFIED_COMPLETE
DATE: 2026-09-21
HOST: Ryzen 7 6800H (8C/16T), 32 GB RAM, RTX 3070 8 GB
CONFIG: Windows `%UserProfile%\.wslconfig`
```ini
[wsl2]
memory=20GB
processors=12
swap=8GB
localhostForwarding=true
```
VERIFICATION:
- `free -h` reported approximately 19 GiB total memory.
- `nproc` returned `12`.
- `swapon --show` reported `/dev/sdc` with size `8G`.
CONCLUSION: `.wslconfig` is applied successfully.

### P1-WSL-09 — Verify systemd
STATUS: VERIFIED_COMPLETE
DATE: 2026-09-21
COMMANDS:
- `ps -p 1 -o comm=`
- `systemctl is-system-running`
ACTUAL_RESULT:
- PID 1 command returned `systemd`.
- `systemctl is-system-running` returned `running`.
CONCLUSION: systemd is active and healthy.

### P1-WSL-10A — Docker clean-install preflight
STATUS: VERIFIED_COMPLETE
COMMANDS:
- `docker --version`
- `dpkg -l | grep -E 'docker|containerd|runc'`
RESULT: No pre-existing Docker Engine/containerd/runc package conflict detected.

### P1-WSL-10B — Docker repository prerequisites
STATUS: VERIFIED_COMPLETE
COMMAND: `sudo apt install -y ca-certificates curl`
RESULT: Both prerequisites already present and current.

### P1-WSL-10C — Docker apt keyring directory
STATUS: VERIFIED_COMPLETE
COMMAND: `sudo install -m 0755 -d /etc/apt/keyrings`
RESULT: `/etc/apt/keyrings` ready.

### P1-WSL-10D — Docker signing key
STATUS: VERIFIED_COMPLETE
COMMANDS:
- `sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc`
- `sudo chmod a+r /etc/apt/keyrings/docker.asc`
- `ls -lh /etc/apt/keyrings/docker.asc`
RESULT: `docker.asc` exists, readable, approximately 3.8 KB.

### P1-WSL-10E — Docker official apt repository
STATUS: VERIFIED_COMPLETE
RESULT: apt successfully fetched `https://download.docker.com/linux/ubuntu noble InRelease`; official repository active and trusted.

### P1-WSL-10F — Docker Engine + Compose package installation
STATUS: VERIFIED_COMPLETE
DATE: 2026-09-21
COMMAND: `sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`
RESULT:
- Docker Engine, Docker CLI, containerd, Buildx and Compose Plugin installed successfully.
- Docker service/socket systemd symlinks created.
- Package triggers completed without visible fatal error.

### P1-WSL-11A — Docker runtime verification
STATUS: VERIFIED_COMPLETE
DATE: 2026-09-21
COMMANDS:
- `docker --version`
- `docker compose version`
- `systemctl is-active docker`
- `sudo docker run --rm hello-world`
ACTUAL_RESULT:
- Docker Engine reported version `29.8.1`.
- Docker Compose reported version `v5.5.1`.
- Docker daemon state returned `active`.
- `hello-world` image was pulled successfully and container output included `Hello from Docker!`.
CONCLUSION: Docker CLI, Compose Plugin, daemon, outbound registry access, image pull and container execution are all verified healthy.

### P1-WSL-11B — Non-root Docker operator setup
STATUS: VERIFIED_COMPLETE
DATE: 2026-09-21
COMMAND: `sudo usermod -aG docker $USER`
RESULT: `amirreza` was added to the `docker` group. Membership was verified after a fresh WSL session.
SECURITY_NOTE: Membership in the `docker` group is effectively privileged/root-equivalent on this host. It is acceptable for this single-owner pilot but must not be handed directly to untrusted users in the future multi-tenant product.

### P1-WSL-11C — WSL restart / Docker autostart / non-root verification
STATUS: VERIFIED_COMPLETE
DATE: 2026-09-21
ACTIONS:
- Exited Ubuntu.
- Ran `wsl --shutdown` from Windows PowerShell.
- Relaunched `Ubuntu-24.04`.
- Ran `groups`.
- Ran `systemctl is-active docker`.
- Ran `docker run --rm hello-world` without `sudo`.
ACTUAL_RESULT:
- `groups` included `docker`.
- Docker daemon returned `active` immediately after WSL relaunch.
- `docker run --rm hello-world` succeeded without `sudo` and printed `Hello from Docker!`.
CONCLUSION: Docker permission setup, systemd autostart behavior, daemon startup and non-root container execution survive a full WSL shutdown/relaunch. P1-WSL-11 is complete.

### P1-WSL-12 — Phase 1 backup/baseline
STATUS: VERIFIED_COMPLETE
DATE: 2026-09-21
PURPOSE: Preserve a known-good rollback point before persistent Growth OS services and databases are introduced.
EXPORT: `C:\GrowthOS-Backups\Ubuntu-24.04-phase1-2026-09-21.tar`
ACTUAL_RESULT:
- `C:\GrowthOS-Backups` directory created successfully.
- WSL shut down before export.
- `wsl --export Ubuntu-24.04 C:\GrowthOS-Backups\Ubuntu-24.04-phase1-2026-09-21.tar` completed successfully.
- Verified exact backup size: `1,944,412,160` bytes (~1.81 GiB / ~1.94 GB decimal).
- Verified SHA256: `823965D6DB48A74111105B8433CD98CF77DA042DA909E96CDFEE3770D8BD77CC`.
- Backup archive itself is intentionally not committed to GitHub.
CONCLUSION: Phase 1 has a verified rollback baseline and is complete.

## Phase 2 run log

### P2-CORE-01 — Host preflight + canonical runtime paths
STATUS: VERIFIED_COMPLETE
DATE: 2026-09-21
DEVICE: `Amirreza-Pc` via authenticated Remote Desktop Commander connection.
VERIFICATION:
- Linux user: `amirreza`, UID/GID 1000; `docker` group present.
- WSL memory: ~19 GiB total, 8 GiB swap.
- CPU allocation: 12.
- Docker Engine: 29.8.1.
- Docker Compose: v5.5.1.
- Docker daemon: `active`.
- Ports 8080, 3001 and 5001 had no LISTEN socket before deployment.
ACTIONS:
- Created `/opt/growth-os/{backups,logs,state}` and `/opt/stacks/{activepieces,uptime-kuma,dockge}`.
- Ownership verified as `amirreza:amirreza`, mode 750 on main runtime directories.
- Cloned public branch `growth-os-bootstrap` to `/opt/growth-os/repo`.
- Verified current branch `growth-os-bootstrap`.
RESULT: Phase 2 host baseline ready.

### P2-CORE-02A — Activepieces sanitized template + host-only secrets
STATUS: VERIFIED_COMPLETE
DATE: 2026-09-21
ACTIONS:
- Added sanitized `growth-os/runtime/core/activepieces.compose.yaml` to GitHub branch.
- Synced template to `/opt/stacks/activepieces/compose.yaml`.
- Generated encryption key, JWT secret and PostgreSQL password locally on `Amirreza-Pc`; values were not printed or committed.
- `.env` permission verified as `600`.
- Required secrets verified non-empty: `SECRETS_OK`.
- `docker compose config` returned `COMPOSE_OK`.
RESULT: Configuration and secret gate passed.

### P2-CORE-02B — Activepieces + PostgreSQL + Redis runtime
STATUS: VERIFIED_COMPLETE
DATE: 2026-09-21
VERIFICATION:
- Activepieces app HTTP health returned `{"status":"Healthy"}`.
- Activepieces worker is running, connected to API and configured with concurrency 1 / `SANDBOX_CODE_ONLY`.
- PostgreSQL `pg_isready` returned accepting connections.
- Redis returned `PONG`.
- Activepieces app/worker restart count remained 0 during runtime investigation.
PINNED_IMAGES:
- `ghcr.io/activepieces/activepieces:0.86.3` → `sha256:208517c4f0d798a477a0c594bf432dd0f4918433f4b6f5b5f188a6e10e638c6c`
- `pgvector/pgvector:0.8.0-pg14` → `sha256:c55d7e7deac05dde62139e0ded4fcf4f58363656cbc382dbea82fbed995aa767`
- `redis:7.0.7` → `sha256:bb474c35022ca2c5618f4c49ca759bd2c0eea1daf5d934c560bd30092b97b498`
STARTUP_NOTE: Early `ENOTFOUND redis` and worker websocket messages were transient dependency-readiness messages and resolved without container restart.

### P2-CORE-03 — Uptime Kuma
STATUS: VERIFIED_COMPLETE
DATE: 2026-09-21
RESULT:
- `louislam/uptime-kuma:2` pulled and started with persistent volume.
- HTTP check inside WSL returned success.
- Pinned image digest: `sha256:c74379ac4509ce2d2c2633f509e67003ee2e45b6e995c5e43fc101f45a0e1fbe`.

### P2-CORE-04 — Dockge
STATUS: VERIFIED_COMPLETE
DATE: 2026-09-21
RESULT:
- Runtime UID/GID verified as 1000/1000 before startup.
- `louislam/dockge:1` pulled and started.
- HTTP check inside WSL returned success.
- Pinned image digest: `sha256:335c6368b880ecc203236ed89e6e5232e0d6578e8ef5920e4a502390451502bf`.
SECURITY_NOTE: Dockge mounts `/var/run/docker.sock`; treat it as privileged and never expose it directly to the public Internet.

### P2-CORE-05 — Unified smoke test + readiness regression
STATUS: VERIFIED_COMPLETE
DATE: 2026-09-21
INITIAL_FAILURE:
- First unified smoke run hit `curl: (56) Recv failure: Connection reset by peer` on Activepieces health while app/worker restart counts remained zero.
ROOT_CAUSE_EVIDENCE:
- Five immediate health probes showed four resets followed by HTTP 200.
- A subsequent sequence of ten health requests returned Healthy ten times consecutively.
- App logs showed normal boot/piece synchronization and no container crash/restart.
RULING: The smoke test had a readiness race under concurrent image extraction / service startup, not an Activepieces crash.
FIX:
- `phase2-smoke.sh` now retries HTTP readiness for up to 60 seconds for Activepieces, Uptime Kuma and Dockge.
FINAL_RESULT:
- Docker active PASS.
- All six containers running PASS.
- Activepieces health PASS.
- PostgreSQL readiness PASS.
- Redis PONG PASS.
- Uptime Kuma HTTP PASS.
- Dockge HTTP PASS.
- Expected ports PASS.
- Final line: `PHASE2_SMOKE_OK`.

### P2-CORE-06 — Backup + restore-input verification
STATUS: VERIFIED_COMPLETE
DATE: 2026-09-21
FINAL_BASELINE: `/opt/growth-os/backups/phase2-20260921-074410`
RESULT:
- `activepieces.dump`: 88,042,466 bytes.
- PostgreSQL dump SHA256: `20f1c1b83f95fe6b9e42b3568594c8341e411c57f3c1dc4ea6190b42b7070ff1`.
- Host-only secret configuration copy: 543 bytes; checksum verified locally but secret contents and checksum are not recorded here.
- `sha256sum -c` passed for both backup files.
- Containerized `pg_restore -l` accepted the dump.
- Required secret-key names were present without printing values.
- Final restore-input check: `RESTORE_INPUTS_READABLE`.
RULING: Use the PostgreSQL container's `pg_restore` instead of adding a host `postgresql-client` dependency; this avoids an unnecessary host package and sudo prompt while testing the exact deployed PostgreSQL toolchain.

### P2-CORE-07 — Windows autostart + AC no-sleep
STATUS: VERIFIED_COMPLETE
DATE: 2026-09-21
INITIAL_ATTEMPT:
- `Register-ScheduledTask` with Highest privileges failed with `Access is denied` because Remote Desktop Commander is not elevated.
- A second non-elevated Scheduled Task attempt was also denied by host policy.
RULING: Do not request extra Administrator privilege for a task that only needs to launch user WSL. Use the current user's Windows Startup folder instead.
FINAL_IMPLEMENTATION:
- `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\GrowthOS-Start-WSL.cmd` created.
- Launcher runs `wsl.exe -d Ubuntu-24.04 --exec /bin/true` at user logon.
- Launcher execution verified Docker returned `active`.
- `windows-autostart.ps1` was updated to reproduce the non-admin Startup-folder implementation.
- AC sleep verification returned `Current AC Power Setting Index: 0x00000000`.
- Script verification returned `GROWTHOS_STARTUP_OK`.

### P2-CORE-08 — License ledger + bilingual runbook
STATUS: VERIFIED_COMPLETE
DATE: 2026-09-21
RESULT:
- Added `growth-os/runtime/core/LICENSE-LEDGER.md` with exact Phase 2 tags/digests and upstream license sources.
- Added and updated `growth-os/operations/PHASE2-RUNBOOK-FA.md` and `PHASE2-RUNBOOK-EN.md`.
- Added `windows-open-uis.ps1` to resolve the current WSL private address, verify all three local UIs and open them for the Windows operator.
- License/productization notes explicitly require a fresh review for future versions and local AI model/voice/media licenses.

### P2-CORE-09 — WSL networking + cold-start closeout
STATUS: VERIFIED_COMPLETE
DATE: 2026-09-21
NETWORK_FINDING:
- Standalone Docker Engine inside WSL publishes host ports through kernel NAT; WSL localhost forwarding detected a normal wildcard Python listener but did not reliably surface Docker-published ports on Windows `localhost`.
- Direct Windows access to the WSL private address returned HTTP 200 for ports 8080, 3001 and 5001.
- The same service ports were not reachable through the Windows LAN address during verification.
RULING:
- Compose management ports bind to `0.0.0.0` inside the private WSL NAT namespace so the Windows host can reach them through WSL's private address.
- Do not publish these UIs directly to the public Internet; later remote access must use the planned controlled tunnel/private-access layer.
FINAL_COLD_START:
- Ran `wsl --shutdown`.
- Relaunched Ubuntu through the installed Startup launcher.
- Waited for service readiness.
- Full `phase2-smoke.sh` returned `PHASE2_SMOKE_OK`.
- Windows then received HTTP 200 from Activepieces, Uptime Kuma and Dockge through the current WSL private address.
CONCLUSION: Phase 2 runtime, persistence, monitoring, management, backup, autostart and cold-start recovery gates are verified complete.

## Documentation assets
- `README.fa.md` / `README.md` — bilingual repository entry points
- `growth-os/START-HERE-FA.md` / `START-HERE-EN.md` — beginner-first start pages
- `growth-os/assets/roadmap-fa.svg` / `roadmap-en.svg` — visual roadmap
- `growth-os/installation/PHASE1-WSL2-FA.md` / `PHASE1-WSL2-EN.md`
- `growth-os/installation/PHASE1-DOCKER-FA.md` / `PHASE1-DOCKER-EN.md`
- `growth-os/installation/PHASE1-BACKUP-FA.md` / `PHASE1-BACKUP-EN.md`
- `growth-os/installation/assets/docker-install-flow.svg`
- `growth-os/runtime/core/README-FA.md` / `README-EN.md`
- `growth-os/runtime/core/activepieces.compose.yaml`
- `growth-os/runtime/core/uptime-kuma.compose.yaml`
- `growth-os/runtime/core/dockge.compose.yaml`
- `growth-os/runtime/core/phase2-smoke.sh`
- `growth-os/runtime/core/phase2-backup.sh`
- `growth-os/runtime/core/phase2-restore-check.sh`
- `growth-os/runtime/core/windows-autostart.ps1`
- `growth-os/runtime/core/windows-open-uis.ps1`
- `growth-os/runtime/core/LICENSE-LEDGER.md`
- `growth-os/operations/PHASE2-RUNBOOK-FA.md` / `PHASE2-RUNBOOK-EN.md`
- `growth-os/troubleshooting/INC-WSL2-0001-HTTP-500.md`
- `growth-os/architecture/CONTENT-SOCIAL-AUTOPILOT-FA.md` / `CONTENT-SOCIAL-AUTOPILOT-EN.md`
- `growth-os/architecture/REVENUE-OPPORTUNITY-ENGINE-FA.md` / `REVENUE-OPPORTUNITY-ENGINE-EN.md`

## Security incident SEC-0001
A GitHub personal access token was exposed in chat during planning. The token value is intentionally not recorded here. Owner action required: revoke/rotate the exposed PAT before operational setup.

## Task record template
ID:
STATUS:
STARTED:
FINISHED:
PURPOSE:
ACTIONS:
EXPECTED_RESULT:
ACTUAL_RESULT:
VERIFICATION:
ROLLBACK:
PROBLEMS:
FIX:
COMMIT_OR_PR:
NEXT_TASK:
