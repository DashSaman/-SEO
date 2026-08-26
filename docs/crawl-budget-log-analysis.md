# Crawl Budget & Server Log Analysis

**Reviewed:** 2026-08-26  
**Primary source:** Google crawl-budget documentation, RFC/robots guidance and Search Console concepts.

## First question: do you actually have a crawl-budget problem?

Google’s current guide is primarily intended for:

- roughly **1M+ unique pages** changing moderately often;
- roughly **10k+ unique pages** changing very rapidly (daily);
- sites where a large share of URLs remain `Discovered - currently not indexed`.

Google explicitly describes those numbers as rough estimates, not exact thresholds. Smaller sites whose pages are crawled promptly usually need a current sitemap and regular Page Indexing checks rather than “crawl budget hacks.”

Source: https://developers.google.com/crawling/docs/crawl-budget

## Model

For Google, crawl budget is shaped by:

- **crawl capacity limit** — how much Google can fetch without harming the host, affected by server health/latency/errors/rate limiting and Google’s resource limits;
- **crawl demand** — need/desire to recrawl based on factors such as site size, update frequency, page quality/relevance and staleness.

A crawl is **not** an index guarantee. Every crawled page still undergoes consolidation and suitability evaluation.

## Why logs matter

External crawlers show what *could* be crawled. Server/CDN logs show what a bot actually requested, when, how often and with what response.

Use logs to answer:

- Which URL classes consume bot requests?
- Are important updated URLs being fetched?
- How much crawl is spent on parameters/facets/duplicates/redirects/errors?
- Does Googlebot receive slow/5xx/429 responses?
- Are sitemaps and internal links leading bots to the right pages?
- Did a release change bot behavior?

## Minimum log fields

Retain where legally/security appropriate:

- timestamp;
- hostname;
- request method;
- path + query string;
- status code;
- response bytes;
- user-agent;
- client IP or privacy-safe derived bot identity;
- response time / upstream time;
- referrer if available;
- cache hit/miss;
- edge/origin indicator.

Protect logs as sensitive operational data. Do not publish raw user IPs/auth tokens/query secrets.

## Verify bots

User-agent strings can be spoofed. For security-sensitive allowlisting or bot segmentation, use the provider’s documented verification method (reverse+forward DNS, published IP ranges, Web Bot Auth or provider-specific guidance as applicable). Do not trust `Googlebot`/`OAI-SearchBot` strings alone.

## URL-class segmentation

Classify paths into buckets such as:

- homepage;
- categories/hubs;
- products/entities;
- articles/guides;
- faceted/filtered URLs;
- pagination;
- search results;
- tracking/session parameters;
- media/assets;
- API routes;
- redirects;
- 404/410;
- 5xx/429;
- canonical duplicates;
- noindex pages;
- robots-blocked paths.

Raw “Googlebot hits” without template segmentation rarely produce an actionable diagnosis.

## Core metrics

### Bot crawl volume

`bot requests / day` by crawler, hostname and URL class.

### Crawl waste proxy

`requests to non-preferred URL classes / total bot requests`

Non-preferred might include duplicate params, endless facets, redirect chains, soft-404 states, obsolete URLs or internal-search permutations. This is a diagnostic proxy, not an official ranking metric.

### Success response distribution

Track percent 2xx / 3xx / 4xx / 5xx / 429 for verified bots.

### Response time

Track p50/p75/p95 TTFB/upstream response by bot and template. Google says crawl capacity can decrease when the site slows, returns 5xx, or rate-limits with 429.

### Recrawl latency

For pages with meaningful updates:

`first verified recrawl timestamp - publish/update timestamp`

### Orphan evidence

Important sitemap URLs with no internal links and no bot fetches need architecture investigation.

### Index correlation

Join URL-level crawl data with Search Console Page Indexing/URL Inspection samples. Remember: crawl frequency and indexation are related operational states, not a simple causal equation.

## High-impact crawl waste patterns

### Facet explosion

Symptoms:

- many combinations of filter/sort parameters;
- repeated crawling of the same content in different order;
- weak/duplicate index candidates.

Actions:

- reduce link exposure to non-indexable combinations;
- normalize URL parameters/order;
- define a finite set of valuable indexable filters;
- use robots/noindex/canonical only for their actual semantics, not as substitutes for architecture;
- monitor logs after change.

### Tracking/session parameters

Do not expose infinite unique URLs through internal links. Strip/share canonical clean URLs, configure application routing and avoid session IDs in crawlable links.

### Redirect chains

Bots and users should reach final URLs directly from internal links/sitemaps. Update references after migrations rather than preserving multi-hop chains forever.

### Soft 404s

If content is permanently unavailable with no equivalent replacement, use a correct `404` or `410`. A 200 page saying “not found” can waste crawl/index processing and confuse quality signals.

### Infinite calendars/search spaces

Avoid crawlable date/price/query combinations without real search value. Bound pagination and generated routes.

## Sitemaps

For large sites:

- list preferred canonical/indexable URLs only;
- split by page type/region/date when useful for diagnostics;
- keep accurate meaningful `lastmod`;
- remove deleted/redirected/noindex URLs;
- compare submitted vs indexed/crawled by sitemap group.

Bing says it ignores sitemap `changefreq` and `priority`; accurate `lastmod` is more useful. Sitemap inclusion does not guarantee indexing.

## Caching and HTTP 304

Use proper validators (`ETag` / `Last-Modified`) where architecture supports them. Conditional responses can reduce transfer/work. Do not fake `lastmod` changes on every build when content did not materially change.

## Server health

Monitor:

- 5xx spikes;
- 429/rate-limit behavior;
- bot-specific WAF blocks;
- TLS/DNS failures;
- origin vs CDN latency;
- cache bypasses;
- oversized HTML/resources;
- deployment windows correlated with crawl drops.

Avoid intentionally returning errors to “slow Googlebot” as a routine crawl optimization. Fix URL-space and server-health causes first.

## Crawl-budget change protocol

1. Define problem by URL class/log evidence.
2. Capture 2–4 week baseline when possible.
3. Change one architecture/control group at a time.
4. Validate no high-value URLs were blocked/deindexed.
5. Monitor bot requests, response codes and Page Indexing.
6. Annotate deployments/migrations/robots changes.
7. Compare before/after by template, not just total requests.
8. Roll back if important discovery/indexation worsens.

## Example weekly report

| Metric | Current | Prior | Interpretation |
|---|---:|---:|---|
| Verified Googlebot requests | — | — | volume alone not success |
| Preferred 2xx URL share | — | — | higher can indicate more efficient crawl |
| Parameter/facet share | — | — | investigate if rising without search value |
| 3xx share | — | — | update old internal/sitemap URLs |
| 404/410 share | — | — | distinguish normal deletions vs broken links |
| 5xx/429 share | — | — | server/capacity risk |
| p95 response time | — | — | crawl-capacity/server-health diagnostic |
| median recrawl latency | — | — | useful for fresh inventory/news |
| discovered-not-indexed | — | — | quality/discovery/capacity diagnosis needed |

## PASS / FAIL

**PASS** when crawl-budget work is justified by scale/log evidence, bot identity is verified, URL classes are explicit, high-value pages remain discoverable, sitemap/internal links prefer clean URLs, server errors are controlled and before/after metrics are recorded.

**FAIL** when a small healthy site spends weeks “optimizing crawl budget,” robots rules accidentally hide important paths, logs are interpreted from spoofable UAs only, or total bot hits are treated as a ranking KPI.

## Sources

- Google crawl budget: https://developers.google.com/crawling/docs/crawl-budget
- Google crawler verification: https://developers.google.com/crawling/docs/crawlers-fetchers/verify-googlebot
- RFC 9309: https://www.rfc-editor.org/rfc/rfc9309.html
- Sitemaps: https://www.sitemaps.org/protocol.html
