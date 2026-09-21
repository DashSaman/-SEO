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

## PASS criteria

`PASS` only when every applicable Critical/High item above has live evidence, priority URLs are available/crawlable/indexable as intended, canonical/rendered output is correct, and no unresolved blocker can invalidate downstream SEO work.

## Common failures

- staging `noindex` or robots rules shipped to production;
- WAF/CDN returns 403/429 to bots while browser tests look normal;
- sitemap lists redirects/noindex/non-canonical URLs;
- canonical changes after JavaScript hydration;
- click handlers replace crawlable links;
- redirect chains or soft 404s hide migration problems;
- Lighthouse score is treated as proof of search readiness.

## Retest

1. Re-fetch representative priority URLs from an external client and record DNS/TLS/status/headers.
2. Re-fetch `/robots.txt`, rendered HTML and raw HTML; compare robots/canonical/title/critical links.
3. Re-crawl affected templates and confirm no new orphan/redirect/4xx classes.
4. Revalidate sitemap contents and structured data where affected.
5. Sample Search Console/Bing URL status after recrawl/index processing when relevant.
6. Attach before/after output and mark each remediated Critical/High issue `PASS` or `FAIL`.
