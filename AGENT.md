# AGENT.md — Growth OS Execution Ledger

PROJECT: Growth OS
STATUS: BOOTSTRAP
CURRENT_PHASE: 0
CURRENT_TASK: P0-06
EXACT_NEXT_TASK: Phase 1 planning after bootstrap PR merge

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
- [x] P0-04 Create Growth OS documentation skeleton
- [x] P0-05 Validate tree, links, and secret hygiene
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
ACTUAL_RESULT: Root English/Persian guides and execution ledger created with repository navigation, 10-phase roadmap, MyTel/TehNet timing boundary, reusable task template, and incident records.
VERIFICATION: All three files were fetched from `growth-os-bootstrap` after commit and reviewed against the approved plan.
ROLLBACK: Reset the bootstrap branch to commit `1474b95d0fea5a0c35a9eb20c2798ded7a4ef0fc`.
PROBLEMS: None in final P0-03 artifacts.
FIX: Not applicable.
COMMIT_OR_PR: `dff71b8b2ffd6c6a0addf8154e165b30208308f1` — `docs: add Growth OS root guides and execution ledger`
NEXT_TASK: P0-04

### P0-04 — Growth OS documentation skeleton
ID: P0-04
STATUS: VERIFIED_COMPLETE
PURPOSE: Give every future architecture, installation, operation, incident, experiment, benchmark, compliance record and site-specific artifact a stable documented home.
ACTIONS: Created `growth-os/` map plus architecture, installation, operations, troubleshooting, product, experiments, benchmarks, compliance and sites indexes; created isolated MyTel and Tehran Network pilot indexes.
EXPECTED_RESULT: Every planned directory is represented by a tracked README; operator documentation contract is recorded; per-site isolation rules are explicit; no empty Git directory is assumed.
ACTUAL_RESULT: 12 tracked README documents created, including dedicated MyTel Growth Mode and Tehran Network Build/Site Factory pilot records. Operator docs require purpose, selection reason, version, prerequisites, installation, configuration, ports, secret variable names only, verification, operation, updates, backup/restore, rollback, failures, removal, upstream repo and license.
VERIFICATION: Recursive Growth OS tree inspection confirmed all required tracked READMEs and both site pilot subdirectories.
ROLLBACK: Reset bootstrap branch to P0-03 commit `dff71b8b2ffd6c6a0addf8154e165b30208308f1`.
PROBLEMS: None.
FIX: Not applicable.
COMMIT_OR_PR: `9c8eef97cb5fa8ecb28d0432118d31da3e18a6f3` — `docs: scaffold Growth OS operating documentation`
NEXT_TASK: P0-05

### P0-05 — Integrity, navigation and secret-hygiene validation
ID: P0-05
STATUS: VERIFIED_COMPLETE
PURPOSE: Prove the bootstrap did not lose SEO knowledge, break relocation-relative navigation, or introduce credential leakage before review.
ACTIONS: Compared baseline/archive trees and counts; inspected final recursive tree; checked required root paths; checked relocation semantics for relative links; searched the repository baseline/default branch for common secret patterns and directly reviewed all branch-only bootstrap content.
EXPECTED_RESULT: 52 baseline SEO files equal 52 archived files with identical content; required Growth OS paths exist; zero relocation-caused broken relative links; no exposed PAT or obvious committed secret assignment; AGENT state is internally consistent.
ACTUAL_RESULT: Archive tree SHA is exactly the baseline tree SHA, proving 52/52 identity. Required root paths, approved spec/plan, Growth OS skeleton and per-site docs exist. Because the complete original corpus moved under one common prefix without content changes, internal relative link topology is unchanged. Root Growth OS docs use repository paths as code text. Searches for `github_pat_`, `API_KEY=`, and `TOKEN=` returned zero results on the pre-bootstrap/default corpus; all branch-only bootstrap blobs were directly reviewed and contain no credential value.
VERIFICATION: Final recursive tree inspection + archive tree identity + direct root/spec/plan/AGENT reads + secret-pattern searches. Pre-existing historical/future references inside the preserved SEO corpus were not rewritten because they were not caused by this relocation.
ROLLBACK: Reset/recreate the bootstrap branch from baseline commit `dabb9794095897a86bc1c5ed7a2ed9d3fb0e264f` or from the last known-good task commit.
PROBLEMS: No validation defect remained after the earlier spec-tree repair.
FIX: Not applicable.
COMMIT_OR_PR: This commit — `chore: validate Growth OS bootstrap integrity`.
NEXT_TASK: P0-06

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
