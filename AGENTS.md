# AGENTS.md — Operating Contract for SEO Research Agents

**Repository:** `DashSaman/-SEO`  
**Last protocol revision:** 2026-08-26

This file is mandatory reading for every AI agent or human researcher working in this repository.

## Mission

Build and maintain an evidence-first SEO reference covering classic search, AI-assisted search, technical implementation, content quality, discoverability, structured data, measurement and open-source tooling. The repository must remain resumable and safe for parallel work.

## Mandatory source hierarchy

1. **Official engine/vendor documentation** — Google Search Central, Bing Webmaster, Yandex Webmaster, Naver Search Advisor, OpenAI, Anthropic, Perplexity, etc.
2. **Standards/protocol owners** — IETF RFCs, Sitemaps.org, Schema.org, IndexNow.
3. **Measured data** — Search Console/Bing Webmaster/SERP measurements/credible datasets.
4. **Established practitioner research** — only when methodology and date can be evaluated.
5. **GitHub/community material** — implementation/tooling inspiration; never automatically treated as ranking truth.

If sources conflict, record the conflict and prefer the most current applicable first-party source unless there is strong reproducible evidence that product behavior differs.

## Required workflow for EVERY source

1. Read `HANDOFF.md` and confirm the source/topic is not already actively claimed by another agent.
2. Research the source and determine:
   - publisher/owner;
   - source class (official / standard / measured / practitioner / community);
   - publication/update date when available;
   - exact scope of the claim;
   - what the source **does not** prove.
3. Add/update the source in `SOURCES.md` with status `VERIFIED`, `PARTIAL`, `SUPERSEDED`, `CONFLICT`, or `BACKLOG`.
4. Synthesize findings into the appropriate `docs/*.md` file. Do not copy lengthy text.
5. Update `PROGRESS.md` if a task, stage, or source count changed.
6. Update `HANDOFF.md`:
   - `LAST_COMPLETED_SOURCE`
   - `LAST_COMPLETED_ACTION`
   - `ACTIVE_WORK`
   - `NEXT_ACTIONS`
   - timestamp
7. Commit with a descriptive message.

**A source is not considered completed until steps 3–6 are done.**

## Required workflow for EVERY stage

At stage completion:

- verify all new claims have source entries;
- run a consistency pass against newer official guidance;
- mark stage status in `PROGRESS.md`;
- record unresolved questions explicitly;
- update the dashboard (`docs/index.html`);
- set the exact next stage in `HANDOFF.md`.

## Parallel-agent protocol

`HANDOFF.md` contains an `ACTIVE_WORK` table. Before starting:

- claim one unclaimed workstream with agent/session label and timestamp;
- avoid editing the same document concurrently unless coordinated;
- if an active claim looks abandoned, do not silently take it over: mark it `STALE-CLAIM-TAKEOVER` with the prior label preserved;
- merge research by source IDs, not by overwriting another agent's ledger entries;
- update the handoff after every meaningful commit.

Recommended workstreams that can run independently:

- Google Search / Google AI Search
- Bing / IndexNow
- Yandex / Naver / Baidu / regional engines
- Web protocols: robots/sitemaps/schema
- AI crawlers / AI answer engines
- GitHub/open-source tools
- SERP/practitioner research
- Local/entity/reputation SEO
- Ecommerce/international/news/video/image SEO
- Measurement/monitoring

## Evidence-writing rules

Every important statement should be tagged mentally as one of:

- **FACT-OFFICIAL** — directly supported by official docs.
- **FACT-STANDARD** — specified by a standard/protocol.
- **OBSERVED** — measured in SERPs/tools; may change by query/location/time.
- **INFERENCE** — reasoned implication from evidence; clearly label it.
- **HYPOTHESIS** — requires testing.

Never write an `OBSERVED`, `INFERENCE`, or `HYPOTHESIS` as a hidden Google/Bing ranking factor.

## Freshness rules

SEO documentation changes frequently. For mutable vendor behavior:

- record `Reviewed: YYYY-MM-DD`;
- prefer sources updated in the last 18 months when alternatives exist;
- for current crawler identities, AI visibility controls, rich-result eligibility, Search Console features and spam policies, always re-check official documentation before changing production guidance;
- preserve obsolete guidance only when useful historically and label it `SUPERSEDED`.

## Safety / quality guardrails

Do not recommend or operationalize:

- paid-link schemes intended to manipulate rankings;
- PBN/link-farm automation;
- cloaking or search-engine-specific deceptive output;
- doorway pages;
- mass-generated low-value pages for query capture;
- fake user reviews, fake forum mentions or fabricated citations;
- hacked-site/link injection;
- evasion of spam enforcement.

Discuss these only as risks/spam-policy concepts when needed.

## Technical correctness rules

- `robots.txt` controls crawler access; it is **not** authentication and is not a reliable method for hiding secrets.
- `noindex` and crawl blocking are different controls; if a bot cannot crawl a page it may not see the page-level meta directive.
- canonical signals are generally hints/preferences, not a guarantee that a chosen URL will be selected by every engine.
- a sitemap aids discovery; it does not guarantee indexing.
- IndexNow notifies participating search engines about URL changes; notification does not guarantee crawl/index/rank.
- structured data can enable/clarify supported search features but is not a generic ranking guarantee.
- Core Web Vitals/page experience are part of overall quality/UX considerations; do not reduce SEO to a Lighthouse score.
- Google’s 2026 guidance says no special AI markup or `llms.txt` is required for Google Search generative features.

## Copyright / quotation rule

Summarize. Keep quotations very short and necessary. Link to the primary source. Do not republish articles, documentation pages, proprietary datasets, or repository content wholesale.

## File responsibilities

- `README.md` — stable entry point and philosophy.
- `AGENTS.md` — this operating contract.
- `HANDOFF.md` — exact current execution state; optimized for a brand-new chat/agent.
- `PROGRESS.md` — human progress dashboard and weighted stage calculation.
- `SOURCES.md` — append/update source ledger.
- `docs/*.md` — durable research synthesis.
- `docs/index.html` — visual progress dashboard; update on stage changes.

## Definition of done for a claim

A claim is production-reference ready only when it has:

1. a named source,
2. a URL,
3. a review date,
4. a clear evidence class,
5. scope/caveat if necessary,
6. synthesis in the relevant reference file.

If any of these are missing, treat the claim as incomplete.