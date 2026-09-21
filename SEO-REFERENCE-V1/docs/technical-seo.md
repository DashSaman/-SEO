# Technical SEO Reference (2026)

**Reviewed:** 2026-08-26  
**Scope:** engine-agnostic technical foundation, with engine-specific caveats called out.

Technical SEO is dependency management for discovery, crawling, rendering, indexing, canonicalization, delivery and measurement. Fix failures in dependency order instead of chasing audit-tool scores.

## 1. Crawl pipeline model

For each important URL ask:

1. Can a crawler **discover** it?
2. Is the URL **allowed to be fetched**?
3. Does fetching return the expected **status, headers and body**?
4. Can critical content be **rendered/parsed**?
5. Is indexing **allowed and sensible**?
6. Is this the preferred **canonical** URL?
7. Can engines understand its **topic/entities/relationships**?
8. Is it connected through **internal links** and useful navigation?
9. Does it meet performance/experience expectations?
10. Can you measure its crawl/index/search outcome?

## 2. HTTP status semantics

Use status codes for what they mean:

- `200` — successful resource. Do not return a branded “not found” page with 200 (soft-404 pattern).
- `301` / `308` — permanent move where the destination is expected to replace the old URL.
- `302` / `307` — temporary move when the original should remain conceptually primary.
- `404` — resource not found.
- `410` — resource intentionally gone; use when that semantic is accurate, not as a ranking trick.
- `429` — too many requests; pair with sensible retry behavior where applicable.
- `5xx` — server failure. Persistent 5xx on crawl paths damages reliability and discovery.

Avoid long redirect chains and loops. Update internal links to final destinations rather than forcing crawlers/users through historical redirects.

## 3. robots.txt: standard behavior and limits

Primary standard: [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309.html)

Key principles:

- file lives at the origin root: `https://example.com/robots.txt`;
- rules are grouped by user-agent;
- `Allow`/`Disallow` control crawler access according to matching rules;
- robots directives are requests to compliant crawlers, **not authorization**;
- never use robots.txt to protect secrets, customer data, admin endpoints or private files;
- rules are origin-specific; subdomains need their own robots file;
- provider-specific bots/tokens can have distinct meanings.

Example baseline (illustrative, not universal):

```text
User-agent: *
Disallow: /internal-search/
Disallow: /cart/

Sitemap: https://example.com/sitemap.xml
```

Before deploying, test against actual URL patterns. A single slash/prefix mistake can remove a large section from crawl access.

## 4. robots.txt vs noindex

These controls are frequently confused.

- **robots disallow**: crawler is asked not to fetch the URL.
- **noindex**: crawler must normally fetch the resource to read the directive, then it can exclude the page from indexing.

Therefore `Disallow` + page-level `noindex` can be contradictory if the crawler cannot fetch the page to see `noindex`.

For content that must be private, use authentication/authorization rather than either control.

## 5. Meta robots / X-Robots-Tag

Typical directives include:

```html
<meta name="robots" content="noindex,follow">
```

or headers such as:

```http
X-Robots-Tag: noindex
```

Use HTTP headers for non-HTML resources when needed. Validate that templates/CDNs do not inject global directives accidentally.

## 6. XML sitemaps

Primary protocol: [Sitemaps.org](https://www.sitemaps.org/protocol.html)

Standard boundaries:

- up to **50,000 URLs** per sitemap;
- up to **50 MB uncompressed** per sitemap;
- split larger sites into sitemap files and a sitemap index;
- use fully qualified URLs;
- keep sitemap URLs consistent with the intended canonical/indexable set.

Practical sitemap rules:

- include canonical URLs you actually want indexed;
- remove redirecting, error, `noindex` and obvious duplicate URLs;
- produce trustworthy modification dates rather than rewriting every `lastmod` on every build;
- segment large sites by content type/section where that improves diagnostics;
- reference relevant sitemaps from robots.txt and submit through engine webmaster tools where supported.

Bing explicitly states in its current guidance that accurate `lastmod` is useful while it ignores sitemap `changefreq` and `priority`.

## 7. IndexNow

Primary source: [IndexNow documentation](https://www.indexnow.org/documentation)

IndexNow lets participating search engines receive notifications that URLs were added, updated or deleted.

Correct mental model:

**publish/change URL → send notification → engine decides when/whether to fetch/process/index**

It is not:

**send IndexNow → guaranteed immediate index/rank**

Operational practices:

- automate submissions on real publish/update/delete events;
- do not spam unchanged URLs continuously;
- verify the ownership key implementation;
- continue maintaining ordinary crawlability/sitemaps/internal links.

## 8. Canonicals and duplicates

Duplicate URLs arise from:

- protocol/host variants;
- trailing slash variants;
- URL parameters;
- sorting/filtering/faceted navigation;
- print/share/session URLs;
- product variants;
- category/tag overlaps;
- syndication/localization;
- copied staging paths.

Canonical management should align:

- redirects;
- `rel=canonical`;
- sitemap inclusion;
- internal links;
- hreflang (when used);
- content/URL architecture.

Do not canonicalize genuinely different user-intent pages merely because they share text. Do not point a canonical to an irrelevant page just to “consolidate authority.”

## 9. Faceted navigation and crawl space

Large ecommerce/catalog sites can create effectively infinite URL combinations through:

- filters;
- sort order;
- pagination;
- tracking parameters;
- session state;
- internal search.

Model each URL class explicitly:

| URL class | User value | Search demand | Index? | Crawl strategy |
|---|---|---|---|---|
| primary category | high | high | usually yes | fully linked/sitemap |
| valuable curated facet | high | demonstrated | maybe yes | static/canonical clean URL |
| arbitrary filter combo | low/duplicate | low | usually no | limit discovery/indexation |
| internal search | transient | not landing-page intent | normally no | engine-specific policy + crawl control |

The objective is not “block all parameters”; it is to prevent unbounded low-value crawl/index space while retaining useful landing pages.

## 10. JavaScript SEO

Important questions:

- Is primary content present or obtainable in rendered output?
- Are title/canonical/meta/structured data correct after rendering?
- Are important links actual anchors with usable URLs?
- Does content require user interaction before it exists?
- Are APIs/assets blocked from crawlers?
- Does hydration replace good server content with errors or empty shells?
- Do route changes produce unique URLs/history state?
- Are status codes meaningful on server responses?

Prefer architectures that deliver meaningful HTML early. JavaScript can be crawlable, but unnecessary rendering dependency increases failure modes and crawl cost.

## 11. Rendering verification

Test at three layers:

1. **Raw HTTP response** — what does the server/CDN send?
2. **Rendered browser DOM** — what appears after JavaScript executes?
3. **Search-engine inspection** — what did the relevant engine actually crawl/render/index?

Do not use browser “View Source” alone as proof that a JS application is invisible or visible to search systems.

## 12. Internal-link graph

Technical link audits should calculate/inspect:

- orphan URLs;
- click depth;
- number of unique internal inlinks;
- contextual vs global/template links;
- broken links;
- redirecting links;
- canonical mismatch destinations;
- nofollow usage where applicable;
- navigation generated only after unsupported interactions.

Use these metrics to find structural problems, not to optimize toward arbitrary counts.

## 13. Hreflang / international architecture

For localized/regional equivalents:

- each hreflang URL should be crawlable/indexable where intended;
- use valid language/region codes;
- use reciprocal annotations;
- point annotations to canonical equivalents;
- keep content meaningfully localized when targeting distinct markets;
- use `x-default` when a neutral/default selector page is appropriate.

Avoid automatic IP redirects that prevent crawlers/users from accessing alternate locales.

## 14. Pagination

Pagination is primarily a crawl/navigation/content-architecture problem. Ensure:

- each page has a distinct crawlable URL;
- next pages are linked with ordinary anchors;
- canonical logic does not incorrectly collapse every paginated page into page 1 when pages contain distinct item sets;
- infinite scroll has a URL-based paginated fallback/discovery mechanism.

Do not depend on obsolete `rel=prev/next` ranking mythology.

## 15. Site performance and Core Web Vitals

Current Google targets:

- LCP ≤ 2.5 seconds;
- INP < 200 ms;
- CLS < 0.1.

Technical diagnostics should distinguish:

- **field data** (real users) from
- **lab data** (controlled test).

Common engineering levers:

- server/edge latency and caching;
- critical resource prioritization;
- image/video sizing and formats;
- unnecessary JS/CSS reduction;
- third-party script governance;
- font loading;
- lazy loading below-the-fold media;
- layout reservation to prevent shifts;
- interaction handler/main-thread work reduction.

Do not ship user-hostile compromises just to produce a higher lab score.

## 16. Images

Technical image SEO/UX basics:

- descriptive filenames where operationally useful;
- meaningful `alt` text for informative images, empty alt for purely decorative images;
- dimensions/aspect ratios to reduce layout shifts;
- modern efficient formats when supported;
- responsive image markup (`srcset`/`sizes`) when relevant;
- crawlable image URLs;
- image sitemaps for image-heavy cases when useful;
- do not lazy-load the primary LCP image in ways that delay it.

## 17. Video

For video-first pages:

- ensure the watch page is crawlable/indexable;
- make the video prominent;
- provide title/description/context in HTML;
- use supported structured data when eligible;
- stable thumbnail/video URLs;
- avoid hiding all meaningful context behind a player script.

## 18. Structured data technical validation

Validate three separate layers:

1. **syntax** — valid JSON-LD/Microdata/RDFa;
2. **vocabulary** — properties/types valid according to Schema.org;
3. **search feature eligibility** — engine-specific requirements/policies satisfied.

A page can be valid Schema.org and still not qualify for a Google rich result.

## 19. Security, CDN and WAF

SEO failures often originate outside the CMS:

- bot challenges on legitimate crawlers;
- geo/IP blocks;
- rate limits;
- CDN cache poisoning/stale redirects;
- HTTP header rewriting;
- blocked JS/CSS/image resources;
- TLS/certificate failures;
- origin overload causing intermittent 5xx.

When validating bots, use provider-published verification methods/IP lists rather than trusting the User-Agent string alone.

## 20. Crawl logs

Server/CDN logs can answer what analytics cannot:

- which bots fetch which URLs;
- status-code distribution;
- crawl frequency;
- wasted crawl on parameters/search/filter URLs;
- redirect loops/chains;
- bot access to sitemaps/resources;
- spikes after deploys;
- AI/search crawler presence.

Normalize bot identity cautiously and verify official crawlers.

## 21. Migration technical gate

Before a migration launch:

- crawl old site and export URLs/metadata/status/canonical/hreflang/internal links;
- map old→new URLs;
- validate redirects in staging safely;
- compare indexable page count;
- validate robots/noindex/canonical/sitemap;
- preserve essential structured data/content;
- benchmark CWV/performance;
- test analytics/Search Console/Bing tools;
- monitor logs and errors immediately after cutover.

## 22. Technical audit severity model

### P0 — catastrophic

- production globally blocked/noindexed;
- DNS/TLS/host unavailable;
- mass 5xx;
- destructive redirect/canonical migration error;
- private content unintentionally exposed.

### P1 — major visibility loss

- key section blocked/index-excluded;
- broken rendering of main content;
- large canonical mismatch;
- orphaned commercial pages;
- sitemap contains wrong domain/environment;
- WAF blocking major crawler.

### P2 — material optimization

- large duplicate crawl spaces;
- redirect chains;
- CWV failures across important templates;
- structured-data errors on eligible pages;
- internal-link depth issues.

### P3 — hygiene

- minor metadata duplication;
- small broken-link sets;
- non-critical asset inefficiency;
- low-impact warnings.

Prioritize by **business impact × affected URLs × confidence × dependency**, not by the number of audit-tool warnings.

## 23. Technical release checklist

Every SEO-sensitive deploy should verify:

- status codes;
- robots.txt diff;
- meta/X-Robots directives;
- canonical diff;
- sitemap generation;
- internal-link crawl;
- rendered main content;
- structured data;
- hreflang if applicable;
- analytics/consent impacts;
- CWV/performance regression;
- crawler/WAF access;
- error logs.

Automate these checks in CI/CD where possible.

## 24. Sources

Primary sources used in this document are logged in [`../SOURCES.md`](../SOURCES.md), especially:

- IETF RFC 9309
- Sitemaps.org protocol
- Google Search Essentials/canonical/CWV/page-experience docs
- Bing sitemap guidance
- IndexNow documentation
- OpenAI/Anthropic/Perplexity crawler guidance for provider-specific bot access
