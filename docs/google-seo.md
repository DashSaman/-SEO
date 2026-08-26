# Google SEO Reference — Search + Generative Search (2026)

**Evidence class:** primarily first-party Google documentation  
**Reviewed:** 2026-08-26  
**Freshness warning:** check [Google Search documentation updates](https://developers.google.com/search/updates) before production changes.

## 1. The durable Google model

Google SEO should be treated as a pipeline:

**Eligible → discoverable → crawlable → renderable → indexable → canonicalized → relevant → useful/trustworthy → competitive → presentable in Search → measurable**

Passing one stage does not guarantee the next. Google Search Essentials explicitly notes that meeting requirements and best practices does not guarantee crawling, indexing or serving.

Primary source: [Google Search Essentials](https://developers.google.com/search/docs/essentials)

## 2. Technical eligibility and discovery

Baseline rules:

- Serve content Googlebot can access over functioning HTTP(S).
- Return meaningful HTTP status codes.
- Do not accidentally block important resources/pages with `robots.txt`, authentication, WAF rules or `noindex`.
- Use ordinary crawlable HTML links (`<a href="...">`) for important discovery paths.
- Maintain a logical site architecture and internal links so important pages are not isolated.
- Submit/maintain XML sitemaps for discoverability, especially on large/new/media-heavy sites.
- Make content usable on mobile and avoid rendering setups that hide critical content from the rendered HTML.

A sitemap is a discovery aid, **not** an indexing guarantee.

## 3. Indexing controls: do not confuse them

| Control | Primary purpose | Key caveat |
|---|---|---|
| `robots.txt` | control crawler access | blocked crawler may not see page-level `noindex`; not security |
| `<meta name="robots" content="noindex">` | request page exclusion from index | crawler must be able to fetch the page to see it |
| `X-Robots-Tag` | robots directive in HTTP header | useful for non-HTML resources too |
| HTTP auth / access control | actual access restriction | use this for private data, not robots.txt |
| canonical | indicate preferred representative among duplicates | signal/hint, not an absolute command |
| redirect | move users/crawlers/signals to another URL | choose correct permanent/temporary semantics |

## 4. Canonicalization

Source: [Google canonicalization documentation](https://developers.google.com/search/docs/crawling-indexing/canonicalization)

Google may select a representative canonical URL from duplicates. Useful signals can include:

- redirects;
- `rel="canonical"`;
- sitemap inclusion;
- HTTPS preference and other consistency signals.

Best practice is to align signals rather than sending contradictory instructions. A canonical tag alone should not be described as a guaranteed command.

### Canonical consistency checklist

- Self-canonicalize indexable canonical pages where appropriate.
- Link internally to canonical URLs, not duplicate variants.
- Put canonical URLs in sitemaps.
- Redirect obsolete equivalents when there is no user need to retain them.
- Avoid contradictory canonical + `noindex` + redirect chains.
- Audit parameters, faceted navigation, print views, HTTP/HTTPS, www/non-www and trailing-slash variants.

## 5. People-first content and quality

Sources:

- [Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Google Search Essentials](https://developers.google.com/search/docs/essentials)

Useful content tends to:

- serve an existing/intended audience;
- answer the actual task/search intent;
- demonstrate first-hand knowledge or substantive expertise where relevant;
- add original information, analysis, experience, examples or data instead of repackaging what already exists;
- make authorship/responsibility clear when users would expect it;
- provide enough context for users to make a decision without forcing unnecessary extra searches;
- avoid mass production solely to capture search traffic.

### E-E-A-T: correct interpretation

Experience, Expertise, Authoritativeness and Trust are useful quality concepts. Google’s guidance emphasizes **Trust** as especially important. Do **not** document “E-E-A-T score” as a single public ranking metric or claim that adding author boxes mechanically boosts rankings.

For YMYL topics, stronger trust/evidence requirements are especially important because errors can affect health, finance, safety or societal well-being.

## 6. Keywords and intent without keyword superstition

Google Search Essentials recommends using words people use to search for the content in prominent descriptive places such as:

- page title;
- main heading;
- descriptive body copy;
- alt text when it meaningfully describes an image;
- link text when it describes destination context.

Avoid treating keyword density, exact-match repetition or every long-tail variation as required. Modern search systems understand related meanings; Google’s 2026 AI guidance explicitly says AI-specific rewriting for every wording variant is unnecessary.

## 7. Titles, snippets and SERP presentation

Create concise, accurate, distinct page titles that describe the page. Avoid boilerplate that makes every page indistinguishable. Meta descriptions can help Search create useful snippets but are not a guaranteed snippet source.

Search presentation can also be affected by:

- structured data eligibility;
- images/video;
- favicon/site name;
- merchant/local/news-specific surfaces;
- content freshness where query intent is freshness-sensitive.

Do not equate richer appearance with higher organic ranking.

## 8. Internal linking and information architecture

A strong architecture should make:

- important pages reachable through ordinary internal links;
- hierarchy understandable to users and crawlers;
- anchor text descriptive rather than generic;
- orphan pages rare and intentional;
- duplicate taxonomies/filters controlled;
- related entities/topics connected contextually.

Internal links are both discovery paths and contextual signals. The practical goal is not “N links per page”; it is a coherent graph where important resources are discoverable and contextually connected.

## 9. Core Web Vitals and page experience

Sources:

- [Understanding Core Web Vitals and Google Search results](https://developers.google.com/search/docs/appearance/core-web-vitals)
- [Understanding page experience](https://developers.google.com/search/docs/appearance/page-experience)

Current good-experience targets documented by Google:

| Metric | Good target |
|---|---:|
| LCP | ≤ 2.5 s |
| INP | < 200 ms |
| CLS | < 0.1 |

Google says Core Web Vitals are used by ranking systems, but there is no single overall “page experience signal” and perfect tooling scores do not guarantee top rankings. Relevance and overall page quality still matter.

Treat CWV as real-user experience engineering, not as a game to hit Lighthouse 100.

## 10. Structured data

Structured data helps machines understand explicit entities/properties and can make pages eligible for supported rich-result experiences. It is **not** a generic ranking guarantee.

Rules:

- mark up content actually visible/represented on the page;
- follow Google feature-specific required/recommended properties in addition to Schema.org vocabulary;
- keep values consistent with page content;
- validate syntax and monitor Search Console enhancement reports where available;
- do not invent reviews, ratings, prices, availability, authorship or organization facts;
- remove obsolete/deprecated rich-result assumptions when Google changes eligibility.

See [`structured-data.md`](structured-data.md).

## 11. Google generative Search: AI Overviews and AI Mode

Primary source: [Optimizing for generative AI features on Google Search](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)

Google’s 2026 position is unusually clear: **SEO is still the foundation** because its generative Search experiences rely on core Search ranking/quality systems and Search-index retrieval.

Google discusses mechanisms such as:

- retrieval-augmented generation / grounding from Search-index sources;
- query fan-out into related sub-queries;
- prominent clickable supporting links.

### What Google says you do NOT need for its generative Search

- a special `llms.txt` file;
- special “AI schema”;
- artificial tiny content chunks solely for AI;
- rewriting pages in a special robotic style;
- a page for every query-fan-out variant;
- inauthentic mentions engineered only to influence AI answers.

Google says `llms.txt` neither helps nor harms Google Search visibility because Google Search ignores it as a special mechanism. Other services may have different behavior, so this is a **Google-specific** conclusion.

### What still helps

- technically accessible/indexable content;
- unique, non-commodity value;
- clear, accurate information;
- useful local/product/image/video content where relevant;
- strong overall user experience;
- correct Search controls;
- measurement in Search Console as Google exposes relevant reporting.

## 12. Google-Extended is NOT Googlebot ranking control

Source: [Google common crawlers — Google-Extended](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers)

Important distinctions:

- `Google-Extended` is a **robots.txt product token**.
- It does **not** have a separate HTTP user-agent string.
- Google documents it as a control for specified uses of crawled content involving future Gemini model training and grounding in Gemini/Vertex contexts.
- Google explicitly says it does **not** affect inclusion in Google Search and is not a Google Search ranking signal.

Therefore never tell a publisher that blocking/allowing Google-Extended is required to rank in Google Search.

## 13. 2026 Google-specific changes worth monitoring

Use the official update log rather than memorizing a static list. Relevant changes already observed during this research include:

- May 15, 2026: dedicated generative-AI optimization guidance added.
- May 27, 2026: Preferred Sources availability expanded to AI Mode/AI Overviews.
- 2026 structured-data/rich-result documentation continues to evolve; old SEO checklists can become stale quickly.
- Search Console is expanding visibility/measurement across newer Search surfaces and eligible platform properties.

Source: [Google Search documentation updates](https://developers.google.com/search/updates)

## 14. Migration/change management

Source: [Site moves with URL changes](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes)

For redesigns/domain/URL migrations:

1. inventory old URLs;
2. build deterministic old→new mapping;
3. test new pages before cutover;
4. use server-side redirects where appropriate;
5. update canonicals/internal links/sitemaps/hreflang;
6. remove accidental staging blocks/noindex;
7. monitor crawl/index/search performance after launch;
8. keep redirects long enough for users/crawlers/signals to migrate.

Large migrations should be treated as SEO releases with rollback/monitoring plans, not a cosmetic deployment.

## 15. Google SEO anti-patterns

Do not recommend:

- scaled low-value content created primarily to manipulate rankings;
- doorway/location pages with no differentiated user value;
- hidden/cloaked content intended to deceive Search;
- paid/automated links intended to manipulate ranking signals;
- fake reviews or fabricated external mentions;
- copied/rephrased commodity content at scale;
- indexing internal search/filter combinations without demand/value control;
- chasing obsolete rich-result tactics after documentation changes.

Always compare tactics against the current Search Essentials spam policies.

## 16. Audit order for Google

A practical remediation priority:

1. **Security/privacy failures**
2. **Site inaccessible / wrong HTTP behavior**
3. **robots/noindex/WAF blockers**
4. **canonical/redirect/migration errors**
5. **rendering/discovery/internal-link failures**
6. **duplicate/thin/low-value index bloat**
7. **intent/content quality gaps**
8. **structured-data/search appearance issues**
9. **CWV/performance/UX bottlenecks**
10. **authority/entity/off-site competitive gaps**
11. **AI/search-surface measurement and iteration**

This order is intentionally dependency-aware: there is little value polishing schema or copy on pages that cannot be crawled/indexed correctly.