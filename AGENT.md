# AGENT.md — Growth OS Execution Ledger

PROJECT: Growth OS
STATUS: BOOTSTRAP
CURRENT_PHASE: 0
CURRENT_TASK: P0-04
EXACT_NEXT_TASK: P0-05

## State rules
- [x] Never repeat a verified completed task unless its verification later fails or an intentional upgrade is approved.
- [x] Never mark a task complete merely because an action ran; verify first.
- [x] Record failures and fixes, not only successes.
- [x] Never store credentials or secret values in this repository.
- [x] Every production-impacting change in later phases requires rollback notes and live verification.
- [x] Keep MyTel and Tehran Network site-specific state isolated.

## Phase 0 — Repository Foundation
- [x] P0-01 Inventory and freeze pre-bootstrap corpus
- [x] P0-02 Move existing SEO corpus to `SEO-REFERENCE-V1/`
- [x] P0-03 Create bilingual root docs and canonical execution ledger
- [ ] P0-04 Create Growth OS documentation skeleton
- [ ] P0-05 Validate tree, links, and secret hygiene
- [ ] P0-06 Open bootstrap PR and complete review

## Later phases
- [ ] Phase 1 — Windows / WSL2 Foundation
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

## Verified task records

### P0-01 — Inventory and freeze pre-bootstrap corpus
ID: P0-01
STATUS: VERIFIED_COMPLETE
PURPOSE: Freeze the exact pre-bootstrap SEO corpus so migration can be proven lossless.
ACTIONS: Read baseline commit and recursive trees; grouped files by root docs, checklists, and legacy docs.
EXPECTED_RESULT: Baseline commit matches approved SHA; zero path collisions; exact file counts recorded.
ACTUAL_RESULT: Baseline commit `dabb9794095897a86bc1c5ed7a2ed9d3fb0e264f`; 8 root docs + 14 checklist files + 30 legacy docs = 52 SEO files; zero `SEO-REFERENCE-V1/` or `growth-os/` collisions.
VERIFICATION: Baseline root/checklists/docs trees inspected directly through GitHub tree objects.
ROLLBACK: Read-only task; no repository change required.
PROBLEMS: None in baseline corpus.
FIX: Not applicable.
COMMIT_OR_PR: No commit required by plan.
NEXT_TASK: P0-02

### P0-02 — Atomic SEO corpus relocation
ID: P0-02
STATUS: VERIFIED_COMPLETE
PURPOSE: Preserve the entire existing SEO operating system under a versioned reference folder without rewriting content.
ACTIONS: Reused original blob/tree SHAs to create `SEO-REFERENCE-V1/`; removed old root SEO paths from the bootstrap tree; kept `docs/superpowers/` at root.
EXPECTED_RESULT: 52 migrated files with 100% blob/content identity; approved spec and implementation plan remain at root-level `docs/superpowers/`.
ACTUAL_RESULT: `SEO-REFERENCE-V1/` tree SHA equals the original baseline tree SHA `009ab50e4d0da8a506f4762fd12f4d4975a747b5`, proving complete content identity. Spec and plan are present and readable after migration.
VERIFICATION: Fetched `SEO-REFERENCE-V1/README.md`, approved design spec, and implementation plan from `growth-os-bootstrap`; archive tree identity matches baseline.
ROLLBACK: Reset/recreate branch from pre-bootstrap commit `dabb9794095897a86bc1c5ed7a2ed9d3fb0e264f`.
PROBLEMS: Before relocation, verification found the approved design spec had dropped out of the working tree while the plan remained.
FIX: Reconstructed `docs/superpowers/` with both approved `specs/` and `plans/` trees before performing relocation.
COMMIT_OR_PR: `1474b95d0fea5a0c35a9eb20c2798ded7a4ef0fc` — `chore: archive SEO reference corpus under SEO-REFERENCE-V1`
NEXT_TASK: P0-03

### P0-03 — Bilingual root docs and execution ledger
ID: P0-03
STATUS: VERIFIED_COMPLETE
PURPOSE: Create human-readable English/Persian entry points and make execution state durable outside chat context.
ACTIONS: Created root `README.md`, `README.fa.md`, and canonical `AGENT.md`; documented phase boundaries, security rules, pilot roles, and exact execution state.
EXPECTED_RESULT: English/Persian root guides are readable; repository paths are correctly named; `AGENT.md` contains one current task and one exact next task; no secret value is recorded.
ACTUAL_RESULT: Root English/Persian guides and execution ledger prepared with repository navigation, 10-phase roadmap, MyTel/TehNet timing boundary, reusable task template, and incident records.
VERIFICATION: Blob contents reviewed against the approved plan; referenced existing paths are correct and future `growth-os/` path is represented as code text until P0-04 creates it. No credential value is present.
ROLLBACK: Remove the three root files or reset the bootstrap branch to commit `1474b95d0fea5a0c35a9eb20c2798ded7a4ef0fc`.
PROBLEMS: None in final P0-03 artifacts.
FIX: Not applicable.
COMMIT_OR_PR: Recorded by the P0-03 commit `docs: add Growth OS root guides and execution ledger`.
NEXT_TASK: P0-04

## Execution notes

### EXEC-0001 — Temporary-file cleanup during bootstrap
Two temporary/placeholder files were accidentally created on the isolated `growth-os-bootstrap` branch while preparing Git objects. Both were removed immediately before the corpus relocation. No temporary path exists in the verified relocation tree and no production/main branch was touched.

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
