# SOURCES.md — Master Evidence Ledger

**Last reconciled:** 2026-08-26  
**Repository:** `DashSaman/-SEO`  
**Rule:** listing a source does not make every statement on it universally true. Scope, date, provider, evidence class and caveats control how it may be used.

## Status legend

- `VERIFIED` — directly reviewed for the stated scope.
- `PARTIAL` — reviewed, but important scope/edge cases remain outside the current baseline.
- `DISCOVERED` — found but not validated enough for synthesis.
- `SUPERSEDED` — useful historical/legacy source replaced by newer guidance or tooling.
- `CONFLICT` — meaningful unresolved evidence conflict requiring explicit documentation.
- `BACKLOG` — deliberately queued and not complete.

## Evidence classes

- `OFFICIAL` — first-party search engine / AI provider documentation.
- `STANDARD` — protocol/vocabulary/standards owner.
- `MEASURED` — dated search/tool/log/console observation.
- `RESEARCH` — peer-reviewed paper or transparent preprint with inspectable methodology.
- `PRACTITIONER` — established third-party workflow/research/case material.
- `COMMUNITY` — GitHub/community implementation or catalogue.

## Confidence

- `HIGH` — authoritative for the stated product/protocol scope.
- `MEDIUM` — useful evidence with contextual limits, volatility or third-party dependence.
- `LOW` — discovery/hypothesis only; not production guidance without verification.

> `Source date = —` means the publisher does not expose a stable publication/update date used by this ledger. `Reviewed` is the repository freshness date and is always required.

---

# Google Search / Google crawling / Search Console

| ID | Status | Class | Title | URL | Provider | Source date | Reviewed | Relevant section | Key finding | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| GGL-ESS-001 | VERIFIED | OFFICIAL | Google Search Essentials | https://developers.google.com/search/docs/essentials | Google | — | 2026-08-26 | Google foundation | Technical eligibility, spam policies and baseline best practices; compliance does not guarantee crawl/index/rank. | HIGH | Primary baseline. |
| GGL-SEO-002 | VERIFIED | OFFICIAL | SEO Starter Guide | https://developers.google.com/search/docs/fundamentals/seo-starter-guide | Google | — | 2026-08-26 | Google foundation | Search-friendly fundamentals; no secret #1 formula. | HIGH | Introductory scope, not exhaustive. |
| GGL-CONTENT-003 | VERIFIED | OFFICIAL | Creating helpful, reliable, people-first content | https://developers.google.com/search/docs/fundamentals/creating-helpful-content | Google | — | 2026-08-26 | Content quality | People-first evaluation; E-E-A-T is conceptual and trust-focused, not a single numeric score. | HIGH | Used with spam policies. |
| GGL-DEV-004 | VERIFIED | OFFICIAL | Google Search developer documentation | https://developers.google.com/search/docs | Google | — | 2026-08-26 | Google reference hub | Current entry point for crawl/index/render/search appearance documentation. | HIGH | Hub source. |
| GGL-AI-005 | VERIFIED | OFFICIAL | Optimizing for generative AI features on Google Search | https://developers.google.com/search/docs/fundamentals/ai-optimization-guide | Google | 2026 | 2026-08-26 | Google AI Search / GEO myths | Foundational SEO remains applicable; no special AI schema, llms.txt, artificial chunking, AI-only rewrites or manufactured mentions are required for Google Search generative features. | HIGH | Provider-specific to Google Search. |
| GGL-AI-006 | VERIFIED | OFFICIAL | New resource for optimizing for generative AI in Google Search | https://developers.google.com/search/blog/2026/05/a-new-resource-for-optimizing | Google | 2026-05-15 | 2026-08-26 | Google AI Search | Official launch/context for 2026 generative Search guidance. | HIGH | Blog announcement plus docs. |
| GGL-CANON-007 | VERIFIED | OFFICIAL | Canonicalization documentation | https://developers.google.com/search/docs/crawling-indexing/canonicalization | Google | updated 2026-08 | 2026-08-26 | Canonicalization | Canonical selection uses multiple signals; declarations are not an absolute command. | HIGH | Current page rechecked in final pass. |
| GGL-UPDATES-008 | VERIFIED | OFFICIAL | Google Search documentation updates | https://developers.google.com/search/updates | Google | 2026-08-20 | 2026-08-26 | Freshness gate | Tracks current documentation/product changes, including 2026 AI Search changes. | HIGH | Must be rechecked in future maintenance. |
| GGL-CRAWL-009 | VERIFIED | OFFICIAL | Google crawling infrastructure | https://developers.google.com/crawling | Google | — | 2026-08-26 | Crawling | Distinguishes Search crawlers and other Google product crawlers/tokens. | HIGH | Some crawl docs moved here from Search Central. |
| GGL-GEXT-010 | VERIFIED | OFFICIAL | Google common crawlers / Google-Extended | https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers | Google | — | 2026-08-26 | AI crawler controls | Google-Extended is a robots product token controlling specified Gemini training/grounding uses; it does not affect Google Search ranking/inclusion. | HIGH | Not a separate HTTP UA. |
| GGL-PREF-011 | VERIFIED | OFFICIAL | Preferred Sources | https://developers.google.com/search/docs/appearance/preferred-sources | Google | 2026 | 2026-08-26 | Publisher/Search surfaces | User preference mechanism expanded in 2026; not a general ranking guarantee. | HIGH | Availability/surface can evolve. |
| GGL-SOCIAL-012 | VERIFIED | OFFICIAL | Analyze social and video platform content | https://developers.google.com/search/docs/monitor-debug/analyze-social-video-content | Google | 2026 | 2026-08-26 | Multi-surface measurement | Search Console guidance for eligible social/video platform content. | HIGH | Eligibility-specific. |
| GGL-MOVE-013 | VERIFIED | OFFICIAL | Site moves and migrations | https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes | Google | updated 2026-08 | 2026-08-26 | Migration | URL mapping, redirects, Search Console and monitoring; Google recommends keeping redirects generally at least one year. | HIGH | Temporary ranking fluctuation can occur. |
| GGL-CWV-014 | VERIFIED | OFFICIAL | Core Web Vitals and Search | https://developers.google.com/search/docs/appearance/core-web-vitals | Google | — | 2026-08-26 | Performance | Good targets: LCP ≤2.5s, INP <200ms, CLS <0.1; good metrics do not guarantee rankings. | HIGH | Field experience should be measured where available. |
| GGL-PAGEEXP-015 | VERIFIED | OFFICIAL | Page experience | https://developers.google.com/search/docs/appearance/page-experience | Google | — | 2026-08-26 | Performance / UX | No single page-experience score determines ranking; useful content and overall experience remain broader than CWV. | HIGH | Prevents Lighthouse-score overclaim. |
| GGL-SD-016 | VERIFIED | OFFICIAL | Structured data introduction | https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data | Google | — | 2026-08-26 | Structured data | JSON-LD is recommended; markup enables eligibility/understanding, not guaranteed rich results/rank. | HIGH | Feature requirements are type-specific. |
| GGL-SDPOL-017 | VERIFIED | OFFICIAL | Structured data general policies | https://developers.google.com/search/docs/appearance/structured-data/sd-policies | Google | — | 2026-08-26 | Structured data policy | Markup must be truthful/visible and comply with feature policies. | HIGH | Misleading markup can lose rich-result eligibility/manual action. |
| GGL-JS-018 | VERIFIED | OFFICIAL | JavaScript SEO basics | https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics | Google | updated 2026 | 2026-08-26 | JavaScript SEO | Rendering, crawlable links, status and deterministic metadata matter; initial noindex can prevent expected JS changes. | HIGH | Used with rendered/live testing. |
| GGL-DYN-019 | VERIFIED | OFFICIAL | Dynamic rendering as a workaround | https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering | Google | — | 2026-08-26 | JavaScript SEO | Dynamic rendering is a workaround/legacy pattern, not the preferred long-term default. | HIGH | Prefer SSR/static/reliable rendering where appropriate. |
| GGL-CBUD-020 | VERIFIED | OFFICIAL | Crawl budget management | https://developers.google.com/crawling/docs/crawl-budget | Google | updated 2026 | 2026-08-26 | Crawl budget/log analysis | Primarily relevant to large/high-change sites; duplicate/low-value crawl spaces waste capacity. | HIGH | Do not over-apply to small sites. |
| GGL-ROBOTS-021 | VERIFIED | OFFICIAL | Robots meta / X-Robots-Tag specifications | https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag | Google | 2026-03-25 | 2026-08-26 | Crawl/index controls | Index/serving directives are only discoverable when crawlers can access the URL. | HIGH | `robots.txt` and `noindex` solve different problems. |
| GGL-CONTROL-022 | VERIFIED | OFFICIAL | Control content shared on Search | https://developers.google.com/search/docs/crawling-indexing/control-what-you-share | Google | 2025-12-10 | 2026-08-26 | Privacy/index controls | Private content requires real access control; noindex/robots are search controls, not authentication. | HIGH | Security precedence. |
| GGL-SPAM-023 | VERIFIED | OFFICIAL | Spam policies for Google web search | https://developers.google.com/search/docs/essentials/spam-policies | Google | — | 2026-08-26 | Links/content/reputation | Covers link spam, scaled content abuse, expired-domain abuse, site-reputation abuse and other manipulation. | HIGH | Controlling policy boundary. |
| GGL-DISAVOW-024 | VERIFIED | OFFICIAL | Disavow links to your site | https://support.google.com/webmasters/answer/2648487 | Google | — | 2026-08-26 | Backlinks | Advanced remediation tool; most sites do not need routine third-party “toxicity cleanup.” | HIGH | Use only under current necessity criteria. |
| GGL-AICTRL-025 | VERIFIED | OFFICIAL | Search generative AI control | https://support.google.com/webmasters/answer/16908024 | Google | 2026 | 2026-08-26 | Google AI controls | Include/exclude covered generative Search surfaces; separate from ordinary Search and model-training control. | HIGH | Rolling/subset availability. |
| GGL-AIREPORT-026 | VERIFIED | OFFICIAL | Generative AI performance report (Search) | https://support.google.com/webmasters/answer/16984139 | Google | 2026 | 2026-08-26 | AI measurement | AI Overviews/AI Mode reporting with page/country/date/device dimensions and canonical attribution. | HIGH | Rolling/subset availability. |
| GGL-AICOUNT-027 | VERIFIED | OFFICIAL | Search Console performance counting | https://support.google.com/webmasters/answer/7042828 | Google | — | 2026-08-26 | AI/Search measurement | Documents clicks/impressions/position treatment for AI Mode/AI Overviews. | HIGH | Follow-up in AI Mode is a new query. |
| GGL-ANOM-028 | VERIFIED | OFFICIAL | Search Console data anomalies | https://support.google.com/webmasters/answer/6211453 | Google | 2026-08 | 2026-08-26 | Measurement | Aug 13–17 2026 generative-AI impression logging anomaly must be considered in analysis. | HIGH | Use as anomaly log, not ranking source. |
| GGL-LOCAL-029 | VERIFIED | OFFICIAL | Tips to improve local ranking on Google | https://support.google.com/business/answer/7091?hl=en | Google | — | 2026-08-26 | Local SEO | Local results are primarily based on relevance, distance and prominence; ranking cannot be bought/requested. | HIGH | Distance is context-dependent. |
| GGL-INTL-030 | VERIFIED | OFFICIAL | International and multilingual sites | https://developers.google.com/search/docs/specialty/international | Google | — | 2026-08-26 | International SEO | Distinct locale URLs and visible-language content are foundational. | HIGH | Locale-adaptive redirects need caution. |
| GGL-HREF-031 | VERIFIED | OFFICIAL | Localized versions / hreflang | https://developers.google.com/search/docs/specialty/international/localized-versions | Google | — | 2026-08-26 | International SEO | Hreflang relationships/codes/reciprocity help locale targeting. | HIGH | Does not replace actual localized content. |
| GGL-MOBILE-032 | VERIFIED | OFFICIAL | Mobile-first indexing best practices | https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing | Google | — | 2026-08-26 | Mobile/rendering | Mobile version must expose equivalent critical content/metadata/resources. | HIGH | Mobile-first does not mean mobile-only. |
| GGL-ECOM-033 | VERIFIED | OFFICIAL | Ecommerce SEO documentation | https://developers.google.com/search/docs/specialty/ecommerce | Google | — | 2026-08-26 | Ecommerce | Architecture, discovery, product data and Merchant Center considerations. | HIGH | Specialty hub. |
| GGL-PRODUCT-034 | VERIFIED | OFFICIAL | Product structured data | https://developers.google.com/search/docs/appearance/structured-data/product | Google | — | 2026-08-26 | Ecommerce/schema | Product markup supports eligible product experiences; on-page facts must remain current. | HIGH | Feed can complement markup. |
| GGL-MERCHANT-035 | VERIFIED | OFFICIAL | Merchant listing structured data | https://developers.google.com/search/docs/appearance/structured-data/merchant-listing | Google | — | 2026-08-26 | Ecommerce/merchant | Merchant listing eligibility has specific product/offer requirements. | HIGH | Feature-specific. |
| GGL-IMAGE-036 | VERIFIED | OFFICIAL | Google Images SEO | https://developers.google.com/search/docs/appearance/google-images | Google | — | 2026-08-26 | Media SEO | Context, crawlability, alt text and image quality/performance support image understanding/discovery. | HIGH | No ranking guarantee from alt alone. |
| GGL-VIDEO-037 | VERIFIED | OFFICIAL | Video SEO | https://developers.google.com/search/docs/appearance/video | Google | — | 2026-08-26 | Media/video | Dedicated watch pages, crawlable video assets and metadata support video eligibility/discovery. | HIGH | Eligibility/surface-specific. |
| GGL-ARTICLE-038 | VERIFIED | OFFICIAL | Article structured data | https://developers.google.com/search/docs/appearance/structured-data/article | Google | — | 2026-08-26 | Publisher/news | Article/NewsArticle markup can clarify article metadata for eligible search experiences. | HIGH | Does not guarantee news/rich visibility. |

---

# Bing / Microsoft / IndexNow

| ID | Status | Class | Title | URL | Provider | Source date | Reviewed | Relevant section | Key finding | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BNG-BWT-001 | VERIFIED | OFFICIAL | Bing Webmaster Tools foundation | https://blogs.bing.com/webmaster/June-2025/Start-Using-Bing-Webmaster-Tools-to-Improve-Your-Site-Visibility | Microsoft/Bing | 2025-06 | 2026-08-26 | Bing foundation | BWT provides search performance, URL inspection, robots testing, sitemaps and IndexNow workflows. | HIGH | First-party blog overview. |
| BNG-SMAP-002 | VERIFIED | OFFICIAL | Sitemaps in AI-powered Search | https://blogs.bing.com/webmaster/July-2025/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search | Microsoft/Bing | 2025-07 | 2026-08-26 | Bing discovery | Accurate lastmod matters; Bing states sitemap changefreq/priority are ignored. | HIGH | Prevent fake freshness. |
| BNG-DUP-003 | VERIFIED | OFFICIAL | Duplicate content and AI Search visibility | https://blogs.bing.com/webmaster/December-2025/Does-Duplicate-Content-Hurt-SEO-and-AI-Search-Visibility | Microsoft/Bing | 2025-12 | 2026-08-26 | Bing canonical/duplicates | Canonical/redirect/IndexNow clarity helps consolidation and selection. | HIGH | Not a duplicate-content “penalty” formula. |
| BNG-AI-004 | VERIFIED | OFFICIAL | AI Performance — Bing Webmaster Tools | https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c | Microsoft/Bing | current 2026 | 2026-08-26 | Bing/Copilot AI measurement | Reports citations, cited pages, average cited pages, grounding queries, page mappings, trends and exports. | HIGH | Citation ≠ ranking/authority/traffic/causality. |
| BNG-AIPREV-005 | VERIFIED | OFFICIAL | AI Performance public preview announcement | https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview | Microsoft/Bing | 2026-02-10 | 2026-08-26 | Bing AI measurement | Establishes product context; current help page controls detailed semantics. | HIGH | Current help also documents preview Intents/Topics/Citation Share/Compare. |
| IDXNOW-001 | VERIFIED | STANDARD | IndexNow documentation | https://www.indexnow.org/documentation | IndexNow | — | 2026-08-26 | Discovery/change notification | Allows change notifications for added/updated/deleted URLs; notification is not crawl/index/rank guarantee. | HIGH | Protocol owner. |
| IDXNOW-002 | VERIFIED | STANDARD | IndexNow FAQ | https://www.indexnow.org/faq | IndexNow | — | 2026-08-26 | IndexNow implementation | CMS/plugin/manual implementation boundaries. | HIGH | Protocol support/operations. |

---

# Shared standards / protocols

| ID | Status | Class | Title | URL | Provider | Source date | Reviewed | Relevant section | Key finding | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| STD-ROBOTS-001 | VERIFIED | STANDARD | RFC 9309 — Robots Exclusion Protocol | https://www.rfc-editor.org/rfc/rfc9309.html | IETF/RFC Editor | 2022 | 2026-08-26 | Robots | Standards-track crawler-access protocol; not authorization/security. | HIGH | Protocol semantics. |
| STD-SITEMAP-002 | VERIFIED | STANDARD | Sitemaps protocol | https://www.sitemaps.org/protocol.html | Sitemaps.org | — | 2026-08-26 | Sitemaps | Maximum 50,000 URLs / 50MB uncompressed per sitemap; indexes support larger sets. | HIGH | Inclusion never guarantees indexing. |
| STD-SCHEMA-003 | VERIFIED | STANDARD | Schema.org getting started | https://schema.org/docs/gs.html | Schema.org | — | 2026-08-26 | Structured data | Vocabulary/data model is broader than any search engine’s supported rich-result features. | HIGH | Keep vocabulary vs Google feature eligibility separate. |

---

# OpenAI / ChatGPT Search

| ID | Status | Class | Title | URL | Provider | Source date | Reviewed | Relevant section | Key finding | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| OAI-PUB-001 | VERIFIED | OFFICIAL | Publishers and Developers FAQ | https://help.openai.com/en/articles/12627856-publishers-and-developers-faq | OpenAI | current 2026 | 2026-08-26 | ChatGPT Search | Public sites can appear in ChatGPT Search; OAI-SearchBot controls search crawling; referrals can include utm_source=chatgpt.com. | HIGH | Search visibility and model training are separate. |
| OAI-CRAWL-002 | VERIFIED | OFFICIAL | Guidance for allowing OpenAI web crawlers | https://help.openai.com/en/articles/20001243-advertiser-guidance-for-allowing-openai-web-crawlers | OpenAI | current 2026 | 2026-08-26 | AI crawler operations | Robots respected; WAF/CDN can accidentally block intended crawlers; official IP files support validation. | HIGH | Verify provider-first. |
| OAI-TRAIN-003 | VERIFIED | OFFICIAL | GPTBot vs OAI-SearchBot control | https://help.openai.com/en/articles/12627856-publishers-and-developers-faq | OpenAI | current 2026 | 2026-08-26 | Search vs training | OAI-SearchBot search control and GPTBot training control must not be conflated. | HIGH | Same source, distinct scoped claim. |

# Anthropic / Claude

| ID | Status | Class | Title | URL | Provider | Source date | Reviewed | Relevant section | Key finding | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ANT-BOTS-001 | VERIFIED | OFFICIAL | Anthropic web crawler guidance | https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler | Anthropic | 2026-04-07 guidance | 2026-08-26 | Claude Search/retrieval/training | ClaudeBot, Claude-User and Claude-SearchBot have separate purposes and robots behavior. | HIGH | Blocking search/user bots can reduce relevant retrieval/visibility. |

# Perplexity

| ID | Status | Class | Title | URL | Provider | Source date | Reviewed | Relevant section | Key finding | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PPLX-ROBOTS-001 | VERIFIED | OFFICIAL | How Perplexity follows robots.txt | https://www.perplexity.ai/help-center/en/articles/10354969-how-does-perplexity-follow-robots-txt | Perplexity | current 2026 | 2026-08-26 | Perplexity Search/retrieval | Documents robots behavior and crawler boundaries; PerplexityBot is not described as foundation-model pretraining. | HIGH | Blocking full-text retrieval does not necessarily erase every brief factual/domain reference. |

---

# Regional / alternative search ecosystems

| ID | Status | Class | Title | URL | Provider | Source date | Reviewed | Relevant section | Key finding | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| YDX-STRUCT-001 | VERIFIED | OFFICIAL | Yandex site structure | https://yandex.com/support/webmaster/en/recommendations/site-structure | Yandex | — | 2026-08-26 | Yandex SEO | Crawlable links, logical structure, sitemaps and duplicate handling. | HIGH | Market-specific use. |
| YDX-IDX-002 | VERIFIED | OFFICIAL | Yandex site indexing | https://yandex.com/support/webmaster/en/recommendations/indexing | Yandex | — | 2026-08-26 | Yandex indexing | Robots/sitemap/indexability fundamentals. | HIGH | Market-specific use. |
| YDX-DIAG-003 | VERIFIED | OFFICIAL | Yandex Webmaster recommendations | https://www.yandex.com/support/webmaster/en/diagnosis/recommendations | Yandex | — | 2026-08-26 | Yandex diagnostics | Mobile, robots, sitemap, status and metadata diagnostics. | HIGH | First-party. |
| NAV-SEO-001 | VERIFIED | OFFICIAL | Naver Search Advisor SEO basics | https://searchadvisor.naver.com/guide/seo-help | Naver | — | 2026-08-26 | Naver SEO | User-beneficial optimization and accurate unique metadata. | HIGH | Korean ecosystem relevance. |
| NAV-ROBOTS-002 | VERIFIED | OFFICIAL | Naver robots.txt | https://searchadvisor.naver.com/guide/seo-basic-robots | Naver | — | 2026-08-26 | Naver crawl | Documents Yeti and robots/sitemap behavior. | HIGH | Provider-specific crawler. |
| NAV-MARKUP-003 | VERIFIED | OFFICIAL | Naver markup structure | https://searchadvisor.naver.com/guide/markup-structure | Naver | — | 2026-08-26 | Naver markup | Naver metadata/markup guidance must stay scoped to Naver. | HIGH | Do not generalize directives. |
| NAV-FEED-004 | VERIFIED | OFFICIAL | Naver feed/sitemap request | https://searchadvisor.naver.com/guide/request-feed | Naver | — | 2026-08-26 | Naver discovery | Feed/sitemap submission and discovery workflow. | HIGH | Submission ≠ guaranteed ranking. |
| BDU-001 | VERIFIED | OFFICIAL | Baidu Search Resource Platform | https://ziyuan.baidu.com/doc/index | Baidu | current | 2026-08-26 | Baidu SEO | First-party hub for verification, crawl/index diagnostics, submissions, dead links, migrations and search traffic. | HIGH | Prefer over stale third-party English summaries. |
| BDU-SMAP-002 | VERIFIED | OFFICIAL | Baidu sitemap/submission guidance | https://ziyuan.baidu.com/college/articleinfo?id=267 | Baidu | — | 2026-08-26 | Baidu discovery | Submission assists discovery but does not guarantee selection/indexing. | HIGH | First-party Chinese documentation. |
| DGG-SRC-001 | VERIFIED | OFFICIAL | Where DuckDuckGo results come from | https://duckduckgo.com/duckduckgo-help-pages/results/sources | DuckDuckGo | current | 2026-08-26 | DuckDuckGo | Traditional links/images rely heavily on Bing while DDG also uses its own crawler/indexes and specialized sources. | HIGH | Avoid “DDG = only Bing” simplification. |
| DGG-AI-002 | VERIFIED | OFFICIAL | DuckAssistBot | https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot | DuckDuckGo | current | 2026-08-26 | DuckDuckGo AI | Real-time crawler for AI-assisted answers/citations; robots opt-out is separate from ordinary organic ranking. | HIGH | DDG says not used to train AI models. |
| DGG-BOT-003 | VERIFIED | OFFICIAL | DuckDuckBot | https://duckduckgo.com/duckduckgo-help-pages/results/duckduckbot | DuckDuckGo | current | 2026-08-26 | DuckDuckGo crawl | First-party crawler identity/behavior. | HIGH | Provider-specific. |
| APPL-001 | VERIFIED | OFFICIAL | About Applebot | https://support.apple.com/119829 | Apple | current | 2026-08-26 | Apple Search | Applebot powers search technology integrated with Spotlight, Siri and Safari and supports robots/meta controls. | HIGH | Can provide current context to AI outputs per Apple docs. |
| APPL-EXT-002 | VERIFIED | OFFICIAL | Applebot-Extended | https://support.apple.com/119829 | Apple | current | 2026-08-26 | Apple AI/training control | Applebot-Extended controls specified model-training use and does not itself crawl; blocking it does not remove ordinary search discoverability. | HIGH | Separate training/search controls. |

---

# GitHub / open-source implementation evidence

`Source date` below is the last meaningful code push observed through GitHub repository metadata on 2026-08-26; for static catalogues it is an activity signal, not proof that every listed resource is current. Community evidence never overrides provider documentation.

| ID | Status | Class | Title | URL | Provider | Source date | Reviewed | Relevant section | Key finding | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| GH-LHOUSE-001 | VERIFIED | COMMUNITY | GoogleChrome/lighthouse | https://github.com/GoogleChrome/lighthouse | GoogleChrome | 2026-08-26 | 2026-08-26 | Performance tooling | Active Apache-2.0 diagnostic/audit tool; Lighthouse score is not a Google ranking score. | MEDIUM | Verdict: RECOMMENDED. |
| GH-WVITALS-002 | VERIFIED | COMMUNITY | GoogleChrome/web-vitals | https://github.com/GoogleChrome/web-vitals | GoogleChrome | 2026-08-25 | 2026-08-26 | RUM/CWV | Active Apache-2.0 field-metric library. | MEDIUM | Verdict: RECOMMENDED. |
| GH-YOAST-003 | VERIFIED | COMMUNITY | Yoast/wordpress-seo | https://github.com/Yoast/wordpress-seo | Yoast | 2026-08-26 | 2026-08-26 | WordPress SEO | Highly active implementation for metadata/canonical/schema/sitemaps; plugin scores are not ranking scores. | MEDIUM | GitHub license metadata Other/NOASSERTION; inspect actual terms. Verdict: RECOMMENDED. |
| GH-ADV-004 | VERIFIED | COMMUNITY | eliasdabbas/advertools | https://github.com/eliasdabbas/advertools | Elias Dabbas | 2026-06-30 | 2026-08-26 | SEO data/crawl/log tooling | Active MIT Python toolkit for crawling, robots, sitemaps, logs and SEO data analysis. | MEDIUM | Verdict: RECOMMENDED. |
| GH-SERPBEAR-005 | VERIFIED | COMMUNITY | towfiqi/serpbear | https://github.com/towfiqi/serpbear | towfiqi | 2026-05-14 | 2026-08-26 | Rank tracking | MIT self-hosted rank tracker; provider integrations and location context require validation. | MEDIUM | Verdict: USEFUL. |
| GH-NEXTSMAP-006 | VERIFIED | COMMUNITY | iamvishnusankar/next-sitemap | https://github.com/iamvishnusankar/next-sitemap | iamvishnusankar | 2026-05-13 | 2026-08-26 | Next.js sitemap/robots | Active MIT generator; tool output does not decide indexability/canonical quality. | MEDIUM | Bing ignores changefreq/priority. Verdict: RECOMMENDED narrow. |
| GH-NEXTSEO-007 | VERIFIED | COMMUNITY | garmeeh/next-seo | https://github.com/garmeeh/next-seo | garmeeh | 2026-07-29 | 2026-08-26 | Next.js schema/metadata | MIT structured-data/helper implementation; README marketing is not search evidence. | MEDIUM | Verdict: USEFUL. |
| GH-NUXTSEO-008 | VERIFIED | COMMUNITY | harlan-zw/nuxt-seo | https://github.com/harlan-zw/nuxt-seo | harlan-zw | 2026-08-20 | 2026-08-26 | Nuxt SEO | Active MIT suite; broad AEO/GEO marketing claims require provider-first verification. | MEDIUM | Verdict: USEFUL. |
| GH-UNLIGHT-009 | VERIFIED | COMMUNITY | harlan-zw/unlighthouse | https://github.com/harlan-zw/unlighthouse | harlan-zw | 2026-08-14 | 2026-08-26 | Site-scale lab audit | Active MIT site-scale Lighthouse tooling; lab score volume can create false precision. | MEDIUM | Verdict: SPECIALIZED. |
| GH-JEKYLL-010 | VERIFIED | COMMUNITY | jekyll/jekyll-seo-tag | https://github.com/jekyll/jekyll-seo-tag | Jekyll | 2026-05-08 | 2026-08-26 | Static-site metadata | Maintained MIT helper for Jekyll metadata/JSON-LD. | MEDIUM | Verdict: SPECIALIZED. |
| GH-LARAVELSM-011 | VERIFIED | COMMUNITY | spatie/laravel-sitemap | https://github.com/spatie/laravel-sitemap | Spatie | 2026-08-07 | 2026-08-26 | Laravel sitemap | Active MIT sitemap generator; generated URLs still require intentional filtering. | MEDIUM | Verdict: SPECIALIZED. |
| GH-SPATIESCH-012 | VERIFIED | COMMUNITY | spatie/schema-org | https://github.com/spatie/schema-org | Spatie | 2026-08-07 | 2026-08-26 | Schema implementation | Active MIT Schema.org builder; vocabulary validity ≠ Google rich-result eligibility. | MEDIUM | Verdict: SPECIALIZED. |
| GH-PYSEO-013 | VERIFIED | COMMUNITY | sethblack/python-seo-analyzer | https://github.com/sethblack/python-seo-analyzer | Seth Black | 2026-07-27 | 2026-08-26 | On-site analysis | Recent lightweight analyzer; heuristic warnings should not define SEO success. | MEDIUM | GitHub license metadata Other/NOASSERTION. Verdict: USEFUL. |
| GH-OPENSERP-014 | VERIFIED | COMMUNITY | karust/openserp | https://github.com/karust/openserp | karust | 2026-07-22 | 2026-08-26 | SERP collection | Active MIT self-hosted SERP API; search markup, anti-bot, legal/provider constraints change. | MEDIUM | Verdict: SPECIALIZED. |
| GH-OPENCRAWL-015 | VERIFIED | COMMUNITY | puneetindersingh/open-seo-crawler | https://github.com/puneetindersingh/open-seo-crawler | puneetindersingh | 2026-08-04 | 2026-08-26 | Technical crawler | Young 2026 MIT crawler; useful but limited production history. | MEDIUM | Verdict: EXPERIMENTAL. |
| GH-CRAWLIE-016 | VERIFIED | COMMUNITY | spronta/crawlie | https://github.com/spronta/crawlie | spronta | 2026-07-18 | 2026-08-26 | SEO/GEO crawler | Very young crawler; GEO positioning is not citation/ranking evidence. | MEDIUM | GitHub license metadata Other/NOASSERTION. Verdict: EXPERIMENTAL. |
| GH-AICRAWL-017 | VERIFIED | COMMUNITY | nobodyscode/ai-crawlers | https://github.com/nobodyscode/ai-crawlers | nobodyscode | 2026-07-16 | 2026-08-26 | AI crawler catalogue | Minimal/no-license catalogue useful only for discovery; provider docs must validate every production directive. | MEDIUM | Verdict: EXPERIMENTAL. |
| GH-BMPI-018 | VERIFIED | COMMUNITY | bmpi-dev/awesome-seo | https://github.com/bmpi-dev/awesome-seo | bmpi-dev | 2026-08-23 | 2026-08-26 | SEO resource catalogue | Active MIT mixed-quality discovery list; includes aggressive/community material. | MEDIUM | Verdict: USEFUL discovery only. |
| GH-SERPAPI-019 | VERIFIED | COMMUNITY | serpapi/awesome-seo-tools | https://github.com/serpapi/awesome-seo-tools | SerpApi | 2026-02-24 | 2026-08-26 | Tool catalogue | Broad tool-discovery list; inclusion is not endorsement/evidence. | MEDIUM | No license exposed. Verdict: USEFUL. |
| GH-GEO-020 | VERIFIED | COMMUNITY | amplifying-ai/awesome-generative-engine-optimization | https://github.com/amplifying-ai/awesome-generative-engine-optimization | amplifying-ai | 2026-04-14 | 2026-08-26 | GEO catalogue | Centralizes papers/tools/guides with mixed evidentiary levels. | MEDIUM | No license exposed. Verdict: USEFUL discovery. |
| GH-AISEO-021 | VERIFIED | COMMUNITY | best-of-ai/awesome-ai-seo | https://github.com/best-of-ai/awesome-ai-seo | best-of-ai | 2026-07-27 | 2026-08-26 | AI SEO catalogue | Active MIT discovery list; marketing claims require independent verification. | MEDIUM | Verdict: USEFUL. |
| GH-RENDERTRON-022 | SUPERSEDED | COMMUNITY | GoogleChrome/rendertron | https://github.com/GoogleChrome/rendertron | GoogleChrome | 2022-10-06 | 2026-08-26 | Legacy rendering | Archived Apache-2.0 dynamic-rendering solution; current Google guidance treats dynamic rendering as workaround. | HIGH | Verdict: STALE. |
| GH-SEOSTATS-023 | SUPERSEDED | COMMUNITY | eyecatchup/SEOstats | https://github.com/eyecatchup/SEOstats | eyecatchup | 2022-06-15 | 2026-08-26 | Legacy metrics | Archived MIT metrics library with aging endpoints/assumptions. | HIGH | Verdict: STALE. |
| GH-VUEMETA-024 | SUPERSEDED | COMMUNITY | nuxt/vue-meta | https://github.com/nuxt/vue-meta | Nuxt | 2025-09-25 | 2026-08-26 | Legacy Vue metadata | Archived; current framework-native/Nuxt approaches preferred for new work. | HIGH | Verdict: STALE. |
| GH-TELES-025 | VERIFIED | COMMUNITY | teles/awesome-seo | https://github.com/teles/awesome-seo | teles | 2026-04-02 | 2026-08-26 | Supplementary catalogue | Unarchived catalogue; no license exposed; use only for discovery/freshness leads. | MEDIUM | Metadata verified, not authority. |
| GH-MARCO-026 | VERIFIED | COMMUNITY | marcobiedermann/search-engine-optimization | https://github.com/marcobiedermann/search-engine-optimization | Marco Biedermann | 2025-02-24 | 2026-08-26 | Supplementary checklist | MIT checklist/resource collection; useful ideas require current official cross-check. | MEDIUM | Unarchived but code activity is older than metadata updated_at. |
| GH-SCRIPTS-027 | VERIFIED | COMMUNITY | johnmurch/awesome-seo-scripts | https://github.com/johnmurch/awesome-seo-scripts | John Murch | 2022-12-10 | 2026-08-26 | Supplementary scripts | Unarchived but stale code activity/no license; inspect every script before use. | MEDIUM | Treat as legacy discovery, not production default. |
| GH-PSEO-028 | VERIFIED | COMMUNITY | guptadeepak/awesome-programmatic-seo | https://github.com/guptadeepak/awesome-programmatic-seo | Deepak Gupta | 2025-09-24 | 2026-08-26 | pSEO catalogue | Very small/new resource list; scale advice must be filtered through Google scaled-content policy. | MEDIUM | No license exposed; experimental discovery only. |

---

# Research / practitioner evidence

| ID | Status | Class | Title | URL | Provider | Source date | Reviewed | Relevant section | Key finding | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RES-GEO-001 | VERIFIED | RESEARCH | Optimizing Visibility in Generative Engines: A Critical Survey of GEO (2023–2026) | https://arxiv.org/abs/2607.14035 | Independent academic authors / arXiv | 2026-07 | 2026-08-26 | GEO evidence | Evidence is heterogeneous; fixed-context citation gains do not prove organic discovery, cross-platform ranking effects or traffic causality. | MEDIUM | Preprint/survey; methodology/scope still matter. |
| RES-GEO-002 | VERIFIED | RESEARCH | Generative Engine Optimization foundational paper | https://arxiv.org/abs/2311.09735 | Academic authors / arXiv | 2023-11 | 2026-08-26 | GEO research history | Introduced experimental GEO framing; experimental gains must remain scoped to the evaluated setup. | MEDIUM | Does not establish universal production ranking tactics. |
| PRAC-BL-TECH-001 | VERIFIED | PRACTITIONER | Technical SEO Guide | https://backlinko.com/technical-seo-guide | Backlinko | 2026-07-24 | 2026-08-26 | Technical SERP/practitioner | Current practitioner synthesis of technical SEO; engine behavior cross-checked against official docs. | MEDIUM | Workflow/examples, not official factors. |
| PRAC-BL-LOCAL-002 | VERIFIED | PRACTITIONER | Local SEO Guide | https://backlinko.com/local-seo-guide | Backlinko | — | 2026-08-26 | Local practitioner | Practical local workflow; Google’s relevance/distance/prominence framing remains authoritative. | MEDIUM | Practitioner layer. |
| PRAC-BL-SAAS-003 | VERIFIED | PRACTITIONER | SaaS SEO | https://backlinko.com/saas-seo | Backlinko | 2026-06-11 | 2026-08-26 | SaaS/B2B SERP | Connects SaaS search demand to product/use-case/acquisition workflow. | MEDIUM | Case examples do not create universal formula. |
| PRAC-BL-B2B-004 | VERIFIED | PRACTITIONER | SEO for B2B | https://backlinko.com/seo-for-b2b | Backlinko | 2025-12-23 | 2026-08-26 | B2B SERP | Emphasizes decision-maker intent, qualified leads and long buying cycles. | MEDIUM | Practitioner guidance. |
| PRAC-BL-PSEO-005 | VERIFIED | PRACTITIONER | Programmatic SEO | https://backlinko.com/programmatic-seo | Backlinko | 2026-01-20 | 2026-08-26 | pSEO SERP | Useful pSEO examples/templates/data; Google scaled-content policy remains controlling boundary. | MEDIUM | No scale exemption. |
| PRAC-BL-ECOM-006 | VERIFIED | PRACTITIONER | Ecommerce SEO | https://backlinko.com/ecommerce-seo | Backlinko | — | 2026-08-26 | Ecommerce SERP | Practitioner architecture/category/product workflow. | MEDIUM | Cross-check with Google ecommerce docs. |
| PRAC-AH-SEO-007 | VERIFIED | PRACTITIONER | Ahrefs SEO learning hub | https://ahrefs.com/seo | Ahrefs | current | 2026-08-26 | SEO guide SERP | Structured learning hub observed prominently for broad SEO education queries. | MEDIUM | Vendor/practitioner source. |
| PRAC-AH-TECH-008 | VERIFIED | PRACTITIONER | Ahrefs Technical SEO | https://ahrefs.com/seo/technical-seo | Ahrefs | current | 2026-08-26 | Technical SERP | Practitioner technical guide used for format/workflow observation. | MEDIUM | Not engine documentation. |
| PRAC-AH-LOCAL-009 | VERIFIED | PRACTITIONER | Ahrefs Local SEO | https://ahrefs.com/seo/local-seo | Ahrefs | current | 2026-08-26 | Local SERP | Practitioner local workflow. | MEDIUM | Official Google local framing controls ranking behavior claims. |
| PRAC-AH-LINK-010 | VERIFIED | PRACTITIONER | Ahrefs Link Building | https://ahrefs.com/seo/link-building | Ahrefs | current | 2026-08-26 | Link SERP | Prospecting/tactic workflow observed; every tactic filtered through Google link-spam policy. | MEDIUM | Link metrics are third-party proxies. |

---

# Measured / observed SERP baseline

All entries below are **dated current web-search observations**, not universal Google rank claims. The connected Ahrefs SERP Overview endpoint was attempted again on 2026-08-26 and returned `Insufficient plan`; therefore no exact Top-10 table, DR/backlink gap or “Google #1” position was fabricated. Full methodology and representative URLs are in [`docs/serp-research.md`](docs/serp-research.md).

| ID | Status | Class | Title | URL | Provider | Source date | Reviewed | Relevant section | Key finding | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SERP-SEO-001 | VERIFIED | MEASURED | `seo guide` observation | docs/serp-research.md | Current web search observation | 2026-08-26 | 2026-08-26 | SERP research | Guide/hub pages with structured learning paths observed prominently. | MEDIUM | Exact rank not asserted. |
| SERP-TECH-002 | VERIFIED | MEASURED | `technical seo` observation | docs/serp-research.md | Current web search observation | 2026-08-26 | 2026-08-26 | SERP research | Comprehensive implementation guides observed; freshness/current platform coverage visible. | MEDIUM | Exact rank not asserted. |
| SERP-LOCAL-003 | VERIFIED | MEASURED | `local seo` observation | docs/serp-research.md | Current web search observation | 2026-08-26 | 2026-08-26 | SERP research | Comprehensive practitioner guides observed; location-sensitive behavior remains market-specific. | MEDIUM | Official Google local docs cross-check. |
| SERP-LINK-004 | VERIFIED | MEASURED | `link building` observation | docs/serp-research.md | Current web search observation | 2026-08-26 | 2026-08-26 | SERP research | Strategy/education guides observed; policy-safe earning must be separated from schemes. | MEDIUM | Exact rank not asserted. |
| SERP-SCHEMA-005 | VERIFIED | MEASURED | `schema markup` observation | docs/serp-research.md | Current web search observation | 2026-08-26 | 2026-08-26 | SERP research | Mixed docs/tutorial/tool intent; Schema.org vocabulary and Google feature docs are distinct authorities. | MEDIUM | Exact rank not asserted. |
| SERP-GEO-006 | VERIFIED | MEASURED | `generative engine optimization` observation | docs/serp-research.md | Current web search observation | 2026-08-26 | 2026-08-26 | SERP research | Volatile mix of academic, agency, vendor and definitional pages; no stable universal tactic inferred. | MEDIUM | High volatility. |
| SERP-ECOM-007 | VERIFIED | MEASURED | `ecommerce seo` observation | docs/serp-research.md | Current web search observation | 2026-08-26 | 2026-08-26 | SERP research | Broad guides cover architecture/categories/products/facets/data/authority. | MEDIUM | Google ecommerce docs remain implementation authority. |
| SERP-INTL-008 | VERIFIED | MEASURED | `international seo` observation | docs/serp-research.md | Current web search observation | 2026-08-26 | 2026-08-26 | SERP research | Detailed URL/localization/hreflang/market guides align with implementation intent. | MEDIUM | Re-measure target market. |
| SERP-SAAS-009 | VERIFIED | MEASURED | `saas seo` observation | docs/serp-research.md | Current web search observation | 2026-08-26 | 2026-08-26 | SERP research | SaaS strategy guides connect use cases/product pages/content and acquisition outcomes. | MEDIUM | Exact rank not asserted. |
| SERP-B2B-010 | VERIFIED | MEASURED | `b2b seo` observation | docs/serp-research.md | Current web search observation | 2026-08-26 | 2026-08-26 | SERP research | B2B guides emphasize decision roles, long cycles and qualified-lead outcomes. | MEDIUM | Business/intent observation, not ranking factor. |
| SERP-PSEO-011 | VERIFIED | MEASURED | `programmatic seo` observation | docs/serp-research.md | Current web search observation | 2026-08-26 | 2026-08-26 | SERP research | Useful-data/template guidance is increasingly separated from thin scaled generation. | MEDIUM | Cross-checked with Google scaled-content abuse policy. |
| TOOL-AHREFS-012 | VERIFIED | MEASURED | Ahrefs SERP Overview access test | docs/serp-research.md | Ahrefs connector | 2026-08-26 | 2026-08-26 | Measurement limitation | Requested US Top-10 SERP data for `saas seo`; connected plan returned `Insufficient plan`. | HIGH | Limitation evidence; no exact rank data derived. |

---

# Reconciliation status

- Baseline official Google/Bing/AI-provider/regional/standards sources used by the operating system are `VERIFIED`.
- Required core GitHub repositories have been individually evaluated or explicitly marked `SUPERSEDED`; supplementary catalogues have scoped metadata reviews.
- The required representative SERP set is completed and marked `MEASURED`, with exact-rank limitation documented.
- No `DISCOVERED`, `BACKLOG` or unresolved `CONFLICT` row remains in the defined final baseline ledger.
- `SUPERSEDED` rows are intentionally preserved to prevent legacy tooling/advice from being mistaken for current defaults.

## Source admission rule for future maintenance

Before promoting a new community/practitioner statement into repository guidance, answer:

1. Is there current official/standard evidence that confirms or contradicts it?
2. Is it product behavior, protocol, measurement, research, correlation, opinion or marketing?
3. Is date/methodology/market scope known?
4. Could the tactic violate current spam/platform policies?
5. What does the evidence **not** prove?
6. Would the recommendation still make sense if the observed rankings changed tomorrow?

If these cannot be answered, classify the item `DISCOVERED`/`PARTIAL` and do not present it as established SEO truth.
