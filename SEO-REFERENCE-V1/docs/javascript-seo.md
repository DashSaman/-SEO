# JavaScript SEO — Production Rendering Playbook

**Reviewed:** 2026-08-26  
**Primary source:** Google JavaScript SEO documentation and current rendering guidance.

## Core principle

Google can render modern JavaScript with evergreen Chromium, but “Google can render JS” does not mean every JavaScript architecture is equally reliable, fast or accessible to every search/AI crawler. Prefer architectures that make critical content, links, metadata and status meaning available without unnecessary rendering dependencies.

## Rendering models

### SSR — Server-Side Rendering

HTML is generated on the server for the request.

**Good for:** dynamic public pages that need immediate complete HTML.  
**Risks:** server cost, cache complexity, hydration bugs.  
**SEO advantage:** critical content/links/meta can be visible in initial response.

### SSG — Static Site Generation

HTML is prebuilt.

**Good for:** documentation, marketing, blogs, many catalog pages with manageable build/update workflows.  
**Risks:** stale builds, huge build times at extreme scale.  
**SEO advantage:** predictable HTML, CDN-friendly, low rendering dependency.

### CSR — Client-Side Rendering

Initial HTML shell relies heavily on JavaScript to create meaningful page content.

**Good for:** authenticated applications and interactive surfaces where search indexing is not primary.  
**Risks for public SEO pages:** delayed/failed content, crawler differences, JS errors, blocked resources, metadata/routing mistakes.  
**Rule:** if CSR is used for indexable pages, verify rendered HTML in Search Console/Chrome and with relevant non-Google bots.

### Hydration / islands / hybrid rendering

Pre-render meaningful HTML, then attach interactivity. Often a strong default for search-facing applications when implemented without hydration mismatch or content replacement bugs.

## Dynamic rendering — legacy workaround

Google’s current documentation explicitly says dynamic rendering **was a workaround and is not a recommended long-term solution**. Google recommends server-side rendering, static rendering or hydration where possible. Dynamic rendering also adds bot detection, rendering infrastructure and parity/cloaking risk.

Source: https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering

## Crawlable links

Critical navigation/internal links should render as real anchors with resolvable URLs:

`<a href="/path/">Descriptive anchor</a>`

Avoid relying solely on click handlers, non-anchor elements or client state with no crawlable destination. Verify menus, pagination, breadcrumbs, related items and canonical paths after hydration.

## Metadata

For indexable URLs verify in rendered output:

- unique `<title>`;
- appropriate meta description;
- robots directives;
- canonical;
- hreflang where used;
- structured data;
- social tags as a presentation concern;
- correct HTTP status behavior at the server/edge when possible.

Avoid racing multiple client components to rewrite canonical/robots/title after load.

## Canonical with JavaScript

A JS-generated canonical can be processed, but server/pre-rendered consistency is safer. Do not initially emit one canonical and then replace it with another after hydration. Keep sitemap/internal links/redirect/canonical signals aligned.

## `noindex` and JavaScript

Do not serve `noindex` initially and remove it with JavaScript hoping Google will index the final state. Search processing may respect the initial directive and not execute the path you expected. Render the intended indexability state deterministically.

## Redirects

Prefer HTTP redirects for permanent/temporary URL changes. Client-side routing should not become a substitute for correct server redirects during migrations or canonical consolidation.

## HTTP status codes

SPAs often return `200` for every route, including nonexistent pages. This can create soft-404/index-quality problems. Make the edge/server return meaningful `404`, `410`, `301/308`, `302/307`, `5xx` statuses where appropriate, or use framework mechanisms that produce equivalent crawl-visible behavior.

## Lazy loading

Lazy-load media and secondary content without requiring user gestures to expose index-critical content. Test:

- image `src/srcset` behavior;
- native `loading="lazy"` where appropriate;
- intersection-observer fallbacks;
- content loaded only after scroll/click;
- LCP hero images accidentally delayed;
- structured-data references to assets that bots cannot fetch.

## Infinite scroll

An infinite interface needs crawlable paginated URLs or another deterministic URL sequence if deeper items should be discovered/indexed. Each page state should have stable content and links. Do not require simulated scrolling for discovery.

## Hydration mismatch risks

Common failures:

- server title/content differs from client content;
- server canonical points to wrong variant;
- React/Vue hydration replaces meaningful HTML with an error/empty state;
- locale detection changes content/URL after load;
- consent/auth checks hide public content from crawlers;
- random/time-dependent IDs alter markup;
- edge cache mixes locales/users.

Test console errors and final DOM, not just source HTML.

## Blocked resources

If critical JS/CSS/API resources are blocked by robots/WAF/auth, rendered content can fail. Ensure intended search crawlers can fetch public dependencies needed to understand the page. Never expose private APIs just for SEO; public pages should have safe public rendering paths.

## SPA routing

For indexable SPA routes:

- every canonical page gets a stable URL;
- direct URL request works without prior client navigation;
- history fallback does not turn missing URLs into fake 200 pages;
- canonical/title/content update correctly per route;
- internal anchors have real hrefs;
- sitemap lists preferred URLs only.

## Framework notes

### Next.js

Use framework-native metadata and server/static rendering patterns where appropriate. Test `generateMetadata`, canonical/robots, route status handling and cached/revalidated content. Tools such as `next-sitemap` can help generate inventories but do not decide indexability quality.

### Nuxt

Use current Nuxt/Nuxt SEO modules as implementation helpers, but inspect server-rendered HTML and do not accept “AEO/GEO” marketing claims as engine rules.

### React/Vue/Angular generic

SEO outcome depends on delivered HTTP/HTML/rendered state, not the framework brand. Audit direct navigation, rendering, status codes, links, metadata and API failure behavior.

## Test matrix

For every critical template sample:

1. `curl -I` — status/redirect/cache headers.
2. fetch raw HTML — title/canonical/robots/critical content/links.
3. browser with JS enabled — final DOM and console/network errors.
4. browser with JS disabled — assess what remains available (not a Googlebot emulator, but useful dependency diagnostic).
5. Google URL Inspection / rendered screenshot where available.
6. Rich Results Test for supported structured data.
7. Lighthouse + field/RUM data for performance.
8. server logs — verify real Googlebot/Bingbot/other intended crawlers fetch important routes/resources.
9. relevant AI crawler/WAF allow rules — provider-specific.

## Release Quality Gate

PASS when:

- preferred URL returns intended status;
- critical content and links are present in initial or reliably rendered output;
- canonical/robots/title are deterministic;
- no index-critical resource requires login/user action;
- 404s are real 404/410 behavior;
- redirects are server-visible;
- pagination/deep navigation is crawlable;
- hydration has no content/metadata mismatch;
- performance is within acceptable field targets;
- bot/WAF logs show no accidental blocking.

FAIL when:

- search eligibility depends on a bot-specific hidden version;
- blank shell/JS exception is common;
- client-only router returns 200 for all missing pages;
- canonical/robots flip unpredictably after load;
- important links have no `href`;
- dynamic rendering is introduced as the default without documented necessity.

## Sources

- Google JS SEO basics: https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics
- Dynamic rendering: https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering
- Canonicalization: https://developers.google.com/search/docs/crawling-indexing/canonicalization
- Google Images lazy-loading/context: https://developers.google.com/search/docs/appearance/google-images
