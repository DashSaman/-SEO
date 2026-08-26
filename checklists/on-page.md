# On-Page SEO Checklist

- [ ] Page owns a defined intent/query cluster.
- [ ] Preferred URL is stable, readable and canonical.
- [ ] `<title>` is unique, descriptive and aligned with actual content.
- [ ] H1 clearly identifies page topic/job.
- [ ] Heading hierarchy supports comprehension; no heading keyword stuffing.
- [ ] Opening content quickly confirms user landed on the right page.
- [ ] Important entities/terms are named naturally and unambiguously.
- [ ] Facts/specs/prices/dates match current source of truth.
- [ ] Meta description is useful snippet input, not treated as a ranking factor guarantee.
- [ ] Images have descriptive filenames/context and alt text when meaningful.
- [ ] Important media is crawlable and performance-optimized.
- [ ] Internal links point to useful next steps with descriptive anchors.
- [ ] External citations point to authoritative original sources where claims need evidence.
- [ ] No unnecessary exact-match repetition/keyword density target.
- [ ] CTA matches search stage.
- [ ] Canonical/robots directives are correct.
- [ ] Structured data, if present, matches visible content.
- [ ] Author/reviewer/update date shown where it adds trust/value.
- [ ] Mobile rendered page contains same essential content and controls.
- [ ] Page does not depend on user interaction to reveal index-critical main content.
- [ ] Conversion tracking works.
- [ ] Before/after title/content changes are annotated for measurement.

## PASS criteria

PASS requires intent match, truthful useful content, correct canonical/index directives, crawlable rendered main content and a measurable user/business outcome. Plugin scores are advisory only.

## Common failures

- optimizing a page for a query whose SERP wants another page type;
- duplicate/boilerplate title/H1 across page classes;
- metadata promises content the page does not provide;
- keyword-density targets create unnatural repetition;
- hidden/interaction-only critical content;
- schema describes reviews/products/entities that are not visible/true;
- mobile rendering drops important copy/links;
- title/content changes are shipped without a baseline or annotation.

## Retest

1. Fetch raw and rendered HTML and verify title, H1, canonical, robots and critical body content.
2. Re-run target-query intent observation and confirm the page type is still appropriate.
3. Validate internal/external links and structured data where present.
4. Test mobile output and CTA/conversion tracking.
5. Compare before/after page snapshot and annotate deploy date.
6. Mark `PASS` only when all applicable High/Critical on-page issues are resolved; otherwise `FAIL`/`MONITOR`.
