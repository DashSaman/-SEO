# SEO Launch Gate Checklist

## Critical preflight
- [ ] Production hostname/DNS/TLS correct.
- [ ] Priority URL samples return expected statuses.
- [ ] Production robots.txt correct; staging rules not copied accidentally.
- [ ] No accidental sitewide `noindex`/X-Robots-Tag.
- [ ] Canonicals point to production preferred URLs.
- [ ] Redirects resolve one hop where possible.
- [ ] Critical rendered content and links present.
- [ ] Analytics/conversion tracking verified.
- [ ] WAF/CDN does not block intended crawlers.

## Discovery
- [ ] Internal navigation links production URLs.
- [ ] Sitemap generated with preferred indexable 200 URLs only.
- [ ] Sitemap URL accessible.
- [ ] Search Console/Bing verification available.
- [ ] IndexNow enabled if intentionally used.

## Content / metadata
- [ ] No placeholder/lorem/test copy.
- [ ] Titles/H1s/page intent sampled across templates.
- [ ] Structured data validates where used.
- [ ] Product/local/international facts correct.
- [ ] Images/video/assets accessible.

## Performance / UX
- [ ] Mobile critical flows tested.
- [ ] Lighthouse/lab regression compared to staging/baseline.
- [ ] Field/RUM instrumentation enabled.
- [ ] LCP hero/media not accidentally lazy-loaded.
- [ ] JS console/network errors checked.

## Risk / rollback
- [ ] Release commit/tag recorded.
- [ ] Old URL mapping preserved if migration.
- [ ] Rollback owner/procedure known.
- [ ] Monitoring alerts active for 5xx/availability.
- [ ] Search/analytics baseline saved.

## PASS / GO criteria

`GO` only when every applicable Critical item is verified on production or a production-equivalent environment and no known issue can block availability, crawlability, indexability, canonicalization, rendering or measurement. Medium/Low issues must have an owner and target date.

## Common failures

- staging `noindex`/robots rules copied to production;
- canonical host/protocol still points to staging/old domain;
- sitemap contains redirects/noindex/test URLs;
- production WAF blocks bots not blocked in staging;
- analytics/consent prevents conversion measurement;
- SPA routes or assets fail only on direct production requests;
- rollback/migration mapping is not available during incident response;
- launch declared successful from homepage-only testing.

## Retest

1. Immediately after release, externally fetch priority URLs, robots, sitemap and critical assets.
2. Verify raw/rendered canonical, robots, title, body content and links on each key template.
3. Test conversion/analytics events and mobile critical flows.
4. Re-run redirects/migration mappings where applicable and check 4xx/5xx/loop alerts.
5. Compare lab/RUM regressions and crawler/WAF logs to baseline.
6. Record `GO/PASS`, `NO-GO/FAIL` or `MONITOR` with timestamp, release commit and saved evidence.
