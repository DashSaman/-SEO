# SEO_AUDIT_SOP.md — Severity-Based Audit and Retest Procedure

**Version:** 2026-08-26  
**Rule:** diagnose in dependency order. Do not optimize titles/schema/backlinks while security, availability, transport, crawl, index, canonical or rendering blockers remain.

## Severity model

- `CRITICAL` — site/large priority set unavailable, accidentally blocked/deindexed, security/privacy exposure or severe migration failure.
- `HIGH` — material index/canonical/rendering/architecture issue affecting priority pages or revenue.
- `MEDIUM` — meaningful quality/discovery/performance issue with bounded impact.
- `LOW` — cleanup/opportunity; no evidence of material current harm.
- `INFO` — observation requiring no action unless context changes.

Every issue must contain: **Severity → Impact → Evidence → Diagnosis → Fix → Verification → Retest → Result** plus owner/date/deploy context.

---

## 1. Security / privacy / unauthorized exposure

**Check:** hacked/spam pages, private/staging/admin exposure, secrets/user data in URLs/source, authentication boundaries, TLS/security anomalies and crawler impersonation.

**CRITICAL examples:** private customer data indexable; compromised pages; security depending on robots.txt.

**Fix:** repair access control first. `robots.txt` is not authentication/authorization.

**Verification / Retest:** unauthenticated requests, affected URL/index state, logs/security scanner and removal workflows where needed.

---

## 2. Site availability

Test homepage plus representative critical templates from an external network/region.

Evidence: uptime, origin/CDN health, browser render and representative endpoint availability.

`CRITICAL`: sustained outage or widespread 5xx/unreachable service.

---

## 3. DNS / HTTPS / HTTP transport

Check before interpreting page semantics:

- DNS resolution/A/AAAA/CNAME as applicable;
- intended hostnames resolve to intended infrastructure;
- TLS certificate validity/hostname/chain;
- HTTP→HTTPS and host normalization;
- CDN/origin routing;
- HSTS/edge behavior where material;
- IPv4/IPv6 differences where material.

`CRITICAL/HIGH`: domain fails resolution, certificate breaks production, old/staging host becomes canonical, CDN routes major traffic to wrong origin.

**Verification / Retest:** independent DNS lookup + TLS/HTTP request from representative locations/clients.

---

## 4. HTTP status semantics

Sample and crawl:

- preferred pages → 200;
- permanent moves → 301/308;
- temporary → 302/307 only when truly temporary;
- gone/nonexistent → 404/410;
- server error → 5xx, not fake 200.

Flag redirect chains/loops, soft 404s and SPA “200 for every route”.

---

## 5. Crawl blocking

Check:

- `/robots.txt` per host/protocol;
- robots meta/X-Robots-Tag;
- WAF/CDN/IP/UA rules;
- auth/cookie/geofence;
- blocked JS/CSS/API dependencies;
- provider-specific intended search/retrieval crawlers.

Remember: robots blocking can prevent a crawler from seeing `noindex`; `Disallow` is not a deindex command.

---

## 6. Indexability / indexation

Use:

- GSC Page Indexing;
- URL Inspection samples;
- Bing Webmaster URL inspection;
- sitemap submitted/indexed cohorts;
- `site:` only as rough supplementary discovery, not a complete index count.

Classify exclusions: intentional noindex, duplicate/canonical, crawled/discovered not indexed, soft 404, blocked, error, unknown.

`HIGH`: priority commercial page unexpectedly non-indexable/not indexed.

---

## 7. Canonicalization

For each priority/template sample compare:

- requested URL;
- redirect target;
- HTML canonical;
- sitemap URL;
- internal links;
- hreflang references;
- GSC user-declared vs Google-selected canonical.

Canonical is a preference signal, not an absolute command. Resolve conflicting signals at source.

---

## 8. Redirects

Check:

- one-hop mappings;
- no mass redirect to homepage/unrelated category;
- protocol/www/trailing-slash consistency;
- query preservation only when meaningful;
- migration mappings;
- internal links/sitemaps use final URLs.

Keep site-move redirects sufficiently long; current Google migration guidance is the authority for current retention recommendations.

---

## 9. Rendering / JavaScript

Compare:

- raw HTML;
- rendered DOM;
- Google rendered output where available;
- console/network errors;
- status/canonical/title/robots before and after hydration;
- direct-request SPA/deep-route behavior.

`HIGH`: primary content/links absent, index directives flip incorrectly, or nonexistent routes return misleading 200 output.

Use `docs/javascript-seo.md`.

---

## 10. Internal linking

Measure:

- orphan URLs;
- crawl depth;
- hub→child coverage;
- broken links;
- links to redirects;
- descriptive anchors;
- pagination/breadcrumbs;
- JS click-only navigation.

Prioritize user navigation/context, not artificial exact-match anchor quotas.

---

## 11. Architecture

Review:

- hierarchy aligned to products/services/topics;
- finite crawl space;
- facet/filter policy;
- internal search/tag archives;
- category/hub usefulness;
- URL stability/pagination;
- locale/location architecture.

`HIGH`: infinite crawl space, large orphan inventories, conflicting duplicate pathways.

---

## 12. Duplication / thin URL classes

Identify parameters/sorts/sessions, near-identical locations, copied manufacturer descriptions, duplicate tags/categories, legacy variants and pSEO templates with no distinct value.

Choose improve, consolidate, redirect, canonical, noindex or remove according to real user purpose and URL semantics.

---

## 13. Content quality

For priority pages ask:

- Does it satisfy current intent?
- Is information accurate/current?
- What is uniquely useful?
- Are material claims sourced?
- Is first-hand evidence/methodology shown where relevant?
- Is authorship/reviewer appropriate?
- Is it commodity paraphrase/filler?
- Is AI-assisted content verified?
- Is scale producing low-value pages?

Use people-first guidance and spam-policy boundaries.

---

## 14. Search intent / SERP fit

Run a dated target-market SERP observation and compare dominant page type, commercial/informational mix, local/shopping/video/AI features, freshness, brand concentration and result format.

`HIGH` strategic issue: trying to rank the wrong page type for a stable observed intent pattern.

Use `RANKING_FRAMEWORK.md` and `docs/serp-research.md`.

---

## 15. Structured data

Check:

- syntax/vocabulary;
- correct semantic type;
- visible-content truth match;
- current Google feature requirements if applicable;
- duplicate/conflicting plugin markup;
- reviews/ratings authenticity;
- product price/availability freshness;
- entity IDs/`sameAs` accuracy.

Valid Schema.org ≠ guaranteed rich result/rank.

---

## 16. Performance / Core Web Vitals

Measure field data first when available. Current good thresholds used in this baseline: LCP ≤2.5s, INP <200ms, CLS <0.1.

Use lab tools for diagnosis; segment by template/device/region. Fix real causes such as origin latency, render-blocking resources, images/fonts, main-thread work and layout instability.

A Lighthouse score is not a ranking score.

---

## 17. External authority / reputation

Review:

- relevant earned referring domains;
- link-spam history/manual actions;
- unlinked/brand mentions;
- brand SERP;
- reviews/local reputation;
- industry/partner citations;
- original research/linkable assets;
- paid/PBN/exchange risk.

Use `docs/links-authority.md` and `docs/entity-brand-reputation.md`.

---

## 18. Special-case modules

Activate only when relevant.

### Local
GBP accuracy, categories, hours, NAP, genuine reviews, local proof and geography-aware measurement.

### International
Distinct locale URLs, real localization, hreflang reciprocity, same-locale canonicals and accessible locale selection.

### Ecommerce
categories/products, variants, facets, merchant feeds, Product schema, inventory lifecycle and pagination.

### Publisher/news
freshness, dates/bylines/sourcing, discovery latency, article/media eligibility, archive/tag controls and corrections.

### SaaS/B2B/service/marketplace/forum/affiliate
Use the corresponding `docs/site-types/` playbook and activate its specific risk/measurement gates.

---

## 19. AI Search / crawler controls

Inventory intended platforms and inspect:

- Google generative AI Search control/report where available;
- Google-Extended separately;
- `OAI-SearchBot` vs `GPTBot`;
- `Claude-SearchBot` / `Claude-User` / `ClaudeBot`;
- Perplexity controls;
- Bing AI Performance;
- Applebot/Applebot-Extended;
- DuckAssistBot.

Check robots plus WAF/CDN logs. Search, training and user-triggered retrieval controls must not be conflated. Citation metrics are not ordinary ranking metrics.

---

## 20. Measurement / causality

Confirm:

- GSC/BWT/analytics connected where applicable;
- conversions valid;
- branded/non-branded separated;
- releases annotated;
- AI referrals/citations tracked separately;
- rank tracker locale/device defined;
- dashboards do not merge incompatible metrics;
- seasonality/algorithm updates/migrations noted.

A fix is not `PASS` because code deployed; it passes only after live verification/retest and appropriate measurement confirmation.

---

# Audit Issue Template

```text
ID: SEO-YYYY-NNN
Severity: CRITICAL/HIGH/MEDIUM/LOW/INFO
Scope: URLs/templates/host
Impact: user/search/business impact
Evidence: exact test/output/source
Diagnosis: evidence-backed root cause or bounded hypothesis
Fix: remediation performed/proposed
Verification: direct check that the intended change exists
Owner:
Deploy/commit:
Retest procedure:
Retest evidence:
Result: PASS/FAIL/MONITOR
Date:
```

# Verification vs Retest

- **Verification** asks: did the intended configuration/code/content change actually ship?
- **Retest** asks: did the original failure condition disappear in live behavior and downstream evidence?

Both are required for Critical/High closure.

# Audit prioritization rule

Prioritize approximately by:

`Priority = severity × affected valuable URLs/users × evidence confidence × business exposure`, adjusted for reversibility/effort.

Do not fix low-confidence cosmetic tool warnings ahead of a verified crawl/index/revenue blocker.

# Definition of audit complete

An audit is complete only when:

- scope and sample methodology are documented;
- Critical/High issues have owners/actions;
- false positives are removed;
- every completed Critical/High fix has verification + live retest evidence;
- residual risk/monitoring is explicit;
- release and measurement annotations exist;
- no plugin/tool score defines success.

**Baseline SOP Quality Gate:** `PASS` when the 20 dependency-ordered stages above are applied in order, issue records use the required evidence fields, and Critical/High closure requires verification plus retest.
