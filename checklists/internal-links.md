# Internal Linking Checklist

## Discovery
- [ ] Every priority page has at least one crawlable contextual/internal path.
- [ ] No priority orphan URLs.
- [ ] Navigation links use real `<a href>` destinations.
- [ ] Pagination/category paths expose deeper inventory where intended.
- [ ] Important JS interactions have crawlable URL alternatives when needed.

## Architecture
- [ ] Hub→child relationships mirror real information/product hierarchy.
- [ ] Child pages link back to useful parent/context.
- [ ] Related-page links are semantically relevant, not random sitewide blocks.
- [ ] Breadcrumbs reflect hierarchy and resolve to valid preferred URLs.
- [ ] High-value pages are not unnecessarily deep.

## Link quality
- [ ] Anchor text describes destination naturally.
- [ ] No sitewide exact-match keyword stuffing.
- [ ] No hidden/off-screen crawler-only links.
- [ ] No artificial footer tag clouds built solely for ranking.
- [ ] Links benefit users even if search engines ignored them.

## Hygiene
- [ ] No broken priority internal links.
- [ ] Internal links point directly to final URLs rather than redirect chains.
- [ ] Canonicalized-away/non-indexable pages are not heavily promoted unintentionally.
- [ ] Removed products/articles are updated from hubs/navigation.
- [ ] HTTP/HTTPS/www/trailing-slash variants are normalized.

## Measurement
- [ ] Orphan rate tracked.
- [ ] Crawl depth tracked by template/value.
- [ ] Internal links to priority pages compared before/after major architecture changes.
- [ ] Bot logs/crawl data checked after large navigation changes.
- [ ] Ranking/conversion changes annotated, without claiming causal certainty from link count alone.

## PASS criteria

PASS when priority pages are reachable through stable preferred URLs, architecture reflects real user relationships, broken/redirected/internal duplicate paths are controlled and no link pattern exists primarily to manipulate rankings.

## Common failures

- priority landing pages have no crawlable parent/contextual link;
- JS buttons navigate without real `href` links;
- internal links point through chains/old migration URLs;
- sitewide exact-match footer/tag blocks create spammy anchors;
- pagination/facets create effectively infinite crawl spaces;
- canonicalized/noindex URLs continue receiving most internal prominence;
- automated related-content blocks link semantically unrelated pages.

## Retest

1. Re-crawl the affected section and export inlinks/outlinks, status targets, canonical targets and crawl depth.
2. Confirm priority orphan count is zero or intentionally documented.
3. Verify sampled links in rendered HTML as real `<a href>` URLs.
4. Confirm no priority internal links terminate on 3xx/4xx/5xx.
5. Compare before/after depth/inlink distribution and inspect logs after major navigation changes.
6. Mark `PASS` only after live crawl evidence confirms the intended graph; otherwise `FAIL`/`MONITOR`.
