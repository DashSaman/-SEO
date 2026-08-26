# HANDOFF.md — Live Continuation State

> **Purpose:** A brand-new chat/agent must be able to continue the research from this file without reconstructing prior conversation history.

**Updated:** 2026-08-26  
**Repository:** `DashSaman/-SEO`  
**Default branch:** `main`

## CURRENT_STAGE

`STAGE-1/OFFICIAL-FOUNDATIONS` — official search-engine, protocol and AI crawler research is in progress. Repository scaffold is complete.

## LAST_COMPLETED_SOURCE

`STD-INDEXNOW-001` — IndexNow official documentation and FAQ reviewed for change-notification semantics and implementation boundaries.

## LAST_COMPLETED_ACTION

Created the core repository operating contract (`AGENTS.md`) after initializing the evidence-first project README.

## ACTIVE_WORK

| Workstream | Agent/session | Status | Started | Target files |
|---|---|---|---|---|
| Official Google/Bing/protocol/AI foundations | primary-research-agent-2026-08-26 | ACTIVE | 2026-08-26 | `SOURCES.md`, `docs/google-seo.md`, `docs/bing-indexnow.md`, `docs/technical-seo.md`, `docs/ai-search.md` |
| GitHub open-source landscape | primary-research-agent-2026-08-26 | ACTIVE | 2026-08-26 | `docs/open-source-seo.md` |
| SERP/practitioner layer | primary-research-agent-2026-08-26 | QUEUED | 2026-08-26 | `docs/serp-research.md` |

## VERIFIED RESEARCH ALREADY AVAILABLE TO CONTINUING AGENTS

### Google
- Search Essentials, SEO Starter Guide, helpful/people-first content guidance and developer SEO guidance reviewed.
- Google 2026 generative-AI SEO guide reviewed: foundational SEO remains relevant; Google Search does not require `llms.txt`, special AI markup, artificial content chunking, AI-only rewrites or inauthentic mentions for AI Overviews/AI Mode.
- Canonicalization documentation reviewed; canonical selection uses multiple signals and is not merely a single tag rule.
- Current 2026 Search documentation update log reviewed, including generative-AI guidance and recent rich-result/documentation changes.
- Google-Extended official crawler documentation reviewed: it is a robots.txt product token, not a separate HTTP user-agent string; it controls certain Gemini training/grounding uses and does not affect Google Search inclusion/ranking.

### Bing
- Bing Webmaster Tools guidance reviewed.
- Bing 2025 sitemap guidance reviewed: accurate `lastmod` is meaningful; Bing states `changefreq` and `priority` are ignored.
- Bing duplicate-content/AI-search guidance reviewed.
- Bing Webmaster blog indicates an AI Performance feature in public preview (2026) for AI citation visibility; re-check exact product documentation before production claims.

### Regional engines
- Yandex Webmaster structure/indexing/recommendation material reviewed.
- Naver Search Advisor SEO, robots and markup guidance reviewed; Naver documents `Yeti` and supports robots controls.
- Baidu/current additional regional-engine verification is still queued; do not invent guidance.

### Standards / protocols
- IETF RFC 9309 Robots Exclusion Protocol reviewed. Robots rules control crawler access and are not authorization/security.
- Sitemaps.org protocol reviewed: standard sitemap size/count boundaries and index-file model recorded for synthesis.
- IndexNow official documentation/FAQ reviewed: change notification is not an indexing/ranking guarantee.
- Schema.org official source verification still queued before final structured-data synthesis.

### AI systems
- OpenAI publisher/developer crawler guidance reviewed: `OAI-SearchBot` is relevant to ChatGPT search discovery; training control (`GPTBot`) is a separate concern.
- Anthropic official April 7, 2026 guidance reviewed: `ClaudeBot`, `Claude-User`, `Claude-SearchBot` have distinct purposes; all honor robots.txt; Claude-SearchBot affects search indexing/visibility.
- Perplexity official robots guidance reviewed; respects robots controls with documented limits/metadata behavior.
- Community crawler lists may be catalogued but must not override first-party bot documentation.

### GitHub landscape discovered
Initial repository discovery has identified candidates including:
- `bmpi-dev/awesome-seo`
- `serpapi/awesome-seo-tools`
- `teles/awesome-seo`
- `marcobiedermann/search-engine-optimization`
- `amplifying-ai/awesome-generative-engine-optimization`
- `best-of-ai/awesome-ai-seo`
- `johnmurch/awesome-seo-scripts`
- `guptadeepak/awesome-programmatic-seo`
- `puneetindersingh/open-seo-crawler`
- `spronta/crawlie`

These are **discovered, not yet all verified/endorsed**. Inspect README/activity/license and validate claims before cataloguing as recommended tools.

## NEXT_ACTIONS — exact order

1. Create/update `SOURCES.md` with every official source already reviewed and evidence class/status.
2. Verify Schema.org official implementation source and current Google Core Web Vitals/Search guidance.
3. Write `docs/google-seo.md` and `docs/technical-seo.md` from verified sources.
4. Write `docs/bing-indexnow.md` and `docs/ai-search.md`.
5. Inspect high-value GitHub candidates individually (README, maintenance/activity, scope) and write `docs/open-source-seo.md`.
6. Run measured SERP research for representative SEO topic classes; distinguish observed rankings from recommendations.
7. Expand regional engines (Baidu and additional engines where current first-party docs can be verified).
8. Write practical checklists and myth/risk sections.
9. Create/update `docs/index.html` progress dashboard and reconcile weighted completion in `PROGRESS.md`.
10. Run final cross-source conflict/freshness review.

## BLOCKERS / LIMITATIONS

- The web is unbounded: “all SEO information” cannot be exhaustively completed in one pass. The repository is therefore designed as a continuously auditable reference with explicit coverage/backlog rather than falsely claiming completeness.
- Search rankings vary by date, country, device, language and personalization. SERP observations must include measurement context.
- Some AI visibility behavior is proprietary and changes quickly; only documented controls and measurable observations should be presented as facts.
- GitHub Pages serving is not assumed enabled. The static dashboard file can be built in `docs/index.html`; repository-native `PROGRESS.md` is always immediately usable.

## CONTINUATION_INSTRUCTIONS FOR A NEW CHAT/AGENT

Read in this order:

1. `AGENTS.md`
2. this file
3. `PROGRESS.md`
4. `SOURCES.md`
5. only then the relevant `docs/*.md`

Then claim one non-conflicting workstream in `ACTIVE_WORK`, perform the next incomplete source/stage, and **before ending your turn** update `SOURCES.md`, `PROGRESS.md` and this file. Never report “done” unless the repository state reflects the work.

## CONCURRENT WORK RULE

If another agent wants to work simultaneously, choose a separate workstream/document. Do not make parallel edits to `SOURCES.md`, `PROGRESS.md` or `HANDOFF.md` without first re-fetching the latest version; these are shared coordination files and must be updated sequentially to avoid lost changes.