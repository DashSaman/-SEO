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

## PASS criteria

Migration passes when mapped priority URLs resolve one hop to equivalent new pages, new pages are indexable/canonical/discoverable, internal links/sitemaps/hreflang use final URLs, user/bot errors are controlled and search/business trends are monitored against a saved baseline.

## Common failures

- blanket redirecting old URLs to homepage or unrelated categories;
- staging `noindex`/robots rules reach production;
- redirect chains, loops or unmapped high-value URLs;
- canonicals/sitemaps/internal links still reference old URLs;
- hreflang points across old/new URL sets inconsistently;
- DNS/TLS/CDN changes are mixed with migration without rollback evidence;
- old domain/redirect infrastructure is shut down too early;
- normal short-term volatility triggers destructive rollback without diagnosing mappings/indexing.

## Retest

1. Re-run the complete old→new mapping list and record status/final URL/hops.
2. Crawl the new site and confirm canonical/internal-link/sitemap/hreflang consistency.
3. Sample raw/rendered output and GSC/Bing URL inspection on highest-value templates.
4. Inspect logs plus 404/5xx/loop reports after launch.
5. Compare traffic/query/conversion metrics against the saved pre-launch baseline with annotations.
6. Mark `PASS` only when Critical/High mapping/indexation errors are resolved; otherwise `FAIL`/`MONITOR` with owner and rollback decision.
