# AGENT.md — Growth OS Execution Ledger

PROJECT: Growth OS
STATUS: BOOTSTRAP + PHASE1 IN PROGRESS
CURRENT_PHASE: Phase 1 — Windows / WSL2 Foundation
CURRENT_TASK: P1-WSL-10 — Install Docker Engine + Compose
EXACT_NEXT_TASK: Perform the Docker preflight/conflict check, then install Docker Engine from Docker's official Ubuntu apt repository. Verify each sub-step before continuing.

## State rules
- [x] Never repeat a verified completed task unless verification later fails or an intentional upgrade is approved.
- [x] Never mark a task complete merely because an action ran; verify first.
- [x] Record failures and fixes, not only successes.
- [x] Never store credentials or secret values in this repository.
- [x] Every production-impacting change in later phases requires rollback notes and live verification.
- [x] Keep MyTel and Tehran Network site-specific state isolated.
- [x] Explain every operator step for a beginner and preserve reusable FA/EN runbooks.
- [x] Keep visual diagrams/checklists for major operator phases.

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
- [ ] P1-WSL-10 Install Docker Engine + Compose
- [ ] P1-WSL-11 Verify Docker and reboot/autostart behavior
- [ ] P1-WSL-12 Create Phase 1 backup/baseline record

## Later phases
- [ ] Phase 2 — Core Platform
- [ ] Phase 3 — AI Layer
- [ ] Phase 4 — SEO Intelligence
- [ ] Phase 5 — Agent Execution
- [ ] Phase 6 — Intelligence Feeds
- [ ] Phase 7 — Social
- [ ] Phase 8 — Pilots
- [ ] Phase 9 — Productization

## Phase timing / site-work boundary
- Phases 0–3 prepare the controlled runtime and AI infrastructure; they do not modify production sites.
- Phase 4 begins real data ingestion/auditing for MyTel and Tehran Network.
- Phase 5 enables controlled Agent-driven code/content changes through branch/PR/QA gates.
- Phase 8 validates the full 24/7 pilot loop and measured business/SEO outcomes.

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
RESULT: Pending base packages were unpacked/configured successfully; package triggers completed and shell prompt returned without visible fatal error.

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

APPLY ACTION: Operator saved the file with Ctrl+S, ran `wsl --shutdown`, and relaunched `Ubuntu-24.04`.
VERIFICATION:
- `free -h` reported approximately 19 GiB total memory.
- `nproc` returned `12`.
- `swapon --show` reported `/dev/sdc` with size `8G`.
CONCLUSION: `.wslconfig` is applied successfully.

### P1-WSL-09 — Verify systemd
STATUS: VERIFIED_COMPLETE
DATE: 2026-09-21
EVIDENCE: Operator screenshot captured both verification commands and outputs.
COMMANDS:
- `ps -p 1 -o comm=`
- `systemctl is-system-running`
ACTUAL_RESULT:
- PID 1 command returned `systemd`.
- `systemctl is-system-running` returned `running`.
CONCLUSION: systemd is already active and healthy in Ubuntu 24.04 under WSL2. No `/etc/wsl.conf` modification is required for systemd on this pilot.
NEXT_OPERATOR_ACTION: Begin P1-WSL-10 using Docker's official Ubuntu apt repository. First perform a conflict/pre-existing Docker check; do not install Docker Desktop.

## Documentation assets
- `README.fa.md` — Persian repository entry point with visual roadmap
- `README.md` — English repository entry point with visual roadmap
- `growth-os/START-HERE-FA.md` — Persian beginner-first start page
- `growth-os/START-HERE-EN.md` — English beginner-first start page
- `growth-os/assets/roadmap-fa.svg` — Persian visual full roadmap
- `growth-os/assets/roadmap-en.svg` — English visual full roadmap
- `growth-os/installation/PHASE1-WSL2-FA.md` — beginner-first Persian WSL2 guide
- `growth-os/installation/PHASE1-WSL2-EN.md` — English WSL2 guide
- `growth-os/installation/assets/wsl2-step-02-web-download-success.svg` — visual WSL install/reboot walkthrough
- `growth-os/installation/assets/wsl2-step-03-resource-limits.svg` — visual WSL resource limits and verification
- `growth-os/installation/assets/phase1-progress-fa.svg` — visual Phase 1 progress checklist
- `growth-os/troubleshooting/INC-WSL2-0001-HTTP-500.md` — real HTTP 500 incident and workaround
- `growth-os/installation/PHASE1-DOCKER-FA.md` — Persian beginner-first Docker Engine guide
- `growth-os/installation/PHASE1-DOCKER-EN.md` — English Docker Engine guide
- `growth-os/installation/assets/docker-install-flow.svg` — visual Docker installation/verification flow

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
