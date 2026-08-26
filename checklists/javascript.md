# JavaScript SEO Checklist

- [ ] Preferred URL returns intended HTTP status on direct request.
- [ ] Raw HTML inspected.
- [ ] Rendered DOM inspected.
- [ ] Critical content appears reliably after render.
- [ ] Critical navigation uses real `<a href>` URLs.
- [ ] Title/canonical/robots deterministic before/after hydration.
- [ ] No initial `noindex` removed later by JS for an indexable page.
- [ ] Missing SPA routes return real 404/410 behavior.
- [ ] Permanent moves use HTTP redirects rather than router-only navigation.
- [ ] JS/CSS/API dependencies needed for public content are crawl-accessible.
- [ ] Console/network/hydration errors checked.
- [ ] Infinite scroll has crawlable paginated/stable URL discovery if deeper content should index.
- [ ] Lazy loading does not require user interaction for index-critical content.
- [ ] LCP media is not incorrectly lazy-delayed.
- [ ] Locale/auth/consent logic does not hide public content from crawlers.
- [ ] Google URL Inspection/rendered output sampled.
- [ ] Relevant non-Google/AI bot behavior checked where important.
- [ ] Dynamic rendering is not the default; if used, reason/parity/security documented.
- [ ] SSR/SSG/hydration/cache behavior tested on staging and live.
- [ ] Release has rollback and before/after evidence.

## PASS criteria

PASS only when direct HTTP, raw HTML, rendered DOM and crawler evidence agree on intended status, main content, crawlable links, canonical/index directives and error handling on representative routes.

## Common failures

- initial HTML ships `noindex`/wrong canonical and JS later changes it;
- navigation is click-only without real `href` URLs;
- SPA fallback returns 200 for nonexistent routes;
- router navigation replaces server-side 3xx redirects for permanent moves;
- hydration removes or changes title/content/schema unexpectedly;
- blocked APIs/JS bundles hide public content from crawlers;
- infinite scroll has no stable crawlable pagination/path;
- user interaction is required to load index-critical content;
- dynamic rendering creates bot/user parity or security risks.

## Retest

1. Request representative routes directly and save status/headers/raw HTML.
2. Render the same routes in a browser/crawler and compare title, canonical, robots, main content and links.
3. Test nonexistent and redirected routes directly, not only client navigation.
4. Check console/network/hydration failures and blocked dependencies.
5. Sample Google rendered output/URL Inspection where available and relevant provider logs for other bots.
6. Re-run after production deployment and mark `PASS`/`FAIL` with before/after evidence and rollback reference.
