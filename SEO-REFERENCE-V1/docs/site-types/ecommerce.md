# Ecommerce SEO Playbook

Use with `../ecommerce-seo.md`.

## Architecture

`Home → Department → Category → Subcategory → Product`

Make categories useful landing pages; do not expose every sort/filter combination as an indexable URL.

## Priority query types

- category/product-type commercial queries;
- brand/model/SKU product queries;
- problem/use-case categories;
- comparisons/buying guides;
- local/store inventory where relevant.

## Category pages

Need:
- inventory matching intent;
- stable canonical URL;
- useful filtering;
- concise category context where helpful;
- internal links to important subcategories/products/guides;
- pagination/incremental loading with crawlable discovery.

## Product pages

Maintain:
- unique product title/specifications;
- price/currency/availability;
- variants and canonical strategy;
- high-quality media;
- genuine reviews/ratings;
- shipping/returns/warranty facts;
- Product structured data matching visible data;
- merchant feed consistency.

## Facets

Classify each filter as:
- indexable search landing;
- user-only non-indexable state;
- blocked/non-discoverable parameter where appropriate.

Prevent combinatorial crawl space and duplicate parameter ordering.

## Out-of-stock lifecycle

Distinguish temporary stockout from permanent removal. Keep temporarily unavailable pages useful if product will return. For permanently gone items, choose 404/410 or a genuinely equivalent replacement redirect; do not redirect everything to category/home.

## Merchant ecosystem

Use both on-page Product structured data and Merchant Center/feed capabilities where appropriate. Feed/on-page price and availability must agree.

## Content support

Create buying guides/comparisons only where they help choose products. Link guides to relevant categories/products and vice versa.

## Performance

Prioritize LCP product/category hero media, JS/filter performance, image sizing, third-party scripts and mobile checkout/search experience. Measure field CWV by template.

## KPIs

- non-brand category/product clicks;
- indexed preferred SKU/product/category URLs;
- organic revenue/conversion rate;
- free listing/shopping visibility where applicable;
- product rich-result/merchant errors;
- crawl share spent on preferred vs facet URLs;
- stock/stale data errors.

## PASS gate

PASS when preferred inventory is crawlable/indexable, facets are controlled, product facts/schema/feed agree, stock lifecycle is defined, internal discovery is strong and organic performance is tied to revenue rather than indexed-page count.
