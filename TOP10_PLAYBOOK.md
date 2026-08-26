# TOP10_PLAYBOOK.md — Evidence-Based Search Growth Operating System

**Version:** 2026-08-26  
**Goal:** maximize the probability of competing successfully in Top 10 organic/eligible search surfaces for a defined query market.  
**Non-guarantee:** no workflow can guarantee page 1. Search outcomes depend on query intent, competition, brand/authority, content, technical quality, links, location/language and changing ranking systems.

## Operating loop

**Business → Market → Competitors → Keywords → Intent → Architecture → Technical → Content → Entities → Structured Data → Internal Links → Authority → AI Search → Launch → Validation → Measurement → Iteration**

Every phase has an input, action, quality gate and output. Do not skip to title/meta/schema before business/query feasibility is known.

---

## 0. Business / outcome definition

**Inputs**
- products/services and margins;
- target geography/languages;
- target customer segments;
- conversion definition;
- legal/compliance constraints;
- existing analytics/GSC/BWT/CRM data.

**Actions**
1. Define primary commercial outcomes: revenue, qualified lead, signup, booking, store visit, etc.
2. Identify the pages/types that can satisfy those outcomes.
3. Separate branded, non-branded and support/navigation demand.
4. Establish a measurement baseline and change log.

**PASS**: every SEO initiative maps to a user/business outcome and target market.  
**FAIL**: KPI is only “Rank Math/SEO score” or raw traffic with no quality target.  
**Output**: `BUSINESS_SEARCH_BRIEF`.

---

## 1. Market and SERP reality

**Inputs**: target country/city/language/device and initial queries.

**Actions**
- run dated target-market SERP observations;
- record AI Overview/local pack/shopping/video/PAA/etc.;
- identify dominant page types and brands;
- note freshness and localization;
- use GSC/BWT/paid keyword/backlink data if available.

**PASS**: SERP is measured in the actual market and dominant intent/page type is explicit.  
**FAIL**: strategy uses a generic keyword-tool score without looking at results.  
**Output**: `SERP_MAP` + query clusters.

---

## 2. Competitive feasibility

For each priority cluster answer:

- Are results mostly giant brands/government/marketplaces or peers?
- Is the dominant page type one we can legitimately create?
- What unique first-party evidence can we add?
- How large is the authority/referring-domain gap when measurable?
- Is freshness or location decisive?
- Is the site technically/indexationally capable?
- What commercial value justifies the effort?

Classify:

- `NOW` — feasible with current assets;
- `BUILD` — feasible after content/authority/entity work;
- `LONG_SHOT` — dominated by materially stronger entities;
- `NO-GO` — wrong intent/economics or no legitimate differentiated answer.

**Output**: priority portfolio, not one giant keyword list.

---

## 3. Keyword → intent → page mapping

Group variants by the **same user task**, not by exact-match phrase.

Example:
- `business voip provider`, `business voip service`, `voip for business` may map to one commercial service page if SERP intent aligns;
- `how does voip work` belongs to an informational guide;
- `voip provider berlin` may require localized evidence if local intent is real.

Avoid one page per keyword synonym.

**PASS**: one preferred page per distinct intent with no cannibalizing duplicates.  
**Output**: URL/content map.

---

## 4. Information architecture

Design:

`Home → Commercial hubs → Services/Categories → Detailed pages → Supporting evidence/guides`

Actions:
- keep important pages within logical crawl depth;
- create hub→child and sibling contextual links;
- expose real `<a href>` links;
- control facets/filters/search URLs;
- define breadcrumbs;
- define canonical URL policy.

**PASS**: every priority page has a logical parent and crawlable internal path.  
**FAIL**: orphan pages, mega footer keyword clouds, infinite faceted space.

---

## 5. Technical eligibility gate

Check in this order:

1. DNS/TLS/site availability;
2. HTTP status;
3. robots/WAF access;
4. `noindex` / X-Robots-Tag;
5. canonical;
6. redirects;
7. rendered critical content/links;
8. sitemap/internal discovery;
9. mobile/user experience;
10. CWV field performance;
11. structured-data validity;
12. hreflang/local/product special cases.

Use `SEO_AUDIT_SOP.md` and technical checklists.

**PASS**: preferred URL is crawlable/indexable/canonical, returns correct status, renders intended content and is discoverable.  
**FAIL**: any Critical blocker exists.  
**Output**: technical PASS evidence with before/after tests.

---

## 6. Content brief built from intent and evidence

A content brief should contain:

- primary user job;
- search stage (learn/compare/buy/troubleshoot/local);
- required factual claims and sources;
- unique first-party evidence;
- questions/objections from SERP/customer/support data;
- page format;
- internal links in/out;
- media/examples/calculators/data;
- authorship/reviewer requirement;
- freshness/update owner;
- conversion action.

Do **not** specify arbitrary keyword density or word count as a ranking formula.

---

## 7. Create differentiated content

High-value differentiators include:

- original data/research;
- real product specifications and availability;
- worked calculations/examples;
- first-hand testing methodology;
- case studies with permission;
- screenshots/video/diagrams;
- decision tables;
- limitations/tradeoffs;
- transparent pricing/process where appropriate;
- expert review for high-stakes topics.

**PASS**: page is useful even if search traffic did not exist.  
**FAIL**: page mostly paraphrases existing top results or is generated to hit phrase variants.

---

## 8. On-page implementation

Validate:

- descriptive concise title aligned with intent;
- one clear main heading and logical subheadings;
- visible answer/product/service evidence;
- descriptive internal anchors;
- image alt where meaningful;
- canonical/robots correct;
- conversion action appropriate;
- no hidden keyword stuffing;
- snippets are earned from page content; meta description is presentation input, not ranking guarantee.

---

## 9. Entity and trust layer

Check:

- clear organization/person/product identity;
- About/contact/support/policies;
- authentic author/reviewer where relevant;
- consistent brand/NAP/location data;
- independent reviews/references;
- claims/credentials verifiable;
- `sameAs` only to true same entities;
- reputation issues addressed operationally.

Use `docs/entity-brand-reputation.md`.

---

## 10. Structured data

Add only markup that accurately describes visible content and has a clear semantic/search purpose.

Workflow:
1. choose Schema.org type;
2. check engine-supported feature if rich result is desired;
3. generate JSON-LD;
4. validate syntax and required/recommended properties;
5. confirm visible-content match;
6. monitor Search Console enhancements where available.

**FAIL**: schema contains invented ratings/reviews/entities or is added merely to increase schema count.

---

## 11. Internal authority/discovery

For every priority page:

- link from relevant hub/navigation where justified;
- link from high-traffic supporting guides when contextually useful;
- create reciprocal conceptual navigation where natural;
- remove dead/redirected internal targets;
- use descriptive anchors without spammy repetition;
- maintain breadcrumbs.

Measure orphan rate, crawl depth and internal-link distribution by template.

---

## 12. External authority / Digital PR

Prioritize:

1. original research/data;
2. useful tools/resources;
3. customer/partner/industry evidence;
4. selective PR/expert commentary;
5. legitimate citations/directories/local profiles;
6. unlinked mention reclamation;
7. relevant resource/broken-link outreach.

Reject PBNs, paid followed ranking links, automated link packages and reputation abuse. See `docs/links-authority.md`.

---

## 13. AI Search readiness

For intended platforms:

- verify crawler/WAF access by provider;
- separate search crawler from training control;
- preserve crawlable public facts and source evidence;
- use clear headings/semantic structure for users, not artificial “AI chunks”;
- make organization/product/entity facts consistent;
- record citations/referrals with provider-specific metrics where available;
- do not create fake Reddit/review/third-party mentions.

Use `docs/ai-search.md` and `docs/geo-myths.md`.

---

## 14. Pre-launch gate

Required evidence:

- HTTP 200 preferred URL;
- no redirect chain;
- intended robots/index directives;
- canonical correct;
- title/H1/content rendered;
- critical links have hrefs;
- structured data valid where used;
- sitemap contains preferred URL if sitemap-managed;
- mobile usable;
- CWV regression checked;
- analytics/conversion tracking working;
- no placeholder/test content;
- legal/privacy requirements satisfied.

Only ship after Critical items PASS.

---

## 15. Post-launch validation

Immediately/next crawls:

- fetch live URL and compare intended output;
- inspect server/CDN logs for 4xx/5xx/WAF errors;
- Search Console URL Inspection/indexing samples;
- Bing Webmaster/IndexNow where relevant;
- verify sitemap `lastmod` only when meaningful;
- compare analytics tracking;
- annotate release date.

Do not judge ranking success the same day.

---

## 16. Measurement framework

Track by page/query cluster:

### Search
- impressions;
- clicks;
- CTR (diagnostic, not direct universal ranking KPI);
- average position with query/locale caution;
- indexed/canonical status;
- conversions/revenue/qualified leads.

### AI
- Bing AI citations/cited pages/grounding queries where available;
- Google generative AI report where available;
- ChatGPT referral sessions (`utm_source=chatgpt.com` where present);
- controlled repeated prompt/query citation observations;
- conversions from AI referrals.

### Technical
- 2xx/3xx/4xx/5xx bot distribution;
- CWV/RUM;
- crawl/index errors;
- schema errors;
- orphan/crawl-depth metrics.

### Authority
- relevant referring domains;
- earned mentions;
- branded demand;
- review/reputation quality.

---

## 17. Iteration decision tree

### Impressions low / page indexed
Check:
- query fit and page type;
- competing authority/brand gap;
- internal linking;
- topical evidence/depth;
- freshness/locality;
- whether another URL is canonical/ranking.

### Impressions high / CTR low
Check:
- title/snippet intent match;
- SERP features satisfying query;
- brand trust;
- wrong position/query mix;
- outdated price/date/value proposition.

### Traffic high / conversion low
SEO may be succeeding while business/intent fails. Re-check offer, page intent, UX, proof and conversion action.

### Not indexed
Use technical/index-quality diagnosis, not more backlinks by default.

### Ranking plateau below Top 10
Re-run target SERP and compare:
- page type;
- missing evidence;
- authority gap;
- internal authority;
- brand/entity reputation;
- freshness;
- competitor improvements.

Then choose the **smallest evidence-backed change**, deploy, annotate and measure.

---

## Definition of a Top-10-ready page

A page is `TOP10_READY` when:

- target query/market is feasible;
- intent/page type matches current SERP;
- technical/index/canonical gate passes;
- content has real differentiated value/evidence;
- entity/trust facts are transparent;
- internal discovery is strong;
- external authority plan is policy-safe;
- AI crawler/search settings are deliberate;
- measurement and rollback exist.

`TOP10_READY` is **not** the same as “guaranteed Top 10.” It means the controllable inputs are competitive and verified.
