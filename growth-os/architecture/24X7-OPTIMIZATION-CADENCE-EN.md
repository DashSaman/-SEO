# Growth OS 24/7 Operating Cadence

## Goal
Growth OS should operate continuously per site. The owner reviews reports, outcomes and suggestions rather than performing routine production work manually.

## Continuous loop

```text
Signals / Health / Search / Competitors / Social / Leads
        ↓
24/7 Monitoring
        ↓
Opportunity Queue + Alerts
        ↓
Daily Analysis + Daily Report
        ↓
7-Day Optimization Cycle
        ↓
Execute low-risk approved work
        ↓
Measure Before/After
        ↓
Learn + Re-score + Repeat
```

## 24/7 Monitoring
- Monitor service health, crawl/indexability, technical errors, GSC/GA4, SERP/rank, competitors, trends, social signals and lead/conversion data whenever the relevant connectors are enabled.
- Fast-changing or incident signals may be checked more frequently; the system must not wait for the daily report to notice an outage or critical issue.
- If the local laptop/worker is temporarily offline, jobs must be recoverable/queueable. A truly always-on commercial SLA requires an always-on control plane during productization.

## Daily Report — every 24 hours
Each site receives an isolated report in its own repository and Telegram reporting destination. The report should include at least:
- health and incidents;
- rank/impression/CTR/traffic/conversion changes when data is available;
- newly detected SEO/marketing/competitor/content/CRO/revenue opportunities;
- actions completed in the prior 24 hours;
- verification/outcome of each action;
- failed/retried/queued work;
- compute/API cost when applicable;
- highest-priority planned work for the next cycle.

## 7-Day Optimization Cycle
Every seven days, each site runs a complete optimization cycle:
1. Capture a before snapshot.
2. Re-score opportunities with fresh evidence.
3. Select lower-risk, higher-commercial-priority actions.
4. Execute SEO/content/internal-link/CRO/social/technical actions appropriate to the enabled phase.
5. Run QA and verification.
6. Capture an after snapshot.
7. Record before/after evidence and early effects.
8. Keep, adjust, roll back or continue testing based on evidence.

## Measurement principle
Success is not measured by task count alone. Depending on available site data, metrics include search visibility, CTR, qualified traffic, leads, calls, conversions, commercial value and revenue/ROI. Higher rankings or traffic alone do not guarantee business success.

## Automation policy
- Monitoring, data collection, reporting, queue management and low-risk actions may be automated.
- Destructive/high-impact actions such as URL deletion, broad redirects/canonicals, major architecture changes, sensitive pricing changes or ad spend without authorization remain fail-closed.
- Owner workflow is review-first: routine content creation, editing, uploading and scheduling should not require manual owner production work.

## Reporting isolation
MyTel and Tehran Network keep separate state, action logs, experiment logs, repository reports and Telegram destinations so results are never mixed.
