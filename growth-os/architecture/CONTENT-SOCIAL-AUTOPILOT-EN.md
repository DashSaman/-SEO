# Unified Content + Social Autopilot Architecture

The goal is for Growth OS to manage the full loop from opportunity discovery through content production, channel-specific repurposing, publishing, measurement, and continuous improvement — not merely SEO monitoring.

## Core loop

```text
Signals
  ├─ GSC
  ├─ GA4
  ├─ Rank/SERP
  ├─ Website crawl
  ├─ Server/log signals
  ├─ Competitor changes
  ├─ Trends/RSS
  └─ Social performance
       ↓
Opportunity Engine
       ↓
Content Planner
       ↓
Content + Media Production
       ↓
QA / Brand / SEO / Safety Gates
       ↓
Publish
  ├─ Website
  ├─ Telegram
  ├─ Instagram
  ├─ YouTube
  ├─ X
  └─ other supported channels
       ↓
Measure
       ↓
Learn / reprioritize / repeat
```

## Principle: do not blindly copy the same content everywhere

One core topic can produce channel-specific assets:

- Website: deep article, service page, FAQ, schema, internal links
- Telegram: practical summary + CTA + link
- Instagram: carousel/reel script/caption
- YouTube: long tutorial + Short
- X: concise technical thread

Agents should adapt content to each channel's intent and format instead of pasting identical text.

## System roles

### Research / Opportunity Agent
Inputs: GSC, GA4, SERP, crawl, competitors, trends
Output: prioritized opportunities with rationale, business value, and effort

### Content Strategist Agent
Decides whether to refresh an existing page or create a new one, which intents to cover, and which social assets to derive.

### Writer / Editor Agent
Creates or improves articles, landing pages, service pages, FAQs, title/meta, schema data, internal-link copy, and channel copy.

### Media Agent
Later phases may generate images, thumbnails, carousels, short/reel storyboards, video scripts, and subtitles/transcripts. On the pilot laptop, heavy media generation should be job-based so an 8GB GPU is not saturated alongside local LLM workloads.

### Publisher Agent
Adapters:
- Website: GitHub PR / SSH deploy / CMS API
- Social: Postiz or official platform APIs
- Telegram: Bot/API

### Measurement Agent
Measures index/crawl status, GSC impressions/clicks/CTR/position, GA4 sessions/conversions, social reach/clicks/engagement, uptime, and errors. Results feed back into the Opportunity Engine.

## Approval tiers

Low risk can later be automated after pilot validation: metadata cleanup, verified internal links, alt/structured housekeeping, approved-content social scheduling, small refreshes with QA.

Medium risk should initially require PR/review: new articles, landing pages, major rewrites, large FAQ/schema changes, new campaigns.

High risk requires explicit human approval: URL deletion/change, site-wide canonical/redirect changes, navigation/architecture changes, sensitive pricing/commercial claims, deletion of important content.

## Productization target

Each site becomes an isolated logical tenant/workspace containing a site manifest, brand profile, content policy, credential references, approved claims, conversion goals, competitors, action history, cost ledger, and result ledger.

The agent should ask the user only for information it cannot reliably discover from the website, repository, connected sources, or site manifest.

## Pilots

MyTel runs in Growth Mode: existing-site audit, GSC/GA4 opportunity mining, content refresh, lead/conversion focus, and social repurposing.

Tehran Network runs in Build + Growth Mode: discover missing business/site inputs, ask targeted questions, complete architecture/pages/content, pass launch QA, then switch to ongoing Growth Mode.

## Success criteria

Success is not content volume. Track qualified organic clicks, conversions/leads, CTR improvements, tracked-query movement, production cost, time to publish, social-to-site traffic, and autonomous actions that remained valid vs actions that required rollback.

Google Page-1 rankings are not guaranteed; the system should continuously identify and test the fastest, highest-value opportunities supported by current data.
