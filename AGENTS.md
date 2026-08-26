# AGENTS.md — Operating Contract for SEO Research Agents

**Repository:** `DashSaman/-SEO`  
**Last protocol revision:** 2026-08-26

This file is mandatory reading for every AI agent or human researcher working in this repository.

## Mission

Build and maintain an evidence-first SEO/AEO/GEO/AI Search operating system covering classic search, AI-assisted search, technical implementation, content quality, discoverability, structured data, authority, measurement and open-source tooling. The repository must remain resumable, auditable and safe for parallel work.

## Non-negotiable rules

> **No source → no factual claim.**  
> **No synthesis → source not complete.**  
> **No coordination update → milestone not complete.**

Also:

- never fabricate an exact search rank, backlink count, traffic number or AI citation metric;
- never promote a community/GitHub statement to an official search-engine rule;
- never present vendor marketing copy as established product behavior without appropriate evidence;
- never turn correlation/observation into causation;
- never keep mutable search/crawler guidance as current without a review date/freshness check;
- never declare a task `PASS` merely because code/content was deployed — verify and retest live behavior;
- never promise Page 1/Top 10 rankings.

## Mandatory evidence hierarchy

1. **OFFICIAL** — current first-party engine/provider docs: Google, Bing/Microsoft, OpenAI, Anthropic, Perplexity, Apple, Baidu, Yandex, Naver, DuckDuckGo, etc.
2. **STANDARD** — IETF/RFC, Sitemaps.org, Schema.org, IndexNow, W3C/WHATWG where relevant.
3. **MEASURED** — GSC/BWT/logs/SERP measurements/credible datasets with context.
4. **RESEARCH** — peer-reviewed research or transparent preprints with inspectable methodology.
5. **PRACTITIONER** — established practitioner/vendor research where date/methodology/limits can be evaluated.
6. **COMMUNITY** — GitHub, Reddit, forums and community catalogues/tooling.

If sources conflict, record the conflict. Prefer the most current applicable first-party/standard source unless strong reproducible measurement shows actual product behavior differs. In that case document both product documentation and observed behavior; do not silently replace one with the other.

## Evidence labels for writing

Every meaningful claim must map to one of:

- `FACT-OFFICIAL`
- `FACT-STANDARD`
- `MEASURED` / `OBSERVED`
- `RESEARCH`
- `PRACTITIONER`
- `COMMUNITY`
- `INFERENCE`
- `HYPOTHESIS`

An `INFERENCE`/`HYPOTHESIS` must be visibly framed as such when it materially affects a recommendation.

## Required workflow for EVERY work unit

A work unit can be one source, one GitHub repository evaluation, one SERP batch, one topic document, one checklist or one validation batch. Complete these in order:

1. **Source research** — identify publisher/provider, URL/repository, date/activity and exact scope.
2. **Evidence classification** — assign OFFICIAL/STANDARD/MEASURED/RESEARCH/PRACTITIONER/COMMUNITY and status.
3. **Synthesis** — record what the evidence means, what it does not prove and any conflict/limitation.
4. **`SOURCES.md` update** — add/update evidence ledger row(s) when factual research changed.
5. **Topic/output update** — modify the relevant `docs/`, root playbook or `checklists/` file.
6. **`PROGRESS.md` update** — only when real stage completion/evidence counts changed; never inflate.
7. **`HANDOFF.md` update** — record current task, last completed task/source/commit context, files changed, conflicts/blockers and exact next task.
8. **Commit** — descriptive, bounded commit message.

**A work unit is not complete until its evidence has been synthesized and continuation state is preserved.** For micro-edits in a single tightly coupled milestone, coordination files may be updated at the milestone boundary rather than after every single contents-API commit, but they must reflect the complete milestone before the agent stops or reports completion.

## Required workflow for EVERY source

Determine:

- publisher/owner;
- evidence class;
- publication/update/review date when available;
- exact scope of the claim;
- applicable market/product/version;
- what the source **does not** prove;
- whether it supersedes/conflicts with older guidance.

Use `SOURCES.md` statuses:

- `VERIFIED`
- `PARTIAL`
- `DISCOVERED`
- `SUPERSEDED`
- `CONFLICT`
- `BACKLOG`

A source row without synthesis in a durable topic document is not enough for production-reference readiness.

## Required workflow for EVERY stage

At stage completion:

- verify new factual claims have appropriate evidence rows;
- run a consistency/freshness pass against current official guidance;
- verify no Critical/High unresolved baseline gap remains for that stage;
- update `PROGRESS.md` weighted completion;
- update `docs/index.html` dashboard;
- update `HANDOFF.md` with the exact next task;
- commit with a descriptive stage message.

## Parallel-agent protocol

Before starting shared work:

- read `HANDOFF.md` and latest commit history;
- claim/identify a non-conflicting workstream;
- do not overwrite shared coordination files from stale SHAs;
- before modifying `SOURCES.md`, `PROGRESS.md`, `HANDOFF.md`, `AGENTS.md` or dashboard, re-fetch the current file/SHA;
- if taking over an apparently abandoned claim, preserve the prior claim and mark the takeover rather than silently erasing history;
- merge evidence by source ID, not by deleting another agent’s valid research.

Independent workstreams can include Google, Bing/IndexNow, regional engines, web standards, AI crawlers, GitHub tooling, SERP/practitioner research, local/entity, ecommerce/international/media, measurement and validation.

## SERP measurement rules

Search rankings are market/time/device dependent.

- Always record query, date, engine and geography when known; device when material.
- If a provider capable of exact positions is unavailable, write `OBSERVED-WEB-SEARCH` or equivalent — never invent `#1`, Top 3 or Top 10 positions.
- Third-party DR/DA/traffic estimates are provider metrics/proxies, not Google metrics.
- Current prominent results can reveal intent/page type/format; they do not prove why a page ranks.
- Re-measure real client commercial queries in the actual target market before implementation.

## Practitioner / vendor rules

Practitioner sources are valuable for workflow, examples and measured hypotheses, but:

- identify ownership/affiliation when material;
- distinguish case-study result from universal rule;
- preserve methodology/date/market limits;
- cross-check spam-policy-sensitive advice against current engine documentation;
- never convert a tool/vendor’s proprietary score into a search-engine score.

## GitHub / community rules

For important repositories record purpose, archive state, maintenance/activity, license metadata/file, last meaningful update, features, strengths, weaknesses, operational/security concerns, claim cautions, official-doc conflicts, recommended use and verdict.

Allowed verdicts:

- `RECOMMENDED`
- `USEFUL`
- `SPECIALIZED`
- `EXPERIMENTAL`
- `STALE`
- `AVOID`

Stars/forks/popularity never raise evidence class.

## Freshness rules

SEO/search/AI documentation changes frequently.

- record `Reviewed: YYYY-MM-DD` on mutable durable documents/sources;
- re-check crawler identity, robots controls, AI Search controls/reporting, rich-result eligibility, spam policies and Webmaster/Search Console product features before production changes;
- prefer current first-party material when older guidance conflicts;
- preserve useful historical advice only as `SUPERSEDED`/legacy;
- archive status or repository `updated_at` is not enough — inspect meaningful push/release/maintenance data when evaluating code.

## Safety / policy guardrails

Do not recommend or operationalize:

- paid-link/PBN/link-farm schemes for ranking manipulation;
- cloaking/deceptive crawler-specific output;
- doorway/location synonym page factories;
- mass low-value scaled content for query capture;
- fake reviews, fake Reddit/forum mentions or fabricated citations;
- hacked-site/link injection;
- fake first-hand tests/experts/customers/data;
- evasion of spam/manual-action enforcement.

Discuss such tactics only to identify/remove risk.

## Technical correctness locks

- `robots.txt` controls crawler access preferences; it is not security/authentication.
- `noindex` and crawl blocking are separate controls; a blocked bot may not see page-level noindex.
- canonical signals are generally preferences/hints, not an absolute guarantee across engines.
- sitemap inclusion helps discovery; it does not guarantee crawl/index/rank.
- IndexNow notifies participating engines of changes; it does not guarantee crawl/index/rank.
- structured data can describe entities/enable supported features; schema count is not a ranking KPI and rich-result display is not guaranteed.
- current Core Web Vitals are useful UX/search diagnostics; Lighthouse/Web Vitals scores are not Google ranking scores.
- Google’s current 2026 generative Search guidance does not require special AI schema, `llms.txt`, artificial chunking or manufactured mentions.
- search crawlers, training crawlers and user-triggered retrieval bots must be treated separately when providers document separate controls.
- AI citation ≠ ranking ≠ authority ≠ traffic ≠ conversion.
- dynamic rendering is a legacy/workaround pattern, not the preferred default architecture in current Google JavaScript guidance.
- disavow is not a routine third-party “toxicity cleanup” workflow; current Google guidance controls when it is appropriate.

## Copyright / quotation rule

Synthesize. Keep quotations short and necessary. Link to primary sources. Do not republish documentation/articles/proprietary datasets/repository content wholesale.

## File responsibilities

- `README.md` — stable entry point/navigation/philosophy.
- `AGENTS.md` — this operating contract.
- `HANDOFF.md` — exact live continuation state.
- `PROGRESS.md` — weighted research/quality progress.
- `SOURCES.md` — master evidence ledger.
- `TOP10_PLAYBOOK.md` — end-to-end execution operating system.
- `SEO_AUDIT_SOP.md` — dependency/severity/retest audit procedure.
- `RANKING_FRAMEWORK.md` — query feasibility/prioritization framework.
- `docs/*.md` — durable topic synthesis.
- `docs/site-types/*.md` — site-type playbooks.
- `checklists/*.md` — auditable deployment/validation gates.
- `docs/index.html` — static GitHub-Pages-compatible dashboard.
- `FINAL_VALIDATION.md` — final adversarial quality-gate record when baseline is finalized.

## Definition of done for a factual claim

Production-reference ready only when it has:

1. named source/repository/dataset;
2. URL or stable identifier;
3. review/observation date;
4. evidence class;
5. scope/caveat and what it does not prove when needed;
6. synthesis in relevant durable documentation.

## Definition of done for a milestone

A milestone is complete only when:

- required artifacts exist and are substantive;
- factual claims are evidence-classified;
- Critical/High gaps are fixed or explicitly block completion;
- before/after verification/retest exists for implementation gates;
- source/progress/handoff/dashboard state is reconciled;
- a descriptive commit records the milestone.

Only `FINAL_VALIDATION.md` can authorize `PROJECT STATUS: 100% COMPLETE`, and only when every defined baseline gate is `PASS`, Critical findings = 0 and High findings = 0.
