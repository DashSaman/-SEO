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
- `RESEARCH` — peer-reviewed or preprint research with inspectable methodology.
- `PRACTITIONER` — established third-party analysis.
- `COMMUNITY` — GitHub/community tooling or compilation.

---

## Google Search / Google crawling / Search Console

| ID | Status | Class | Source | Reviewed | Key scope / takeaway |
|---|---|---|---|---|---|
| GGL-ESS-001 | VERIFIED | OFFICIAL | [Google Search Essentials](https://developers.google.com/search/docs/essentials) | 2026-08-26 | Technical eligibility, spam policies and baseline best practices; compliance does not guarantee crawl/index/rank. |
| GGL-SEO-002 | VERIFIED | OFFICIAL | [SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) | 2026-08-26 | Search-friendly fundamentals; no secret #1 formula. |
| GGL-CONTENT-003 | VERIFIED | OFFICIAL | [Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | 2026-08-26 | People-first evaluation; E-E-A-T is a conceptual quality framework and not a single numeric score. |
| GGL-DEV-004 | VERIFIED | OFFICIAL | [Search developer documentation](https://developers.google.com/search/docs) | 2026-08-26 | Current entry point for crawl/index/render/search appearance guidance. |
| GGL-AI-005 | VERIFIED | OFFICIAL | [Optimizing for generative AI features on Google Search](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) | 2026-08-26 | Foundational SEO remains applicable to AI Overviews/AI Mode; no special AI schema, `llms.txt`, artificial chunking, AI-only rewrites, or inauthentic mentions required. |
| GGL-AI-006 | VERIFIED | OFFICIAL | [New resource for optimizing for generative AI in Google Search](https://developers.google.com/search/blog/2026/05/a-new-resource-for-optimizing) | 2026-08-26 | May 15 2026 announcement and GEO/AEO myth boundaries. |
| GGL-CANON-007 | VERIFIED | OFFICIAL | [Canonicalization documentation](https://developers.google.com/search/docs/crawling-indexing/canonicalization) | 2026-08-26 | Canonical selection uses multiple signals; declarations are not an absolute guarantee. |
| GGL-UPDATES-008 | VERIFIED | OFFICIAL | [Google Search documentation updates](https://developers.google.com/search/updates) | 2026-08-26 | Freshness gate for current Search documentation and 2026 product/policy changes. |
| GGL-CRAWL-009 | VERIFIED | OFFICIAL | [Google crawling infrastructure](https://developers.google.com/crawling) | 2026-08-26 | Distinguishes Googlebot/Search from product crawlers and special-purpose fetchers. |
| GGL-GEXT-010 | VERIFIED | OFFICIAL | [Google common crawlers — Google-Extended](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers) | 2026-08-26 | Google-Extended is a robots product token; controls specified Gemini training/grounding uses and does not affect Google Search inclusion/ranking. |
| GGL-PREF-011 | VERIFIED | OFFICIAL | [Preferred Sources](https://developers.google.com/search/docs/appearance/preferred-sources) | 2026-08-26 | User preference mechanism expanded in 2026; not a general ranking guarantee. |
| GGL-SOCIAL-012 | VERIFIED | OFFICIAL | [Analyze social and video platform content](https://developers.google.com/search/docs/monitor-debug/analyze-social-video-content) | 2026-08-26 | Current Search Console guidance for eligible platform-property visibility. |
| GGL-MOVE-013 | VERIFIED | OFFICIAL | [Site moves and migrations](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes) | 2026-08-26 | Mapping, permanent redirects, validation and migration signaling; migrations can take weeks or longer. |
| GGL-CWV-014 | VERIFIED | OFFICIAL | [Core Web Vitals and Search](https://developers.google.com/search/docs/appearance/core-web-vitals) + [Page experience](https://developers.google.com/search/docs/appearance/page-experience) | 2026-08-26 | Good CWV targets: LCP ≤2.5s, INP <200ms, CLS <0.1. CWV/page experience matter, but perfect scores do not guarantee rankings. |
| GGL-SD-015 | VERIFIED | OFFICIAL | [Structured data intro](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) + [policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) | 2026-08-26 | JSON-LD recommended; valid markup can create eligibility, not guaranteed rich results or rank. |
| GGL-JS-016 | VERIFIED | OFFICIAL | [JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics) | 2026-08-26 | Google processes crawl/render/index with evergreen Chromium; rendering and crawlable links remain implementation concerns. |
| GGL-CBUD-017 | VERIFIED | OFFICIAL | [Crawl budget management](https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget) | 2026-08-26 | Primarily relevant to very large/rapidly changing sites; capacity and demand constrain crawling; duplicate/low-value URL space wastes capacity. |
| GGL-SPAM-018 | VERIFIED | OFFICIAL | [Spam policies for Google web search](https://developers.google.com/search/docs/essentials/spam-policies) | 2026-08-26 | Covers link spam, scaled content abuse, expired-domain abuse, site-reputation abuse and other manipulative practices; policies also apply to generative AI responses. |
| GGL-DISAVOW-019 | VERIFIED | OFFICIAL | [Disavow links to your site](https://support.google.com/webmasters/answer/2648487) | 2026-08-26 | Advanced remediation tool; not a routine “toxic backlink cleanup” requirement. |
| GGL-AICTRL-020 | VERIFIED | OFFICIAL | [Search generative AI control](https://support.google.com/webmasters/answer/16908024) | 2026-08-26 | Rollout feature to include/exclude covered Google generative Search surfaces; exclusion does not affect ordinary Search ranking/inclusion and is separate from model-training controls. |
| GGL-AIREPORT-021 | VERIFIED | OFFICIAL | [Generative AI performance report (Search)](https://support.google.com/webmasters/answer/16984139) | 2026-08-26 | Subset rollout reporting for AI Overviews and AI Mode with Pages/Countries/Dates/Devices and canonical attribution. |
| GGL-AICOUNT-022 | VERIFIED | OFFICIAL | [Search Console performance counting](https://support.google.com/webmasters/answer/7042828) | 2026-08-26 | AI Mode and AI Overview impression/click/position counting rules; follow-up in AI Mode is a new query. |
| GGL-ANOM-023 | VERIFIED | OFFICIAL | [Search Console data anomalies](https://support.google.com/webmasters/answer/6211453) | 2026-08-26 | Includes Aug 13–17 2026 generative-AI impression logging error; measurement anomalies must be annotated before causal interpretation. |
| GGL-LOCAL-024 | VERIFIED | OFFICIAL | [Tips to improve local ranking on Google](https://support.google.com/business/answer/7091?hl=en) | 2026-08-26 | Local results are primarily based on relevance, distance and prominence; no way to pay/request a higher local ranking. |
| GGL-INTL-025 | VERIFIED | OFFICIAL | [International and multilingual sites](https://developers.google.com/search/docs/specialty/international) | 2026-08-26 | Distinct locale URLs and visible-language content are foundational; language is not inferred from `hreflang` or HTML `lang` alone. |
| GGL-HREF-026 | VERIFIED | OFFICIAL | [Localized versions](https://developers.google.com/search/docs/specialty/international/localized-versions) | 2026-08-26 | `hreflang` relationship rules and reciprocal locale annotations. |
| GGL-ECOM-027 | VERIFIED | OFFICIAL | [Ecommerce SEO documentation](https://developers.google.com/search/docs/specialty/ecommerce) | 2026-08-26 | Product/category architecture, structured data, Merchant Center and discovery considerations. |
| GGL-PRODUCT-028 | VERIFIED | OFFICIAL | [Product structured data](https://developers.google.com/search/docs/appearance/structured-data/product) | 2026-08-26 | Product markup supports eligible search experiences; merchant feeds can complement on-page markup. |
| GGL-IMAGE-029 | VERIFIED | OFFICIAL | [Google Images SEO](https://developers.google.com/search/docs/appearance/google-images) | 2026-08-26 | Context, crawlability, descriptive alt/text and image quality/performance considerations. |
| GGL-VIDEO-030 | VERIFIED | OFFICIAL | [Video SEO](https://developers.google.com/search/docs/appearance/video) | 2026-08-26 | Dedicated watch pages, crawlable video assets, metadata and structured data improve eligibility/discovery. |

## Bing / Microsoft / IndexNow

| ID | Status | Class | Source | Reviewed | Key scope / takeaway |
|---|---|---|---|---|---|
| BNG-BWT-001 | VERIFIED | OFFICIAL | [Bing Webmaster Tools overview](https://blogs.bing.com/webmaster/June-2025/Start-Using-Bing-Webmaster-Tools-to-Improve-Your-Site-Visibility) | 2026-08-26 | Search performance, URL inspection, robots testing, sitemaps and IndexNow. |
| BNG-SMAP-002 | VERIFIED | OFFICIAL | [Sitemaps in AI-powered Search](https://blogs.bing.com/webmaster/July-2025/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search) | 2026-08-26 | Accurate `lastmod` useful; Bing states `changefreq` and `priority` are ignored. |
| BNG-DUP-003 | VERIFIED | OFFICIAL | [Duplicate content and AI Search visibility](https://blogs.bing.com/webmaster/December-2025/Does-Duplicate-Content-Hurt-SEO-and-AI-Search-Visibility) | 2026-08-26 | Canonical/redirect/IndexNow clarity helps consolidation and selection. |
| BNG-AI-004 | VERIFIED | OFFICIAL | [AI Performance help](https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c) + [Feb 2026 announcement](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview) | 2026-08-26 | Reports citations, cited pages, grounding queries and trends across Microsoft Copilot/Bing AI surfaces. Citation counts are not rankings, authority, importance, traffic or causality. |
| IDXNOW-001 | VERIFIED | STANDARD/OFFICIAL | [IndexNow documentation](https://www.indexnow.org/documentation) | 2026-08-26 | URL-change notification protocol; notification does not guarantee crawl/index/rank. |
| IDXNOW-002 | VERIFIED | STANDARD/OFFICIAL | [IndexNow FAQ](https://www.indexnow.org/faq) | 2026-08-26 | CMS/plugin and manual implementation boundaries. |

## Web standards / shared protocols

| ID | Status | Class | Source | Reviewed | Key scope / takeaway |
|---|---|---|---|---|---|
| STD-ROBOTS-001 | VERIFIED | STANDARD | [RFC 9309 — Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309.html) | 2026-08-26 | Crawler-access protocol; not authorization/security. |
| STD-SITEMAP-002 | VERIFIED | STANDARD | [Sitemaps protocol](https://www.sitemaps.org/protocol.html) | 2026-08-26 | Max 50,000 URLs / 50MB uncompressed per sitemap; sitemap indexes for larger sets. |
| STD-SCHEMA-003 | VERIFIED | STANDARD | [Schema.org getting started](https://schema.org/docs/gs.html) | 2026-08-26 | Vocabulary/data model source; search-engine feature eligibility is engine-specific and should not be inferred from vocabulary existence alone. |

## OpenAI / ChatGPT Search

| ID | Status | Class | Source | Reviewed | Key scope / takeaway |
|---|---|---|---|---|---|
| OAI-PUB-001 | VERIFIED | OFFICIAL | [Publishers and Developers FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq) | 2026-08-26 | Public sites can appear in ChatGPT search; allow `OAI-SearchBot` for search crawling; referrals include `utm_source=chatgpt.com`. |
| OAI-CRAWL-002 | VERIFIED | OFFICIAL | [Guidance for allowing OpenAI web crawlers](https://help.openai.com/en/articles/20001243-advertiser-guidance-for-allowing-openai-web-crawlers) | 2026-08-26 | Robots respected; WAF/CDN can accidentally block; official crawler IP files support validation. |
| OAI-TRAIN-003 | VERIFIED | OFFICIAL | [Publishers and Developers FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq) | 2026-08-26 | `OAI-SearchBot` search control and `GPTBot` model-training control are distinct. |

## Anthropic / Claude

| ID | Status | Class | Source | Reviewed | Key scope / takeaway |
|---|---|---|---|---|---|
| ANT-BOTS-001 | VERIFIED | OFFICIAL | [Anthropic web crawler guidance](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) | 2026-08-26 | `ClaudeBot` (model development), `Claude-User` (user retrieval), `Claude-SearchBot` (search quality/indexing) are distinct and honor robots. |

## Perplexity

| ID | Status | Class | Source | Reviewed | Key scope / takeaway |
|---|---|---|---|---|---|
| PPLX-ROBOTS-001 | VERIFIED | OFFICIAL | [How Perplexity follows robots.txt](https://www.perplexity.ai/help-center/en/articles/10354969-how-does-perplexity-follow-robots-txt) | 2026-08-26 | Robots controls respected within documented boundaries; PerplexityBot is described separately from foundation-model pretraining. |

## Yandex

| ID | Status | Class | Source | Reviewed | Key scope / takeaway |
|---|---|---|---|---|---|
| YDX-STRUCT-001 | VERIFIED | OFFICIAL | [Yandex — Site structure](https://yandex.com/support/webmaster/en/recommendations/site-structure) | 2026-08-26 | Crawlable links, logical structure, sitemaps and duplicate handling. |
| YDX-IDX-002 | VERIFIED | OFFICIAL | [Yandex — Site indexing](https://yandex.com/support/webmaster/en/recommendations/indexing) | 2026-08-26 | Indexing, robots, sitemap and indexability fundamentals. |
| YDX-DIAG-003 | VERIFIED | OFFICIAL | [Yandex Webmaster recommendations](https://www.yandex.com/support/webmaster/en/diagnosis/recommendations) | 2026-08-26 | Diagnostic recommendations around mobile, robots, sitemaps, statuses and metadata. |

## Naver

| ID | Status | Class | Source | Reviewed | Key scope / takeaway |
|---|---|---|---|---|---|
| NAV-SEO-001 | VERIFIED | OFFICIAL | [Naver Search Advisor — SEO basics](https://searchadvisor.naver.com/guide/seo-help) | 2026-08-26 | User-beneficial optimization and accurate unique metadata. |
| NAV-ROBOTS-002 | VERIFIED | OFFICIAL | [Naver — robots.txt](https://searchadvisor.naver.com/guide/seo-basic-robots) | 2026-08-26 | Documents crawler `Yeti`, root robots rules and sitemap declaration. |
| NAV-MARKUP-003 | VERIFIED | OFFICIAL | [Naver — markup structure](https://searchadvisor.naver.com/guide/markup-structure) | 2026-08-26 | Meta/markup guidance; keep Naver-specific directives scoped to Naver. |
| NAV-FEED-004 | VERIFIED | OFFICIAL | [Naver — feed/sitemap request](https://searchadvisor.naver.com/guide/request-feed) | 2026-08-26 | Feed/sitemap submission and discovery guidance. |

## Baidu

| ID | Status | Class | Source | Reviewed | Key scope / takeaway |
|---|---|---|---|---|---|
| BDU-001 | VERIFIED | OFFICIAL | [Baidu Search Resource Platform](https://ziyuan.baidu.com/doc/index) | 2026-08-26 | Current first-party hub for verification, crawl/index diagnostics, submissions, dead links, migrations and search traffic. |
| BDU-SMAP-002 | VERIFIED | OFFICIAL | [Baidu sitemap guidance](https://ziyuan.baidu.com/college/articleinfo?id=267) | 2026-08-26 | Submission assists discovery but does not guarantee selection/indexing. |

## DuckDuckGo

| ID | Status | Class | Source | Reviewed | Key scope / takeaway |
|---|---|---|---|---|---|
| DGG-SRC-001 | VERIFIED | OFFICIAL | [Where DuckDuckGo results come from](https://duckduckgo.com/duckduckgo-help-pages/results/sources) | 2026-08-26 | DDG uses its own crawler/indexes and many specialized sources; traditional links/images are largely sourced from Bing. |
| DGG-AI-002 | VERIFIED | OFFICIAL | [DuckAssistBot](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot) | 2026-08-26 | Real-time crawler for AI-assisted answers/citations; robots opt-out does not affect ordinary organic rankings; stated not used to train AI models. |
| DGG-BOT-003 | VERIFIED | OFFICIAL | [DuckDuckBot](https://duckduckgo.com/duckduckgo-help-pages/results/duckduckbot) | 2026-08-26 | First-party crawler identity and robots behavior. |

## Apple Search / Applebot

| ID | Status | Class | Source | Reviewed | Key scope / takeaway |
|---|---|---|---|---|---|
| APPL-001 | VERIFIED | OFFICIAL | [About Applebot](https://support.apple.com/119829) | 2026-08-26 | Applebot powers search technology in Spotlight, Siri and Safari; supports robots/meta controls and JavaScript rendering. |
| APPL-EXT-002 | VERIFIED | OFFICIAL | [About Applebot](https://support.apple.com/119829) | 2026-08-26 | Applebot-Extended controls specified model-training use and does not itself crawl; blocking it does not remove search discoverability. |

## GitHub / open-source landscape

| ID | Status | Class | Repository | Reviewed | Intended evaluation |
|---|---|---|---|---|---|
| GH-AWESOME-001 | PARTIAL | COMMUNITY | [bmpi-dev/awesome-seo](https://github.com/bmpi-dev/awesome-seo) | 2026-08-26 | Curated catalogue; includes material of mixed quality including black-hat/community resources; never an authority source. |
| GH-AWESOME-002 | PARTIAL | COMMUNITY | [serpapi/awesome-seo-tools](https://github.com/serpapi/awesome-seo-tools) | 2026-08-26 | Broad tooling catalogue; useful discovery source, not evidence of ranking factors. |
| GH-AWESOME-003 | DISCOVERED | COMMUNITY | [teles/awesome-seo](https://github.com/teles/awesome-seo) | — | General SEO resource catalogue; activity/freshness review pending. |
| GH-CHECKLIST-004 | DISCOVERED | COMMUNITY | [marcobiedermann/search-engine-optimization](https://github.com/marcobiedermann/search-engine-optimization) | — | Checklist/reference; current official-doc conflict audit pending. |
| GH-GEO-005 | DISCOVERED | COMMUNITY | [amplifying-ai/awesome-generative-engine-optimization](https://github.com/amplifying-ai/awesome-generative-engine-optimization) | — | GEO research/resources; papers must be separated from marketing claims. |
| GH-AISEO-006 | DISCOVERED | COMMUNITY | [best-of-ai/awesome-ai-seo](https://github.com/best-of-ai/awesome-ai-seo) | — | AI SEO catalogue; validation pending. |
| GH-SCRIPT-007 | DISCOVERED | COMMUNITY | [johnmurch/awesome-seo-scripts](https://github.com/johnmurch/awesome-seo-scripts) | — | Automation scripts; maintenance/security review pending. |
| GH-PSEO-008 | DISCOVERED | COMMUNITY | [guptadeepak/awesome-programmatic-seo](https://github.com/guptadeepak/awesome-programmatic-seo) | — | Programmatic SEO resources; scaled-content boundaries must be applied. |
| GH-CRAWL-009 | DISCOVERED | COMMUNITY | [puneetindersingh/open-seo-crawler](https://github.com/puneetindersingh/open-seo-crawler) | — | Crawler feature/activity/license validation pending. |
| GH-CRAWL-010 | DISCOVERED | COMMUNITY | [spronta/crawlie](https://github.com/spronta/crawlie) | — | Crawler maturity/license/activity validation pending. |
| GH-AICRAWL-011 | PARTIAL | COMMUNITY | [nobodyscode/ai-crawlers](https://github.com/nobodyscode/ai-crawlers) | 2026-08-26 | Useful crawler catalogue; production directives require provider-first verification. |
| GH-LHOUSE-012 | VERIFIED | COMMUNITY/VENDOR | [GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse) | 2026-08-26 | Active Lighthouse implementation/tooling; performance/accessibility/SEO audits are diagnostics, not ranking scores. |
| GH-WVITALS-013 | VERIFIED | COMMUNITY/VENDOR | [GoogleChrome/web-vitals](https://github.com/GoogleChrome/web-vitals) | 2026-08-26 | Active field-measurement library for web-vitals metrics. |
| GH-ADV-014 | VERIFIED | COMMUNITY | [eliasdabbas/advertools](https://github.com/eliasdabbas/advertools) | 2026-08-26 | Active Python marketing/SEO toolkit: crawling, robots, sitemaps and SERP-data analysis. |
| GH-SERPBEAR-015 | PARTIAL | COMMUNITY | [towfiqi/serpbear](https://github.com/towfiqi/serpbear) | 2026-08-26 | Open-source rank tracker with GSC/API options; provider integrations require current compatibility checks. |
| GH-YOAST-016 | VERIFIED | COMMUNITY/VENDOR | [Yoast/wordpress-seo](https://github.com/Yoast/wordpress-seo) | 2026-08-26 | Active WordPress SEO plugin source/dev repository; plugin scores are not Google ranking scores. |
| GH-NEXTSMAP-017 | VERIFIED | COMMUNITY | [iamvishnusankar/next-sitemap](https://github.com/iamvishnusankar/next-sitemap) | 2026-08-26 | Next.js sitemap/robots generation; note that emitted `changefreq`/`priority` are ignored by Bing. |
| GH-NEXTSEO-018 | PARTIAL | COMMUNITY | [garmeeh/next-seo](https://github.com/garmeeh/next-seo) | 2026-08-26 | Next.js structured-data helpers; implementation utility, not ranking authority. |
| GH-NUXTSEO-019 | PARTIAL | COMMUNITY | [harlan-zw/nuxt-seo](https://github.com/harlan-zw/nuxt-seo) | 2026-08-26 | Nuxt robots/sitemap/schema/OG/link ecosystem; marketing/AEO claims require official-source verification. |
| GH-UNLIGHT-020 | DISCOVERED | COMMUNITY | [harlan-zw/unlighthouse](https://github.com/harlan-zw/unlighthouse) | — | Site-scale Lighthouse tooling; deeper maintenance/license review pending. |
| GH-PYSEO-021 | DISCOVERED | COMMUNITY | [sethblack/python-seo-analyzer](https://github.com/sethblack/python-seo-analyzer) | — | On-site analyzer; freshness/limitations review pending. |
| GH-JEKYLL-022 | DISCOVERED | COMMUNITY | [jekyll/jekyll-seo-tag](https://github.com/jekyll/jekyll-seo-tag) | — | Jekyll metadata helper; validation pending. |
| GH-LARAVELSM-023 | DISCOVERED | COMMUNITY | [spatie/laravel-sitemap](https://github.com/spatie/laravel-sitemap) | — | Laravel sitemap generator; validation pending. |
| GH-SPATIESCH-024 | DISCOVERED | COMMUNITY | [spatie/schema-org](https://github.com/spatie/schema-org) | — | Schema.org PHP builder; vocabulary support ≠ rich-result eligibility. |
| GH-OPENSERP-025 | DISCOVERED | COMMUNITY | [karust/openserp](https://github.com/karust/openserp) | — | SERP collection tooling; operational/legal/provider risks review pending. |
| GH-RENDERTRON-026 | SUPERSEDED | COMMUNITY/VENDOR | [GoogleChrome/rendertron](https://github.com/GoogleChrome/rendertron) | 2026-08-26 | Legacy dynamic-rendering solution; should not be treated as current default JS SEO architecture. |
| GH-SEOSTATS-027 | SUPERSEDED | COMMUNITY | [eyecatchup/SEOstats](https://github.com/eyecatchup/SEOstats) | 2026-08-26 | Archived/legacy SEO metrics library. |
| GH-VUEMETA-028 | SUPERSEDED | COMMUNITY | [nuxt/vue-meta](https://github.com/nuxt/vue-meta) | 2026-08-26 | Legacy ecosystem component; framework-native/current Nuxt SEO paths preferred. |

## Research / practitioner evidence

| ID | Status | Class | Source | Reviewed | Key scope / takeaway |
|---|---|---|---|---|---|
| RES-GEO-001 | VERIFIED | RESEARCH | [Optimizing Visibility in Generative Engines: A Critical Survey of GEO (2023–2026)](https://arxiv.org/abs/2607.14035) | 2026-08-26 | GEO evidence is heterogeneous; fixed-context citation gains do not prove organic discovery or cross-platform causal ranking effects. |
| PRAC-BACKLINKO-001 | PARTIAL | PRACTITIONER | [Backlinko Technical SEO Guide](https://backlinko.com/technical-seo-guide) | 2026-08-26 | Current practitioner synthesis; use only after cross-checking engine behavior against first-party docs. |
| PRAC-BACKLINKO-002 | PARTIAL | PRACTITIONER | [Backlinko Local SEO Guide](https://backlinko.com/local-seo-guide) | 2026-08-26 | Practitioner tactics and workflow; local ranking-factor claims must be scoped against Google’s official relevance/distance/prominence framing. |

## Practitioner / measured SERP research queue

| ID | Status | Class | Topic | Measurement context |
|---|---|---|---|---|
| SERP-SEO-GUIDE-001 | BACKLOG | MEASURED | `seo guide` | Current web search; record engine/date/locale and avoid universal rank claims. |
| SERP-TECH-SEO-002 | BACKLOG | MEASURED | `technical seo` | Current web search; representative SERP study. |
| SERP-LOCAL-SEO-003 | BACKLOG | MEASURED | `local seo` | Current web search; location-sensitive. |
| SERP-LINK-004 | BACKLOG | MEASURED | `link building` | Current web search; distinguish compliant earning/outreach from schemes. |
| SERP-SCHEMA-005 | BACKLOG | MEASURED | `schema markup` | Current web search; distinguish vocabulary/help pages/tool sites. |
| SERP-AISEO-006 | BACKLOG | MEASURED | `generative engine optimization` / `AI SEO` | Current web search; high volatility expected. |
| SERP-ECOM-007 | BACKLOG | MEASURED | `ecommerce seo` | Current web search. |
| SERP-INTL-008 | BACKLOG | MEASURED | `international seo` | Current web search. |

---

## Known tooling limitation

- Ahrefs SERP Overview was attempted on 2026-08-26 but the connected plan returned **Insufficient plan**. Exact Google #1/Top-10 positions must therefore not be fabricated. Representative web-search observations can be logged as observations with date/context, not universal rank truth.

## Source admission rule

Before promoting a community/practitioner statement into a reference recommendation, answer:

1. Is there a current official source that confirms or contradicts it?
2. Is it a standard, product behavior, observation, correlation or opinion?
3. Does the source provide a date/methodology?
4. Could the tactic violate a search-engine spam policy?
5. Would the advice still be valid if rankings changed tomorrow?

If these cannot be answered, keep the item `DISCOVERED`/`PARTIAL` rather than presenting it as established SEO truth.
