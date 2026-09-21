# AI Search / GEO / AEO Reference (2026)

**Reviewed:** 2026-08-26  
**Evidence policy:** provider-specific behavior must come from current first-party documentation wherever possible.

## 1. First principle: AI visibility is not one system

“AI SEO”, “GEO”, “AEO” and “LLMO” are umbrella labels. Different products may involve different stages:

**crawler access → web/index discovery → retrieval → reranking/context selection → generation → citation/link selection → user click/conversion**

A tactic that affects one stage does not prove an effect on another.

Examples:

- allowing a crawler can make retrieval possible but does not guarantee citation;
- being cited does not guarantee traffic;
- a content rewrite that increases citation in a fixed experimental context does not prove improved organic discovery;
- a training opt-out bot is not necessarily the bot used for search retrieval;
- an AI-feature inclusion toggle is not necessarily a normal Search ranking control.

## 2. Evidence hierarchy for AI search

1. first-party crawler/search/control/reporting documentation;
2. repeated measured observations with date/query/model/location context;
3. peer-reviewed/preprint research with clearly stated assumptions;
4. practitioner case studies with reproducible methodology;
5. community crawler lists/tool marketing.

Do not turn a vendor marketing claim into a universal AI ranking factor.

## 3. Google AI Overviews / AI Mode

Primary source: [Google’s 2026 generative-AI Search guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)

Google states that its generative Search features are rooted in core Search ranking/quality systems and retrieve from the Search index. Conventional SEO remains foundational.

Google says you do **not** need, for Google Search:

- `llms.txt`;
- special AI markup/schema;
- artificial content chunking;
- an AI-specific writing style;
- pages for every query-fan-out wording;
- inauthentic external mentions.

Focus instead on accessible/indexable pages and differentiated, helpful, trustworthy content with useful media/local/product information where relevant.

## 4. NEW in 2026: Search generative AI control in Search Console

Official source: [Search generative AI control](https://support.google.com/webmasters/answer/16908024)

Google is rolling out a **Search generative AI control** to a subset of Search Console properties. It governs whether a property’s links/content can participate in:

- AI Overviews;
- AI Mode;
- generative AI features in Google Discover.

The documented states are:

| Setting | Effect |
|---|---|
| **Include** | default; links/content may appear and may help ground responses; eligibility does not guarantee appearance |
| **Exclude** | links/content are prevented from appearing or grounding responses in covered Search generative-AI features; no impressions/traffic from those features |
| **Inherit from parent** | child property follows the closest configured parent unless overridden |

Important boundaries documented by Google:

- this setting is **not** used as a ranking or inclusion signal for other parts of Search;
- it does not control AI model training;
- `Google-Extended` remains the separate control for specified model-training uses;
- `noindex` remains the control for removing content from Google Search entirely;
- rollout is gradual, so absence of the setting/report does not prove exclusion;
- setting changes generally take days to propagate, with some caching delay.

### Operational audit field

Every 2026 Google AI visibility audit should now record:

```text
Search generative AI control availability: yes/no
Property setting: Include / Exclude / Inherit / unavailable
Parent property setting (if inherited):
Date changed:
Expected propagation window:
```

This control materially changes how zero AI impressions should be interpreted.

## 5. NEW in 2026: Generative AI performance report

Official source: [Generative AI performance report (Search)](https://support.google.com/webmasters/answer/16984139)

Google is rolling out a separate report that shows **organic impressions** from supported generative-AI Search features, currently including:

- AI Overviews;
- AI Mode.

Current documented dimensions include:

- pages;
- countries;
- dates;
- devices.

Google notes:

- not all properties have access yet;
- a property may not show the report if it lacks sufficient impressions;
- the report inherits usual Search Console data/row/aggregation limitations;
- most page data is attributed to canonical URLs;
- current report data can be preliminary;
- Search Labs experiments are excluded.

### Counting details

Google’s Search Console documentation currently specifies:

- clicking an external link in AI Mode counts as a click;
- AI Mode impressions use standard impression rules;
- follow-up questions in AI Mode are treated as new queries;
- an AI Overview is assigned a single Search position and links within it inherit that position;
- an AI Overview link must be scrolled/expanded into view to count as an impression.

Do not compare AI Overview/AI Mode “position” mechanically with an ordinary blue-link position without accounting for these counting rules.

## 6. Google-Extended

Official source: [Google common crawlers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers)

`Google-Extended`:

- is a robots.txt **product token**;
- does not have a separate HTTP User-Agent string;
- controls specified uses of Google-crawled content for future Gemini model training and grounding in Gemini/Vertex contexts;
- does **not** affect inclusion in Google Search;
- is **not** a Google Search ranking signal.

### Google control separation

| Goal | Current Google control |
|---|---|
| participate in ordinary Search | normal Googlebot/index controls |
| include/exclude from covered Search generative-AI features | Search Console **Search generative AI control** (where available) |
| limit specified model-training/Gemini uses | `Google-Extended` |
| remove page from Google Search | `noindex` / access removal as appropriate |

Never collapse these into one “AI bot” switch.

## 7. OpenAI / ChatGPT Search

Official sources:

- [Publishers and Developers FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq)
- [Guidance for allowing OpenAI web crawlers](https://help.openai.com/en/articles/20001243-advertiser-guidance-for-allowing-openai-web-crawlers)

### Bot/control separation

| OpenAI control | Primary documented role | Visibility implication |
|---|---|---|
| `OAI-SearchBot` | search crawling/discovery for ChatGPT search | blocking can prevent content from being crawled for search summaries/snippets |
| `GPTBot` | model-training related crawling | training preference; do not treat as SearchBot |
| user-triggered retrieval behavior | fetch content in response to user action where applicable | can differ from scheduled search crawling |

OpenAI notes that a public URL known through other sources may still appear in limited form even if page crawling is restricted; crawler blocking is not a privacy/access-control system.

OpenAI documents referral attribution using `utm_source=chatgpt.com` for ChatGPT search referrals.

### Operational checklist

- allow `OAI-SearchBot` if ChatGPT Search discoverability is desired;
- ensure robots rules are not unintentionally overridden by WAF/CDN bot protection;
- verify official bot/IP mechanisms rather than trusting User-Agent alone;
- keep important content server-accessible and not locked behind unnecessary interaction;
- measure ChatGPT referrals separately from citation/mention monitoring.

## 8. Anthropic / Claude

Official source: [Anthropic crawler guidance — April 7, 2026](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)

Anthropic documents three separate robots:

| Bot | Documented use | If blocked |
|---|---|---|
| `ClaudeBot` | content that may contribute to model development/training | signals future materials should be excluded from training datasets |
| `Claude-User` | user-directed retrieval when Claude users ask questions | can reduce ability to retrieve site content for user requests |
| `Claude-SearchBot` | web navigation/indexing to improve search-result quality | can reduce site visibility/accuracy in Claude search results |

Anthropic states these bots honor robots.txt. It also documents support for a non-standard `Crawl-delay` extension. Anthropic warns that simply IP-blocking bots can interfere with robots access and may not be a durable opt-out mechanism.

Do not advise “block ClaudeBot to disappear from Claude Search” or “allow ClaudeBot to rank in Claude Search” without distinguishing the three bots.

## 9. Perplexity

Official source: [Perplexity robots.txt guidance](https://www.perplexity.ai/help-center/en/articles/10354969-how-does-perplexity-follow-robots-txt)

Perplexity’s current 2026 guidance says it respects robots.txt for crawling/indexing behavior. Restricting full-content crawling does not necessarily erase every possible domain/headline/brief factual reference learned from other sources.

Practical implications:

- decide intentionally whether Perplexity may fetch/index content;
- use provider-documented robots directives;
- do not rely on crawler blocking as privacy/access control;
- monitor citations/referrals separately from bot hits.

## 10. DuckDuckGo AI answers / DuckAssistBot

Official source: [DuckAssistBot](https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot)

DuckDuckGo documents `DuckAssistBot` as a real-time crawler supporting AI-assisted answers with source citations.

Current documented boundaries:

- publishers can opt out through robots.txt;
- opting out of DuckAssistBot does **not** affect ordinary DuckDuckGo organic ranking/inclusion;
- DuckDuckGo says DuckAssistBot data is not used to train AI models.

This is another example of **AI-answer retrieval ≠ normal web ranking ≠ model training**.

## 11. Applebot / Applebot-Extended

Official source: [About Applebot](https://support.apple.com/119829)

Apple documents:

- `Applebot` for search technologies used in experiences such as Spotlight, Siri and Safari-related search;
- Applebot-fetched content may also contribute to contextual/up-to-date information in some AI-generated experiences;
- `Applebot-Extended` is a separate robots control for whether content already crawled by Applebot may be used to train Apple’s general-purpose foundation models;
- Applebot-Extended itself does not crawl pages.

Therefore a publisher can reason separately about Apple search discoverability and Apple model-training preference.

## 12. Provider control matrix

| Provider/system | Search / AI-answer discovery control | Training/model-development control | User-triggered retrieval | Notes |
|---|---|---|---|---|
| Google Search | Googlebot + Search Console Search generative AI control for covered AI features | `Google-Extended` for specified uses | product-specific fetchers may exist | Search AI control is gradual rollout |
| OpenAI / ChatGPT | `OAI-SearchBot` | `GPTBot` | user-triggered retrieval behavior can differ | verify current official bot/IP docs |
| Anthropic / Claude | `Claude-SearchBot` | `ClaudeBot` | `Claude-User` | three distinct bots |
| Perplexity | provider-documented Perplexity crawler rules | provider-specific policy | product behavior differs | verify current help page |
| DuckDuckGo | ordinary search sources/crawlers; `DuckAssistBot` for AI answers | DuckDuckGo says DuckAssistBot is not training use | product-specific | DuckAssist opt-out does not affect organic rankings |
| Apple | `Applebot` | `Applebot-Extended` | Apple product behavior | Extended does not crawl itself |

Never copy a crawler list from a random repository directly into production robots.txt without checking current first-party provider documentation.

## 13. Example robots policy pattern

This is conceptual; verify exact current provider bot names before deployment:

```text
# Search / answer discovery desired
User-agent: OAI-SearchBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: Claude-User
Allow: /

# Separate model-development preferences
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /
```

Google must be configured separately because its 2026 Search generative AI participation control is in Search Console, while Google-Extended handles separate specified AI uses.

## 14. Content characteristics likely to help retrieval/citation — evidence-safe framing

Do not call these hidden “AI ranking factors.” They are durable content-engineering principles:

- precise page/topic scope;
- factual claims supported by primary evidence;
- original data, examples, expert experience or useful synthesis;
- clear entity names, definitions and relationships;
- descriptive headings matching real sections;
- tables/lists where they improve comprehension;
- stable crawlable URLs and HTML;
- visible publication/update/authorship context where useful;
- clear sourcing to authoritative evidence;
- unique images/charts/data where informative;
- consistent organization/contact/about/entity information;
- current information for freshness-sensitive topics.

These improve human and machine interpretability but do not guarantee citation.

## 15. What NOT to overclaim about GEO/AEO

### `llms.txt`

Google Search explicitly says it does not use `llms.txt` as a special Search visibility mechanism. Other services may choose differently; keep conclusions provider-specific.

### “AI schema”

There is no universal special schema required for AI citations. Use Schema.org/search-engine-supported structured data to represent real facts and supported search features.

### Content chunk size

There is no universal optimal paragraph/word/token size. Google explicitly rejects mandatory artificial chunking for generative Search.

### FAQ spam

Turning every article into formulaic Q&A blocks is not automatically better for AI. Structure content for user intent.

### Mention spam

Fake Reddit/forum/listicle mentions are not a durable GEO strategy and may violate platform/search policies.

### Citation count ≠ business value

Track the full funnel:

**presence → citation → linked citation → referral → engagement → lead/revenue**

## 16. Measuring AI visibility

For each external AI provider/prompt set, record:

- provider/model/version when available;
- date/time;
- country/language/account context;
- prompt wording and paraphrases;
- whether web search/retrieval was active;
- brand mention yes/no;
- cited URL/domain;
- citation placement/prominence;
- factual correctness;
- referral traffic/conversion.

Repeat prompts because generated results can vary run-to-run.

### Google-specific measurement

Where Search Console exposes the 2026 Generative AI report, record:

- AI impressions trend;
- canonical pages receiving impressions;
- country/device split;
- control state (Include/Exclude/Inherit);
- change date and propagation window;
- anomalies/logging incidents noted by Google.

Do not infer “AI optimization success” from impressions alone.

### Suggested KPIs

- prompt coverage rate;
- citation share;
- distinct cited pages;
- competitor citation share;
- citation-to-referral rate;
- referral conversion rate;
- factual accuracy of generated brand descriptions;
- crawler access/error rate;
- Google AI feature impressions where first-party reporting is available.

## 17. Research evidence caution

A 2026 critical survey of GEO literature notes that evidence remains heterogeneous and many reported optimization effects are conditional on content already being retrieved/placed in model context. Treat “X% visibility gain” headlines cautiously unless a study demonstrates organic discovery, repeated cross-platform effects and downstream outcomes.

Research reference: [Optimizing Visibility in Generative Engines: A Critical Survey of Generative Engine Optimization (2023–2026)](https://arxiv.org/abs/2607.14035). This is research evidence, not provider documentation.

## 18. AI visibility deployment checklist

- [ ] Search pages are crawlable/indexable/canonical.
- [ ] Google Search generative AI control state is recorded where available.
- [ ] Provider-specific search/retrieval bots are intentionally allowed/blocked.
- [ ] Training preferences are configured separately.
- [ ] WAF/CDN does not accidentally challenge desired bots.
- [ ] Important facts are visible in accessible page content.
- [ ] Claims have trustworthy sources and dates where relevant.
- [ ] Organization/product/entity facts are consistent across owned properties.
- [ ] Pages provide unique value beyond commodity summaries.
- [ ] Search Console AI report is monitored where available.
- [ ] External AI referrals are separately tracked.
- [ ] Prompt/citation monitoring uses repeated tests and stores context.
- [ ] Crawler/control guidance is re-verified periodically.

## 19. Bottom line

The most defensible 2026 strategy is not “replace SEO with GEO.” It is:

**strong search fundamentals + explicit provider-specific participation/crawler policy + differentiated source-quality content + first-party/observable AI visibility measurement.**

This repository only labels a tactic as AI-specific when first-party documentation or repeatable evidence supports that narrower claim.