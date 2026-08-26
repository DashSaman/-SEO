# SEO_AUDIT_SOP.md — Severity-Based Audit and Retest Procedure

**Version:** 2026-08-26  
**Rule:** diagnose in dependency order. Do not optimize titles/schema/backlinks while availability, crawl, index or canonical blockers remain.

## Severity model

- `CRITICAL` — site/large priority set unavailable, accidentally blocked/deindexed, security/privacy exposure or severe migration failure.
- `HIGH` — material index/canonical/rendering/architecture issue affecting priority pages or revenue.
- `MEDIUM` — meaningful quality/discovery/performance issue with bounded impact.
- `LOW` — cleanup/opportunity; no evidence of material current harm.
- `INFO` — observation requiring no action unless context changes.

Every issue must contain: **Evidence → Impact → Diagnosis → Remediation → Retest → Owner → Date → Result**.

---

## 1. Security / privacy / unauthorized exposure

**Check**
- HTTPS/TLS, certificate/redirect integrity;
- hacked/spam pages/links;
- staging/dev/admin/private URLs exposed/indexable;
- secrets/tokens/user data in URLs or rendered source;
- unexpected WAF rules and bot impersonation.

**CRITICAL examples**: private customer data indexed; hacked pages; production robots exposes nothing confidential but security relies on it.

**Remediation**: fix access control first. `robots.txt` is not security. Use authentication/authorization/removal processes as required.

**Retest**: unauthenticated access, Search removal/index state, logs/security scanner.

---

## 2. Site availability

Test homepage + representative critical templates from external network/regions.

Evidence:
- DNS;
- TLS;
- status;
- uptime;
- CDN/origin health;
- browser render.

`CRITICAL`: sustained outage, domain/DNS failure, widespread 5xx.

---

## 3. HTTP/status semantics

Sample and crawl:

- preferred pages → 200;
- permanent moves → 301/308;
- temporary → 302/307 only when truly temporary;
- gone/nonexistent → 404/410;
- server error → 5xx, not fake 200.

Flag redirect chains/loops and SPA soft-404 behavior.

---

## 4. Crawl blocking

Check:

- `/robots.txt` per host/protocol;
- robots meta/X-Robots-Tag;
- WAF/CDN/IP/UA rules;
- auth/cookie/geofence;
- blocked JS/CSS/API dependencies;
- provider-specific AI crawlers.

Remember: robots blocking can prevent a crawler from seeing `noindex`; do not treat `Disallow` as a deindex command.

---

## 5. Indexation

Use:

- GSC Page Indexing;
- URL Inspection samples;
- Bing Webmaster URL inspection;
- sitemap submitted/indexed groups;
- site: operator only as rough supplementary discovery, not a complete index count.

Classify exclusions:

- intentional noindex;
- duplicate/canonical;
- crawled/discovered not indexed;
- soft 404;
- blocked;
- error;
- unknown.

`HIGH`: priority commercial page unexpectedly not indexed.

---

## 6. Canonicalization

For each priority/template sample compare:

- URL requested;
- HTTP redirect target;
- HTML canonical;
- sitemap URL;
- internal links;
- hreflang references;
- GSC user-declared vs Google-selected canonical.

Canonical is a preference signal, not an absolute command. Resolve conflicting signals at source.

---

## 7. Redirects

Check:

- one-hop mapping;
- no mass redirect to homepage/unrelated category;
- protocol/www/trailing slash consistency;
- query preservation only when meaningful;
- migrated URL mapping;
- internal links and sitemap updated to final URL.

Keep migration redirects long enough for users/search systems; Google generally recommends retaining them at least a year in site moves.

---

## 8. Rendering / JavaScript

For samples compare:

- raw HTML;
- rendered DOM;
- Google rendered output where available;
- JS disabled dependency diagnostic;
- console/network errors;
- status/canonical/title/robots before and after hydration.

`HIGH`: primary content/links absent from rendered output or hydration changes index directives incorrectly.

Use `docs/javascript-seo.md`.

---

## 9. Internal linking

Measure:

- orphan URLs;
- crawl depth;
- hub→child coverage;
- broken links;
- links to redirects;
- descriptive anchors;
- pagination links;
- breadcrumbs;
- JS click-only navigation.

Prioritize links that improve navigation/context, not artificial exact-match anchor quotas.

---

## 10. Architecture

Review:

- hierarchy aligned to products/services/topics;
- finite crawl space;
- facet/filter policy;
- internal search/tag archives;
- category/hub usefulness;
- URL stability;
- pagination;
- separate locale/location architecture.

`HIGH`: infinite crawl space, large orphan inventories, conflicting duplicate pathways.

---

## 11. Duplication / thin URL classes

Identify:

- parameters/sort/session URLs;
- near-identical location pages;
- copied manufacturer descriptions;
- duplicate tags/categories;
- printer/AMP/legacy variants;
- protocol/subdomain duplicates;
- programmatic templates with no distinct value.

Choose: consolidate, redirect, canonical, noindex, remove or improve — based on user purpose and URL semantics.

---

## 12. Content quality

For priority pages ask:

- Does it satisfy current intent?
- Is information accurate/current?
- What is uniquely useful?
- Are claims sourced?
- Is first-hand evidence/methodology shown where relevant?
- Is authorship/reviewer appropriate?
- Is page mostly paraphrase/commodity?
- Are AI-assisted sections verified?
- Is scale creating low-value pages?

Use people-first guidance and spam-policy boundaries.

---

## 13. Search intent / SERP fit

Run dated target-market SERP observation.

Compare:
- dominant page type;
- commercial vs informational mix;
- local/shopping/video/AI features;
- freshness;
- brand concentration;
- result format.

`HIGH` strategic issue: trying to rank a service landing page where results consistently demand product/category/comparison content, or vice versa.

---

## 14. Structured data

Check:

- JSON-LD syntax;
- correct type;
- visible-content match;
- Google-supported feature requirements if applicable;
- duplicate/conflicting plugin markup;
- fake reviews/ratings;
- product price/availability freshness;
- entity IDs/sameAs accuracy.

Valid schema ≠ guaranteed rich result/rank.

---

## 15. Performance / Core Web Vitals

Measure field data first when available:

- LCP target ≤2.5s;
- INP target <200ms;
- CLS target <0.1.

Use lab tools for diagnosis. Segment by template/device/region. Fix user-impacting causes: server latency, render-blocking resources, images/fonts, JS main-thread work, layout instability.

Do not treat Lighthouse 100 as an SEO guarantee.

---

## 16. External authority / reputation

Review:

- relevant earned referring domains;
- link-spam history/manual actions;
- unlinked mentions;
- brand SERP;
- reviews/local reputation;
- industry/partner citations;
- original research/linkable assets;
- fake/PBN/paid followed links.

Use `docs/links-authority.md` and `docs/entity-brand-reputation.md`.

---

## 17. Special-case modules

Activate only when relevant:

### Local
GBP accuracy, categories, hours, NAP, reviews, local page evidence, relevance/distance/prominence interpretation.

### International
Distinct locale URLs, localized visible language, hreflang reciprocity, canonical, georedirect/crawl accessibility.

### Ecommerce
categories/products, variants, facets, merchant feeds, Product schema, out-of-stock lifecycle, pagination.

### Publisher/news
freshness, dates/bylines, crawl speed, article/video/image eligibility, archive/tag architecture, corrections.

---

## 18. AI Search / crawler controls

Inventory intended platforms and inspect:

- Google generative AI control/report;
- Google-Extended policy separately;
- `OAI-SearchBot` vs `GPTBot`;
- `Claude-SearchBot` / `Claude-User` / `ClaudeBot`;
- Perplexity controls;
- Bing AI Performance;
- Applebot/Applebot-Extended;
- DuckAssistBot.

Check robots plus WAF/CDN logs. Never assume search and training controls are the same.

---

## 19. Measurement / causality

Confirm:

- GSC/BWT connected;
- analytics conversions valid;
- branded/non-branded separated;
- releases annotated;
- AI referrals/citations tracked separately;
- rank tracker locale/device defined;
- dashboards do not merge incompatible metrics;
- seasonality/algorithm updates/migrations noted.

A fix is not `PASS` because code deployed; it passes only after live retest and relevant search/measurement confirmation.

---

# Audit Issue Template

```text
ID: SEO-YYYY-NNN
Severity: CRITICAL/HIGH/MEDIUM/LOW/INFO
Scope: URLs/templates/host
Evidence: exact test/output/source
Impact: user/search/business impact
Root-cause hypothesis:
Remediation:
Owner:
Deploy/commit:
Retest procedure:
Retest evidence:
Result: PASS/FAIL/MONITOR
Date:
```

# Audit Prioritization Rule

Prioritize using:

`Priority = severity × affected valuable URLs/users × confidence × reversibility/effort consideration`

Do not “fix” low-confidence minor warnings ahead of a verified index/canonical/revenue blocker.

# Definition of Audit Complete

An audit is complete only when:

- scope and sample methodology documented;
- Critical/High issues have owners/actions;
- false positives removed;
- every completed fix has live retest evidence;
- residual risk/backlog explicit;
- release and measurement annotations recorded;
- no plugin/tool score is used as the definition of success.
