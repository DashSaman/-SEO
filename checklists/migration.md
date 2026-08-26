# SEO Migration / Relaunch Checklist

## Before
- [ ] Full old URL inventory captured from crawl, sitemap, analytics, GSC/BWT, backlinks/logs where available.
- [ ] Old→new URL mapping defined one-to-one where equivalent.
- [ ] No blanket redirect of unrelated URLs to homepage.
- [ ] New information architecture crawled on staging.
- [ ] Staging protected from public indexing with real access controls as needed.
- [ ] Canonical/robots/noindex/hreflang/schema templates tested.
- [ ] Analytics/conversions/consent configured.
- [ ] DNS/TLS/CDN plan and rollback documented.
- [ ] Critical rankings/traffic/revenue baseline exported.

## Launch
- [ ] Production index directives correct.
- [ ] Permanent changes use 301/308.
- [ ] Redirects are one hop.
- [ ] Internal links point to new final URLs.
- [ ] Canonicals point to new preferred URLs.
- [ ] Hreflang updated reciprocally.
- [ ] XML sitemaps list new preferred URLs.
- [ ] Search Console/Bing properties/verification ready.
- [ ] Google Change of Address used when applicable to domain move.
- [ ] Key backlinks/partners updated where practical.
- [ ] 404/5xx/redirect loops monitored in real time.

## After
- [ ] Live crawl compares mapped URLs and statuses.
- [ ] Priority URL Inspection/indexing sampled.
- [ ] Logs confirm bot access.
- [ ] Old URLs continue redirecting.
- [ ] Old sitemap can be retained temporarily for discovery diagnostics if strategy requires, while new sitemap is submitted.
- [ ] Traffic/rank/conversion changes annotated daily/weekly.
- [ ] Unmapped high-value 404s investigated.
- [ ] Canonical mismatch/excluded pages investigated.
- [ ] Redirects retained long enough; Google generally recommends at least one year for site moves.
- [ ] No old domain/assets shut down prematurely.

## PASS
Migration passes when mapped priority URLs resolve one hop to equivalent new pages, new pages are indexable/canonical/discoverable, bot/user errors are controlled and search/business trends are monitored against baseline. Temporary volatility is expected; do not reverse good mappings solely from a few days of data.
