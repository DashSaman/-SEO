# Post-Launch SEO Checklist

Use after a launch, major content release, template change, migration, international rollout, structured-data deployment, or crawler/WAF change.

## Immediate live validation
- [ ] Priority URLs return expected HTTP statuses.
- [ ] Redirects resolve to intended final URLs without loops/chains.
- [ ] Production robots.txt is accessible and correct.
- [ ] Robots meta / X-Robots-Tag matches intended indexability.
- [ ] Canonicals point to preferred live URLs.
- [ ] Critical content, links, title and metadata are present in rendered output.
- [ ] Structured data validates where applicable.
- [ ] Analytics, consent and conversion tracking are firing correctly.
- [ ] No staging hostname, placeholder content or test data leaked into production.

## Crawl / index follow-up
- [ ] Search Console URL Inspection sampled for critical templates.
- [ ] Page Indexing reports monitored for unexpected exclusions.
- [ ] Bing Webmaster URL/sitemap state sampled where relevant.
- [ ] XML sitemap contains only intended preferred canonical indexable URLs.
- [ ] Sitemap `lastmod` reflects meaningful updates rather than every build.
- [ ] IndexNow events sent only for actual add/update/delete changes when used.
- [ ] Server/CDN logs confirm Googlebot/Bingbot/intended AI crawlers are not accidentally blocked.
- [ ] 404/410/5xx/429 spikes investigated.

## Performance / rendering
- [ ] Field/RUM Core Web Vitals monitored by template/device/region.
- [ ] Lighthouse/lab results compared against pre-launch baseline for diagnosis.
- [ ] JavaScript console/network/hydration regressions checked.
- [ ] LCP media, lazy loading and third-party scripts reviewed for regressions.
- [ ] SPA/deep routes still work on direct request.

## Search performance
- [ ] Launch date annotated in analytics/GSC/BWT/rank tracking.
- [ ] Branded and non-branded query trends separated.
- [ ] Priority page impressions/clicks/positions monitored over an appropriate window.
- [ ] Query-to-page mapping checked for cannibalization/wrong URL ranking.
- [ ] SERP features and dominant page type rechecked if performance changes materially.
- [ ] Local/international results are measured in their actual geography/language.

## Business outcomes
- [ ] Leads/revenue/signups/bookings tracked, not traffic only.
- [ ] Lead quality or downstream CRM outcome reviewed where available.
- [ ] Conversion changes separated from ranking/traffic changes.
- [ ] Broken forms, phone tracking, checkout or booking flows investigated immediately.

## AI search visibility
- [ ] ChatGPT referrals measured where present (`utm_source=chatgpt.com`).
- [ ] Bing AI Performance citations/cited pages/grounding queries reviewed where available.
- [ ] Google Generative AI performance reporting reviewed where available.
- [ ] Controlled prompt/query observation set rerun only with provider/date/language context.
- [ ] Citation count is not treated as ranking, authority, traffic or conversion.

## Migration-specific follow-up
- [ ] Old→new mappings sampled repeatedly.
- [ ] Old high-value URLs do not fall to 404 unexpectedly.
- [ ] Old internal links/sitemaps/backlinks updated where practical.
- [ ] User-declared vs search-engine-selected canonical mismatches monitored.
- [ ] Old domain/host infrastructure remains available long enough for redirects.

## Content / inventory lifecycle
- [ ] Prices, stock, product/service availability and dates remain current.
- [ ] Removed entities/products/articles are handled intentionally.
- [ ] No accidental low-value programmatic URL explosion after launch.
- [ ] New tag/search/facet/query-parameter crawl space reviewed in logs.
- [ ] Editorial/update owner assigned for time-sensitive pages.

## Incident thresholds
Escalate immediately when any of the following occurs:

- sitewide/priority-template `noindex` or robots block;
- canonical points to wrong domain/page class;
- major 5xx/availability failure;
- large migration redirect failure;
- private/staging content exposed;
- severe conversion tracking outage;
- high-value pages disappear from index unexpectedly;
- WAF blocks intended search crawlers at scale.

## PASS criteria

PASS when live output matches intended release state, crawler/index/analytics evidence is healthy, Critical/High regressions are absent or fixed with retest evidence, and search/business outcomes are being monitored against an annotated baseline over an appropriate window.

## Common failures

- monitoring only rankings while indexation/conversion errors go unnoticed;
- assuming an unchanged homepage means all templates are healthy;
- unannotated launches make before/after diagnosis impossible;
- delayed WAF/429 or JS regressions appear only after crawler/user load;
- Search Console exclusions or selected-canonical changes are ignored;
- local/international measurements use the wrong geography/language;
- AI citation changes are merged with ordinary search traffic or treated causally;
- temporary migration volatility causes new destructive changes before root-cause diagnosis.

## Retest

1. Re-run immediate live validation after every Critical/High remediation.
2. Repeat crawler/index checks after search-engine processing rather than relying only on launch-day output.
3. Re-crawl priority templates and migration mappings; inspect logs for bot/status/crawl-space regressions.
4. Compare RUM/CWV, queries, conversions and business metrics to the saved annotated baseline.
5. Re-run provider-specific AI/search observations with date/language/model context when relevant.
6. Close an issue only with before/after evidence and explicit `PASS`; otherwise retain `FAIL`/`MONITOR` with owner and next review date.
