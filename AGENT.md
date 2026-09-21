# AGENT.md — Growth OS Execution Ledger

PROJECT: Growth OS
STATUS: PHASE1 COMPLETE + PHASE2 READY
CURRENT_PHASE: Phase 2 — Core Platform
CURRENT_TASK: P2-CORE-01 — Design and deploy the always-on core platform
EXACT_NEXT_TASK: Finalize the Phase 2 service composition (n8n, PostgreSQL, Redis, Uptime Kuma, secrets/backups and service management), then deploy the first persistent 24/7 services without modifying production sites.

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

## Later phases
- [ ] Phase 2 — Core Platform
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
- schedule and publish through official APIs/connectors where available;
- measure website/search/social and business outcomes and feed results back into the next planning cycle;
- use approval tiers so low-risk work can become automated while destructive/high-impact changes stay gated;
- keep a full action/cost/result history for later multi-site commercialization.

Canonical design docs:
- `growth-os/architecture/CONTENT-SOCIAL-AUTOPILOT-FA.md`
- `growth-os/architecture/CONTENT-SOCIAL-AUTOPILOT-EN.md`
- `growth-os/architecture/REVENUE-OPPORTUNITY-ENGINE-FA.md`
- `growth-os/architecture/REVENUE-OPPORTUNITY-ENGINE-EN.md`

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

## Documentation assets
- `README.fa.md` / `README.md` — bilingual repository entry points
- `growth-os/START-HERE-FA.md` / `START-HERE-EN.md` — beginner-first start pages
- `growth-os/assets/roadmap-fa.svg` / `roadmap-en.svg` — visual roadmap
- `growth-os/installation/PHASE1-WSL2-FA.md` / `PHASE1-WSL2-EN.md`
- `growth-os/installation/PHASE1-DOCKER-FA.md` / `PHASE1-DOCKER-EN.md`
- `growth-os/installation/PHASE1-BACKUP-FA.md` / `PHASE1-BACKUP-EN.md`
- `growth-os/installation/assets/docker-install-flow.svg`
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
