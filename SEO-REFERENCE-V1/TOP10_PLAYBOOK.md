# TOP10_PLAYBOOK.md — Evidence-Based Search Growth Operating System

**Version:** 2026-08-26  
**Goal:** maximize the probability of competing successfully in Top 10 organic/eligible search surfaces for a defined query market.  
**Non-guarantee:** no workflow can guarantee page 1. Search outcomes depend on query intent, competition, brand/authority, content, technical quality, links, location/language and changing ranking systems.

## Operating loop

**Business → Market → Competitors → Query universe → Intent → Architecture → Technical → Content → Entities → Structured Data → Internal Links → Authority → AI Search → Launch → Validation → Measurement → Iteration**

Do not skip to title/meta/schema before business/query feasibility is known.

## Mandatory phase record — required for every phase

Every phase below MUST be executed and recorded with these eight fields:

```text
PHASE:
INPUTS:
ACTIONS:
TOOLS:
EVIDENCE:
OUTPUT:
PASS CRITERIA:
FAIL CRITERIA:
NEXT ACTION:
```

A phase is not complete because work was performed. It is complete only when its **evidence, output and PASS/FAIL result** are recorded and the next dependency is explicit.

### Phase execution matrix

| Phase | Typical tools | Minimum evidence | Required output | Next action after PASS |
|---|---|---|---|---|
| 0 Business | analytics/CRM/business data | outcomes, margins, market, baseline | `BUSINESS_SEARCH_BRIEF` | Market/SERP research |
| 1 Market/SERP | live search, GSC/BWT, measured SERP provider if available | dated locale/device SERP observations | `SERP_MAP` | Feasibility |
| 2 Feasibility | `RANKING_FRAMEWORK.md`, measured authority data | intent/page type, gaps, economics | prioritized query portfolio | Query→page map |
| 3 Query mapping | SERP map, keyword/query data | cluster-to-intent evidence | URL/content map | Architecture |
| 4 Architecture | crawler, diagrams, CMS routes | crawl paths, URL classes, facet rules | architecture/internal-link spec | Technical audit |
| 5 Technical | `SEO_AUDIT_SOP.md`, crawler, headers, GSC/BWT, logs | before/after status/index/canonical/render evidence | technical gate report | Content brief |
| 6 Brief | SERP, customer/support data, first-party sources | source/evidence inventory and user job | production content brief | Create content |
| 7 Content | primary sources, product/data/testing systems | unique evidence, accuracy review | publishable page/content asset | On-page implementation |
| 8 On-page | rendered HTML, page source, analytics test | title/H1/body/canonical/robots/CTA evidence | implemented page | Entity/trust |
| 9 Entity/trust | organization records, reviews, profiles | consistent identity/claims | entity/trust map | Structured data |
| 10 Structured data | Schema.org, Google docs, validators | rendered JSON-LD + validator output | validated semantic markup | Internal discovery |
| 11 Internal links | crawler/inlink export | orphan/depth/target evidence | internal-link deployment | External authority |
| 12 Authority | backlink/mention datasets, PR assets | editorial relevance/policy classification | authority/PR roadmap | AI Search readiness |
| 13 AI Search | provider docs, robots/WAF logs, AI reports | crawler settings + provider-specific baseline | AI visibility baseline | Launch gate |
| 14 Launch | launch checklist, HTTP/render tests | preflight PASS artifacts | release decision | Post-launch validation |
| 15 Validation | live crawl, logs, GSC/BWT, analytics | production before/after evidence | validated release | Measurement window |
| 16 Measurement | GSC/BWT/analytics/CRM/AI reports | dated comparable KPI cohorts | performance review | Iteration decision |
| 17 Iteration | all prior evidence | diagnosed bottleneck + hypothesis | smallest evidence-backed change | return to affected phase |

If a listed commercial tool/API is unavailable, record the limitation and use an evidence-safe alternative. Never invent data.

---

## 0. Business / outcome definition

**Inputs:** products/services/margins, geography/languages, customer segments, conversion definition, legal constraints, analytics/GSC/BWT/CRM data.  
**Actions:** define commercial outcomes; identify page types that can create them; separate branded/non-branded/support demand; capture baseline/change log.  
**Tools:** business records, analytics/CRM, GSC/BWT where connected.  
**Evidence:** actual conversion/revenue/lead definitions and current baseline.  
**Output:** `BUSINESS_SEARCH_BRIEF`.  
**PASS:** every SEO initiative maps to a user/business outcome and target market.  
**FAIL:** KPI is only plugin score/raw traffic with no quality target.  
**Next:** market/SERP reality.

## 1. Market and SERP reality

**Inputs:** target country/city/language/device and seed queries.  
**Actions:** run dated SERP observations; record AI/local/shopping/video/PAA features; identify dominant page types/brands; note freshness/localization.  
**Tools:** live search, `docs/serp-research.md`, GSC/BWT, measured keyword/backlink provider if actually available.  
**Evidence:** date, market, query, visible result/page type/features.  
**Output:** `SERP_MAP` + query clusters.  
**PASS:** actual market measured and intent/page type explicit.  
**FAIL:** strategy uses a generic difficulty/volume score without looking at results.  
**Next:** competitive feasibility.

## 2. Competitive feasibility

**Inputs:** `SERP_MAP`, business value, current site/entity/authority state.  
**Actions:** assess competitor class, page type legitimacy, unique evidence, authority gap when measured, freshness/location/YMYL/ecommerce constraints and economics.  
**Tools:** `RANKING_FRAMEWORK.md`, GSC/BWT, measured backlink/authority data when available.  
**Evidence:** competitor/page-type observations and measured gaps with source/context.  
**Output:** priority portfolio with `GO / NOT-YET / GO-LONG-TERM / LOW-PRIORITY / NO-GO`.  
**PASS:** required differentiator and legitimate path exist.  
**FAIL:** no matching page/evidence/economics or only copied competitor strategy.  
**Next:** query→intent→page mapping.

## 3. Query → intent → page mapping

**Inputs:** prioritized clusters and SERP intent evidence.  
**Actions:** group variants by same user task; assign one preferred page per distinct intent; identify local/commercial/informational boundaries.  
**Tools:** SERP map, query data, site inventory/crawler.  
**Evidence:** SERP page-type consistency and current URL inventory.  
**Output:** URL/content map.  
**PASS:** one preferred page per distinct intent with no unnecessary synonym pages/cannibalization.  
**FAIL:** one page per exact keyword or conflicting URLs target same stable intent.  
**Next:** architecture.

## 4. Information architecture

**Inputs:** URL/content map, product/service/topic hierarchy.  
**Actions:** design `Home → Commercial hubs → Services/Categories → Detailed pages → Supporting evidence/guides`; define crawlable links, breadcrumbs, facet/search controls and canonical URL policy.  
**Tools:** crawler, sitemap/CMS route inventory, architecture diagram.  
**Evidence:** crawl paths, URL classes, orphan/depth/facet rules.  
**Output:** architecture/internal-link specification.  
**PASS:** every priority page has a logical parent and crawlable path; crawl space is finite.  
**FAIL:** orphans, keyword footer clouds or uncontrolled faceted space.  
**Next:** technical eligibility gate.

## 5. Technical eligibility gate

**Inputs:** architecture, production/staging URLs, current crawl/index state.  
**Actions:** execute the dependency order in `SEO_AUDIT_SOP.md`: security → availability → DNS/HTTPS/HTTP → status → crawl → indexability → canonical → redirects → rendering → internal links → architecture → duplication → content/intent → structured data → CWV → authority/special modules → AI Search → measurement.  
**Tools:** crawler, HTTP/header tests, browser rendering, GSC/BWT, logs, validators.  
**Evidence:** before/after tests for all Critical/High issues.  
**Output:** technical gate report.  
**PASS:** preferred URL is available/crawlable/indexable/canonical, returns correct status, renders intended content and is discoverable.  
**FAIL:** any unresolved Critical blocker.  
**Next:** content brief.

## 6. Content brief built from intent and evidence

**Inputs:** query/page mapping, competitive evidence, first-party/customer/support sources.  
**Actions:** define user job, search stage, sourced factual claims, unique evidence, objections/questions, format, internal links, media/data, author/reviewer, freshness owner and CTA.  
**Tools:** current SERP, customer/support/sales data, primary source documents.  
**Evidence:** source list and user/business requirements.  
**Output:** production brief.  
**PASS:** every material section exists for a user/evidence reason.  
**FAIL:** arbitrary word count/keyword density or competitor-outline cloning drives the brief.  
**Next:** content creation.

## 7. Create differentiated content

**Inputs:** approved brief and source/evidence set.  
**Actions:** produce original data/research, real product facts, worked examples, first-hand testing/cases, media, decision aids, limitations and expert review as appropriate.  
**Tools:** product/data/testing systems, editorial workflow, primary sources.  
**Evidence:** source/methodology records and factual QA.  
**Output:** publishable page/asset.  
**PASS:** page is materially useful even if search traffic did not exist.  
**FAIL:** page mostly paraphrases competitors or exists to hit phrase/location variants.  
**Next:** on-page implementation.

## 8. On-page implementation

**Inputs:** approved content + target URL/intent.  
**Actions:** implement descriptive title/H1, visible evidence, internal anchors, media/alt, canonical/robots, CTA and appropriate snippet metadata.  
**Tools:** CMS/source/rendered HTML, analytics test, `checklists/on-page.md`.  
**Evidence:** raw/rendered output and tracking test.  
**Output:** implemented page.  
**PASS:** intent/content/technical directives agree.  
**FAIL:** hidden stuffing, wrong canonical/noindex, mobile content loss or metadata promise mismatch.  
**Next:** entity/trust layer.

## 9. Entity and trust layer

**Inputs:** organization/person/product/location facts and reputation sources.  
**Actions:** verify About/contact/support/policies, authorship/review, brand/NAP, credentials, independent references and reputation issues.  
**Tools:** `docs/entity-brand-reputation.md`, official organization records, relevant profiles/review platforms.  
**Evidence:** verifiable same-entity facts and source URLs.  
**Output:** entity/trust map and corrections.  
**PASS:** important claims/identities are consistent and verifiable.  
**FAIL:** fake credentials/reviews/locations or ambiguous entity identity.  
**Next:** structured data.

## 10. Structured data

**Inputs:** visible semantic entities and desired supported search features.  
**Actions:** choose Schema.org type; check engine-specific feature docs; generate JSON-LD; validate syntax/properties; compare visible content; monitor applicable reports.  
**Tools:** Schema.org, current Google Search docs, Rich Results Test/validators.  
**Evidence:** rendered markup + validator output + visible-content match.  
**Output:** validated semantic markup.  
**PASS:** truthful valid markup; feature requirements satisfied when targeting a feature.  
**FAIL:** invented ratings/entities or schema count is the KPI.  
**Next:** internal authority/discovery.

## 11. Internal authority / discovery

**Inputs:** architecture and priority URL portfolio.  
**Actions:** link from relevant hubs/guides, remove redirect/dead targets, use descriptive anchors, maintain breadcrumbs and useful reciprocal conceptual navigation.  
**Tools:** crawler/inlink export, `checklists/internal-links.md`.  
**Evidence:** orphan/depth/inlink/target-status before/after.  
**Output:** deployed internal-link graph.  
**PASS:** priority pages have crawlable contextual paths through final URLs.  
**FAIL:** orphans, spam anchors or large links to redirect/noindex paths.  
**Next:** external authority.

## 12. External authority / Digital PR

**Inputs:** authority gap and real assets/relationships.  
**Actions:** prioritize original research/data, tools/resources, partner/customer evidence, selective PR, legitimate directories/profiles and mention reclamation.  
**Tools:** measured backlink/mention data when available, `docs/links-authority.md`.  
**Evidence:** source relevance/editorial context/disclosure classification.  
**Output:** policy-safe authority/PR roadmap.  
**PASS:** every tactic serves a real audience/relationship and complies with link-spam boundaries.  
**FAIL:** PBNs, paid followed ranking links, automated packages, fake mentions or reputation abuse.  
**Next:** AI Search readiness.

## 13. AI Search readiness

**Inputs:** target AI/search providers, public content/entity facts.  
**Actions:** verify crawler/WAF access; separate search/training/user retrieval controls; preserve source evidence; track provider-specific citations/referrals; reject fake third-party mention tactics.  
**Tools:** `docs/ai-search.md`, `docs/geo-myths.md`, provider docs, robots/WAF logs, Bing/Google AI reports where available.  
**Evidence:** provider settings, access logs and dated baseline.  
**Output:** AI visibility baseline/control matrix.  
**PASS:** intended retrieval access and measurement are deliberate/provider-specific.  
**FAIL:** `llms.txt`/schema folklore or one citation is treated as universal ranking proof.  
**Next:** pre-launch gate.

## 14. Pre-launch gate

**Inputs:** final release candidate and all prior PASS artifacts.  
**Actions:** run `checklists/launch.md`: status, robots/index, canonical, rendering, links, schema, sitemap, mobile, performance regression, analytics, placeholder/privacy checks.  
**Tools:** HTTP/render tests, validators, analytics, crawler.  
**Evidence:** dated preflight output + release commit/tag + rollback plan.  
**Output:** `GO` or `NO-GO`.  
**PASS:** all applicable Critical items pass.  
**FAIL:** any Critical launch blocker.  
**Next:** deploy then post-launch validation.

## 15. Post-launch validation

**Inputs:** live release and pre-launch baseline.  
**Actions:** execute `checklists/post-launch.md`: live fetch/render, logs, GSC/BWT sampling, sitemap/IndexNow checks, analytics, migration mappings and release annotation.  
**Tools:** crawler, logs, GSC/BWT, analytics/RUM.  
**Evidence:** production before/after output.  
**Output:** validated release + open issue list.  
**PASS:** live state matches intended release; no unresolved Critical/High regression.  
**FAIL:** blocker/regression remains.  
**Next:** measurement window.

## 16. Measurement framework

**Inputs:** baseline, launch annotation and target query/page cohorts.  
**Actions:** track search impressions/clicks/query-page/canonical/conversions; AI citations/referrals separately; technical crawl/CWV/schema; relevant authority/reputation.  
**Tools:** GSC/BWT/analytics/CRM/RUM/rank tracker with locale context/AI reports.  
**Evidence:** comparable dated cohorts; known anomalies documented.  
**Output:** performance review.  
**PASS:** business/search/technical metrics are comparable and not incorrectly merged.  
**FAIL:** only rank/traffic/citation counts are reported without context/outcome.  
**Next:** iteration diagnosis.

## 17. Iteration decision tree

**Inputs:** performance review, current SERP and all prior phase evidence.  
**Actions:** diagnose low impressions, low CTR, poor conversion, non-indexation or Top-10 plateau against intent, technical state, evidence, authority, internal links, brand, freshness and competitor change. Select the smallest evidence-backed change.  
**Tools:** current SERP, GSC/BWT/analytics/CRM/logs, audit framework.  
**Evidence:** explicit bottleneck and bounded hypothesis.  
**Output:** one prioritized change + success/fail/stop condition.  
**PASS:** change addresses the diagnosed bottleneck and has measurement/rollback.  
**FAIL:** random title/content/link edits because a tool still shows warnings.  
**Next:** return to the affected phase and repeat the loop.

---

## Fast diagnosis patterns

### Impressions low / page indexed
Check query/page-type fit, authority/brand gap, internal discovery, evidence/depth, freshness/locality and whether another URL is selected/ranking.

### Impressions high / CTR low
Check title/snippet intent, SERP features, brand trust, position/query mix and stale pricing/date/value proposition.

### Traffic high / conversion low
SEO may be creating visits while business/intent fails. Re-check offer, page intent, UX, proof and CTA.

### Not indexed
Run technical/index-quality diagnosis; do not default to more backlinks.

### Plateau below Top 10
Re-run target SERP and compare page type, missing evidence, authority, internal links, entity reputation, freshness and competitor improvements. Then make the smallest testable change.

---

## Definition of a Top-10-ready page

A page is `TOP10_READY` when:

- target query/market is feasible;
- intent/page type matches current SERP;
- technical/index/canonical gate passes;
- content has real differentiated evidence;
- entity/trust facts are transparent;
- internal discovery is strong;
- external authority plan is policy-safe;
- AI crawler/search settings are deliberate;
- measurement, stop condition and rollback exist.

`TOP10_READY` is **not** “guaranteed Top 10.” It means the controllable inputs are competitive and verified according to this operating system.

## Playbook Quality Gate

`PASS` only when every executed phase has the mandatory eight-field record and all upstream Critical/High failures are closed before downstream optimization is declared complete.
