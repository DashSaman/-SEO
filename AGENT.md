# AGENT.md — Growth OS Execution Ledger

PROJECT: Growth OS
STATUS: BOOTSTRAP + PHASE1 PREPARATION
CURRENT_PHASE: 0 / Phase 1 preflight in progress
CURRENT_TASK: P1-WSL-04 — Create Linux user/password
EXACT_NEXT_TASK: Finish the Ubuntu first-run account prompt, then capture the resulting shell prompt. Do not share the password.

## State rules
- [x] Never repeat a verified completed task unless verification later fails or an intentional upgrade is approved.
- [x] Never mark a task complete merely because an action ran; verify first.
- [x] Record failures and fixes, not only successes.
- [x] Never store credentials or secret values in this repository.
- [x] Every production-impacting change in later phases requires rollback notes and live verification.
- [x] Keep MyTel and Tehran Network site-specific state isolated.
- [x] Explain every operator step for a beginner and preserve a reusable FA/EN runbook.

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
- [ ] P1-WSL-04 Create Linux user/password
- [ ] P1-WSL-05 Verify Ubuntu runs on WSL VERSION 2
- [ ] P1-WSL-06 Verify RTX 3070 is visible inside Ubuntu
- [ ] P1-WSL-07 Update Ubuntu packages
- [ ] P1-WSL-08 Configure WSL resource limits
- [ ] P1-WSL-09 Verify systemd
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

### P0-01 — Inventory and freeze
STATUS: VERIFIED_COMPLETE
RESULT: Baseline commit `dabb9794095897a86bc1c5ed7a2ed9d3fb0e264f`; 8 root docs + 14 checklist files + 30 legacy docs = 52 SEO files; no target-path collisions.

### P0-02 — Atomic SEO corpus relocation
STATUS: VERIFIED_COMPLETE
RESULT: `SEO-REFERENCE-V1/` tree SHA equals baseline tree SHA `009ab50e4d0da8a506f4762fd12f4d4975a747b5`, proving content identity for all 52 migrated files.

### P0-03 — Bilingual root docs + execution ledger
STATUS: VERIFIED_COMPLETE
RESULT: Root `README.md`, `README.fa.md`, and canonical `AGENT.md` created and verified.

### P0-04 — Growth OS documentation skeleton
STATUS: VERIFIED_COMPLETE
RESULT: Architecture, installation, operations, troubleshooting, product, experiments, benchmarks, compliance, MyTel, and Tehran Network documentation homes created.

### P0-05 — Integrity / navigation / secret hygiene
STATUS: VERIFIED_COMPLETE
RESULT: 52/52 SEO files preserved; required paths present; no committed PAT/API secret values found in reviewed bootstrap content.

### P0-06 — Bootstrap PR
STATUS: REVIEWED_AWAITING_MERGE_APPROVAL
PR: `#1 Bootstrap Growth OS repository structure`
NOTE: Do not merge without explicit owner approval.

## Phase 1 run log

### P1-WSL-01 — Initial preflight
STATUS: VERIFIED_COMPLETE
DATE: 2026-09-21
EVIDENCE: Operator ran `wsl --status`, `wsl --list --verbose`, and Windows `nvidia-smi`.
RESULT:
- WSL was not installed.
- No Linux distribution was installed.
- GPU detected: NVIDIA GeForce RTX 3070 Laptop GPU.
- VRAM: 8192 MiB.
- Windows NVIDIA driver reported: 616.92.
- CUDA UMD reported by Windows: 13.4.
DECISION: Use WSL2 + Ubuntu 24.04 LTS; do not use VMware/Ubuntu Desktop for the pilot runtime.

### P1-WSL-02A — Normal WSL install attempt
STATUS: FAILED_RECORDED
COMMAND: `wsl --install -d Ubuntu-24.04`
RESULT: `Downloading: Windows Subsystem for Linux 2.7.14` followed by `Internal server error (500)`.
ACTION: No destructive cleanup attempted.
INCIDENT: `growth-os/troubleshooting/INC-WSL2-0001-HTTP-500.md`

### P1-WSL-02B — Web-download workaround
STATUS: VERIFIED_COMPLETE
COMMAND: `wsl --install --web-download -d Ubuntu-24.04`
RESULT:
- Windows Subsystem for Linux 2.7.14 installed.
- `VirtualMachinePlatform` enabled to 100%.
- Windows explicitly required reboot before changes became effective.
ACTION: Operator rebooted Windows.

### P1-WSL-02C — Post-reboot verification
STATUS: VERIFIED_COMPLETE
DATE: 2026-09-21
EVIDENCE: Operator ran `wsl --status`, `wsl --list --verbose`, and `wsl --list --online` after reboot.
RESULT:
- `Default Version: 2` — WSL2 is the default.
- WSL reported no installed distributions yet.
- Online distro list worked and included `Ubuntu-24.04` (`Ubuntu 24.04 LTS`).
- WSL1 warning is not a blocker; WSL1 is not required for this project.

### P1-WSL-03 — Ubuntu 24.04 distribution installation
STATUS: VERIFIED_COMPLETE
DATE: 2026-09-21
COMMAND: `wsl --install --web-download -d Ubuntu-24.04`
EVIDENCE: Operator screenshot captured the completed installer output.
RESULT:
- `Downloading: Ubuntu 24.04 LTS`
- `Installing: Ubuntu 24.04 LTS`
- `Distribution successfully installed. It can be launched via 'wsl.exe -d Ubuntu-24.04'`
- Ubuntu launched automatically and began first-run provisioning.
- Prompt reached: `Create a default Unix user account:`
CONCLUSION: Ubuntu 24.04 distribution install is complete; first Linux user creation is now the active task.
NEXT_OPERATOR_ACTION: Finish the username/password prompts. Do not share the password in chat or Git.

## Documentation assets
- `growth-os/installation/PHASE1-WSL2-FA.md` — beginner-first Persian guide
- `growth-os/installation/PHASE1-WSL2-EN.md` — English guide
- `growth-os/installation/assets/wsl2-step-02-web-download-success.svg` — visual install/reboot walkthrough
- `growth-os/troubleshooting/INC-WSL2-0001-HTTP-500.md` — real HTTP 500 incident and workaround

## Execution notes

### EXEC-0001 — Temporary-file cleanup during bootstrap
Two temporary/placeholder files were accidentally created on the isolated `growth-os-bootstrap` branch while preparing Git objects. Both were removed before corpus relocation. No temporary path exists in the verified relocation tree and `main` was not touched.

### Security incident SEC-0001
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
