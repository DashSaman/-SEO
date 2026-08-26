# SEO Reference — Search, AI Search & Discoverability (2026)

> **Living reference repository** for evidence-based SEO across Google, Bing, other search engines, AI search/citation systems, technical SEO, content, structured data, performance, local/entity visibility, measurement, and open-source tooling.
>
> **مرجع زنده سئو** برای موتورهای جستجو و سیستم‌های جستجوی هوش مصنوعی؛ با اولویت منابع رسمی، داده‌های قابل‌اندازه‌گیری و مستندات قابل‌راستی‌آزمایی.

**Research snapshot:** 2026-08-26  
**Status:** Active research  
**Current baseline completion:** see [`PROGRESS.md`](PROGRESS.md)  
**Agent continuation state:** see [`HANDOFF.md`](HANDOFF.md)  
**Agent operating rules:** see [`AGENTS.md`](AGENTS.md)

---

## What this repository is

This repository is designed to answer four different questions without mixing them together:

1. **What do search engines officially require/recommend?**
2. **What do web standards actually specify?**
3. **What does observed SERP / industry data suggest?**
4. **What do community tools and repositories implement?**

A community claim is never promoted to an official ranking rule merely because it is popular. A ranking correlation is never documented as causation without evidence. No repository, consultant, plugin, score, schema type, keyword-density target, backlink count, or AI-specific file can guarantee a #1 ranking.

## Evidence hierarchy

| Level | Evidence class | Examples | How it is used |
|---|---|---|---|
| A | Official search/AI vendor documentation | Google Search Central, Bing Webmaster, Yandex, Naver, OpenAI, Anthropic, Perplexity | Primary source for product behavior and supported controls |
| A | Web standards/protocols | IETF RFC 9309, Sitemaps.org, Schema.org, IndexNow | Primary source for syntax/protocol behavior |
| B | Measured search data | SERP observations, Search Console, Bing Webmaster, Ahrefs-style measurements | Used for observed outcomes, never as proof of hidden ranking factors |
| B/C | Established practitioner research | Reproducible case studies and respected technical resources | Used when official documentation is incomplete |
| C | GitHub/community repositories | SEO crawlers, scripts, awesome lists, GEO/AEO projects | Tooling/ideas; claims are independently verified before promotion |

## Core model

Durable organic visibility is treated as a system rather than a checklist score:

**Discovery → Crawlability → Indexability → Canonicalization → Rendering → Relevance/Intent → Quality/Trust → Internal discovery → External/entity signals → Search presentation → AI retrieval/citation eligibility → Measurement → Iteration**

For Google’s generative Search experiences, Google’s current 2026 guidance explicitly says foundational SEO still applies and that special `llms.txt`, artificial content chunking, AI-only rewrites, inauthentic mentions, or special AI schema are not required for Google Search. AI crawler access for other services is a separate control plane and is documented independently in this repository.

## Reference map

- [`docs/google-seo.md`](docs/google-seo.md) — Google Search + AI Overviews/AI Mode + 2026 changes
- [`docs/bing-indexnow.md`](docs/bing-indexnow.md) — Bing, sitemaps, IndexNow, AI visibility
- [`docs/other-search-engines.md`](docs/other-search-engines.md) — Yandex, Naver and expansion queue
- [`docs/technical-seo.md`](docs/technical-seo.md) — crawling, indexing, canonical, redirects, robots, sitemaps, rendering, architecture
- [`docs/content-quality.md`](docs/content-quality.md) — intent, people-first content, E-E-A-T interpretation, spam boundaries
- [`docs/structured-data.md`](docs/structured-data.md) — Schema.org / search-engine structured-data implementation
- [`docs/ai-search.md`](docs/ai-search.md) — ChatGPT/OpenAI, Claude, Perplexity, Gemini/Google controls, crawler matrix
- [`docs/open-source-seo.md`](docs/open-source-seo.md) — curated GitHub repositories and tooling
- [`docs/serp-research.md`](docs/serp-research.md) — observed top-ranking resources and measured research notes
- [`docs/implementation-checklists.md`](docs/implementation-checklists.md) — practical audit/build/launch/monitoring checklists
- [`SOURCES.md`](SOURCES.md) — source-by-source research ledger

Some linked files are created as their research stage is completed; `PROGRESS.md` is the source of truth for availability/status.

## What is explicitly out of scope

- Guaranteed rankings or “secret ranking-factor” claims.
- Link schemes, cloaking, doorway pages, scaled content abuse, hacked links, parasite spam, fake reviews/mentions, or other policy-evasion tactics.
- Copying long passages from third-party sources. This repository synthesizes and cites.
- Treating SEO plugin scores as search-engine ranking scores.

## Live dashboard

A repository-native dashboard is maintained in [`PROGRESS.md`](PROGRESS.md). A static browser dashboard is maintained at [`docs/index.html`](docs/index.html) and is ready to be served with GitHub Pages if Pages is enabled for this repository.

## Contribution / multi-agent rule

Before any agent edits research content, it **must** read `AGENTS.md`, `HANDOFF.md`, `PROGRESS.md`, and `SOURCES.md`. After every completed source or research stage, update the source ledger, progress, and handoff state so another agent can resume without reconstructing context.

---

### Persian summary / خلاصه فارسی

این ریپازیتوری قرار است مرجع «حرف‌های قابل اثبات» باشد، نه مجموعه‌ای از ترفندهای سئو. هر ادعا باید مشخص کند از منبع رسمی آمده، استاندارد وب است، داده مشاهده‌شده است یا فقط تجربه/نظر جامعه سئو. هدف این است که یک انسان یا ایجنت هوش مصنوعی بتواند دقیقاً بفهمد چه چیزی قطعی است، چه چیزی توصیه است، چه چیزی هنوز نیاز به آزمایش دارد و آخرین مرحله تحقیق کجاست.
