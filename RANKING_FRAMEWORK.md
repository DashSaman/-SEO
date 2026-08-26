# RANKING_FRAMEWORK.md — Query-Level Competitive Decision System

**Version:** 2026-08-26  
**Purpose:** decide whether and how a site should compete for a specific query before spending resources.

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
- measured authority/link data if available.

## Step 1 — Is the query commercially relevant?

Score:

- `3` directly maps to profitable product/service/action;
- `2` assists comparison/qualification;
- `1` upper-funnel learning with a clear path to value;
- `0` traffic has little realistic business value.

Do not prioritize a high-volume `0` over a lower-volume `3` solely for traffic.

## Step 2 — Intent confidence

Inspect current results.

Classify:

- informational;
- commercial investigation;
- transactional;
- local;
- navigational/branded;
- mixed/ambiguous.

**High confidence**: results consistently show one page type/job.  
**Low confidence**: SERP is mixed/volatile; test multiple formats or deprioritize until clearer.

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

- `+2` we can produce materially better evidence;
- `+1` modest differentiation;
- `0` parity only;
- `-1` competitors have proprietary evidence we cannot match.

## Step 6 — Brand/entity gap

Inspect:

- branded search presence;
- known/recognized organizations in SERP;
- reviews/reputation;
- independent references/media;
- author/expert credibility;
- local prominence where applicable.

A new domain facing government/major marketplaces/top global brands on a trust-sensitive query may need a long authority-building runway even with excellent content.

## Step 7 — Link/authority gap

Only use measured data when a real dataset is available. Record:

- referring domains to ranking page and domain;
- relevance/quality pattern, not only count;
- earned editorial vs directory/paid/spam patterns;
- unique linkable assets;
- competitor link velocity/freshness if measured.

Third-party DR/DA are comparative proxies, not Google metrics.

Rate feasibility:

- `GREEN`: peer competitors + realistic earned authority path;
- `AMBER`: substantial gap but assets/brand/PR can close it;
- `RED`: extraordinary gap/no legitimate acquisition path in required horizon.

## Step 8 — Freshness / recency

Ask:

- do results favor recent dates/news/current prices?;
- is the topic evergreen?;
- does old content remain stable because fundamentals change slowly?;
- what update cadence can the business sustain?

Do not change dates without meaningful content updates.

## Step 9 — Local considerations

If local intent exists:

- distance cannot be “optimized away” for every searcher;
- improve relevance and prominence legitimately;
- GBP accuracy/category/hours/services;
- real location/service-area evidence;
- reviews/reputation;
- local organic page fit;
- consistent business data.

A query can be feasible in one city and infeasible in another.

## Step 10 — International considerations

For multilingual/multiregional targets:

- dedicated locale URL?;
- genuinely localized visible language/content?;
- hreflang reciprocal?;
- canonical aligned?;
- local pricing/currency/legal/logistics?;
- local competitors/brand recognition?;
- georedirect not blocking crawler/user access?

## Step 11 — AI citation relevance

Ask whether AI surfaces materially influence this query class.

Measure:

- AI Overviews/AI Mode presence;
- Bing Copilot citations/grounding queries;
- ChatGPT/Perplexity/Claude controlled prompts;
- AI referral/conversion data.

Do not overvalue citation share where the business outcome is negligible.

## Step 12 — Competitive scorecard

Score each 0–3:

| Factor | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Business value | none | weak | assist | direct/high |
| Intent/page-type fit | mismatch | uncertain | reasonable | exact |
| Technical readiness | blocked | major issues | minor | clean |
| Content differentiation | commodity | limited | good | unique evidence |
| Brand/entity trust | weak | emerging | competitive | strong |
| Authority/link feasibility | red | hard | feasible | advantage |
| Freshness capability | cannot maintain | weak | adequate | strong |
| Local/international fit | mismatch | partial | good | exact |
| Measurement quality | none | weak | partial | robust |

This score is an internal prioritization tool, **not a Google score**.

## Decision bands

### `NOW`

- high business value;
- page type/intention clear;
- no Critical technical block;
- meaningful differentiation possible;
- authority gap realistically addressable.

Action: build/upgrade now and measure.

### `BUILD`

Good query but prerequisites missing: brand, authority, data asset, architecture or content depth.

Action: define prerequisite roadmap and leading indicators.

### `LONG_SHOT`

Strategically relevant but dominated by materially stronger entities/assets.

Action: pursue long-tail/adjacent clusters first; create evidence/authority moat before head term.

### `NO-GO`

Wrong intent, no legitimate matching page, negligible business value or unrealistic resource economics.

Action: stop spending and redirect resources.

## Common blockers below Top 10

Diagnose in this order:

1. wrong URL/page type for intent;
2. not indexed / wrong canonical / rendering issue;
3. weak architecture/internal discovery;
4. commodity or incomplete content;
5. missing first-party evidence/trust;
6. severe authority/reputation gap;
7. local/international mismatch;
8. freshness mismatch;
9. SERP changed since original plan;
10. competition simply stronger — requiring a better asset/brand strategy, not cosmetic on-page edits.

## Stop-loss rule

For every major target define before launch:

- observation window appropriate to site/query;
- minimum impression/indexing evidence;
- business value threshold;
- maximum content/PR engineering investment;
- conditions for consolidate/retarget/prune.

SEO iteration should be evidence-driven portfolio management, not endless editing because a tool still shows warnings.

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
Content/evidence gap:
Brand/entity gap:
Measured authority gap:
Freshness requirement:
Local/international requirement:
AI surface relevance:
Decision: NOW/BUILD/LONG_SHOT/NO-GO
Primary blocker:
Next action:
Success metric:
Stop condition:
```

## Final principle

“Can this page rank?” is the wrong first question. Ask: **Can this business produce the page/evidence/entity/authority that this query’s users and current competitive environment require, while remaining technically eligible and policy-safe?**
