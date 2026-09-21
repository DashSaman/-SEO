# Structured Data Checklist

- [ ] Identify semantic entity/content type actually visible on page.
- [ ] Check Schema.org definition.
- [ ] If targeting a Google Search feature, check current Google type-specific documentation.
- [ ] Do not assume every Schema.org type is a Google rich-result feature.
- [ ] Prefer JSON-LD when practical/current Google guidance supports it.
- [ ] Required properties present.
- [ ] Recommended properties added only when truthful/available.
- [ ] Values match visible content.
- [ ] Prices/availability/dates/reviews are current.
- [ ] No fabricated aggregate rating/reviews.
- [ ] Organization/Person/Product identifiers are consistent.
- [ ] `sameAs` points only to the same real entity.
- [ ] Canonical page contains the markup.
- [ ] No conflicting duplicate plugin/theme markup.
- [ ] Rich Results Test used for Google-supported features.
- [ ] Schema validator used for vocabulary/syntax as appropriate.
- [ ] Rendered DOM checked when markup is injected by JavaScript.
- [ ] Search Console enhancement reports monitored where available.
- [ ] Rich-result loss not automatically interpreted as ranking loss.
- [ ] Schema count is never a KPI.

## PASS criteria

Markup passes when it is syntactically valid, semantically truthful, matches visible content and — when a Google feature is desired — meets that feature’s current requirements/policies. Search appearance is never guaranteed.

## Common failures

- valid Schema.org type is assumed to be Google rich-result eligible;
- product price/availability/review values disagree with visible content;
- plugins/themes emit duplicate/conflicting Organization/Product/Breadcrumb graphs;
- `sameAs` links to related-but-not-identical entities;
- reviews/ratings are fabricated or self-serving where policy disallows the use case;
- JavaScript-generated JSON-LD disappears or changes after hydration;
- rich-result disappearance is misreported as a ranking penalty;
- teams maximize schema type/property count instead of semantic accuracy.

## Retest

1. Fetch rendered HTML and capture the final JSON-LD actually delivered.
2. Validate syntax/vocabulary with an appropriate schema validator.
3. Run Google Rich Results Test for supported Google features.
4. Compare every material structured-data value with visible page/source-of-truth data.
5. Check canonical URL and duplicate markup from plugins/themes.
6. After deployment, monitor Search Console enhancement reports where available and mark `PASS`/`FAIL` with saved test evidence.
