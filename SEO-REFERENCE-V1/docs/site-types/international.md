# International / Multilingual SEO Playbook

Use with `../international-seo.md`.

## Decide scope first

Separate:
- multilingual: same market, multiple languages;
- multiregional: different countries/regions;
- both.

Do not create country folders merely because a keyword tool shows volume; each locale needs a business/content/fulfillment reason.

## URL strategy

Prefer distinct stable locale URLs such as subdirectories/subdomains/country domains according to business needs. Avoid forcing all markets through one locale-adaptive URL when content must be independently discovered and controlled.

## Localization

Translate meaning, not just strings:
- terminology;
- currency/tax;
- shipping/service availability;
- legal/contact information;
- examples and cultural context;
- local product names;
- CTAs and support.

Google detects language primarily from visible content; `hreflang`/HTML `lang` do not substitute for real localized content.

## Hreflang

For alternate equivalents:
- valid language/region codes;
- reciprocal annotations;
- self-reference where appropriate;
- URLs return successful indexable content;
- canonical normally aligns within locale page, not all locales canonicalized to one language;
- `x-default` only when conceptually appropriate.

## Geolocation / redirects

Avoid mandatory IP/language redirects that prevent users or crawlers from choosing/accessing another locale. Provide a visible locale selector and persistent URLs.

## Market research

Measure each market separately:
- SERP intent/page types;
- local competitors;
- local search engines where material (Baidu/Naver/Yandex etc.);
- brand familiarity;
- local backlinks/media/directories;
- mobile/device behavior;
- legal/commercial constraints.

## Sitemaps / architecture

Locale hubs should link to their own important sections. Sitemaps can be segmented by locale for diagnostics. Keep alternate and canonical signals internally consistent.

## KPIs

- clicks/conversions by country/language;
- correct-locale landing rate;
- hreflang errors;
- wrong-locale ranking/canonical cases;
- indexed locale URLs;
- local referring domains/brand demand;
- AI/search citations by language/provider.

## PASS gate

PASS when each locale has stable URLs, real localization, correct canonical/hreflang relationships, accessible locale switching, market-specific SERP research and business-supported fulfillment. FAIL when pages are auto-translated keyword clones or redirects make alternate locales inaccessible.
