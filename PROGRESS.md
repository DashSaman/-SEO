# PROGRESS.md — SEO Reference Research Dashboard

**Updated:** 2026-08-26  
**Overall baseline completion: 44%**  
**Repository state:** ACTIVE / RESUMABLE

> This percentage measures completion of the defined baseline research program below. It does **not** claim that the entire web or every SEO edge case has been exhaustively researched.

## Progress bar

`█████████░░░░░░░░░░░ 44%`

## Weighted stages

| Stage | Weight | Status | Stage completion | Weighted contribution | Current evidence/work |
|---|---:|---|---:|---:|---|
| 0. Repository architecture + agent continuity | 10% | ✅ COMPLETE | 100% | 10.0% | README, AGENTS, HANDOFF, source ledger, progress system |
| 1. Official Google + Bing foundations | 20% | 🟡 IN PROGRESS | 80% | 16.0% | Google Search Essentials/content/AI/canonical/crawlers; Bing BWT/sitemaps/duplicates |
| 2. Standards + regional search engines | 15% | 🟡 IN PROGRESS | 55% | 8.25% | RFC 9309, Sitemaps, IndexNow, Yandex, Naver; Schema/Baidu/etc queued |
| 3. AI search/crawler ecosystem | 15% | 🟡 IN PROGRESS | 65% | 9.75% | Google-Extended, OpenAI, Anthropic, Perplexity; Apple/additional providers queued |
| 4. GitHub/open-source ecosystem validation | 15% | 🟠 DISCOVERY DONE | 0% verified catalogue | 0.0% | Candidate repositories discovered; individual README/activity validation next |
| 5. Measured SERP + practitioner research | 15% | ⚪ QUEUED | 0% | 0.0% | Representative query study queued |
| 6. Synthesis + implementation checklists | 5% | ⚪ QUEUED | 0% | 0.0% | Durable reference docs/checklists next |
| 7. Visual dashboard + final conflict/freshness pass | 5% | ⚪ QUEUED | 0% | 0.0% | `docs/index.html` and final reconciliation queued |
| **TOTAL** | **100%** |  |  | **44.0%** |  |

## Source counts

- Official/standards sources reviewed and entered: **31 ledger rows** (including distinct scoped uses of shared official pages).
- GitHub/community candidates discovered: **11 initial candidates**.
- Regional engines with first-party material already reviewed: **Yandex, Naver**.
- AI providers with first-party crawler/search guidance already reviewed: **Google, OpenAI, Anthropic, Perplexity**.
- Measured SERP topics completed: **0 / 6 initial baseline topics**.

## Completed work

- [x] Confirmed target repository exists, is writable and uses `main`.
- [x] Established evidence hierarchy and anti-myth rules.
- [x] Created mandatory multi-agent update/coordination protocol.
- [x] Created resumable live handoff state.
- [x] Created source-by-source evidence ledger.
- [x] Reviewed Google Search Essentials and core SEO guidance.
- [x] Reviewed Google people-first/content quality guidance and E-E-A-T framing.
- [x] Reviewed current 2026 Google generative-AI Search guidance.
- [x] Verified Google explicitly says `llms.txt`/special AI markup is not needed for Google Search generative features.
- [x] Reviewed Google canonicalization and current documentation update log.
- [x] Verified Google-Extended purpose and its separation from Google Search ranking/inclusion.
- [x] Reviewed Bing Webmaster basics, sitemap guidance and duplicate-content/AI-search guidance.
- [x] Reviewed RFC 9309 robots standard.
- [x] Reviewed Sitemaps protocol and IndexNow documentation.
- [x] Reviewed Yandex Webmaster foundation material.
- [x] Reviewed Naver Search Advisor foundation material.
- [x] Reviewed OpenAI publisher/crawler guidance.
- [x] Reviewed Anthropic crawler guidance including ClaudeBot / Claude-User / Claude-SearchBot separation.
- [x] Reviewed Perplexity robots guidance.
- [x] Ran broad GitHub repository discovery for classic SEO, AI/GEO, programmatic SEO and technical crawler categories.

## Current work

- [ ] Verify current Schema.org + Google structured-data documentation.
- [ ] Verify current Core Web Vitals/Search wording and thresholds.
- [ ] Convert verified source notes into durable topic reference documents.
- [ ] Inspect selected GitHub repositories individually for scope, maintenance, license and unsupported claims.
- [ ] Run measured current SERP research for representative SEO categories.

## Next work queue

- [ ] Baidu first-party webmaster/search documentation.
- [ ] DuckDuckGo discovery/index behavior from current official sources.
- [ ] Applebot / Applebot-Extended documentation.
- [ ] Local SEO/entity/review ecosystem first-party sources.
- [ ] Ecommerce/Product structured-data and Merchant Center discovery layer.
- [ ] Image/video/news/international SEO specialties.
- [ ] Search Console/Bing measurement playbook.
- [ ] Backlink/link-earning research with spam-policy boundaries.
- [ ] Migration/relaunch checklist.
- [ ] JavaScript SEO/rendering checklist.
- [ ] Static visual dashboard (`docs/index.html`).
- [ ] Final stale-source/conflict review.

## Important findings already locked

1. **SEO is still foundational for Google generative Search.** Google’s 2026 guidance explicitly frames AI Overviews/AI Mode optimization as Search optimization, not a separate magic discipline.
2. **`llms.txt` is not a Google Search ranking/AI requirement.** Google says it ignores such files for Search visibility; other systems may choose differently.
3. **AI crawler controls must be provider-specific.** Search crawling, training crawling and user-triggered retrieval are often separate bots/tokens.
4. **robots.txt is not security.** RFC 9309 defines crawler-access rules, not authorization.
5. **Sitemaps/IndexNow help discovery/change notification; neither guarantees indexing/ranking.**
6. **Community GitHub repositories are evidence inputs, not authorities.** Their recommendations must be checked against current first-party sources.

## How percentage must be updated

When a stage changes, update its `Stage completion`, compute:

`weighted contribution = stage weight × stage completion`

Then sum all weighted contributions and update both the numeric headline and ASCII progress bar. Never inflate the percentage because many URLs were skimmed; count only research that is logged and synthesized/validated according to `AGENTS.md`.

## Activity log

| Date | Milestone | Result |
|---|---|---|
| 2026-08-26 | Repository initialization | ✅ Evidence-first architecture created |
| 2026-08-26 | Official foundation pass #1 | ✅ Google/Bing/Yandex/Naver/OpenAI/Anthropic/Perplexity + robots/sitemaps/IndexNow reviewed |
| 2026-08-26 | GitHub landscape discovery #1 | ✅ Initial classic SEO/GEO/crawler repositories identified; verification pending |
| 2026-08-26 | Multi-agent continuity | ✅ `AGENTS.md` + `HANDOFF.md` established |
