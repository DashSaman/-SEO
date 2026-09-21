# Phase 4 — Site Intelligence + Revenue Opportunity Execution Plan

## Goal
Move Growth OS from infrastructure into real site work on `mytel.one` and `tehnet.ir`: continuous public-site monitoring, technical crawling, search/analytics ingestion when connected, competitor/trend signals, daily per-site reports, and a 7-day measured optimization queue.

## Operating contract
- Monitoring loop runs continuously while the worker is online; fast health/incident checks run more frequently than daily reporting.
- One daily report per site every 24h, written to that site's repo state and Telegram destination when connected.
- One measured optimization cycle per site every 7 days with Before/After evidence.
- MyTel runs in Growth Mode; TehNet begins in Build/Site-Factory Mode, then transitions to Growth Mode.
- No destructive production change is auto-executed in Phase 4. Phase 4 detects, measures, prioritizes and prepares actionable work; Phase 5 adds controlled execution gates.
- No rank guarantee. The optimization target is increased qualified first-page visibility, leads/conversions and commercial impact.

## Data layers
1. Public Site Health: HTTP/TLS/uptime/robots/sitemap/status/redirect/canonical basics.
2. Technical Crawl: SiteOne Crawler for repeatable SEO crawl/audit; Crawl4AI for AI-ready extraction and page understanding.
3. Performance: Lighthouse CI/page performance checks for representative URLs.
4. Search: Google Search Console via official API/connected tooling; Bing where available.
5. Analytics/Revenue: GA4 plus leads/forms/calls/CRM/revenue connectors when available.
6. Competitors/Trends: changedetection/RSS/public feeds + selected competitor pages.
7. Local AI: Phase 3 LiteLLM/Ollama summarizes and scores opportunities.

## Tasks

### P4-INTEL-01 — Site manifests and isolated state
Create per-site manifests, report/history directories and machine-readable action/opportunity schemas. Never mix MyTel and TehNet state.

### P4-INTEL-02 — Public baseline monitor
For each site collect and store: HTTP status, final URL, latency, TLS reachability, robots.txt, sitemap candidates, title/meta basics and timestamp. This can begin without GSC credentials.

### P4-INTEL-03 — Technical crawler
Deploy SiteOne Crawler pinned to a reviewed version. Produce machine-readable crawl artifacts for each site. Add Crawl4AI only after SiteOne baseline is stable; do not duplicate work blindly.

### P4-INTEL-04 — Search/analytics connectors
Connect GSC first because it directly supports query/page/CTR/position opportunity detection. Connect GA4 next. Store tokens only in host secrets, never Git.

### P4-INTEL-05 — Revenue Opportunity queue
Normalize evidence into the canonical opportunity schema and score technical/search/content/CRO/offer/social opportunities. Every item must have evidence, expected metric and next measurement date.

### P4-INTEL-06 — Daily report pipeline
Every 24h generate per-site report using `growth-os/operations/DAILY-REPORT-SCHEMA-FA.md`. Report what happened, what changed, what failed, what improved, what is too early to judge and what happens next.

### P4-INTEL-07 — 7-day optimization review
Create weekly Before/After review and prioritized change package for Phase 5 execution. Stop/adjust/rollback recommendations must be evidence-based.

### P4-INTEL-08 — Cold-start / queue recovery
Verify monitor schedules, state, crawler jobs and reports recover after WSL restart. Jobs must be idempotent and resumable.

## Phase 4 completion gate
- Both sites have isolated manifests/state.
- Public baseline monitoring is producing timestamped evidence.
- Repeatable technical crawl works for both sites.
- GSC ingestion works for every connected property, or is explicitly marked WAITING_FOR_OWNER_CONNECTION rather than fabricated.
- Daily report generator produces one evidence-based report per site.
- 7-day cycle state exists and has a defined Before baseline.
- Opportunity queue has evidence-backed items, not invented rankings/traffic.
- Phase 2 and Phase 3 health remain green.

## Handoff to Phase 5
Phase 5 consumes the opportunity queue and executes low-risk website/content/code changes through branch/PR/QA/deploy gates, then writes verification and impact back into the daily/weekly reporting loop.
