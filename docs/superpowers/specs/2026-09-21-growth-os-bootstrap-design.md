# Growth OS Bootstrap Design

Date: 2026-09-21
Status: Draft for user review
Repository: `DashSaman/-SEO`
Target branch: `growth-os-bootstrap`

## 1. Product intent

Turn the existing SEO research repository into the foundation for a reusable, revenue-capable **Site-to-Growth Autopilot**. The first two pilots are:

- **MyTel.one** — existing/mature site, used to validate Growth Mode.
- **Tehran Network / tehnet.ir** — incomplete site, used to validate Build Mode / Site Factory.

The system must eventually be able to onboard a new customer/site by asking only the questions that cannot be inferred from the site, repository, Search Console, connected social channels, prior project context, and public brand assets.

## 2. Core principles

1. Do not rebuild mature open-source capabilities unnecessarily.
2. Keep AI providers replaceable; no direct hard dependency on one LLM vendor.
3. Every change must be auditable, testable, reversible, and documented.
4. No production change is complete until live verification passes.
5. Secrets/tokens must never be committed to Git.
6. Build for two pilots now, but avoid decisions that block multi-site / multi-tenant productization later.
7. Keep MyTel and Tehran Network data, prompts, credentials, analytics, and history isolated.
8. Do not treat ranking guarantees as controllable. Optimize for the fastest realistic Top-10 opportunities and record measured outcomes.
9. Avoid spam-policy-sensitive tactics such as doorway pages, cloaking, fake engagement, PBNs, mass low-value content, fabricated reviews, or manipulative link schemes.

## 3. Repository restructuring

The current repository content remains valuable and becomes the versioned SEO knowledge base.

Proposed root structure after bootstrap:

```text
DashSaman/-SEO
├── README.md
├── README.fa.md
├── AGENT.md
├── SEO-REFERENCE-V1/
│   ├── AGENTS.md
│   ├── HANDOFF.md
│   ├── PROGRESS.md
│   ├── RANKING_FRAMEWORK.md
│   ├── README.md
│   ├── SEO_AUDIT_SOP.md
│   ├── SOURCES.md
│   ├── TOP10_PLAYBOOK.md
│   ├── checklists/
│   └── docs/
├── growth-os/
│   ├── architecture/
│   ├── installation/
│   ├── operations/
│   ├── troubleshooting/
│   ├── product/
│   ├── experiments/
│   ├── benchmarks/
│   ├── compliance/
│   └── sites/
└── docs/superpowers/specs/
```

Migration rule: preserve all current content and history. The bootstrap migration is organizational, not deletion.

## 4. `AGENT.md` as the project control file

`AGENT.md` becomes the human-readable single source of truth for execution state.

It must contain:

- project status;
- current phase;
- current task ID;
- completed tasks `[x]`;
- pending tasks `[ ]`;
- blocked tasks `[!]`;
- verification status;
- rollback notes;
- commit/PR references;
- exact next task;
- known incidents and their fixes.

Every task entry should support this minimum record:

```text
ID:
STATUS:
STARTED:
FINISHED:
PURPOSE:
COMMANDS/ACTIONS:
EXPECTED RESULT:
ACTUAL RESULT:
VERIFICATION:
ROLLBACK:
PROBLEMS:
FIX:
COMMIT/PR:
NEXT TASK:
```

Rules:

- Never mark a task complete merely because it was executed.
- Mark `[x]` only after verification.
- Do not repeat a completed task unless verification later fails or the recorded version is intentionally upgraded.
- Record failures as well as successes.
- Never place secrets in `AGENT.md`.

## 5. Runtime environment

Preferred pilot environment:

```text
Windows 11 host
└── WSL2 Ubuntu 24.04
    └── Docker / Docker Compose
```

Reasoning:

- lower overhead than a full VMware VM;
- straightforward NVIDIA GPU access;
- Linux-native container stack;
- easy future migration to VPS/dedicated Linux;
- keeps Windows available as the user workstation.

Expected host hardware:

- Ryzen 7 6800H class CPU;
- 32 GB RAM;
- NVIDIA RTX 3070 Laptop 8 GB VRAM;
- SSD storage.

The design must cap WSL memory so Windows remains usable. Heavy jobs such as local LLM inference, deep crawls, image generation, and code agents should be scheduled rather than all running concurrently.

## 6. High-level system architecture

```text
                         GROWTH OS
                            │
                         n8n
                    orchestration layer
                            │
       ┌────────────────────┼────────────────────┐
       │                    │                    │
 DispatchSEO            OpenGSC              Postiz
 Action Engine      Search Intelligence     Social Publishing
       │                    │                    │
       └───────────────┬────┴───────────────┬────┘
                       │                    │
                    LiteLLM              Data feeds
                  AI Gateway          GSC/GA4/SERP/etc.
                       │
          ┌────────────┼─────────────┐
          │            │             │
       Ollama       Low-cost       Premium
       Local        providers       providers
          │            │             │
          └────────────┴──────┬──────┘
                              │
                         OpenHands
                              │
                         GitHub PR
                              │
                       Quality Gates
                SiteOne / Lighthouse / tests
                              │
                            Deploy
                              │
                 ┌────────────┴────────────┐
                 │                         │
             MyTel.one                 tehnet.ir
```

## 7. Primary open-source components

### Core / control

- WSL2 Ubuntu 24.04
- Docker / Docker Compose
- PostgreSQL
- Redis
- Dockge
- Uptime Kuma
- Restic
- Cloudflare Tunnel where public HTTPS callbacks are required

### AI

- LiteLLM as the production AI gateway
- Ollama for local models
- 9Router only as an optional developer/coding subscription router, not the production control plane
- RouteLLM later if measured routing economics justify it
- OpenHands for repository/code execution

### SEO / intelligence

- DispatchSEO as action/queue/publishing/rank workflow engine
- OpenGSC as search intelligence / AEO visibility layer, excluding unsafe cloaking/doorway features
- Crawl4AI for research and competitor/content extraction
- SiteOne Crawler for deterministic technical QA
- Lighthouse CI for performance/SEO regression gates
- changedetection.io for competitor/page change monitoring
- RSSHub for trend/source feeds where permitted

### Social

- Postiz for supported social publishing/scheduling
- direct Telegram Bot API where simpler/more reliable

### Security / quality

- Trivy in CI
- Gitleaks in CI
- dedicated secret-management approach before production/customer use

### Later, only if justified

- Langfuse
- Umami
- GrowthBook
- ComfyUI
- Remotion
- whisper.cpp

## 8. Two operating modes

### Build Mode / Site Factory

For missing or incomplete websites.

```text
Discover existing assets
→ adaptive interview
→ site.manifest.yaml
→ information architecture
→ design system
→ content plan
→ site implementation
→ QA
→ launch
→ switch to Growth Mode
```

The interview should ask only missing information. It should first attempt to infer facts from connected/private sources and approved public assets.

The canonical site manifest should describe at least:

- brand identity;
- domain/languages;
- business model;
- target users;
- primary offers;
- target geographies;
- goals;
- social channels;
- conversion actions;
- constraints;
- content topics;
- competitors;
- selected technology adapter.

Default technology for a new greenfield site: Next.js/TypeScript, unless the user/site requirements make WordPress or an existing stack more appropriate.

### Growth Mode

For existing sites.

```text
Audit
→ baseline
→ query/opportunity discovery
→ prioritize likely wins
→ implement changes
→ QA
→ deploy
→ distribute socially where useful
→ measure
→ learn
→ repeat
```

## 9. Site isolation model

Proposed durable project data layout:

```text
growth-os/sites/
├── mytel/
│   ├── site.manifest.yaml
│   ├── brand.yaml
│   ├── competitors.yaml
│   ├── channels.yaml
│   ├── experiments/
│   ├── reports/
│   └── history/
└── tehnet/
    ├── site.manifest.yaml
    ├── brand.yaml
    ├── competitors.yaml
    ├── channels.yaml
    ├── experiments/
    ├── reports/
    └── history/
```

Do not store credentials in these files.

## 10. AI routing design

No production agent should call a named premium provider directly.

```text
Agent
→ LiteLLM
→ task/model policy
→ local / low-cost / premium provider
→ retries/fallback
```

Initial workload policy:

- local models: classification, clustering, summaries, metadata, simple content transforms, lightweight QA;
- low-cost APIs: large-volume research and extraction where quality is adequate;
- premium APIs: difficult architecture, complex code, high-value commercial copy, adversarial review, hard reasoning.

Routing policies and actual cost/quality results must be benchmarked and stored so later product pricing can be evidence-based.

## 11. Change safety model

Changes are risk-tiered.

### Low risk — eligible for automatic merge after deterministic checks

Examples:

- metadata formatting;
- broken internal-link repair;
- alt text corrections;
- non-destructive schema fixes;
- typo/format cleanup.

### Medium risk — AI review plus deterministic checks

Examples:

- content rewrites;
- new informational pages;
- FAQ blocks;
- internal-link strategy changes.

### High risk — human approval required initially

Examples:

- URL changes;
- redirect maps;
- deleting pages;
- canonical strategy changes;
- navigation/site architecture changes;
- pricing/legal/commercial claims;
- authentication/payment/critical infrastructure changes.

Maturity may reduce human approval later only after measured reliability supports it.

## 12. Quality gate

A code/content change must move through:

```text
Agent branch
→ tests/build
→ preview if available
→ SiteOne checks
→ Lighthouse CI
→ security/secret scans where relevant
→ AI review
→ merge/deploy
→ live verification
→ measured result logging
```

A deployment that passes CI but fails live verification is not complete.

## 13. Observability and backups

Minimum observability:

- Uptime Kuma for service/site availability;
- Docker health checks;
- n8n execution history;
- application logs;
- AI gateway usage/cost metrics;
- GSC/GA4 ingestion status;
- social publishing failure alerts.

Backup policy must cover configuration, databases, site manifests, operational state, and documentation. Restores must be tested rather than assumed.

## 14. Documentation standard

Every reusable component must have bilingual operator documentation where user operation is involved.

Minimum sections:

- what it is;
- why selected;
- installed version;
- prerequisites;
- installation;
- configuration;
- ports/network exposure;
- secrets used (names only, never values);
- verification;
- normal operation;
- update procedure;
- backup/restore;
- rollback;
- common failures;
- removal procedure;
- upstream repository/license.

All meaningful architecture decisions should get an ADR when alternatives existed and the choice matters long-term.

## 15. Measurement / product-learning model

For each meaningful SEO/Growth experiment record:

- hypothesis;
- target query/page/channel;
- baseline date and metrics;
- change made;
- deployment date;
- cost (tokens/API/local compute/human time if known);
- observed results;
- confidence/limitations;
- keep/revert/iterate decision.

This evidence will later support:

- case studies;
- task routing policies;
- customer pricing;
- gross-margin modeling;
- onboarding defaults;
- product claims that can actually be substantiated.

## 16. Bootstrap phases

### Phase 0 — Repository foundation

- move existing SEO corpus under `SEO-REFERENCE-V1/`;
- create root bilingual README files;
- create `AGENT.md`;
- create `growth-os/` documentation skeleton;
- preserve existing content and relative links where possible;
- verify repository tree and link integrity.

### Phase 1 — Windows/WSL foundation

- WSL2;
- Ubuntu 24.04;
- systemd;
- GPU verification;
- Docker;
- WSL resource limits;
- startup/restart behavior;
- baseline backup.

### Phase 2 — Core platform

- PostgreSQL;
- Redis;
- Dockge;
- Cloudflare Tunnel where required;
- Uptime Kuma;
- Restic.

### Phase 3 — AI layer

- Ollama;
- LiteLLM;
- provider configuration;
- fallback policy;
- budgets/usage tracking;
- local model benchmark;
- optional 9Router developer path.

### Phase 4 — SEO intelligence

- OpenGSC;
- DispatchSEO;
- Crawl4AI;
- SiteOne;
- Lighthouse CI;
- GSC;
- GA4.

### Phase 5 — Agent execution

- OpenHands;
- GitHub integration;
- branch/PR workflow;
- quality gates;
- deploy verification.

### Phase 6 — intelligence feeds

- changedetection.io;
- RSSHub;
- competitor monitoring;
- trend monitoring.

### Phase 7 — social

- Postiz;
- Telegram;
- Instagram;
- YouTube;
- X and other approved channels.

### Phase 8 — pilots

- MyTel Growth Mode;
- Tehran Network Build Mode;
- measure outcomes and operational reliability.

### Phase 9 — productization

- cost accounting;
- multi-site hardening;
- multi-user/multi-tenant design;
- customer onboarding;
- permissions/secrets isolation;
- pricing and billing model;
- customer dashboard;
- support/runbook model.

## 17. Bootstrap success criteria

The repository bootstrap is complete only when:

1. current SEO content is preserved under `SEO-REFERENCE-V1/`;
2. root documentation clearly explains old reference vs new Growth OS;
3. `AGENT.md` exists and contains exact current/next task state;
4. a bilingual documentation framework exists;
5. no secret/token is committed;
6. link/tree validation is performed;
7. migration has rollback/recovery path;
8. a PR against `main` presents the complete bootstrap diff for review.

## 18. Explicit non-goals for bootstrap

The bootstrap does not yet:

- install WSL/Docker;
- connect Google/social accounts;
- publish content;
- modify MyTel/Tehran Network production sites;
- deploy any autonomous agent;
- promise a specific Google ranking outcome.

Those actions begin only after repository bootstrap and its implementation plan are approved.

## 19. Security note

A GitHub personal access token was exposed in chat during planning. It must be revoked/rotated by the account owner. The exposed value must never be copied into this repository, documentation, logs, examples, environment files, or automation configuration.
