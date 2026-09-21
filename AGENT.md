# AGENT.md — Growth OS Execution Ledger

PROJECT: Growth OS
STATUS: PHASE3 EXECUTING + PHASE4 LIVE MONITORING STARTED
CURRENT_PHASE: Phase 3 — Local AI + Phase 4 — Site Intelligence (parallel execution)
CURRENT_TASK: P3-AI-03 — Pull/test Qwen3.5 models + P4-INTEL-03 — Technical crawl analysis
EXACT_NEXT_TASK: Finish `qwen3.5:4b` pull and GPU smoke test; verify TehNet site-wide noindex independently; convert first SiteOne crawls into evidence-backed opportunity queues; then pull 9B, deploy LiteLLM, and implement free direct GSC OAuth/API ingestion.

> Detailed Phase 0–2 history remains preserved in Git history and the Phase 1/2 runbooks/plans. This file is the compact canonical live ledger from Phase 3 onward.

## Non-negotiable operating rules
- [x] Never repeat a verified completed task unless verification later fails or an intentional upgrade is approved.
- [x] Never mark a task complete because a command ran; verify the outcome.
- [x] Record failures/root causes/fixes, not only successes.
- [x] Never store credentials, OAuth secrets, tokens or raw `.env` values in Git.
- [x] MyTel and TehNet state, reports, experiments and Telegram destinations stay isolated.
- [x] Monitoring must operate continuously while the worker is online; fast incidents must not wait for the daily report.
- [x] Every site gets one evidence-based report every 24 hours in Repo + Telegram when the Telegram connector is configured.
- [x] Every site gets a 7-day optimization cycle with Before/After, Keep/Adjust/Rollback and next-measurement dates.
- [x] Every daily report includes an Impact / Time-Waste Check: what produced value, what is too early to judge, what had zero/negative impact, compute/API cost, and commercial outcome when data exists.
- [x] Paid generative APIs are disabled by default; AI generation is Local/Free-first.
- [x] No fabricated rankings, traffic, backlinks, GSC metrics, leads, conversions or revenue.
- [x] No Page-1/Top-10 guarantee. Goal: maximize qualified/commercial first-page visibility, leads, conversions and revenue using measured white-hat work.
- [x] No PBN, cloaking, doorway factories, hacked links, fake reviews/mentions or mass low-value content.
- [x] Low-risk work may become autonomous only after pilot verification; destructive/high-impact changes remain fail-closed.
- [x] Production changes later require rollback notes, QA and live verification.
- [x] PR #1 must not be merged to `main` without explicit owner approval.

## Phase status

### Phase 0 — Repository Foundation
- [x] P0-01 Inventory/freeze original SEO corpus
- [x] P0-02 Preserve original corpus under `SEO-REFERENCE-V1/`
- [x] P0-03 Bilingual root docs + execution ledger
- [x] P0-04 Growth OS documentation/site isolation skeleton
- [x] P0-05 Tree/navigation/secret hygiene
- [~] P0-06 PR #1 open/reviewed; merge still requires owner approval

### Phase 1 — Windows / WSL2 / Docker Foundation
- [x] WSL2 + Ubuntu 24.04
- [x] RTX 3070 visible inside WSL
- [x] Resource limits: 20GB RAM / 12 CPU / 8GB swap
- [x] systemd
- [x] Docker Engine 29.8.1 + Compose v5.5.1
- [x] Non-root Docker and restart verification
- [x] Verified Phase 1 WSL export backup

### Phase 2 — Core Platform
- [x] Activepieces CE + worker
- [x] PostgreSQL + Redis
- [x] Uptime Kuma
- [x] Dockge
- [x] Unified smoke test
- [x] Backup + restore-input verification
- [x] Windows/WSL autostart + AC no-sleep
- [x] License ledger + bilingual runbook
- [x] Cold-start verification

Final verified Phase 2 gate ended with `PHASE2_SMOKE_OK`, `RESTORE_INPUTS_READABLE`, `NO_TRACKED_ENV`, `FINAL_WSL_GATE_OK`.
Final Phase 2 baseline backup: `/opt/growth-os/backups/phase2-20260921-074410`.

### Phase 3 — Local AI Layer
- [x] P3-AI-00 Native implementation plan written and upgraded to current Qwen3.5 models
- [x] P3-AI-01 Read-only preflight: Phase 2 healthy; RTX 3070 8GB visible; RAM/disk headroom sufficient; ports 11434/4000 free
- [x] P3-AI-02 Ollama native install + systemd resource policy
- [~] P3-AI-03 Local models: `qwen3.5:4b` pull in progress; `qwen3.5:9b` pending
- [ ] P3-AI-04 LiteLLM local gateway
- [ ] P3-AI-05 GPU-safe serialized queue/lock and health policy
- [ ] P3-AI-06 WSL cold-start verification including AI layer
- [ ] P3-AI-07 Bilingual AI runbook + post-AI baseline backup

#### P3-AI-01/02 verified evidence — 2026-09-21
- Phase 2 re-check returned `PHASE2_SMOKE_OK` / `P3_PREFLIGHT_OK`.
- Preflight at test time: RTX 3070 8192 MiB with ~6945 MiB free, ~16 GiB free WSL RAM, 8 GiB swap free, ~947GB disk free.
- First official Ollama installer attempt stopped because `zstd` was missing. Root cause was explicit installer requirement; no workaround was guessed.
- Installed Ubuntu `zstd`, reran the official installer successfully.
- Ollama version verified: `0.34.2`.
- API verified: `127.0.0.1:11434/api/version` responded.
- systemd service verified `active`.
- Verified service policy: `OLLAMA_HOST=127.0.0.1:11434`, `OLLAMA_MAX_LOADED_MODELS=1`, `OLLAMA_NUM_PARALLEL=1`, `OLLAMA_MAX_QUEUE=32`, `OLLAMA_CONTEXT_LENGTH=8192`, `OLLAMA_KEEP_ALIVE=2m`, `OLLAMA_NO_CLOUD=1`.
- Primary target: `qwen3.5:9b`; fast fallback: `qwen3.5:4b`.

### Phase 4 — SEO + Revenue Intelligence
- [x] P4-INTEL-00 Implementation plan written
- [x] P4-INTEL-01 Per-site manifests + isolated runtime state
- [x] P4-INTEL-02 Public baseline collector built with tests and first live baselines collected
- [~] P4-INTEL-03 SiteOne technical crawler installed/verified and first crawls completed; machine-readable opportunity parsing/recurring orchestration in progress
- [ ] P4-INTEL-04 Free direct Google Search Console + GA4 ingestion
- [ ] P4-INTEL-05 Revenue Opportunity queue/scoring persistence
- [ ] P4-INTEL-06 Automated daily Repo + Telegram report pipeline
- [ ] P4-INTEL-07 Automated 7-day Before/After optimization review
- [ ] P4-INTEL-08 Cold-start/queue recovery verification

#### P4 live public baseline — 2026-09-21
MyTel raw baseline: `/opt/growth-os/state/sites/mytel/baselines/20260921T044021Z.json`
- Root HTTP 200; final URL `https://mytel.one`
- sampled root latency 1448 ms
- title/meta description/canonical detected
- robots.txt 200
- standard `/sitemap.xml` and `/sitemap_index.xml` both returned 200

TehNet raw baseline: `/opt/growth-os/state/sites/tehnet/baselines/20260921T044024Z.json`
- Root HTTP 200; final URL `https://tehnet.ir`
- sampled root latency 928 ms
- title + canonical detected
- homepage meta description not detected
- robots.txt 200
- standard `/sitemap.xml` and `/sitemap_index.xml` returned 404; do NOT infer that no non-standard sitemap exists until robots/CMS/site references are checked

Reports:
- `growth-os/sites/mytel/reports/2026-09-21-public-baseline.md`
- `growth-os/sites/tehnet/reports/2026-09-21-public-baseline.md`

#### P4 SiteOne crawler — 2026-09-21
Upstream reviewed: `janreges/siteone-crawler` v2.5.1, MIT license.
Installed package: `siteone-crawler-static_2.5.1-1_amd64.deb`.
Verified upstream/package SHA256: `294add3b77f4b90c1a68c900cd2c18495f538b8212222b7433ae081e9c271181`.
Installed version verified: `2.5.1.20260627`.
Safety settings for initial crawl: mobile UA, assets disabled, 2 workers, max 3 requests/sec, 10s timeout, max 1000 visited URLs.

MyTel first crawl:
- 35 HTML URLs, all crawl responses status 200
- SiteOne overall score 8.3/10; SEO 10.0 in this crawl configuration
- notices include 4 title-length outliers and 1 meta-description-length outlier
- accessibility warnings include skipped heading levels on 12 pages and no main landmark on 10 pages
- security score 6.5 with missing/hardening security-header findings requiring later independent review
- no crawl 404s in the 35-page set
- raw reports: `/opt/growth-os/state/sites/mytel/crawls/2026-09-21-initial/report.{json,html}`

TehNet first crawl:
- 19 HTML URLs, all crawl responses status 200
- SiteOne overall score 7.9/10; SEO 6.1
- **critical evidence to independently verify before action: SiteOne reports 19/19 crawled pages as `noindex`**
- 2 pages without H1
- empty/non-unique meta descriptions reported across crawl
- SiteOne reports TLS 1.0 and TLS 1.1 support; independently verify before remediation
- no crawl 404s in the 19-page set
- raw reports: `/opt/growth-os/state/sites/tehnet/crawls/2026-09-21-initial/report.{json,html}`

#### Search Console connector decision
- Installed GSC Wizard connector was tested and returned `payment_required` because its trial/subscription is inactive.
- Project rule: do not depend on a paid intermediary for core SEO telemetry.
- Decision: implement direct official Google Search Console API + OAuth on our own runtime; credentials remain host-only.
- Windsor.ai free-plan connector was surfaced only as an optional accelerator; it is not a Growth OS dependency.

### Phase 5 — Controlled Agent Execution
- [ ] Opportunity → branch/PR → QA/test → deploy adapters
- [ ] Low-risk production action policy
- [ ] Post-change live verification + rollback

### Phase 6 — Competitors / Trends / Market Signals
- [ ] changedetection/RSS/public-feed layer
- [ ] competitor diff and trend scoring

### Phase 7 — Content / Social / Video Autopilot
- [ ] Local content generation and refresh
- [ ] per-platform social transformation
- [ ] local image/video/TTS/subtitle/edit pipeline
- [ ] official free/quota publishing adapters where available

### Phase 8 — Pilots
- [ ] MyTel full Growth Mode loop
- [ ] TehNet Build/Site-Factory → Growth Mode loop
- [ ] Daily reports and 7-day optimization cycles validated with measured outcomes

### Phase 9 — Productization
- [ ] Multi-site/multi-tenant isolation
- [ ] always-on control plane + home GPU worker architecture
- [ ] commercial licensing/security/SLA review

## Reporting contract
Canonical cadence: `growth-os/architecture/24X7-OPTIMIZATION-CADENCE-FA.md` / `-EN.md`.
Daily report schema: `growth-os/operations/DAILY-REPORT-SCHEMA-FA.md`.
Agent topology: `growth-os/architecture/AGENT-TOPOLOGY-FA.md`.

Daily reports must answer, with evidence:
1. What changed in the last 24h?
2. What did Growth OS actually do?
3. What passed/failed/retried/queued?
4. What improved/worsened and what is too early to judge?
5. What was the compute/API cost (paid generative API target = 0)?
6. What happened to qualified search/lead/conversion/revenue metrics when those data sources are connected?
7. What will be done next and when will impact be measured again?

## Canonical plans/designs
- `docs/superpowers/specs/2026-09-21-growth-os-autonomous-content-video-reporting-design.md`
- `docs/superpowers/plans/2026-09-21-growth-os-phase2-core-platform.md`
- `docs/superpowers/plans/2026-09-21-growth-os-phase3-local-ai.md`
- `docs/superpowers/plans/2026-09-21-growth-os-phase4-site-intelligence.md`
- `growth-os/architecture/REVENUE-OPPORTUNITY-ENGINE-FA.md` / `-EN.md`
- `growth-os/architecture/CONTENT-SOCIAL-AUTOPILOT-FA.md` / `-EN.md`

## Security incident SEC-0001
A GitHub personal access token was exposed in chat earlier. The token value is intentionally not recorded. Owner action remains revoke/rotate if not already completed.

## Current hard boundary
Phase 4 may collect, crawl, measure, score and prepare actionable work. Production modifications are still blocked until Phase 5 execution/rollback gates are ready. This prevents a newly deployed autonomous system from changing live sites before it has measurement and recovery controls.
