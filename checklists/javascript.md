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

## PASS
PASS only when direct HTTP + raw HTML + rendered DOM + crawler evidence agree on status, content, links and index directives.
