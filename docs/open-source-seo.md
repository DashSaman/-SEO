# Open-Source SEO Tooling — Evidence-Safe Catalogue

**Reviewed:** 2026-08-26  
**Evidence class:** `COMMUNITY / IMPLEMENTATION`  
**Rule:** a useful repository is an implementation/tooling source, **not** proof of a search-engine ranking factor.

## Verdict scale

- `RECOMMENDED` — strong, current tool for its stated job; production use still requires ordinary engineering review.
- `USEFUL` — practical for many teams, with important scope/caveats.
- `SPECIALIZED` — good for a narrow workflow or framework.
- `EXPERIMENTAL` — promising, but maturity/evidence/maintenance needs caution.
- `STALE` — historical/archived/outdated for current default use.
- `AVOID` — unsuitable or materially misleading for this evidence-first workflow.

## Evaluation method

For the core catalogue we checked, as available:

1. repository identity and purpose;
2. archive flag;
3. last meaningful code push visible from GitHub metadata;
4. maintenance/activity signal;
5. license metadata exposed by GitHub;
6. README/product scope;
7. operational/security concerns;
8. claims that need first-party verification;
9. conflicts with current Google/Bing/provider guidance;
10. a bounded recommended use and verdict.

`updated_at` alone is not treated as code activity because stars/issues can update repository metadata without a code change. Popularity/star count is never an evidence class.

## Core validation matrix

| Repository | Category | Archived? | Last code push observed | License metadata | Maintenance signal | Verdict |
|---|---|---:|---|---|---|---|
| `GoogleChrome/lighthouse` | web/performance audit | No | 2026-08-26 | Apache-2.0 | highly active | `RECOMMENDED` |
| `GoogleChrome/web-vitals` | RUM / Web Vitals | No | 2026-08-25 | Apache-2.0 | highly active | `RECOMMENDED` |
| `Yoast/wordpress-seo` | WordPress SEO implementation | No | 2026-08-26 | GitHub: Other/NOASSERTION | highly active | `RECOMMENDED` |
| `eliasdabbas/advertools` | Python SEO/data analysis | No | 2026-06-30 | MIT | active | `RECOMMENDED` |
| `towfiqi/serpbear` | rank tracking | No | 2026-05-14 | MIT | active/recent | `USEFUL` |
| `iamvishnusankar/next-sitemap` | Next.js sitemap/robots | No | 2026-05-13 | MIT | active/recent | `RECOMMENDED` (narrow) |
| `garmeeh/next-seo` | Next.js structured data/meta helpers | No | 2026-07-29 | MIT | active | `USEFUL` |
| `harlan-zw/nuxt-seo` | Nuxt technical SEO suite | No | 2026-08-20 | MIT | highly active | `USEFUL` |
| `harlan-zw/unlighthouse` | site-scale Lighthouse | No | 2026-08-14 | MIT | highly active | `SPECIALIZED` |
| `jekyll/jekyll-seo-tag` | Jekyll metadata | No | 2026-05-08 | MIT | maintained | `SPECIALIZED` |
| `spatie/laravel-sitemap` | Laravel sitemap | No | 2026-08-07 | MIT | active | `SPECIALIZED` |
| `spatie/schema-org` | PHP Schema.org builder | No | 2026-08-07 | MIT | active | `SPECIALIZED` |
| `sethblack/python-seo-analyzer` | lightweight site analyzer | No | 2026-07-27 | GitHub: Other/NOASSERTION | active/recent | `USEFUL` |
| `karust/openserp` | self-hosted SERP API | No | 2026-07-22 | MIT | active | `SPECIALIZED` |
| `puneetindersingh/open-seo-crawler` | technical SEO crawler | No | 2026-08-04 | MIT | new/active | `EXPERIMENTAL` |
| `spronta/crawlie` | SEO/GEO crawler | No | 2026-07-18 | GitHub: Other/NOASSERTION | very new/active | `EXPERIMENTAL` |
| `nobodyscode/ai-crawlers` | AI crawler list | No | 2026-07-16 | none exposed | very new/minimal | `EXPERIMENTAL` |
| `bmpi-dev/awesome-seo` | resource catalogue | No | 2026-08-23 | MIT | active | `USEFUL` |
| `serpapi/awesome-seo-tools` | tool catalogue | No | 2026-02-24 | none exposed | maintained catalogue | `USEFUL` |
| `amplifying-ai/awesome-generative-engine-optimization` | GEO resource catalogue | No | 2026-04-14 | none exposed | recent | `USEFUL` |
| `best-of-ai/awesome-ai-seo` | AI SEO catalogue | No | 2026-07-27 | MIT | active | `USEFUL` |
| `GoogleChrome/rendertron` | dynamic rendering | **Yes** | 2022-10-06 | Apache-2.0 | archived | `STALE` |
| `eyecatchup/SEOstats` | historic SEO metrics API library | **Yes** | 2022-06-15 | MIT | archived | `STALE` |
| `nuxt/vue-meta` | legacy Vue metadata | **Yes** | 2025-09-25 | GitHub: Other/NOASSERTION | archived | `STALE` |

**Date rule:** the dates above are repository push metadata observed on 2026-08-26. A future adopter must re-check current status before production adoption.

---

# Detailed evaluations

## GoogleChrome/lighthouse — `RECOMMENDED`

**Repository:** https://github.com/GoogleChrome/lighthouse  
**Purpose:** automated web audits, performance metrics and best-practice diagnostics.  
**Strengths:** reproducible lab diagnostics; excellent regression gate; broad ecosystem support.  
**Weaknesses:** lab data is not field user data; the SEO audit subset is not a complete SEO audit.  
**Security/operational concern:** CI score thresholds can create false certainty and may encourage teams to optimize the score instead of real user/search outcomes.  
**Claim caution:** Lighthouse scores are diagnostic scores, not Google ranking scores.  
**Official-doc conflict:** none when used as diagnostics; Google Search guidance explicitly does not equate perfect page experience with guaranteed ranking.  
**Recommended use:** pre/post-release diagnostics together with CrUX/Search Console/RUM and crawl/index tests.

## GoogleChrome/web-vitals — `RECOMMENDED`

**Repository:** https://github.com/GoogleChrome/web-vitals  
**Purpose:** client-side Web Vitals measurement.  
**Features:** production collection primitives for LCP, INP and CLS.  
**Strengths:** focused, first-party implementation useful for RUM.  
**Weaknesses:** it measures; it does not fix performance or interpret business impact.  
**Operational concern:** sampling, SPA navigation and analytics pipelines must be implemented correctly.  
**Recommended use:** field measurement segmented by template/device/release.  
**Claim caution:** good CWV is not a standalone ranking guarantee.

## Yoast/wordpress-seo — `RECOMMENDED` for WordPress implementation

**Repository:** https://github.com/Yoast/wordpress-seo  
**Purpose:** WordPress SEO metadata, canonical, XML sitemap, schema and editorial implementation.  
**Strengths:** mature WordPress integration and active development.  
**Weaknesses:** plugin keyword/readability scores are editorial heuristics; defaults can conflict with custom architecture/plugins.  
**Security/operational concern:** test generated canonical/schema/robots/sitemap output after plugin/theme changes and avoid duplicate schema/SEO plugins.  
**License caution:** GitHub metadata exposes `Other/NOASSERTION`; inspect the project’s actual licensing terms before redistribution/derivative distribution.  
**Official-doc conflict:** Google does not use Yoast/Rank Math scores as ranking scores.  
**Recommended use:** implementation layer, not ranking oracle.

## eliasdabbas/advertools — `RECOMMENDED`

**Repository:** https://github.com/eliasdabbas/advertools  
**Purpose:** Python marketing/SEO data toolkit.  
**Features:** crawler workflows, robots/sitemap parsing, log/URL/data analysis and SERP-data processing.  
**Strengths:** reproducible, scriptable, data-frame-friendly technical analysis.  
**Weaknesses:** requires Python/data skills; its crawler is not Googlebot.  
**Operational concern:** use responsible crawl rates and validate parser assumptions.  
**Recommended use:** inventories, sitemap/robots checks, log analysis and reproducible audit pipelines.

## towfiqi/serpbear — `USEFUL`

**Purpose:** self-hosted rank tracking.  
**Strengths:** historical keyword monitoring and Search Console/integration options.  
**Weaknesses:** upstream scraping/API providers and integrations can break.  
**Operational concern:** explicitly set country/location/device and respect provider terms/rate limits.  
**Claim caution:** one tracked SERP is not universal rank truth.  
**Recommended use:** controlled rank monitoring with dated measurement context.

## iamvishnusankar/next-sitemap — `RECOMMENDED` for a narrow function

**Purpose:** Next.js sitemap and robots generation.  
**Strengths:** sitemap splitting/indexes and framework-friendly automation.  
**Weaknesses:** generated defaults cannot decide which URLs deserve indexation/canonical status.  
**Official nuance:** it can emit `changefreq`/`priority`; Bing explicitly says it ignores those fields.  
**Recommended use:** generate intentionally filtered canonical URL sets, then validate live XML/robots output.

## garmeeh/next-seo — `USEFUL`

**Purpose:** Next.js structured-data and SEO helpers.  
**Activity/license:** active in 2026; MIT.  
**Strengths:** convenient JSON-LD/schema composition.  
**Weaknesses:** framework-native Next.js metadata APIs may be preferable for ordinary metadata; README/promotional statements are not search evidence.  
**Operational concern:** validate rendered output, duplicate tags and Google feature requirements.  
**Recommended use:** implementation convenience, especially structured data.

## harlan-zw/nuxt-seo — `USEFUL`

**Purpose:** integrated Nuxt robots/sitemap/schema/social/SEO module ecosystem.  
**Activity/license:** highly active in 2026; MIT.  
**Strengths:** cohesive framework integration.  
**Weaknesses/claim caution:** broad “AEO/AI SEO” marketing terminology can imply more than current provider evidence proves.  
**Official-doc conflict rule:** provider/Google/Bing documentation wins over module marketing language.  
**Recommended use:** implementation layer after rendered-output validation.

## harlan-zw/unlighthouse — `SPECIALIZED`

**Purpose:** run Lighthouse at site scale.  
**Activity/license:** active in 2026; MIT.  
**Strengths:** fast regression triage across URL classes.  
**Weaknesses:** large numbers of lab scores can encourage false precision.  
**Operational concern:** control crawl concurrency and sample by template/traffic class.  
**Recommended use:** regression discovery, not a ranking dashboard.

## jekyll/jekyll-seo-tag — `SPECIALIZED`

**Purpose:** metadata/JSON-LD/Open Graph support for Jekyll.  
**Activity/license:** maintained in 2026; MIT.  
**Strengths:** stable, narrow static-site integration.  
**Weakness:** cannot substitute for architecture/content/crawl decisions.  
**Recommended use:** Jekyll sites followed by rendered-output validation.

## spatie/laravel-sitemap — `SPECIALIZED`

**Purpose:** Laravel sitemap creation/crawling.  
**Activity/license:** active in 2026; MIT.  
**Strengths:** mature framework integration.  
**Weakness:** sitemap generation does not decide indexability or canonical quality.  
**Operational concern:** filter parameters/internal search/private/duplicate URLs before output.  
**Recommended use:** controlled sitemap generation.

## spatie/schema-org — `SPECIALIZED`

**Purpose:** PHP Schema.org fluent builder / JSON-LD generator.  
**Activity/license:** active in 2026; MIT.  
**Strengths:** broad vocabulary implementation.  
**Critical caveat:** Schema.org vocabulary is broader than Google rich-result support. Valid Schema.org does not imply a Google Search feature.  
**Recommended use:** semantic implementation after selecting accurate visible entities and engine-supported requirements when rich results are desired.

## sethblack/python-seo-analyzer — `USEFUL`

**Purpose:** lightweight site structure/technical analysis.  
**Activity:** recent 2026 push; unarchived.  
**License caution:** GitHub metadata exposes Other/NOASSERTION.  
**Strengths:** simple supplementary crawl checks.  
**Weaknesses:** hardcoded heuristics/word-count warnings can age and should not define SEO success.  
**Recommended use:** secondary audit signal, never sole production crawler or ranking diagnosis.

## karust/openserp — `SPECIALIZED`

**Purpose:** self-hosted browser-rendered SERP API across multiple engines.  
**Activity/license:** active 2026; MIT.  
**Strengths:** controlled research and measurement infrastructure.  
**Weaknesses:** search markup, anti-bot behavior, localization and provider behavior change frequently.  
**Security/operational concerns:** protect proxy credentials; control concurrency; comply with applicable provider terms and law.  
**Recommended use:** research/monitoring where the operator accepts collection/compliance maintenance burden.  
**Evidence caution:** results remain date/location/device dependent.

## puneetindersingh/open-seo-crawler — `EXPERIMENTAL`

**Purpose:** self-hosted technical SEO crawler.  
**Activity/license:** created 2026-04-23; active push 2026-08-04; MIT.  
**Strengths:** current development, CMS-aware positioning, exports.  
**Weaknesses:** young project with limited long-term production history.  
**Operational concern:** first run on staging/small sample; verify concurrency/resource use and findings with a second source/logs.  
**Recommended use:** exploratory/secondary crawler until production maturity is demonstrated.

## spronta/crawlie — `EXPERIMENTAL`

**Purpose:** Rust technical SEO/GEO crawler for humans/agents.  
**Activity:** created 2026-06-18; recent 2026 development; unarchived.  
**License caution:** GitHub metadata exposes Other/NOASSERTION.  
**Strengths:** modern crawler/agent focus.  
**Weaknesses:** extremely young; “GEO” positioning must not be treated as proof of provider-specific citation optimization.  
**Recommended use:** test/secondary crawler only until maturity, licensing and edge cases are better established.

## nobodyscode/ai-crawlers — `EXPERIMENTAL`

**Purpose:** machine-readable list of AI crawler user agents and robots examples.  
**Activity:** created/pushed 2026-07-16; repository is minimal; no license exposed.  
**Strength:** useful discovery lead.  
**Weakness:** very new, tiny, no independent authority and no guarantee that entries remain current.  
**Operational risk:** a stale/mistyped bot token can accidentally block intended search/retrieval traffic.  
**Recommended use:** inventory lead **only**; verify every crawler/token/IP/control against the provider’s current first-party documentation before modifying robots/WAF.

---

# Curated resource catalogues

## bmpi-dev/awesome-seo — `USEFUL`

**Activity/license:** active push 2026-08-23; MIT; unarchived.  
**Purpose:** broad SEO resource discovery.  
**Strengths:** wide source/tool/community map.  
**Weaknesses:** mixed-quality ecosystem and material that can include aggressive/black-hat discussions.  
**Recommended use:** discovery only; follow each claim to primary evidence.

## serpapi/awesome-seo-tools — `USEFUL`

**Activity:** unarchived; last observed code push 2026-02-24. No license exposed by GitHub.  
**Purpose:** SEO tool catalogue.  
**Weakness:** inclusion is not endorsement and does not validate each tool’s claims/security/maintenance.  
**Recommended use:** tool discovery.

## teles/awesome-seo — `SPECIALIZED`

**Purpose:** general SEO resource catalogue.  
**Use:** discovery/history.  
**Caution:** re-check freshness and primary evidence before adopting advice.

## marcobiedermann/search-engine-optimization — `USEFUL`

**Purpose:** SEO checklist/reference implementation.  
**Use:** checklist inspiration.  
**Conflict rule:** current Google/Bing/provider documentation wins.

## johnmurch/awesome-seo-scripts — `USEFUL`

**Purpose:** SEO automation/script discovery.  
**Security concern:** inspect code/dependencies/credentials, outbound network access and rate limits before execution.

## guptadeepak/awesome-programmatic-seo — `USEFUL`

**Purpose:** programmatic SEO resources.  
**Critical official boundary:** scale is not a quality exemption; Google’s scaled-content-abuse policy applies regardless of whether pages are generated with AI, scripts or humans.  
**Recommended use:** ideas/data architecture, filtered through `docs/programmatic-seo.md` quality gates.

---

# AI / GEO catalogues

## amplifying-ai/awesome-generative-engine-optimization — `USEFUL`

**Activity:** unarchived; last observed push 2026-04-14; no license exposed by GitHub.  
**Purpose:** GEO research/guides/tools discovery.  
**Strength:** centralizes a fast-moving literature/tool space.  
**Weakness:** papers, vendor content and anecdotes have different evidentiary weight.  
**Recommended use:** discovery; evaluate experimental methodology and provider-specific documentation independently.

## best-of-ai/awesome-ai-seo — `USEFUL`

**Activity/license:** active 2026; MIT; unarchived.  
**Purpose:** AI marketing/SEO tool and resource catalogue.  
**Weakness:** fast-moving category with marketing-driven claims.  
**Recommended use:** discovery only; do not infer citation/ranking benefit from tool inclusion.

---

# Legacy / archived tools

## GoogleChrome/rendertron — `STALE`

**Purpose:** Headless Chrome dynamic-rendering solution.  
**Archived:** yes.  
**Last push:** 2022-10-06.  
**License:** Apache-2.0.  
**Why stale:** Google now describes dynamic rendering as a workaround, not a recommended long-term solution. Prefer server-side/static rendering or reliable client rendering where appropriate and test what crawlers/users actually receive.

## eyecatchup/SEOstats — `STALE`

**Purpose:** historic PHP SEO metrics/API aggregation.  
**Archived:** yes.  
**Last push:** 2022-06-15.  
**License:** MIT.  
**Risk:** third-party metrics/endpoints age rapidly; do not use as current evidence.

## nuxt/vue-meta — `STALE`

**Purpose:** legacy Vue metadata management with SSR support.  
**Archived:** yes.  
**Last push observed:** 2025-09-25.  
**License metadata:** Other/NOASSERTION.  
**Recommended use:** existing legacy projects only; use current Nuxt/framework-native approaches for new projects.

---

# Official-document conflict rules discovered during validation

1. **Lighthouse/Web Vitals:** useful measurement ≠ Google ranking score.
2. **Sitemap generators:** a generated sitemap entry ≠ indexability/canonical/rank; Bing ignores sitemap `changefreq` and `priority`.
3. **Schema builders:** Schema.org validity ≠ Google rich-result eligibility or ranking.
4. **AI/GEO modules/catalogues:** “AEO/GEO optimization” claims require provider/measurement evidence; no universal special AI schema or content pattern is established.
5. **Dynamic rendering:** Rendertron/dynamic rendering is legacy workaround guidance, not current default architecture.
6. **SERP scrapers/rank trackers:** observed result ≠ universal rank; country/device/time/context must be captured.
7. **Crawler lists:** provider-first bot documentation wins over community user-agent lists.
8. **Plugin/editor scores:** Yoast/Rank Math-style scores are not search-engine ranking scores.

# Production selection checklist

Before adopting any repository:

1. re-check archive status and latest meaningful release/commit;
2. inspect the real license file and redistribution obligations, not only GitHub metadata;
3. review dependency/security posture and network/credential access;
4. test on staging/sampled URLs;
5. inspect rendered output and HTTP behavior;
6. compare search-related claims with `SOURCES.md` first-party entries;
7. capture before/after measurement and rollback path;
8. control crawler/rank-tracker rate limits and provider compliance;
9. never make destructive robots/index/canonical changes from tool defaults alone;
10. re-evaluate the tool periodically because framework/search APIs change.

# Final catalogue verdict

**PASS for baseline open-source research:** the required core, framework, crawler, SERP, AI/GEO catalogue and legacy examples have been individually classified and key metadata/risks documented. This catalogue remains a maintained implementation reference; it deliberately does not turn repository popularity or README claims into ranking evidence.
