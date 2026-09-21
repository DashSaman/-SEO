# Revenue Opportunity Engine Architecture

The Growth OS must be more than an SEO or content-publishing stack. Its product goal is to continuously discover, score, execute, and measure revenue and competitive opportunities.

## Product principle

The system should continuously ingest market and business-performance signals, turn opportunities into executable actions, measure outcomes, and learn from the results.

```text
Signals
  ├─ GSC / queries / CTR / positions
  ├─ GA4 / conversions / landing-page performance
  ├─ SERP / competitors / content gaps
  ├─ Website crawl / technical SEO / internal linking
  ├─ Competitor pages / pricing / offers / launches
  ├─ Trends / RSS / news / communities
  ├─ Social reach / engagement / search visibility
  ├─ Leads / forms / calls / CRM signals when connected
  ├─ Product/service margin and business priority
  └─ Server / logs / indexation / uptime
          ↓
Revenue Opportunity Engine
          ↓
Score = revenue potential + intent + demand + speed + confidence - effort - risk
          ↓
Action Plan
          ↓
Website / Content / Social / Offer / Conversion / Product / Outreach
          ↓
QA + Approval Tier
          ↓
Publish / Deploy / Schedule
          ↓
Measure revenue-oriented outcome
          ↓
Learn / Re-score / Repeat
```

## Opportunity classes

### Search / SEO
- high-impression queries close to page one;
- low CTR relative to position;
- content decay;
- cannibalization;
- weak internal-link coverage;
- competitor topics we do not cover;
- SERPs where a tool, FAQ, video, or service page could create differentiation;
- crawl/index/schema/performance issues blocking commercial pages.

### Commercial / Revenue
- purchase/contact/pricing/comparison/service-request intent;
- services with demand but weak website coverage;
- landing-page or tool opportunities for lead generation;
- upsell/cross-sell opportunities;
- offers and CTAs that should be tested;
- product/service ideas supported by observed demand.

### Competitor Intelligence
- new competitor pages or services;
- pricing, offer, CTA, and landing-page changes;
- new topic clusters;
- new free tools or lead magnets;
- content gaining visibility quickly;
- meaningful navigation/schema/content-format changes;
- unmet gaps competitors have not covered.

### Content / Social
- fresh and trending topics;
- web content that can become Reel/Short/Carousel/Thread assets;
- social posts that should become evergreen pages;
- high-performing social/video assets that deserve reinforcement;
- channel/timing patterns learned from first-party performance data.

### Conversion / CRO
- traffic-rich pages with low conversion;
- weak CTAs;
- broken or overlong forms;
- user journeys losing leads;
- A/B test opportunities for title, hero, CTA, offer, and form.

### Product / Business Discovery
- recurring customer questions and requests;
- search demand for services/products not currently offered;
- recurring audience problems that could become a tool, SaaS, service package, or downloadable asset;
- opportunities aligned with existing business capabilities.

## Opportunity data model

```yaml
opportunity:
  site: mytel | tehnet
  source: gsc | serp | competitor | trend | social | analytics | crm
  type: seo | content | offer | cro | product | social | technical
  title: "..."
  evidence: "..."
  revenue_potential: 0-100
  commercial_intent: 0-100
  demand: 0-100
  speed_to_result: 0-100
  confidence: 0-100
  effort: 0-100
  risk: 0-100
  priority_score: calculated
  recommended_action: "..."
  approval_tier: auto | review | manual
  owner_agent: "..."
  status: detected | planned | executing | measuring | closed
```

## Revenue over vanity traffic

The system should distinguish between large traffic with no business outcome and smaller traffic that generates qualified leads. The final dashboard should therefore combine rank/traffic with leads, calls, conversion, commercial value, production/AI cost, and ROI wherever the required first-party data is connected.

## Automation tiers

### Auto
Low-risk, reversible actions after pilot validation, such as approved scheduling, reporting, selected internal-link updates, and pre-approved refresh workflows.

### Review
Content, landing pages, CTA changes, social campaigns, and normal PRs should initially pass human or multi-agent review.

### Manual
URL deletion, broad canonical/redirect changes, major architecture changes, sensitive pricing/offers, advertising spend, and financial actions must not run without explicit approval.

## Future commercial product

A customer connects a site and channels; the system builds a Business Manifest, discovers opportunities, prioritizes them by expected business value, executes through specialized agents, and exposes results through a Revenue Dashboard.

MyTel and Tehran Network are the first pilots used to build real decision data. Both successful and failed opportunities should be retained so the product's prioritization logic improves from first-party experience.
