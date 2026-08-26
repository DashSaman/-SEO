# Other Search Engines Reference — Yandex, Naver, Baidu, DuckDuckGo, Apple (2026)

**Reviewed:** 2026-08-26  
**Rule:** optimize from each engine’s current first-party documentation; do not assume every Google-specific directive/feature is universal.

## 1. Shared foundation

Across engines, durable fundamentals recur:

- reliable crawlable URLs;
- correct robots/index controls;
- meaningful HTTP status codes;
- internal links and understandable site structure;
- useful unique content;
- canonical/duplicate discipline;
- sitemaps/submission tools where supported;
- webmaster/search performance monitoring;
- platform-specific markup/crawler policy only when documented.

Engine-specific features should be layered on top of this shared foundation.

---

## 2. Yandex

Official sources:

- [Site structure](https://yandex.com/support/webmaster/en/recommendations/site-structure)
- [Site indexing](https://yandex.com/support/webmaster/en/recommendations/indexing)
- [Webmaster recommendations/diagnostics](https://www.yandex.com/support/webmaster/en/diagnosis/recommendations)

### Important Yandex practices

- Build crawlable navigation using ordinary links.
- Keep site structure logical and important pages reachable.
- Supply sitemaps where useful.
- Use robots controls deliberately for technical/duplicate spaces.
- Return correct status codes, especially real 404s for missing resources.
- Keep titles/descriptions useful and avoid mass duplication.
- Monitor indexing/crawl diagnostics in Yandex Webmaster.

### Implementation stance

Do not port old Yandex SEO folklore into this repository unless it is still supported by current Yandex documentation or measured evidence. Treat Yandex-specific webmaster diagnostics as the operational source of truth.

---

## 3. Naver

Official sources:

- [Naver Search Advisor SEO basics](https://searchadvisor.naver.com/guide/seo-help)
- [robots.txt guide](https://searchadvisor.naver.com/guide/seo-basic-robots)
- [markup/structure guide](https://searchadvisor.naver.com/guide/markup-structure)
- [feed/sitemap submission](https://searchadvisor.naver.com/guide/request-feed)

### Naver-specific notes

- Naver documents its crawler `Yeti`.
- robots.txt should live at the appropriate site root and be intentionally configured.
- unique, accurate page titles/descriptions remain foundational.
- sitemap/feed submission can aid discovery.
- Naver documents engine-specific markup/directives; keep them scoped to Naver rather than assuming other engines honor them.

### Practical checklist

- [ ] Verify site in Naver Search Advisor.
- [ ] Validate Yeti crawl access.
- [ ] Check robots and sitemap/feed submission.
- [ ] Use unique descriptive metadata.
- [ ] Monitor indexing/diagnostic feedback.
- [ ] Re-check Naver-specific AI/source-description directives before production use because feature semantics can change.

---

## 4. Baidu

Current official entry point found during this research:

- [Baidu Search Resource Platform optimization guide](https://ziyuan.baidu.com/doc/index)
- [Baidu search algorithm/policy guide](https://zy.baidu.com/act/guide?isResponsible=1)

Baidu’s current resource platform exposes guidance/tooling around:

- site verification;
- robots;
- crawl frequency and diagnostics;
- crawl anomalies;
- ordinary/rapid resource submission;
- index status;
- dead-link submission;
- site migrations;
- traffic/keyword reporting;
- site attributes/branding;
- content-quality and algorithm/spam policies.

Baidu’s policy documentation explicitly focuses on user-oriented content quality and flags classes of low-quality/manipulative behavior such as site networks, cross-topic/irrelevant content, poor aggregation, scraped/collected content, mismatched title/content and low-quality pages.

### Baidu operating rule

Because much English-language Baidu SEO advice is stale, prefer current Chinese first-party Resource Platform material. Translate concepts carefully and preserve the original source URL in `SOURCES.md`.

### Baidu checklist

- [ ] Verify site/resource property.
- [ ] Validate robots/crawl status.
- [ ] Use official crawl/index submission mechanisms appropriate to account/site eligibility.
- [ ] Submit dead URLs through supported tools where relevant.
- [ ] Use migration tooling for URL/site changes where applicable.
- [ ] Audit content against current Baidu quality/algorithm policies.
- [ ] Measure Baidu-specific traffic/keywords rather than extrapolating from Google.

---

## 5. DuckDuckGo

Official sources:

- [Where DuckDuckGo search results come from](https://duckduckgo.com/duckduckgo-help-pages/results/sources)
- [DuckAssistBot](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot)

DuckDuckGo says:

- it uses multiple specialized sources and its own crawler/indexes;
- many traditional organic links/images are largely sourced from Bing;
- it does not rely on Google results;
- AI-assisted answers have a distinct real-time crawler, `DuckAssistBot`.

### Consequence for SEO

A sensible DuckDuckGo strategy includes strong Bing discoverability plus ordinary crawlability for DuckDuckGo’s own systems. Do not describe DuckDuckGo as simply a “Bing skin”; its results blend multiple sources/indexes.

### DuckAssistBot

DuckDuckGo documents `DuckAssistBot` as a crawler for AI-assisted answers with prominent source citations. It states:

- publishers can opt out through robots.txt;
- opting out of DuckAssistBot does not affect ordinary DuckDuckGo organic ranking/inclusion;
- the crawled data is not used by DuckDuckGo to train AI models according to the current help page.

This is another example of why AI-answer crawling and classic organic search crawling must be modeled separately.

---

## 6. Apple Search / Siri / Spotlight

Official source: [About Applebot](https://support.apple.com/en-gb/119829)

Apple says data crawled by **Applebot** can power search technology integrated into experiences including:

- Spotlight;
- Siri;
- Safari/search-related Apple experiences;
- contextual up-to-date information for some AI-generated outputs.

Apple documents `robots.txt` and robots/meta controls for Applebot.

### Applebot-Extended

Apple also documents **Applebot-Extended** as a separate robots control governing whether content already crawled by Applebot may be used to train Apple’s general-purpose foundation models.

Important distinction:

- Applebot-Extended itself does not crawl webpages.
- Blocking Applebot-Extended can opt content out of specified model-training use while pages may still remain discoverable via Applebot-powered search experiences.

This resembles the separation between search crawling and training controls seen at other AI/search providers.

### Apple ranking factors disclosed by Apple

Apple says Search may consider factors including:

- aggregated user engagement with results;
- relevance/matching of search terms to page topic/content;
- number/quality of links from other web pages;
- approximate location-based signals;
- web-page design characteristics.

Apple says there is no predetermined importance assigned in the disclosure. Do not convert this list into fixed weights.

### Paywalled content

Current Applebot documentation supports page-level `schema.org` `isAccessibleForFree` information for paywalled/subscription content. Verify exact current syntax/behavior before deployment.

---

## 7. Search-engine matrix

| Engine/system | Webmaster/first-party control | Main discovery considerations | AI-specific separation observed |
|---|---|---|---|
| Google | Search Console/Search Central | Googlebot, sitemaps, internal links, indexing/canonical | Google-Extended separate from Search ranking |
| Bing | Bing Webmaster Tools | Bingbot, sitemaps, IndexNow | AI/citation reporting and Copilot ecosystem evolving |
| Yandex | Yandex Webmaster | crawl/index diagnostics, links, sitemaps | verify product-specific AI guidance separately |
| Naver | Search Advisor | Yeti, metadata, robots, feeds/sitemaps | Naver-specific source/AI directives exist; verify current docs |
| Baidu | Search Resource Platform | crawl/index submission, robots, quality policies | verify current Baidu AI surfaces separately |
| DuckDuckGo | Help pages + underlying Bing ecosystem | Bing visibility + DuckDuckGo crawler/indexes | DuckAssistBot separate from organic search |
| Apple | Applebot docs | Applebot crawlability, relevance/site signals | Applebot-Extended is training-use control |

## 8. What not to do

- Do not translate Google Search Console errors 1:1 into every engine’s terminology.
- Do not assume IndexNow is supported by every search engine.
- Do not assume Google-specific structured-data rich results are universal.
- Do not assume every AI-training bot is required for search discovery.
- Do not rely on decade-old regional SEO blog advice when current first-party docs exist.
- Do not submit scraped/low-value pages at scale simply because a platform offers fast-submission tools.

## 9. Remaining expansion queue

Future passes should add current first-party documentation for:

- Brave Search and its crawler/index controls;
- Seznam and other market-specific engines where relevant;
- regional/local search ecosystems tied to business directories/maps;
- specialized vertical search systems (shopping, jobs, travel, app search) as separate surface-specific modules.

All additions must follow `AGENTS.md` evidence and freshness rules.