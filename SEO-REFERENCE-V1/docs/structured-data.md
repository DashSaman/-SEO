# Structured Data / Schema.org Reference (2026)

**Reviewed:** 2026-08-26  
**Primary sources:** Schema.org + Google Search Central structured-data documentation.

## 1. Separate vocabulary from search feature

This distinction prevents many SEO mistakes:

- **Schema.org** defines a shared vocabulary of types/properties that can be expressed with formats such as JSON-LD, Microdata or RDFa.
- **Google Search structured-data documentation** defines which Schema.org concepts Google supports for particular Search features/rich results and what policies/required properties apply.

A Schema.org-valid type/property is **not automatically a Google rich-result feature**.

Sources:

- [Schema.org getting started](https://schema.org/docs/gs.html)
- [Google introduction to structured data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)

## 2. Formats

Google currently supports:

- JSON-LD (recommended by Google in most cases for maintainability);
- Microdata;
- RDFa.

Choose a format your stack can produce accurately and consistently. JSON-LD is usually easiest to centralize/test, but format choice does not excuse inaccurate data.

## 3. What structured data can do

Structured data can:

- give explicit machine-readable clues about entities and properties on a page;
- make a page eligible for supported rich-result/search appearances;
- improve consistency of organization/product/article/event/etc facts across machine consumers.

It does **not**:

- guarantee a rich result;
- guarantee ranking improvement;
- replace visible page content;
- justify fake reviews/ratings/entities;
- create an AI-specific ranking advantage by itself.

Google explicitly says correct markup enables eligibility but does not guarantee a rich-result appearance.

## 4. Google quality rules

Source: [General structured data guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)

Structured data should:

- represent the main/visible content accurately;
- be current;
- be relevant to the page;
- include feature-specific required properties;
- avoid misleading/fabricated values;
- use crawlable/indexable referenced image URLs when relevant;
- comply with Search Essentials/spam policies and feature-specific policies.

A structured-data manual action can remove rich-result eligibility without necessarily changing ordinary web-ranking position. Do not confuse rich-result penalties with a generic site ranking penalty.

## 5. Implementation model

For every template:

1. identify the real primary entity/page type;
2. map only facts you actually have;
3. choose the most specific appropriate Schema.org type;
4. check whether Google/other target engines support a relevant search feature;
5. satisfy required properties;
6. add recommended properties only when accurate/available;
7. ensure markup matches visible content;
8. validate syntax;
9. inspect rendered output;
10. deploy to a small sample;
11. inspect in search-engine tools;
12. monitor enhancement/rich-result reports and regressions.

## 6. Entity graph design

Stable identifiers help keep relationships coherent. A useful JSON-LD graph may connect real entities with `@id` values, for example:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://example.com/#organization",
      "name": "Example Company",
      "url": "https://example.com/"
    },
    {
      "@type": "WebSite",
      "@id": "https://example.com/#website",
      "url": "https://example.com/",
      "publisher": { "@id": "https://example.com/#organization" }
    }
  ]
}
```

The goal is factual consistency, not making the graph artificially large.

## 7. Common page/entity types to evaluate

Depending on actual business/content:

- `Organization` / appropriate subtype;
- `WebSite` / `WebPage`;
- `BreadcrumbList`;
- `Article` / `NewsArticle` / `BlogPosting`;
- `Product` / `Offer` and merchant-related properties;
- `LocalBusiness` and appropriate subtype;
- `VideoObject`;
- `Event`;
- `JobPosting`;
- `ProfilePage`;
- `DiscussionForumPosting` / Q&A types where content genuinely matches;
- `Dataset`;
- `SoftwareApplication`;
- subscription/paywall signals where supported.

Always check current Google Search appearance documentation because feature eligibility changes.

## 8. Organization markup

Google’s current Organization guidance recommends using organization information on a home/about organization page rather than mechanically duplicating an enormous block everywhere. Use the most specific appropriate subtype where documented.

Useful real facts may include:

- legal/brand name;
- URL;
- logo;
- contact information where supported;
- address for a real physical organization;
- identifiers;
- relevant `sameAs` profiles that truly represent the same organization.

`sameAs` is not a backlink-building tactic. Link only to authoritative identity-equivalent profiles/pages.

## 9. Product / ecommerce

Current Google product documentation distinguishes:

- **Product snippets** — including editorial/non-purchase contexts where appropriate;
- **Merchant listings** — purchase pages with merchant-focused properties.

For merchant listings, Google currently expects pages where shoppers can actually purchase the product and has page/product-specific eligibility rules.

Product data must match reality:

- name/variant;
- price/currency;
- availability;
- condition;
- shipping/returns where supported;
- valid reviews/ratings only;
- stable product identifiers where applicable.

Synchronize structured data with merchant/feed/backend data; conflicting price/availability erodes reliability.

## 10. Reviews and ratings

Never generate fake review markup. Only mark up reviews/ratings that meet the applicable feature policies and reflect genuine user/editorial data visible/represented appropriately.

Common failure modes:

- rating markup for values users cannot see;
- business self-rating practices that violate feature rules;
- aggregate values inconsistent with actual reviews;
- copying ratings from another site;
- marking every page with organization stars regardless of content.

## 11. Article / author

Article markup can clarify:

- headline;
- author;
- dates;
- images;
- publisher relationships.

Keep visible byline/date/content consistent with markup. Do not invent an expert author persona solely for SEO.

## 12. Local business

LocalBusiness markup can help express real business facts, but it does not replace a correctly managed business profile/maps ecosystem.

Keep NAP and identity information consistent across:

- site;
- business profile/map listing;
- structured data;
- authoritative directory/industry profiles.

Do not create fictional locations or addresses for location-page ranking.

## 13. Video/images

For video markup, ensure the page is genuinely about/hosts the video and the video/thumbnail URLs are accessible. Provide accurate name/description/upload dates and supported properties.

For image properties, Google’s structured-data policies require relevant, crawlable/indexable image URLs for supported features.

## 14. Paywalled/subscription content

Search engines/platforms may support specific paywall signals. Applebot’s current documentation, for example, supports page-level `isAccessibleForFree` to identify paywalled/subscription content for Apple-specific behavior. Google has its own subscription/paywall documentation.

Do not assume one platform’s semantics apply everywhere.

## 15. Validation stack

Use multiple layers:

- schema syntax/vocabulary validator;
- Google Rich Results Test for Google-supported features;
- URL Inspection/rendered output;
- Search Console rich-result/enhancement reports;
- crawler extraction across templates;
- automated unit/CI validation for generated JSON-LD.

### CI invariants worth testing

- valid JSON;
- no empty required values;
- URLs absolute/canonical;
- price/date formats valid;
- page data equals structured-data values;
- no staging hostnames;
- only one intended primary entity ID per stable entity;
- no duplicated/conflicting scripts emitted by multiple plugins.

## 16. Common WordPress/CMS failure mode

Multiple plugins/theme modules may output overlapping Organization, WebSite, Breadcrumb, Article or Product graphs with conflicting IDs/data. Audit the final rendered page, not just each plugin setting screen.

Prefer one clear owner for each entity graph where possible.

## 17. AI-search myths

Google’s 2026 generative Search guide states:

- structured data is not required specifically for generative AI Search;
- there is no special AI schema required;
- normal structured data remains useful in overall SEO where appropriate.

Therefore use schema because it accurately describes content/entities and supports search/platform features, not because a vendor claims “10x ChatGPT ranking from schema.”

## 18. Maintenance

Structured-data reference files become stale quickly. Re-check:

- supported Google rich-result feature list;
- required/recommended fields;
- deprecated feature types;
- product/merchant policy changes;
- manual-action policies;
- schema vocabulary changes;
- platform-specific AI/paywall directives.

## Sources

- https://schema.org/docs/gs.html
- https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- https://developers.google.com/search/docs/appearance
- https://developers.google.com/search/docs/appearance/structured-data/product
- https://developers.google.com/search/docs/appearance/structured-data/merchant-listing
- https://developers.google.com/search/docs/appearance/structured-data/organization
