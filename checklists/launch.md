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

## GO decision
Launch only when all Critical items pass. Medium/Low known issues must be documented with owner/date rather than silently ignored.
