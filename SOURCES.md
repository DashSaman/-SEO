# SOURCES.md — Research Evidence Ledger

**Last updated:** 2026-08-26  
**Rule:** A source being listed does not mean every statement on it is universally applicable. Scope, date and evidence class matter.

## Status legend

- `VERIFIED` — reviewed directly; ready for synthesis within documented scope.
- `PARTIAL` — reviewed but additional linked documentation/edge cases remain.
- `DISCOVERED` — found but not yet individually validated.
- `SUPERSEDED` — useful historical source replaced by newer guidance.
- `CONFLICT` — conflicts with another source; requires explicit resolution.
- `BACKLOG` — intentionally queued.

## Evidence classes

- `OFFICIAL` — first-party search engine / AI provider.
- `STANDARD` — protocol/standards owner.
- `MEASURED` — observed SERP/tool data.
- `PRACTITIONER` — established third-party analysis.
- `COMMUNITY` — GitHub/community tooling or compilation.

---

## Google Search / Google crawling

| ID | Status | Class | Source | Reviewed | Key scope / takeaway |
|---|---|---|---|---|---|
| GGL-ESS-001 | VERIFIED | OFFICIAL | [Google Search Essentials](https://developers.google.com/search/docs/essentials) | 2026-08-26 | Technical eligibility, spam policies and baseline best practices; compliance does not guarantee crawl/index/rank. |
| GGL-SEO-002 | VERIFIED | OFFICIAL | [SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) | 2026-08-26 | Search-friendly fundamentals, useful descriptive content/site organization; no secret #1 formula. |
| GGL-CONTENT-003 | VERIFIED | OFFICIAL | [Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | 2026-08-26 | People-first evaluation; E-E-A-T is a conceptual quality framework with trust emphasized, not a single numeric ranking factor. |
| GGL-DEV-004 | VERIFIED | OFFICIAL | [Search developer documentation](https://developers.google.com/search/docs) | 2026-08-26 | Entry point for crawl/index/render/structured-data/search appearance guidance. |
| GGL-AI-005 | VERIFIED | OFFICIAL | [Optimizing for generative AI features on Google Search](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) | 2026-08-26 | 2026 guidance: foundational SEO remains relevant; Google Search does not require llms.txt, special AI markup, artificial chunking, AI-only rewrites or inauthentic mentions. |
| GGL-AI-006 | VERIFIED | OFFICIAL | [New resource for optimizing for generative AI in Google Search](https://developers.google.com/search/blog/2026/05/a-new-resource-for-optimizing) | 2026-08-26 | Official May 15, 2026 announcement emphasizing unique/non-commodity content, media/local/shopping considerations and AEO/GEO mythbusting. |
| GGL-CANON-007 | VERIFIED | OFFICIAL | [Canonicalization documentation](https://developers.google.com/search/docs/crawling-indexing/canonicalization) | 2026-08-26 | Canonical selection uses multiple signals; redirects, rel=canonical and sitemap signals can align; canonical is not merely a guaranteed command. |
| GGL-UPDATES-008 | VERIFIED | OFFICIAL | [Google Search documentation updates](https://developers.google.com/search/updates) | 2026-08-26 | Current change log used as freshness gate; includes 2026 generative-AI, rich-result and crawler/documentation changes. |
| GGL-CRAWL-009 | VERIFIED | OFFICIAL | [Google crawling infrastructure](https://developers.google.com/crawling) | 2026-08-26 | Distinguishes Googlebot/Search and other Google product crawlers/tokens. |
| GGL-GEXT-010 | VERIFIED | OFFICIAL | [Google common crawlers — Google-Extended](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers) | 2026-08-26 | Google-Extended is a robots product token, not its own HTTP UA string; controls specified Gemini training/grounding uses and does not affect Google Search inclusion/ranking. |
| GGL-PREF-011 | VERIFIED | OFFICIAL | [Preferred Sources](https://developers.google.com/search/docs/appearance/preferred-sources) | 2026-08-26 | 2026 publisher mechanism related to user-selected preferred sources in eligible Google surfaces; not a general ranking guarantee. |
| GGL-SOCIAL-012 | VERIFIED | OFFICIAL | [Analyze social and video platform content](https://developers.google.com/search/docs/monitor-debug/analyze-social-video-content) | 2026-08-26 | Current Search Console guidance for eligible platform-property visibility measurement; useful for multi-surface search strategy. |
| GGL-MOVE-013 | VERIFIED | OFFICIAL | [Site moves and migrations](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes) | 2026-08-26 | URL mapping, redirects, validation and migration signaling; relevant to preserving search signals during moves. |
| GGL-CWV-014 | BACKLOG | OFFICIAL | Google Core Web Vitals/Search documentation | — | Verify current 2026 metrics/threshold wording before synthesis. |
| GGL-SD-015 | BACKLOG | OFFICIAL | Google structured data documentation | — | Review together with Schema.org; distinguish Google rich-result eligibility from schema vocabulary. |

## Bing / IndexNow

| ID | Status | Class | Source | Reviewed | Key scope / takeaway |
|---|---|---|---|---|---|
| BNG-BWT-001 | VERIFIED | OFFICIAL | [Start Using Bing Webmaster Tools to Improve Your Site Visibility](https://blogs.bing.com/webmaster/June-2025/Start-Using-Bing-Webmaster-Tools-to-Improve-Your-Site-Visibility) | 2026-08-26 | BWT tools include search performance, URL inspection, robots testing, sitemaps and IndexNow; relevant to Bing/Copilot ecosystem discovery. |
| BNG-SMAP-002 | VERIFIED | OFFICIAL | [Keeping Content Discoverable with Sitemaps in AI-Powered Search](https://blogs.bing.com/webmaster/July-2025/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search) | 2026-08-26 | Bing emphasizes sitemap + IndexNow; accurate `lastmod`; states `changefreq`/`priority` are ignored by Bing. |
| BNG-DUP-003 | VERIFIED | OFFICIAL | [Does Duplicate Content Hurt SEO and AI Search Visibility?](https://blogs.bing.com/webmaster/December-2025/Does-Duplicate-Content-Hurt-SEO-and-AI-Search-Visibility) | 2026-08-26 | Canonical/redirect/IndexNow clarity helps duplicate consolidation and can matter to AI/search selection. |
| BNG-AI-004 | PARTIAL | OFFICIAL | [Bing Webmaster Blog](https://blogs.bing.com/webmaster) | 2026-08-26 | Feb 10, 2026 blog listing indicates AI Performance public preview for AI citations; locate/fetch dedicated documentation before detailed implementation claims. |
| IDXNOW-001 | VERIFIED | STANDARD/OFFICIAL | [IndexNow documentation](https://www.indexnow.org/documentation) | 2026-08-26 | URL-change notification protocol; supports added/updated/deleted URL submission with ownership key. Notification is not a ranking guarantee. |
| IDXNOW-002 | VERIFIED | STANDARD/OFFICIAL | [IndexNow FAQ](https://www.indexnow.org/faq) | 2026-08-26 | CMS/plugin support and manual implementation boundaries; use for practical deployment notes. |

## Web standards / shared protocols

| ID | Status | Class | Source | Reviewed | Key scope / takeaway |
|---|---|---|---|---|---|
| STD-ROBOTS-001 | VERIFIED | STANDARD | [RFC 9309 — Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309.html) | 2026-08-26 | Standards-track robots protocol. Controls crawler access preferences; explicitly not access authorization/security. |
| STD-SITEMAP-002 | VERIFIED | STANDARD | [Sitemaps protocol](https://www.sitemaps.org/protocol.html) | 2026-08-26 | XML/text/feed sitemap format and limits; max 50,000 URLs per sitemap and 50MB uncompressed; sitemap index for larger sets. |
| STD-SCHEMA-003 | BACKLOG | STANDARD | [Schema.org](https://schema.org/) | — | Verify current getting-started/data-model guidance before structured-data synthesis. |

## OpenAI / ChatGPT Search

| ID | Status | Class | Source | Reviewed | Key scope / takeaway |
|---|---|---|---|---|---|
| OAI-PUB-001 | VERIFIED | OFFICIAL | [Publishers and Developers FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq) | 2026-08-26 | Public sites can be surfaced in ChatGPT search; `OAI-SearchBot` controls search crawling. Page-level noindex and crawl access are separate concerns. |
| OAI-CRAWL-002 | VERIFIED | OFFICIAL | [Guidance for allowing OpenAI web crawlers](https://help.openai.com/en/articles/20001243-advertiser-guidance-for-allowing-openai-web-crawlers) | 2026-08-26 | OpenAI crawlers respect robots controls; WAF/CDN configuration can accidentally block crawlers; official IP files exist for crawler validation. |
| OAI-TRAIN-003 | VERIFIED | OFFICIAL | [Publishers and Developers FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq) | 2026-08-26 | Search visibility control (`OAI-SearchBot`) and model-training control (`GPTBot`) should not be conflated. |

## Anthropic / Claude

| ID | Status | Class | Source | Reviewed | Key scope / takeaway |
|---|---|---|---|---|---|
| ANT-BOTS-001 | VERIFIED | OFFICIAL | [Anthropic web crawler guidance](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) | 2026-08-26 | April 7, 2026: `ClaudeBot` (model development), `Claude-User` (user-directed retrieval), `Claude-SearchBot` (search quality/indexing) have distinct roles and honor robots.txt. Blocking search/user bots may reduce relevant Claude visibility. |

## Perplexity

| ID | Status | Class | Source | Reviewed | Key scope / takeaway |
|---|---|---|---|---|---|
| PPLX-ROBOTS-001 | VERIFIED | OFFICIAL | [How does Perplexity follow robots.txt?](https://www.perplexity.ai/help-center/en/articles/10354969-how-does-perplexity-follow-robots-txt) | 2026-08-26 | Current 2026 crawler/robots behavior and content-indexing boundaries; direct retrieval and discovery behavior should be interpreted using this first-party source. |

## Yandex

| ID | Status | Class | Source | Reviewed | Key scope / takeaway |
|---|---|---|---|---|---|
| YDX-STRUCT-001 | VERIFIED | OFFICIAL | [Yandex — Site structure](https://yandex.com/support/webmaster/en/recommendations/site-structure) | 2026-08-26 | Crawlable `<a href>` navigation, logical structure, sitemaps and duplicate/technical page handling. |
| YDX-IDX-002 | VERIFIED | OFFICIAL | [Yandex — Site indexing](https://yandex.com/support/webmaster/en/recommendations/indexing) | 2026-08-26 | Yandex Webmaster/indexing fundamentals; robots/sitemap/indexability considerations. |
| YDX-DIAG-003 | VERIFIED | OFFICIAL | [Yandex Webmaster recommendations](https://www.yandex.com/support/webmaster/en/diagnosis/recommendations) | 2026-08-26 | Diagnostic recommendations around mobile, robots, sitemaps, status codes and metadata quality. |

## Naver

| ID | Status | Class | Source | Reviewed | Key scope / takeaway |
|---|---|---|---|---|---|
| NAV-SEO-001 | VERIFIED | OFFICIAL | [Naver Search Advisor — SEO basics](https://searchadvisor.naver.com/guide/seo-help) | 2026-08-26 | User-beneficial optimization; accurate unique titles/descriptions and search-friendly fundamentals. |
| NAV-ROBOTS-002 | VERIFIED | OFFICIAL | [Naver — robots.txt](https://searchadvisor.naver.com/guide/seo-basic-robots) | 2026-08-26 | Documents Naver crawler `Yeti`, root robots rules and sitemap declaration; references modern robots standards. |
| NAV-MARKUP-003 | VERIFIED | OFFICIAL | [Naver — markup structure](https://searchadvisor.naver.com/guide/markup-structure) | 2026-08-26 | Naver meta/markup guidance including Naver-specific source-description controls; keep engine-specific directives scoped to Naver. |
| NAV-FEED-004 | VERIFIED | OFFICIAL | [Naver — feed/sitemap request](https://searchadvisor.naver.com/guide/request-feed) | 2026-08-26 | Feed/sitemap submission and discovery guidance. |

## Regional / additional engines backlog

| ID | Status | Class | Source | Reviewed | Key scope / takeaway |
|---|---|---|---|---|---|
| BDU-001 | BACKLOG | OFFICIAL | Baidu official webmaster/search documentation | — | Require current first-party source; do not synthesize from stale English blog posts. |
| DGG-001 | BACKLOG | OFFICIAL | DuckDuckGo official discovery/index sources | — | Verify current dependence on partner indexes/crawler behavior before recommendations. |
| APPL-001 | BACKLOG | OFFICIAL | Applebot / Applebot-Extended official documentation | — | Verify current crawl/search/training control semantics. |

## GitHub / open-source landscape — discovered, validation pending

| ID | Status | Class | Repository | Reviewed | Intended evaluation |
|---|---|---|---|---|---|
| GH-AWESOME-001 | DISCOVERED | COMMUNITY | [bmpi-dev/awesome-seo](https://github.com/bmpi-dev/awesome-seo) | — | Curated SEO resource map; inspect freshness/sourcing. |
| GH-AWESOME-002 | DISCOVERED | COMMUNITY | [serpapi/awesome-seo-tools](https://github.com/serpapi/awesome-seo-tools) | — | SEO tool catalogue; inspect scope/maintenance. |
| GH-AWESOME-003 | DISCOVERED | COMMUNITY | [teles/awesome-seo](https://github.com/teles/awesome-seo) | — | General SEO resource catalogue. |
| GH-CHECKLIST-004 | DISCOVERED | COMMUNITY | [marcobiedermann/search-engine-optimization](https://github.com/marcobiedermann/search-engine-optimization) | — | SEO checklist/reference implementation; validate against current official docs. |
| GH-GEO-005 | DISCOVERED | COMMUNITY | [amplifying-ai/awesome-generative-engine-optimization](https://github.com/amplifying-ai/awesome-generative-engine-optimization) | — | GEO research/resources; distinguish papers/data from marketing claims. |
| GH-AISEO-006 | DISCOVERED | COMMUNITY | [best-of-ai/awesome-ai-seo](https://github.com/best-of-ai/awesome-ai-seo) | — | AI SEO tool/resource catalogue. |
| GH-SCRIPT-007 | DISCOVERED | COMMUNITY | [johnmurch/awesome-seo-scripts](https://github.com/johnmurch/awesome-seo-scripts) | — | Automation scripts; inspect maintenance/safety. |
| GH-PSEO-008 | DISCOVERED | COMMUNITY | [guptadeepak/awesome-programmatic-seo](https://github.com/guptadeepak/awesome-programmatic-seo) | — | Programmatic SEO resources; flag scaled-content/spam risks. |
| GH-CRAWL-009 | DISCOVERED | COMMUNITY | [puneetindersingh/open-seo-crawler](https://github.com/puneetindersingh/open-seo-crawler) | — | Technical crawler; evaluate feature set/activity. |
| GH-CRAWL-010 | DISCOVERED | COMMUNITY | [spronta/crawlie](https://github.com/spronta/crawlie) | — | Technical crawler; evaluate maturity/license/activity. |
| GH-AICRAWL-011 | DISCOVERED | COMMUNITY | [nobodyscode/ai-crawlers](https://github.com/nobodyscode/ai-crawlers) | 2026-08-26 | Useful machine-readable crawler catalogue, but every production bot directive must be verified against first-party provider docs. |

## Practitioner / measured SERP research queue

| ID | Status | Class | Topic | Measurement context |
|---|---|---|---|---|
| SERP-SEO-GUIDE-001 | BACKLOG | MEASURED | `seo guide` | US, current date; record top organic results + update date |
| SERP-TECH-SEO-002 | BACKLOG | MEASURED | `technical seo` | US, current date |
| SERP-LOCAL-SEO-003 | BACKLOG | MEASURED | `local seo` | US, current date |
| SERP-LINK-004 | BACKLOG | MEASURED | `link building` | US, current date; distinguish compliant earning/outreach from schemes |
| SERP-SCHEMA-005 | BACKLOG | MEASURED | `schema markup` | US, current date |
| SERP-AISEO-006 | BACKLOG | MEASURED | `generative engine optimization` / `AI SEO` | US, current date; high volatility expected |

---

## Source admission rule

Before promoting a community/practitioner statement into a reference recommendation, answer:

1. Is there a current official source that confirms or contradicts it?
2. Is it a standard, product behavior, observation, correlation or opinion?
3. Does the source provide a date/methodology?
4. Could the tactic violate a search-engine spam policy?
5. Would the advice still be valid if rankings changed tomorrow?

If these cannot be answered, keep the item `DISCOVERED`/`PARTIAL` rather than presenting it as established SEO truth.