# GSC URL-Inspection Interpretation Pitfalls — observed 2026-11-05

**Evidence class:** OBSERVED, single low-volume Persian B2B property, first-party GSC UI reads on one day (2026-11-05). Not an official Google statement; sample size = a handful of URLs. Reuse as caution flags, not laws.

## Pitfall 1 — Same-day CNI label instability

Two URL-inspection reads of the same URL on the same day returned different index-status labels: `Crawled – currently not indexed` in one read and `Discovered – currently not indexed` in another, hours later. A third URL kept its label stable across reads.

**Implication:** a single CNI-snapshot label is **not stable evidence** for choosing between "crawl-quality problem" vs "discovery/priority problem". Before building a root-cause case, take 2+ reads spaced hours apart, and label the diagnosis `HYPOTHESIS` unless the label is stable across reads AND corroborated by rendered-HTML/canonical/sitemap checks. Never fire repeat indexing requests because the label changed.

## Pitfall 2 — `Referring page: None detected` ≠ orphan page

The same property showed `Referring page: None detected` for a page that **does** have a real in-body link from an indexed page (verified in rendered HTML) and is listed in the submitted sitemap. The field can lag real link discovery on low-priority pages.

**Implication:** before diagnosing "orphan", verify (a) rendered HTML link graph, (b) sitemap membership, (c) crawl date of the linking page. If a linking page exists but Google hasn't recrawled it, the honest fix is *trigger a meaningful recrawl of the linking page* (content change/priority signal), not blanket sitewide link additions.

## Pitfall 3 — Tiny query×page rows cannot license "easy win" claims

A query with ≤4 impressions and a mid-range average position is `INSUFFICIENT_DATA` for an "easy page-one opportunity" claim, even when the SERP looks weak. The SERP weakness observation (labeled `GEO_UNVERIFIED` when location cannot be verified) supports *candidate* status only; label confidence LOW–MEDIUM and set a matured-data retest window.

## Reusable recipe — CNI root-cause file (what is CONFIRMED vs HYPOTHESIS)

CONFIRMED inputs: URL-inspection status (+date), sitemap membership, rendered content depth, robots/canonical directives, count and location of internal inlinks (rendered HTML/DB), HTTP status. HYPOTHESIS inputs (never LIKELY without corroboration): site-level authority, content-quality threshold, duplication, discovery priority. Write the case file with the two lists separated and a decision per hypothesis: `KEEP / DISMISS / NEEDS_EVIDENCE`.
