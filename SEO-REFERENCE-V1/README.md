# SEO Reference — Search, AEO, GEO & AI Search Operating System (2026)

> Evidence-backed reference and execution system for classic SEO, AI-assisted search, technical implementation, content, authority, entities, structured data, measurement and validation.
>
> مرجع عملیاتی و evidence-first برای SEO / AEO / GEO / AI Search؛ با تفکیک منابع رسمی، استاندارد، داده مشاهده‌شده، پژوهش، practitioner و community.

**Research snapshot:** 2026-08-26  
**Project state:** see [`PROGRESS.md`](PROGRESS.md) and [`FINAL_VALIDATION.md`](FINAL_VALIDATION.md) once the final gate exists.  
**Live continuation state:** [`HANDOFF.md`](HANDOFF.md)  
**Agent contract:** [`AGENTS.md`](AGENTS.md)  
**Visual dashboard:** [`docs/index.html`](docs/index.html) — static/GitHub-Pages-compatible; this does not imply GitHub Pages hosting is enabled.

---

# START HERE

## I want to audit a site

Start with **[`SEO_AUDIT_SOP.md`](SEO_AUDIT_SOP.md)**.

It runs issues in dependency order:

`Security → Availability → DNS/HTTPS/HTTP → Status → Crawl → Index → Canonical → Redirects → Rendering → Internal Links → Architecture → Duplication → Content → Intent → Structured Data → CWV → Authority → Special Cases → AI Search → Measurement`

Use the relevant [`checklists/`](checklists/) file for live PASS/FAIL/retest evidence.

## I want to decide whether a query is worth targeting

Use **[`RANKING_FRAMEWORK.md`](RANKING_FRAMEWORK.md)**.

It evaluates:

- business value;
- current SERP intent/page type;
- technical readiness;
- differentiation/evidence;
- YMYL/high-stakes risk;
- brand/entity gap;
- measured authority gap when available;
- freshness;
- local/international/ecommerce constraints;
- AI surface relevance;
- stop-loss/economics.

Output is a bounded decision such as `GO`, `NOT-YET`, `GO-LONG-TERM`, `LOW-PRIORITY`, or `NO-GO` — never a fake guaranteed ranking probability.

## I want an end-to-end Top 10 execution workflow

Use **[`TOP10_PLAYBOOK.md`](TOP10_PLAYBOOK.md)**.

It runs:

**Business → Market → Competitors → Query Universe → Intent → Architecture → Technical → Content → Entities → Structured Data → Internal Links → Authority → AI Search → Launch → Validation → Measurement → Iteration**

Every phase requires:

`Inputs / Actions / Tools / Evidence / Output / PASS / FAIL / Next Action`

`TOP10_READY` means controllable inputs are competitive and verified; it does **not** mean Top 10 is guaranteed.

## I need a specific SEO topic

Use the topic reference map below under [`docs/`](docs/).

## I need deployment/retest validation

Use [`checklists/`](checklists/). All baseline checklists require actionable checks, PASS criteria, common failures and live retest evidence.

## I am another AI agent

Read, in this order:

1. [`AGENTS.md`](AGENTS.md)
2. [`HANDOFF.md`](HANDOFF.md)
3. [`PROGRESS.md`](PROGRESS.md)
4. [`SOURCES.md`](SOURCES.md)
5. the relevant topic/output files.

Do not start from chat memory or an old progress percentage.

## I want the evidence ledger

Use **[`SOURCES.md`](SOURCES.md)**.

## I want project status / final quality state

Use:

- [`PROGRESS.md`](PROGRESS.md)
- [`docs/index.html`](docs/index.html)
- [`HANDOFF.md`](HANDOFF.md)
- [`FINAL_VALIDATION.md`](FINAL_VALIDATION.md) after final validation has been created.

---

# What this repository is — and is not

This repository separates six evidence classes instead of mixing them:

| Priority | Evidence class | Typical examples | Use |
|---:|---|---|---|
| 1 | `OFFICIAL` | Google, Bing/Microsoft, OpenAI, Anthropic, Perplexity, Apple, Baidu, Yandex, Naver, DuckDuckGo | product behavior, controls, policies |
| 2 | `STANDARD` | RFC 9309, Sitemaps.org, Schema.org, IndexNow | protocol/vocabulary behavior |
| 3 | `MEASURED` | GSC/BWT/logs/SERP observations/datasets | observed outcomes with date/context |
| 4 | `RESEARCH` | peer-reviewed or transparent preprint studies | methodology-bound evidence |
| 5 | `PRACTITIONER` | Ahrefs, Semrush, Moz, Backlinko, technical SEO practitioners | workflow/examples/hypotheses |
| 6 | `COMMUNITY` | GitHub, forums, Reddit/community tooling | implementation/discovery, not ranking truth |

A community claim never becomes an official ranking rule because it is popular. A correlation never becomes causation because a chart looks convincing. A plugin score, Lighthouse score, DR/DA, schema count, keyword-density target, backlink count or AI-specific file cannot guarantee #1/Page 1.

# Core model

Durable visibility is treated as a system:

**Discovery → Crawlability → Indexability → Canonicalization → Rendering → Intent/Relevance → Quality/Evidence → Internal Discovery → Entity/Reputation → External Authority → Search Presentation → AI Retrieval/Citation Eligibility → Measurement → Iteration**

For Google’s current 2026 generative Search experiences, foundational SEO remains applicable; no special `llms.txt`, artificial chunking, AI-only rewrite, manufactured mentions or universal “AI schema” is required for Google Search. Other provider crawler/search/training controls are documented separately.

---

# Reference map

## Search engines / standards

- [`docs/google-seo.md`](docs/google-seo.md) — Google Search + AI Overviews/AI Mode + 2026 controls/reporting
- [`docs/bing-indexnow.md`](docs/bing-indexnow.md) — Bing, IndexNow, Bing AI Performance/Copilot citation measurement
- [`docs/other-search-engines.md`](docs/other-search-engines.md) — Yandex, Naver, Baidu, DuckDuckGo, Apple
- [`docs/technical-seo.md`](docs/technical-seo.md) — crawl/index/canonical/redirects/robots/sitemaps/architecture
- [`docs/javascript-seo.md`](docs/javascript-seo.md) — SSR/SSG/CSR/hydration/rendering/SPA/infinite scroll
- [`docs/crawl-budget-log-analysis.md`](docs/crawl-budget-log-analysis.md) — logs, crawl waste, bot verification and scale
- [`docs/structured-data.md`](docs/structured-data.md) — Schema.org vs engine feature support

## Content / authority / entities

- [`docs/content-quality.md`](docs/content-quality.md) — intent, people-first quality, E-E-A-T interpretation, scaled-content boundaries
- [`docs/links-authority.md`](docs/links-authority.md) — link earning, Digital PR, spam boundaries, disavow nuance
- [`docs/entity-brand-reputation.md`](docs/entity-brand-reputation.md) — brand/entity/reputation/NAP/sameAs concepts
- [`docs/offsite-platforms.md`](docs/offsite-platforms.md) — authentic third-party presence without manipulation
- [`docs/programmatic-seo.md`](docs/programmatic-seo.md) — pSEO quality/index/crawl gates

## Specialties

- [`docs/local-seo.md`](docs/local-seo.md)
- [`docs/international-seo.md`](docs/international-seo.md)
- [`docs/ecommerce-seo.md`](docs/ecommerce-seo.md)
- [`docs/media-seo.md`](docs/media-seo.md) — image/video/media

## AI Search / GEO / AEO

- [`docs/ai-search.md`](docs/ai-search.md) — Google/OpenAI/Claude/Perplexity/Bing/other crawler controls and measurement
- [`docs/geo-myths.md`](docs/geo-myths.md) — provider-specific myth busting
- [`docs/measurement.md`](docs/measurement.md) — classic + AI search measurement/causality

## Research / tooling

- [`docs/open-source-seo.md`](docs/open-source-seo.md) — individually evaluated GitHub/open-source tools with activity/license/risks/verdicts
- [`docs/serp-research.md`](docs/serp-research.md) — dated representative SERP/practitioner observations and measurement limits

---

# Site-type playbooks

Use the relevant file under [`docs/site-types/`](docs/site-types/):

- [`saas-b2b.md`](docs/site-types/saas-b2b.md)
- [`ecommerce.md`](docs/site-types/ecommerce.md)
- [`local-business.md`](docs/site-types/local-business.md)
- [`publisher-news.md`](docs/site-types/publisher-news.md)
- [`affiliate.md`](docs/site-types/affiliate.md)
- [`marketplace-directory.md`](docs/site-types/marketplace-directory.md)
- [`forum-ugc.md`](docs/site-types/forum-ugc.md)
- [`international.md`](docs/site-types/international.md)
- [`service-business.md`](docs/site-types/service-business.md)

---

# Operational checklists

Available under [`checklists/`](checklists/):

- [`technical-seo.md`](checklists/technical-seo.md)
- [`content.md`](checklists/content.md)
- [`on-page.md`](checklists/on-page.md)
- [`internal-links.md`](checklists/internal-links.md)
- [`structured-data.md`](checklists/structured-data.md)
- [`backlinks.md`](checklists/backlinks.md)
- [`local.md`](checklists/local.md)
- [`ecommerce.md`](checklists/ecommerce.md)
- [`international.md`](checklists/international.md)
- [`javascript.md`](checklists/javascript.md)
- [`migration.md`](checklists/migration.md)
- [`ai-search.md`](checklists/ai-search.md)
- [`launch.md`](checklists/launch.md)
- [`post-launch.md`](checklists/post-launch.md)

A checklist passes only with evidence. Deployment alone is not PASS.

---

# Explicitly out of scope

- guaranteed Page 1 / Top 10 / #1 claims;
- secret-ranking-factor claims without appropriate evidence;
- PBNs, paid followed ranking-link schemes, cloaking, doorway pages, hacked links or spam-evasion tactics;
- fake reviews/Reddit/forum mentions/citations;
- scaled low-value page factories;
- fabricated tests, experts, customers, data or case studies;
- treating plugin/vendor/tool scores as search-engine scores;
- reproducing third-party articles/documentation rather than synthesizing them.

# Working definition of success

> This repository is an evidence-based SEO operating system designed to maximize the probability of successful organic competition through technical quality, search intent, differentiated content/evidence, authority, entity/reputation signals, AI-search visibility, measurement and iteration.

Actual rankings remain query-, market-, competition-, time- and engine-dependent.

---

## خلاصه فارسی

این Repository قرار نیست «ترفند تضمینی صفحه اول» بدهد. هدفش این است که انسان یا AI Agent بتواند برای یک سایت واقعی ابتدا امکان رقابت را بسنجد، مشکلات فنی را به‌ترتیب وابستگی پیدا کند، Intent و Page Type درست را انتخاب کند، محتوای متمایز و قابل‌اثبات بسازد، Authority/Entity/AI Search را اصولی مدیریت کند و همه تغییرات را با قبل/بعد و PASS/FAIL اندازه‌گیری کند. هر ادعا باید معلوم کند رسمی است، استاندارد است، اندازه‌گیری شده، پژوهشی است یا صرفاً practitioner/community evidence.
