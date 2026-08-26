# RANKING_FRAMEWORK.md — Query-Level Competitive Decision System

**Version:** 2026-08-26  
**Purpose:** decide whether and how a site should compete for a specific query before spending resources. This is an internal prioritization framework, never a Google scoring model or ranking guarantee.

## Input record

For every target cluster record:

- exact query + close variants;
- market/country/city/language;
- device where material;
- business value/conversion;
- current ranking URL if any;
- current impressions/clicks/conversions if available;
- observed SERP date;
- dominant page types;
- SERP features;
- key competitors;
- measured authority/link data if available;
- YMYL/high-stakes sensitivity;
- ecommerce/local/international constraints where applicable.

## Step 1 — Commercial relevance

Score:

- `3` directly maps to profitable product/service/action;
- `2` assists comparison/qualification;
- `1` upper-funnel learning with a clear path to value;
- `0` traffic has little realistic business value.

Do not prioritize a high-volume `0` over a lower-volume `3` solely for traffic.

## Step 2 — Intent confidence

Inspect current results and classify: informational, commercial investigation, transactional, local, navigational/branded or mixed/ambiguous.

**High confidence:** results consistently show one page type/job.  
**Low confidence:** SERP is mixed/volatile; test/observe more or reduce priority.

## Step 3 — Required page type

Choose from observed intent:

- homepage/entity page;
- service landing page;
- category/listing;
- product/detail;
- comparison;
- guide/tutorial;
- tool/calculator;
- location page;
- video/watch page;
- marketplace/directory page.

If the business cannot legitimately create the dominant useful page type, mark `NO-GO` or target an adjacent query.

## Step 4 — Technical eligibility

Gate:

- crawlable?;
- indexable?;
- correct status?;
- preferred canonical?;
- rendered critical content/links?;
- internal discovery?;
- no migration/duplicate conflict?;
- acceptable mobile/performance?

Any Critical fail means **fix technical first**, not “build more links.”

## Step 5 — Content/evidence gap

Compare target page vs competitive set across:

- completeness for user task;
- original data/first-hand evidence;
- examples/screenshots/video/tools;
- pricing/specification/availability accuracy;
- limitations/tradeoffs;
- expert review/authorship where relevant;
- freshness;
- clarity/structure;
- local/international specificity.

Rate:

- `+2` materially better evidence is realistically possible;
- `+1` modest defensible differentiation;
- `0` parity only;
- `-1` competitors have proprietary evidence/assets we cannot match.

### Required differentiator statement

Before proceeding, write one sentence:

`This page deserves attention because it uniquely provides ______ for ______ that the current competitive set does not provide as well.`

If this cannot be filled with a truthful user benefit, the target is not `NOW`.

## Step 6 — YMYL / high-stakes risk

Classify:

- `LOW`: ordinary low-stakes information/product use;
- `MEDIUM`: meaningful financial/safety/technical consequence;
- `HIGH`: health, finance, legal, safety or other life-impacting advice.

For `HIGH`:

- require stronger primary/authoritative sourcing;
- verify expert/reviewer competence where relevant;
- disclose limitations/conflicts;
- avoid unsupported predictions/claims;
- raise freshness/correction standards;
- consider whether the business has legitimate expertise to compete.

A commercially attractive high-stakes query can still be `NO-GO` when evidence/expertise is not credible enough.

## Step 7 — Brand/entity gap

Inspect branded search presence, recognized entities in the SERP, reviews/reputation, independent references/media, author/expert credibility and local prominence where applicable.

A new domain facing government/major institutions/global brands on a trust-sensitive query may need a long authority-building runway even with excellent content.

## Step 8 — Link/authority gap

Use measured data only when a real dataset is available. Record:

- referring domains to ranking page/domain;
- relevance/quality pattern, not only count;
- earned editorial vs directory/paid/spam patterns;
- unique linkable assets;
- competitor link velocity/freshness if measured.

Third-party DR/DA are comparative proxies, not Google metrics.

Feasibility:

- `GREEN`: peer competitors + realistic earned authority path;
- `AMBER`: substantial gap but assets/brand/PR can plausibly close it;
- `RED`: extraordinary gap/no legitimate acquisition path in the required horizon.

## Step 9 — Freshness / recency

Ask whether the query favors recent facts/news/pricing, is evergreen, and what truthful update cadence the business can sustain. Never refresh dates without meaningful changes.

## Step 10 — Local considerations

If local intent exists:

- distance cannot be “optimized away” for every searcher;
- improve relevance/prominence legitimately;
- verify GBP accuracy/categories/hours/services;
- require real location/service-area evidence;
- review reputation and local organic page fit;
- measure in actual geography.

A query can be feasible in one city and infeasible in another.

## Step 11 — International considerations

For multilingual/multiregional targets verify dedicated locale URLs, genuine localization, hreflang/canonical alignment, local currency/legal/logistics, local competitors/brand familiarity and accessible locale switching without crawl-blocking redirects.

## Step 12 — Ecommerce / transactional considerations

If ecommerce/marketplace intent exists, inspect:

- dominant result is category vs product vs marketplace vs editorial comparison;
- real inventory/availability depth;
- variant/facet architecture;
- price/shipping/returns competitiveness and accuracy;
- Product/Merchant data consistency where relevant;
- genuine review/reputation evidence;
- whether the business can maintain inventory/content freshness;
- whether a new thin category page would add any user value.

A query with strong category/marketplace intent should not be forced into an informational article merely because article production is easier.

## Step 13 — AI citation relevance

Ask whether AI surfaces materially influence this query class. Measure AI Overviews/AI Mode presence, Bing Copilot citation/grounding data, controlled ChatGPT/Perplexity/Claude observations and AI referral/conversion data where available.

Do not overvalue citation presence when it produces little business outcome. Citation ≠ ranking ≠ traffic.

## Step 14 — Competitive scorecard

Score each 0–3:

| Factor | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Business value | none | weak | assist | direct/high |
| Intent/page-type fit | mismatch | uncertain | reasonable | exact |
| Technical readiness | blocked | major issues | minor | clean |
| Content differentiation | commodity | limited | good | unique evidence |
| YMYL/evidence readiness | unqualified | weak | adequate | strong/not material |
| Brand/entity trust | weak | emerging | competitive | strong |
| Authority/link feasibility | red | hard | feasible | advantage |
| Freshness capability | cannot maintain | weak | adequate | strong |
| Local/international/ecommerce fit | mismatch | partial | good | exact |
| Measurement quality | none | weak | partial | robust |

This score prioritizes work. It is **not a Google score** and does not produce a ranking probability percentage.

## Decision bands

### `NOW` / `GO`

High business value, clear page type, no Critical technical block, credible differentiator and realistically addressable trust/authority gap.

**Action:** build/upgrade now and measure.

### `BUILD` / `NOT-YET`

Good query but prerequisites are missing: brand, authority, data asset, expertise, architecture or content depth.

**Action:** define prerequisite roadmap and leading indicators.

### `LONG_SHOT` / `GO-LONG-TERM`

Strategically relevant but dominated by materially stronger entities/assets.

**Action:** pursue adjacent/long-tail clusters and build an evidence/authority moat first.

### `LOW-PRIORITY`

Feasible but low business value, weak differentiation or poor opportunity cost relative to other clusters.

**Action:** schedule after higher-value targets or retain for supportive coverage only.

### `NO-GO`

Wrong intent, no legitimate matching page, insufficient expertise/evidence, negligible business value or unrealistic resource economics.

**Action:** stop spending and redirect resources.

## Common blockers below Top 10

Diagnose in dependency order:

1. wrong URL/page type for intent;
2. not indexed / wrong canonical / rendering issue;
3. weak architecture/internal discovery;
4. commodity or incomplete content;
5. missing first-party evidence/expertise/trust;
6. severe authority/reputation gap;
7. local/international/ecommerce mismatch;
8. freshness mismatch;
9. SERP changed since the original plan;
10. competition is simply stronger — requiring a better asset/brand strategy, not cosmetic on-page edits.

## Stop-loss rule

For every major target define before launch:

- observation window appropriate to site/query;
- minimum index/impression evidence;
- business value threshold;
- maximum content/PR/engineering investment;
- conditions for consolidate/retarget/prune.

SEO iteration is evidence-driven portfolio management, not endless editing because a tool still shows warnings.

## Output template

```text
Query cluster:
Market/language/device:
Observed date:
Business value: 0-3
Intent:
Dominant page type:
SERP features:
Current URL/state:
Technical gate: PASS/FAIL
YMYL/high-stakes risk: LOW/MEDIUM/HIGH
Required differentiator:
Content/evidence gap:
Brand/entity gap:
Measured authority gap:
Freshness requirement:
Local requirement:
International requirement:
Ecommerce/transactional requirement:
AI surface relevance:
Decision: GO / NOT-YET / GO-LONG-TERM / LOW-PRIORITY / NO-GO
Primary blocker:
Next action:
Success metric:
Stop condition:
```

## Quality gate

`PASS` when a query decision contains a dated SERP observation, intent/page type, technical state, evidence/differentiator gap, brand/authority gap, YMYL risk, relevant local/international/ecommerce constraints, measurement plan, decision and stop condition.

`FAIL` when a decision is based only on search volume, keyword difficulty, content length, DR/DA, a plugin score or an unsupported “ranking probability.”

## Final principle

“Can this page rank?” is the wrong first question. Ask: **Can this business legitimately produce the page, evidence, entity trust and authority that this query’s users and current competitive environment require, while remaining technically eligible, policy-safe and economically worthwhile?**
