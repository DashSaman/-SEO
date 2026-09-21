# International SEO Checklist

- [ ] Target country/language/business purpose defined per locale.
- [ ] Distinct stable URL exists for each indexable locale.
- [ ] Visible content is genuinely localized, not only machine-translated labels.
- [ ] Currency/tax/shipping/contact/legal facts localized where relevant.
- [ ] Locale selector is crawlable/user accessible.
- [ ] No mandatory IP redirect blocks alternate locale access.
- [ ] Hreflang codes valid.
- [ ] Hreflang reciprocal relationships present.
- [ ] Hreflang targets return indexable preferred pages.
- [ ] Canonical normally points to the same-locale preferred URL rather than collapsing all languages to one page.
- [ ] `x-default` used only when conceptually appropriate.
- [ ] Sitemaps/architecture segment locales cleanly.
- [ ] Local competitors/SERP intent researched separately per market.
- [ ] Regional search engines considered where material (Baidu/Naver/Yandex etc.).
- [ ] Wrong-locale canonical/ranking cases monitored.
- [ ] Search Console/Bing performance segmented by country/page/query.
- [ ] AI/search citation tests include language/provider context where material.

## PASS criteria

PASS when each target locale is independently accessible, genuinely localized, correctly canonicalized/hreflanged, crawlable without forced georedirects and backed by market-specific search/business evidence.

## Common failures

- all translated pages canonicalize to one language;
- hreflang is non-reciprocal or targets redirects/noindex/404 URLs;
- machine translation changes words but not pricing/legal/logistics/local usefulness;
- IP/language redirects prevent crawlers/users from reaching alternate locale URLs;
- one global keyword/SERP assumption is applied to every country;
- `x-default` is added mechanically without a true default/fallback page;
- country/language performance is merged, hiding wrong-locale ranking.

## Retest

1. Fetch each locale URL directly without locale cookies and verify HTTP/canonical/index state.
2. Validate hreflang codes, reciprocity and target status on representative clusters.
3. Confirm locale selector links are crawlable and forced georedirects do not block access.
4. Compare visible language plus currency/tax/shipping/legal/contact facts to the market brief.
5. Re-run representative SERPs separately per market/language and segment GSC/Bing data.
6. Mark `PASS`/`FAIL` with locale-level evidence; do not pass the whole program because one language works.
