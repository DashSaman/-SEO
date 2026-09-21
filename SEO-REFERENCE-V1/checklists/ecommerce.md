# Ecommerce SEO Checklist

## Architecture
- [ ] Categories/subcategories reflect real shopping intent.
- [ ] Products reachable from crawlable category/internal links.
- [ ] Facet/indexability matrix documented.
- [ ] Sort/session/tracking URLs not creating crawl explosion.
- [ ] Pagination/deep inventory crawlable where intended.

## Products
- [ ] Unique accurate product name/specifications.
- [ ] Price/currency/availability current.
- [ ] Variants have defined URL/canonical policy.
- [ ] Manufacturer copy enhanced with genuine value where needed.
- [ ] High-quality images/video accessible and optimized.
- [ ] Shipping/returns/warranty clear.
- [ ] Reviews/ratings authentic.

## Structured data / feeds
- [ ] Product structured data matches visible facts.
- [ ] Merchant feed and page price/availability agree.
- [ ] No fake reviews/aggregateRating.
- [ ] Rich Result/Merchant issues monitored.

## Lifecycle
- [ ] Temporary stockout handling defined.
- [ ] Permanently removed item handling defined.
- [ ] Equivalent replacement redirects only when truly equivalent.
- [ ] Dead products removed from sitemap/navigation when appropriate.

## Technical/performance
- [ ] Canonical URLs clean.
- [ ] Sitemap includes preferred 200 indexable inventory.
- [ ] JS filters do not hide crawlable products.
- [ ] LCP image/third-party scripts/CWV checked by template.
- [ ] Bot logs checked for facet waste on large catalogs.

## Measurement
- [ ] Organic revenue/conversions by category/product tracked.
- [ ] Indexed/submitted inventory by template tracked.
- [ ] Zero-value indexed facet rate monitored.
- [ ] Search/merchant/AI visibility separated.

## PASS criteria

PASS when real inventory is crawlable/discoverable, duplicate facet space is controlled, product/page/feed/schema facts agree, variant/lifecycle policy is explicit and success is measured in transactions/revenue rather than indexed-URL count alone.

## Common failures

- uncontrolled facets/sorts/session parameters create crawl/index bloat;
- product variants compete with conflicting canonicals;
- page price/availability differs from Product markup or merchant feed;
- removed products stay in navigation/sitemaps indefinitely;
- stockout pages are deleted/redirected without lifecycle logic;
- manufacturer descriptions are copied at scale with no additional value;
- JS filters hide inventory from crawlable links;
- fake/unsupported review markup is published.

## Retest

1. Re-crawl category/product/facet samples and classify 200/indexable/canonical/noindex/redirect states.
2. Compare visible product facts with Product JSON-LD and merchant-feed values.
3. Verify variant canonicals, pagination and sitemap contents.
4. Test temporary and permanent product-lifecycle scenarios.
5. Review bot-log facet waste and field/lab performance by template where scale warrants it.
6. Re-check organic conversions/revenue and indexed inventory after an appropriate window; mark `PASS`/`FAIL` with evidence.
