# Open-Source SEO Tooling — Evidence-Safe Catalogue

**Reviewed:** 2026-08-26  
**Rule:** A useful repository is an implementation/tooling source, not proof of a search-engine ranking factor.

## Verdict scale

- `RECOMMENDED` — strong, current tool for its stated job; production use still requires normal engineering review.
- `USEFUL` — practical for many teams, with important scope/caveats.
- `SPECIALIZED` — good for a narrow workflow or stack.
- `EXPERIMENTAL` — promising but maturity/evidence/maintenance needs caution.
- `STALE` — historical/archived/outdated for current default use.
- `AVOID` — unsuitable or misleading for the defined evidence-first workflow.

## Evaluation method

For important candidates we checked repository status, archive flag, activity/push recency where available, README/scope, license where exposed by GitHub, and whether marketing claims conflict with current official Google/Bing/provider documentation. Popularity is not an evidence class.

## Core recommended tooling

### GoogleChrome/lighthouse — `RECOMMENDED`

- Repository: https://github.com/GoogleChrome/lighthouse
- Purpose/category: automated web audits, performance metrics and best-practice diagnostics.
- Activity: active; GitHub reported a push on **2026-08-26** during review.
- Archived: no.
- License: Apache-2.0.
- Strengths: reproducible lab diagnostics; broad ecosystem support; highly useful release gate for performance/accessibility/technical regressions.
- Weaknesses: lab conditions are not the same as field user data; the SEO audit subset is not a complete SEO audit.
- Operational concern: CI thresholds can create false certainty if teams optimize the score instead of user/search outcomes.
- Official-doc conflict: none as a diagnostic tool. **A Lighthouse score is not a Google ranking score.** Google’s own Search guidance says good page experience does not guarantee ranking.
- Recommended use: pre/post-release diagnostics combined with CrUX/Search Console/real-user metrics and crawl/index tests.

### GoogleChrome/web-vitals — `RECOMMENDED`

- Repository: https://github.com/GoogleChrome/web-vitals
- Purpose/category: client library for measuring Web Vitals.
- Activity: active; GitHub reported push **2026-08-25**.
- Archived: no.
- License: Apache-2.0.
- Strengths: focused implementation of field-side metrics; good RUM instrumentation primitive.
- Weaknesses: measurement library, not an optimizer; requires telemetry/backend interpretation.
- Recommended use: production RUM for LCP/INP/CLS and release-change annotations.
- Caveat: good CWV helps page experience but is not a standalone ranking guarantee.

### eliasdabbas/advertools — `RECOMMENDED`

- Repository: https://github.com/eliasdabbas/advertools
- Purpose/category: Python marketing/SEO analysis toolkit.
- Activity: active; GitHub reported last push **2026-06-30** at review.
- Archived: no.
- License: MIT.
- Features: crawling, robots/sitemap parsing, log/URL/data analysis, SERP-import workflows and general marketing analysis.
- Strengths: scriptable, data-frame-friendly, excellent for reproducible audits and log/sitemap processing.
- Weaknesses: requires Python/data competence; crawler behavior is not identical to Googlebot.
- Recommended use: reproducible technical audits, URL inventories, robots/sitemap validation and data pipelines.

### Yoast/wordpress-seo — `RECOMMENDED` for WordPress implementation

- Repository: https://github.com/Yoast/wordpress-seo
- Purpose/category: source/dev repository for Yoast SEO for WordPress.
- Activity: highly active; GitHub reported push **2026-08-26**.
- Archived: no.
- License metadata: GitHub exposes `NOASSERTION/Other`; inspect project licensing before redistribution or derivative distribution.
- Strengths: mature WordPress metadata, canonical, XML sitemap, schema and editorial implementation ecosystem.
- Weaknesses: plugin heuristics/readability/keyword scores are proxies, not search-engine scores.
- Recommended use: WordPress implementation when its generated canonical/schema/sitemap output has been tested against the site’s architecture.
- Official-doc conflict: treat plugin scores as editorial assistance only; Google does not rank by Yoast/Rank Math scores.

## Measurement / rank tracking

### towfiqi/serpbear — `USEFUL`

- Repository: https://github.com/towfiqi/serpbear
- Purpose: self-hosted search-position tracking.
- Activity: unarchived; GitHub reported push **2026-05-14**.
- License: MIT.
- Strengths: self-hosted dashboard, keyword/history tracking, Search Console integration and multiple collection-provider options.
- Weaknesses: README/integrations may outlive third-party scraping/API compatibility; SERP providers can change frequently.
- Operational concerns: respect search-provider terms and rate limits; avoid interpreting one location/device snapshot as a universal rank.
- Recommended use: controlled, configured rank monitoring with explicit locale/device/query context.

### karust/openserp — `EXPERIMENTAL`

- Repository: https://github.com/karust/openserp
- Purpose: SERP collection/scraping-oriented tooling.
- Strengths: can support controlled measurement research.
- Risks: search-page markup, anti-bot systems, terms, localization and personalization make scraping brittle.
- Recommended use: research/test environments only after current maintenance, license and provider-compliance review.

## Framework / CMS implementation helpers

### iamvishnusankar/next-sitemap — `RECOMMENDED` for its narrow function

- Repository: https://github.com/iamvishnusankar/next-sitemap
- Purpose: Next.js sitemap and robots generation for static/dynamic/server-rendered pages.
- Activity: unarchived; GitHub reported push **2026-05-13**.
- License: MIT.
- Strengths: sitemap splitting/indexes, robots generation and framework integration.
- Weaknesses: generated defaults still require architecture review; including a URL in a sitemap does not make it indexable or canonical.
- Important engine nuance: the library can emit fields such as `changefreq` and `priority`; Bing explicitly says it ignores those sitemap fields. Do not treat them as ranking controls.

### garmeeh/next-seo — `USEFUL`

- Repository: https://github.com/garmeeh/next-seo
- Purpose: Next.js SEO/structured-data components.
- Strengths: convenient structured-data composition.
- Weaknesses/caution: current Next.js metadata APIs may be preferable for standard metadata; README/promotional claims are not search evidence.
- Recommended use: use for implementation convenience after validating rendered HTML and Google-supported rich-result requirements.

### harlan-zw/nuxt-seo — `USEFUL`

- Repository: https://github.com/harlan-zw/nuxt-seo
- Purpose: Nuxt SEO module ecosystem covering robots, sitemap, schema, social/OG and related tooling.
- Strengths: integrated framework experience.
- Weaknesses: broad “AEO/AI SEO” marketing language can be stronger than current first-party evidence.
- Recommended use: implementation layer; validate each claim/output against Google/Bing/provider docs.

### harlan-zw/unlighthouse — `SPECIALIZED`

- Repository: https://github.com/harlan-zw/unlighthouse
- Purpose: site-scale Lighthouse crawling/reporting.
- Recommended use: regression triage across many URLs; sample templates and important traffic classes rather than chasing a global score.

### jekyll/jekyll-seo-tag — `SPECIALIZED`

- Repository: https://github.com/jekyll/jekyll-seo-tag
- Purpose: Jekyll metadata helper.
- Recommended use: static Jekyll projects, followed by rendered-output validation.

### spatie/laravel-sitemap — `SPECIALIZED`

- Repository: https://github.com/spatie/laravel-sitemap
- Purpose: Laravel sitemap generation/crawling.
- Caveat: sitemap generation does not decide canonical/indexability quality; filter URLs intentionally.

### spatie/schema-org — `SPECIALIZED`

- Repository: https://github.com/spatie/schema-org
- Purpose: PHP Schema.org builder.
- Caveat: Schema.org vocabulary support is broader than Google rich-result support. A valid type is not automatically a Search feature.

## Crawling / auditing

### sethblack/python-seo-analyzer — `USEFUL`

- Repository: https://github.com/sethblack/python-seo-analyzer
- Purpose: on-site SEO analysis.
- Recommended use: lightweight supplementary audit, not the sole production crawler.
- Caveat: re-check maintenance and rules before relying on any hardcoded SEO heuristic.

### puneetindersingh/open-seo-crawler — `EXPERIMENTAL`

- Repository: https://github.com/puneetindersingh/open-seo-crawler
- Purpose: open technical SEO crawler.
- Recommended use: evaluate in non-destructive test crawl first; compare output with server logs and a second crawler.
- Pending caution: deeper release/security review is needed before production-critical use.

### spronta/crawlie — `EXPERIMENTAL`

- Repository: https://github.com/spronta/crawlie
- Purpose: crawling/SEO analysis tooling.
- Recommended use: exploratory/secondary crawler until maintenance, scale behavior and edge cases are verified in the target environment.

## Resource catalogues — useful discovery, not authority

### bmpi-dev/awesome-seo — `USEFUL`

- Repository: https://github.com/bmpi-dev/awesome-seo
- Purpose: curated SEO resource map.
- Strength: broad discovery surface.
- Weakness: mixed-quality ecosystem; includes communities/resources that may discuss black-hat tactics.
- Rule: follow links as leads, then verify claims against current first-party sources.

### serpapi/awesome-seo-tools — `USEFUL`

- Repository: https://github.com/serpapi/awesome-seo-tools
- Purpose: broad SEO tools catalogue.
- Rule: tool inclusion is not endorsement and says nothing about ranking-factor truth.

### teles/awesome-seo — `SPECIALIZED`

- Repository: https://github.com/teles/awesome-seo
- Purpose: general SEO resource list.
- Use: discovery/history; verify freshness before following advice.

### marcobiedermann/search-engine-optimization — `USEFUL`

- Repository: https://github.com/marcobiedermann/search-engine-optimization
- Purpose: SEO checklist/reference.
- Use: checklist inspiration; current Google/Bing documentation wins on conflicts.

### johnmurch/awesome-seo-scripts — `USEFUL`

- Repository: https://github.com/johnmurch/awesome-seo-scripts
- Purpose: SEO automation/script discovery.
- Security rule: review source, dependencies, credentials/access and rate limits before execution.

### guptadeepak/awesome-programmatic-seo — `USEFUL`

- Repository: https://github.com/guptadeepak/awesome-programmatic-seo
- Purpose: programmatic SEO resource catalogue.
- Critical caveat: scale is not a quality exemption. Google’s scaled-content-abuse policy applies regardless of whether pages were generated by AI, scripts or humans.

## AI/GEO catalogues

### amplifying-ai/awesome-generative-engine-optimization — `USEFUL`

- Repository: https://github.com/amplifying-ai/awesome-generative-engine-optimization
- Purpose: GEO papers/resources/tools discovery.
- Rule: separate papers with explicit experiments from vendor claims and anecdotes. Provider-specific crawler/Search controls outrank community advice.

### best-of-ai/awesome-ai-seo — `USEFUL`

- Repository: https://github.com/best-of-ai/awesome-ai-seo
- Purpose: AI SEO/GEO tool and resource discovery.
- Caveat: fast-moving category with marketing-driven claims. Never infer that a listed tactic improves ChatGPT/Google/Claude citations without measured/provider evidence.

### nobodyscode/ai-crawlers — `USEFUL`

- Repository: https://github.com/nobodyscode/ai-crawlers
- Purpose: AI crawler catalogue.
- Strong use: inventory/detection lead.
- Production rule: verify every user-agent/token/IP/control against the relevant provider’s current first-party documentation before editing robots/WAF rules.

## Legacy / archived tools

### GoogleChrome/rendertron — `STALE`

- Repository: https://github.com/GoogleChrome/rendertron
- Purpose: Headless Chrome dynamic-rendering solution.
- Archived: **yes**.
- Last push reported by GitHub: **2022-10-06**.
- License: Apache-2.0.
- Verdict reason: useful historical context, but not a current default JavaScript SEO architecture. Prefer SSR/SSG/server-compatible rendering or robust client rendering and test what bots/users receive.

### eyecatchup/SEOstats — `STALE`

- Repository: https://github.com/eyecatchup/SEOstats
- Purpose: historical SEO metrics/API aggregation library.
- Status: archived/legacy in the reviewed landscape.
- Risk: old third-party endpoints and metrics age badly; not suitable as a current evidence source.

### nuxt/vue-meta — `STALE`

- Repository: https://github.com/nuxt/vue-meta
- Purpose: historic Vue/Nuxt metadata management.
- Use: legacy projects only; prefer current framework-native/Nuxt SEO implementation for new systems.

## What this catalogue deliberately refuses to do

- No repository gets `RECOMMENDED` merely because it has many stars.
- No README claim becomes a ranking factor.
- No crawler is assumed to behave exactly like Googlebot/Bingbot/OAI-SearchBot.
- No SERP scraper result is treated as global rank truth.
- No “AI SEO” file, schema, paragraph pattern or crawler list is treated as universally required.

## Production selection checklist

Before adopting any repository:

1. verify it is not archived/abandoned;
2. inspect license and dependency/security posture;
3. review last meaningful release/commit, not just repository `updated_at`;
4. test on staging/sampled URLs;
5. inspect rendered output and HTTP behavior;
6. compare claims with `SOURCES.md` first-party entries;
7. capture a before/after measurement and rollback path;
8. never make destructive crawl/index/robots/canonical changes from tool defaults alone.
