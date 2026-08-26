# Technical SEO Checklist

Use with `SEO_AUDIT_SOP.md` and `docs/technical-seo.md`.

## Availability / HTTP
- [ ] DNS/TLS valid.
- [ ] Priority URLs load externally.
- [ ] Preferred pages return `200`.
- [ ] Permanent moves use `301/308` and one-hop targets.
- [ ] Missing/permanently removed content returns correct `404/410` when no equivalent exists.
- [ ] No widespread soft-404 or SPA “200 for everything”.
- [ ] No 5xx/429 spike affecting crawlers/users.

## Crawl / index
- [ ] `/robots.txt` returns expected rules per hostname.
- [ ] robots is not being used as security/access control.
- [ ] Priority pages not accidentally blocked.
- [ ] robots meta/X-Robots-Tag matches intent.
- [ ] `noindex` pages are crawlable when bot must see directive.
- [ ] WAF/CDN does not block intended search/AI crawlers.
- [ ] Search Console Page Indexing sampled.
- [ ] Bing Webmaster status sampled where relevant.

## Canonical / duplicates
- [ ] One preferred canonical per indexable page.
- [ ] HTML canonical, redirects, sitemap and internal links align.
- [ ] No canonical points to non-equivalent page.
- [ ] Parameters/session/sort duplicates controlled.
- [ ] HTTP/www/trailing-slash variants consolidate consistently.

## Architecture / links
- [ ] Priority pages reachable via real `<a href>` links.
- [ ] No critical orphan pages.
- [ ] Crawl depth reasonable for important pages.
- [ ] Breadcrumbs/hubs coherent.
- [ ] No large internal link set points to redirects/404s.
- [ ] Pagination/deep inventory discoverable without user-only gestures.

## Sitemaps
- [ ] Sitemaps contain preferred canonical indexable 200 URLs only.
- [ ] Sitemap limits respected.
- [ ] `lastmod` changes only for meaningful updates.
- [ ] Deleted/noindex/redirect URLs removed.
- [ ] Submitted in relevant webmaster tools.

## JavaScript/rendering
- [ ] Critical content visible in reliable rendered output.
- [ ] Critical links have hrefs.
- [ ] Title/canonical/robots do not flip incorrectly after hydration.
- [ ] Direct navigation to SPA routes works.
- [ ] No critical JS/CSS/API blocked.
- [ ] Dynamic rendering not used as default architecture without documented need.

## Performance
- [ ] Field CWV reviewed where available.
- [ ] LCP target ≤2.5s.
- [ ] INP target <200ms.
- [ ] CLS target <0.1.
- [ ] Lab tools used for diagnosis, not ranking-score claims.
- [ ] Mobile/template/region segmentation checked.

## Special
- [ ] Hreflang reciprocal/canonical relationships correct if international.
- [ ] Facets finite and intentional if ecommerce/directory.
- [ ] Product/local/video/image requirements tested where relevant.
- [ ] Server logs reviewed for large/high-change sites.

## Release evidence
- [ ] Before state captured.
- [ ] Change/commit annotated.
- [ ] Live after state captured.
- [ ] Critical/High fixes explicitly `PASS` after retest.
- [ ] Rollback path known.
