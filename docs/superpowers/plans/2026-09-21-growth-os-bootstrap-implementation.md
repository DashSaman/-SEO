# Growth OS Bootstrap Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reorganize `DashSaman/-SEO` so the existing SEO corpus becomes a preserved versioned knowledge base while a new bilingual, auditable Growth OS control layer is created around it.

**Architecture:** Phase 0 is documentation/repository bootstrap only. Existing SEO content is moved under `SEO-REFERENCE-V1/` in one bounded migration, while root files become the entry point for Growth OS and `AGENT.md` becomes the execution state ledger. New `growth-os/` documentation areas are created with operator-facing indexes, but no WSL/Docker/service installation begins in this plan.

**Tech Stack:** GitHub Git Data API / Git tree operations, Markdown, YAML examples, repository validation by tree inspection and link/path checks.

**Spec:** `docs/superpowers/specs/2026-09-21-growth-os-bootstrap-design.md`

## Global Constraints

- Existing SEO content must be preserved, not rewritten or deleted during bootstrap.
- No secret/token may be committed, echoed into docs, examples, logs, or config.
- `AGENT.md` is the single human-readable execution-state source of truth.
- A task is marked `[x]` only after verification passes.
- MyTel and Tehran Network state must remain logically isolated.
- Bootstrap must remain reversible to the pre-bootstrap commit `dabb9794095897a86bc1c5ed7a2ed9d3fb0e264f`.
- Phase 0 must not install WSL/Docker, connect accounts, publish content, or modify production sites.
- The exposed GitHub PAT from chat must never be copied into the repository.

## Review Focus

1. **Accidental corpus loss during move** — every original blob path must have a corresponding archived path and identical blob SHA/content.
2. **Broken internal relative links after relocation** — links within the moved SEO corpus should still resolve relative to their new common root; root links must point to the new paths.
3. **Bootstrap metadata accidentally archived** — `docs/superpowers/specs/` and `docs/superpowers/plans/` must remain at the new root documentation layer, not inside `SEO-REFERENCE-V1/`.
4. **Secret leakage** — validation must reject files containing the exposed PAT prefix or other obvious credential patterns.
5. **Agent state drift** — `AGENT.md` must name exactly one current task and one exact next task, with completed tasks tied to verification evidence.

---

## File Structure

### Root files

- `README.md` — English Growth OS entry point, architecture summary, repository navigation, current pilot scope.
- `README.fa.md` — Persian operator-facing equivalent of the root overview.
- `AGENT.md` — canonical execution ledger and checklist.

### Preserved knowledge base

- `SEO-REFERENCE-V1/` — all pre-bootstrap SEO root docs, `checklists/`, and legacy SEO `docs/` content.
- `SEO-REFERENCE-V1/README.md` — the original SEO README, preserved unchanged.

### Growth OS docs

- `growth-os/README.md` — map of the new system docs and phases.
- `growth-os/architecture/README.md` — architecture/ADR index.
- `growth-os/installation/README.md` — installation docs index; Phase 1+ only.
- `growth-os/operations/README.md` — start/stop/update/backup/runbook index.
- `growth-os/troubleshooting/README.md` — incidents and troubleshooting index.
- `growth-os/product/README.md` — productization, onboarding, cost/pricing learning index.
- `growth-os/experiments/README.md` — experiment record standard and pilot folders.
- `growth-os/benchmarks/README.md` — model/cost/performance benchmarks index.
- `growth-os/compliance/README.md` — license/provider/privacy/policy tracking index.
- `growth-os/sites/README.md` — site isolation rules and manifest conventions.
- `growth-os/sites/mytel/README.md` — pilot identity and Growth Mode scope only; no credentials.
- `growth-os/sites/tehnet/README.md` — pilot identity and Build Mode scope only; no credentials.

### Superpowers workflow docs

- `docs/superpowers/specs/2026-09-21-growth-os-bootstrap-design.md` — approved design spec.
- `docs/superpowers/plans/2026-09-21-growth-os-bootstrap-implementation.md` — this plan.

---

### Task 1: Freeze and inventory the pre-bootstrap repository

**Files:**
- Read only: repository tree at commit `dabb9794095897a86bc1c5ed7a2ed9d3fb0e264f`
- Create during execution record: `AGENT.md` only after Task 3

**Interfaces:**
- Consumes: approved design spec and baseline commit SHA.
- Produces: exact list of source paths/blobs to migrate and an exclusion list for new bootstrap files.

- [ ] **Step 1: Fetch the recursive tree for the baseline commit and save the path/blob mapping in execution notes.**

Required source groups:

```text
AGENTS.md
HANDOFF.md
PROGRESS.md
RANKING_FRAMEWORK.md
README.md
SEO_AUDIT_SOP.md
SOURCES.md
TOP10_PLAYBOOK.md
checklists/**
docs/**   (excluding docs/superpowers/** created after baseline)
```

- [ ] **Step 2: Verify the baseline commit equals the intended pre-bootstrap revision.**

Expected:

```text
dabb9794095897a86bc1c5ed7a2ed9d3fb0e264f
```

If the branch base differs, stop and reconcile before moving files.

- [ ] **Step 3: Verify no existing source path already begins with `SEO-REFERENCE-V1/` or `growth-os/`.**

Expected: zero collisions.

- [ ] **Step 4: Record exact counts for source blobs grouped by root docs, `checklists/`, and legacy `docs/`.**

Expected: counts are later matched one-for-one after migration.

- [ ] **Step 5: Commit is not needed for this read-only task; record verification in `AGENT.md` when that file is created in Task 3.**

---

### Task 2: Perform one atomic SEO corpus relocation

**Files:**
- Move: `AGENTS.md` → `SEO-REFERENCE-V1/AGENTS.md`
- Move: `HANDOFF.md` → `SEO-REFERENCE-V1/HANDOFF.md`
- Move: `PROGRESS.md` → `SEO-REFERENCE-V1/PROGRESS.md`
- Move: `RANKING_FRAMEWORK.md` → `SEO-REFERENCE-V1/RANKING_FRAMEWORK.md`
- Move: `README.md` → `SEO-REFERENCE-V1/README.md`
- Move: `SEO_AUDIT_SOP.md` → `SEO-REFERENCE-V1/SEO_AUDIT_SOP.md`
- Move: `SOURCES.md` → `SEO-REFERENCE-V1/SOURCES.md`
- Move: `TOP10_PLAYBOOK.md` → `SEO-REFERENCE-V1/TOP10_PLAYBOOK.md`
- Move: `checklists/**` → `SEO-REFERENCE-V1/checklists/**`
- Move: legacy `docs/**` → `SEO-REFERENCE-V1/docs/**`
- Preserve at root: `docs/superpowers/**`

**Interfaces:**
- Consumes: exact source path/blob mapping from Task 1.
- Produces: archived corpus with identical blob SHAs/content under the new prefix.

- [ ] **Step 1: Build a Git tree that reuses each existing blob SHA at its new `SEO-REFERENCE-V1/...` path.**

Do not re-encode or rewrite file contents during this move.

- [ ] **Step 2: Remove each migrated old path from the new tree while preserving `docs/superpowers/**`.**

Expected root after relocation has no old SEO root docs except the new Growth OS files created later.

- [ ] **Step 3: Create one commit with message:**

```text
chore: archive SEO reference corpus under SEO-REFERENCE-V1
```

- [ ] **Step 4: Verify every migrated file has identical content/blob identity to its baseline source.**

Acceptance condition:

```text
source_count == archived_count
AND
for every source path: source_blob_sha == archived_blob_sha
```

- [ ] **Step 5: Verify `docs/superpowers/specs/2026-09-21-growth-os-bootstrap-design.md` and this plan still exist at root-level `docs/superpowers/...`.**

Expected: both present and readable.

---

### Task 3: Create the root Growth OS entry points and canonical `AGENT.md`

**Files:**
- Create: `README.md`
- Create: `README.fa.md`
- Create: `AGENT.md`

**Interfaces:**
- Consumes: approved spec, completed Task 1-2 verification, archived corpus location.
- Produces: root navigation and canonical execution state used by all later phases.

- [ ] **Step 1: Create `README.md` with the exact top-level sections below.**

```markdown
# Growth OS

Site-to-Growth Autopilot research and implementation repository.

## Pilots
- MyTel.one — Growth Mode
- Tehran Network — Build Mode / Site Factory

## Repository map
- `AGENT.md` — current execution state and exact next task
- `SEO-REFERENCE-V1/` — preserved SEO knowledge base
- `growth-os/` — Growth OS architecture, operations, experiments, productization
- `docs/superpowers/` — approved designs and implementation plans

## Operating rule
No task is complete until verification passes and `AGENT.md` is updated.

## Security
Never commit credentials, OAuth secrets, API keys, PATs, cookies, or session tokens.

## Current stage
Phase 0 — Repository Bootstrap
```

- [ ] **Step 2: Create `README.fa.md` with a faithful Persian operator-facing equivalent and the same repository map/security rules.**

Required Persian opening:

```markdown
# Growth OS — راهنمای فارسی

این ریپو مرجع طراحی، نصب، اجرا، عیب‌یابی و تبدیل سیستم Site-to-Growth Autopilot به محصول قابل فروش است.
```

- [ ] **Step 3: Create `AGENT.md` with the canonical status header.**

Initial verified state after Tasks 1-2:

```markdown
# AGENT.md — Growth OS Execution Ledger

PROJECT: Growth OS
STATUS: BOOTSTRAP
CURRENT_PHASE: 0
CURRENT_TASK: P0-03
EXACT_NEXT_TASK: P0-04

## State rules
- [x] Never repeat a verified completed task unless its verification later fails or an intentional upgrade is approved.
- [x] Never mark a task complete merely because an action ran; verify first.
- [x] Record failures and fixes, not only successes.
- [x] Never store credentials or secret values in this repository.
- [x] Every production-impacting change in later phases requires rollback notes and live verification.

## Phase 0 — Repository Foundation
- [x] P0-01 Inventory and freeze pre-bootstrap corpus
- [x] P0-02 Move existing SEO corpus to `SEO-REFERENCE-V1/`
- [ ] P0-03 Create bilingual root docs and canonical execution ledger
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
```

- [ ] **Step 4: Add a reusable task record template to `AGENT.md`.**

```markdown
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
```

- [ ] **Step 5: Add an incident note that a PAT was exposed in chat and must be rotated, without recording any part of the token value.**

Required wording:

```markdown
### Security incident SEC-0001
A GitHub personal access token was exposed in chat during planning. The token value is intentionally not recorded here. Owner action required: revoke/rotate the exposed PAT before operational setup.
```

- [ ] **Step 6: After verifying all three files render and link to valid repository paths, update `AGENT.md` so `P0-03` is `[x]`, `CURRENT_TASK` becomes `P0-04`, and `EXACT_NEXT_TASK` becomes `P0-05`.**

- [ ] **Step 7: Commit with message:**

```text
docs: add Growth OS root guides and execution ledger
```

---

### Task 4: Create the Growth OS documentation skeleton

**Files:**
- Create: `growth-os/README.md`
- Create: `growth-os/architecture/README.md`
- Create: `growth-os/installation/README.md`
- Create: `growth-os/operations/README.md`
- Create: `growth-os/troubleshooting/README.md`
- Create: `growth-os/product/README.md`
- Create: `growth-os/experiments/README.md`
- Create: `growth-os/benchmarks/README.md`
- Create: `growth-os/compliance/README.md`
- Create: `growth-os/sites/README.md`
- Create: `growth-os/sites/mytel/README.md`
- Create: `growth-os/sites/tehnet/README.md`
- Modify: `AGENT.md`

**Interfaces:**
- Consumes: repository navigation from Task 3.
- Produces: stable locations for all future phase documentation and per-site isolation.

- [ ] **Step 1: Create `growth-os/README.md` as the documentation map.**

It must identify:

```text
architecture/     long-lived architecture and ADRs
installation/     installation guides beginning in Phase 1
operations/       start/stop/update/backup/restore/runbooks
troubleshooting/  incidents, symptoms, causes, fixes
product/          onboarding, cost model, pricing, multi-tenant evolution
experiments/      hypotheses, actions, metrics, results
benchmarks/       LLM/task/cost/performance measurements
compliance/       licenses, provider policies, privacy/security constraints
sites/            non-secret per-site manifests, reports, history and pilot notes
```

- [ ] **Step 2: Create each directory index with the common documentation contract.**

Each index must state that component/operator docs eventually record:

```text
purpose
why selected
version
prerequisites
installation
configuration
ports/network exposure
secret variable names only
verification
normal operation
update procedure
backup/restore
rollback
common failures
removal procedure
upstream repository and license
```

- [ ] **Step 3: Create `growth-os/sites/README.md` with strict tenant/site isolation rules.**

Required rules:

```text
- No credentials in site files.
- MyTel data must not be copied into Tehran Network context unless intentionally shared as generic system learning.
- Tehran Network data must not be copied into MyTel context unless intentionally shared as generic system learning.
- Each site gets its own manifest, brand profile, competitors, channels, experiments, reports and history.
```

- [ ] **Step 4: Create `growth-os/sites/mytel/README.md`.**

Required content:

```text
Pilot: MyTel.one
Mode: Growth
Purpose: validate optimization of an existing/mature site.
Initial scope: baseline audit, opportunity discovery, technical/content improvements, social distribution where useful, measured outcome tracking.
Credentials: never stored here.
```

- [ ] **Step 5: Create `growth-os/sites/tehnet/README.md`.**

Required content:

```text
Pilot: Tehran Network / tehnet.ir
Mode: Build / Site Factory, then Growth
Purpose: validate completing an incomplete site through adaptive questioning and inferred brand/business context before continuous growth work.
Initial scope: asset discovery, adaptive interview, manifest, architecture, design/content completion, QA, launch readiness, then Growth Mode.
Credentials: never stored here.
```

- [ ] **Step 6: Verify every directory is represented by a tracked README and no empty Git directories are assumed.**

- [ ] **Step 7: Update `AGENT.md`: mark `P0-04` `[x]`, set `CURRENT_TASK: P0-05`, `EXACT_NEXT_TASK: P0-06`.**

- [ ] **Step 8: Commit with message:**

```text
docs: scaffold Growth OS operating documentation
```

---

### Task 5: Validate corpus integrity, navigation, links, and secret hygiene

**Files:**
- Modify only if validation finds defects: root docs / `AGENT.md`
- No production/runtime files exist yet.

**Interfaces:**
- Consumes: final Phase 0 tree from Tasks 2-4.
- Produces: verification evidence required before PR.

- [ ] **Step 1: Compare baseline corpus count with archived corpus count.**

Expected:

```text
number of baseline SEO files == number of files under SEO-REFERENCE-V1/
```

Exclude only bootstrap files created after the baseline commit.

- [ ] **Step 2: Compare each archived file content/blob against its baseline source.**

Expected: 100% identity.

- [ ] **Step 3: Verify required root paths exist.**

Required:

```text
README.md
README.fa.md
AGENT.md
SEO-REFERENCE-V1/README.md
growth-os/README.md
docs/superpowers/specs/2026-09-21-growth-os-bootstrap-design.md
docs/superpowers/plans/2026-09-21-growth-os-bootstrap-implementation.md
```

- [ ] **Step 4: Check Markdown links in root Growth OS docs and moved corpus for broken relative-path references caused by relocation.**

Fix only links whose target moved outside their relative subtree; do not rewrite historical content otherwise.

- [ ] **Step 5: Scan repository text for the exposed PAT value and obvious secret assignments.**

Expected:

```text
0 matches for exposed token
0 committed .env secret values
0 obvious API_KEY=<real-value> / TOKEN=<real-value> patterns introduced by bootstrap
```

Do not print matched secret values to logs; report file/path only if a finding occurs.

- [ ] **Step 6: Verify `AGENT.md` state consistency.**

Expected exactly:

```text
CURRENT_PHASE: 0
CURRENT_TASK: P0-05
EXACT_NEXT_TASK: P0-06
```

Before marking validation done.

- [ ] **Step 7: Record validation evidence in `AGENT.md`, mark `P0-05` `[x]`, set `CURRENT_TASK: P0-06`, and `EXACT_NEXT_TASK: Phase 1 planning after bootstrap PR merge`.**

- [ ] **Step 8: Commit with message:**

```text
chore: validate Growth OS bootstrap integrity
```

---

### Task 6: Open and review the bootstrap pull request

**Files:**
- No new implementation files required unless review finds defects.
- Modify: `AGENT.md` only after PR/merge state is known.

**Interfaces:**
- Consumes: verified Phase 0 branch.
- Produces: reviewable bootstrap PR and completion state.

- [ ] **Step 1: Compare `main...growth-os-bootstrap` and verify the diff contains only repository organization/documentation changes.**

Reject the branch if it contains runtime installation, credentials, production-site changes, or unrelated edits.

- [ ] **Step 2: Open a PR with title:**

```text
Bootstrap Growth OS repository structure
```

PR body must summarize:

```text
- archives the existing SEO corpus under SEO-REFERENCE-V1/
- adds bilingual root documentation
- adds AGENT.md as execution ledger
- scaffolds Growth OS documentation and site isolation
- preserves the approved spec/plan at docs/superpowers/
- contains no service installation or production-site change
- contains no secrets
```

- [ ] **Step 3: Review changed filenames and the PR patch.**

Acceptance criteria:

```text
no corpus loss
no secret values
no unexpected runtime/code changes
AGENT.md state is internally consistent
root navigation resolves
```

- [ ] **Step 4: If review finds defects, fix them on the branch, rerun Task 5 validation, and update the PR.**

- [ ] **Step 5: After approval/merge, update `AGENT.md` on the next authorized branch so Phase 0 shows complete and the exact next work item is `Phase 1 — Windows/WSL2 Foundation planning`.**

Do not begin Phase 1 installation from this plan.

---

## Self-Review Results

### Spec coverage

- Repository archive/migration: Task 2.
- Root bilingual docs: Task 3.
- `AGENT.md` state ledger: Task 3 and every later task.
- Growth OS docs skeleton: Task 4.
- Site isolation: Task 4.
- Preserve superpowers spec/plan: Tasks 2 and 5.
- Secret safety: Tasks 3 and 5.
- Rollback/recovery anchor: global constraint + baseline commit.
- Verification before completion: Tasks 2, 3, 4, 5, 6.
- PR against `main`: Task 6.
- Bootstrap-only boundary: global constraints and Task 6 diff review.

No bootstrap-spec requirement is intentionally deferred except runtime installation and operational phases explicitly marked non-goals by the approved spec.

### Placeholder scan

No `TBD`, `TODO`, `implement later`, unspecified tests, or undefined implementation interfaces remain in this plan.

### Type/interface consistency

The plan has no runtime application types. Repository interfaces are stable paths, task IDs, branch names and commit SHA anchors and are used consistently.

### Review Focus coverage

- Corpus loss → Tasks 1, 2, 5.
- Broken links → Task 5.
- Superpowers files accidentally archived → Tasks 2, 5.
- Secret leakage → Tasks 3, 5, 6.
- Agent state drift → Tasks 3, 4, 5, 6.
