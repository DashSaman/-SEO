# AI Search / GEO / AEO Reference (2026)

**Reviewed:** 2026-08-26  
**Evidence policy:** provider-specific behavior must come from current first-party documentation wherever possible.

## 1. First principle: AI visibility is not one system

“AI SEO”, “GEO”, “AEO” and “LLMO” are umbrella labels. Different products may involve different stages:

**crawler access → web/index discovery → retrieval → reranking/context selection → generation → citation/link selection → user click/conversion**

A tactic that affects one stage does not prove an effect on another.

For example:

- allowing a crawler can make retrieval possible but does not guarantee citation;
- being cited does not guarantee traffic;
- a content rewrite that increases citation in a fixed experimental context does not prove improved organic discoverability;
- a training opt-out bot is not necessarily the bot used for search retrieval.

## 2. Evidence hierarchy for AI search

1. first-party crawler/search documentation;
2. repeated measured observations with date/query/model/location context;
3. peer-reviewed/preprint research with clearly stated experimental assumptions;
4. practitioner case studies;
5. community crawler lists/tool marketing.

Do not turn a vendor marketing claim into a universal AI ranking factor.

## 3. Google AI Overviews / AI Mode

Source: [Google’s 2026 generative-AI Search guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)

Google states that its generative Search features are rooted in core Search ranking/quality systems and retrieve from the Search index. Google explicitly says conventional SEO remains foundational.

Google says you do **not** need, for Google Search:

- `llms.txt`;
- special AI markup/schema;
- artificial content chunking;
- AI-specific writing style;
- pages for every fan-out query variant;
- inauthentic mention generation.

Focus instead on accessible/indexable pages and differentiated, helpful, trustworthy content with useful media/local/product information where relevant.

## 4. Google-Extended

Official source: [Google common crawlers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers)

`Google-Extended`:

- is a robots.txt **product token**;
- does not have a separate HTTP User-Agent string;
- controls specified uses of Google-crawled content for future Gemini model training and grounding in Gemini/Vertex contexts;
- does **not** affect inclusion in Google Search;
- is **not** a Google Search ranking signal.

This is separate from Googlebot access needed for Google Search crawling.

## 5. OpenAI / ChatGPT Search

Official sources:

- [Publishers and Developers FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq)
- [Guidance for allowing OpenAI web crawlers](https://help.openai.com/en/articles/20001243-advertiser-guidance-for-allowing-openai-web-crawlers)

### Bot/control separation

| OpenAI control | Primary documented role | Visibility implication |
|---|---|---|
| `OAI-SearchBot` | search crawling/discovery for ChatGPT search | blocking can prevent content from being crawled for search summaries/snippets |
| `GPTBot` | model-training related crawling | training preference; do not treat as the same as SearchBot |
| user-triggered retrieval agents where documented | fetch content in response to user action | behavior can differ from scheduled search crawling |

OpenAI notes that a public URL known through other sources may still appear in limited form even if page crawling is restricted; if a page should not be indexed/public, use appropriate access/index controls rather than assuming bot blocking is privacy.

OpenAI also documents referral attribution using `utm_source=chatgpt.com` for ChatGPT search referrals.

### Operational checklist

- allow `OAI-SearchBot` if ChatGPT Search discoverability is desired;
- ensure robots rules are not unintentionally overridden by WAF/CDN bot protection;
- verify official bot/IP mechanisms rather than trusting User-Agent alone;
- keep important content server-accessible and not locked behind unnecessary interaction;
- measure ChatGPT referrals separately from citation/mention monitoring.

## 6. Anthropic / Claude

Official source: [Anthropic crawler guidance — April 7, 2026](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)

Anthropic documents three separate robots:

| Bot | Documented use | If blocked |
|---|---|---|
| `ClaudeBot` | content that may contribute to model development/training | signals future materials should be excluded from training datasets |
| `Claude-User` | user-directed retrieval when Claude users ask questions | can reduce ability to retrieve site content for user requests |
| `Claude-SearchBot` | web navigation/indexing to improve search-result quality | can reduce site visibility/accuracy in Claude search results |

Anthropic states these bots honor robots.txt. It also documents support for a non-standard `Crawl-delay` extension. Anthropic warns that simply IP-blocking bots may interfere with reading robots.txt and may not be a persistent opt-out mechanism.

### Key lesson

Do not advise “block ClaudeBot to disappear from Claude Search” or “allow ClaudeBot to rank in Claude Search” without distinguishing the three robots.

## 7. Perplexity

Official source: [Perplexity robots.txt guidance](https://www.perplexity.ai/help-center/en/articles/10354969-how-does-perplexity-follow-robots-txt)

Perplexity’s current 2026 guidance says it respects robots.txt for crawling/indexing behavior. It explains that restricting full-content crawling does not necessarily erase every possible domain/headline/brief factual reference that can be learned from elsewhere.

Practical implications:

- decide whether you want Perplexity to fetch/index content;
- manage crawler policy through provider-documented robots directives;
- do not rely on crawler blocking as a privacy/access-control layer;
- monitor citations/referrals separately from bot hits.

## 8. Crawler-policy matrix

A publisher should document its policy intentionally rather than using one blanket `Disallow: /` for all AI-related identifiers.

| Provider/system | Search/discovery control | Training/model-development control | User-triggered retrieval | First-party verification required? |
|---|---|---|---|---|
| Google Search / AI Overviews | Googlebot/Search controls | Google-Extended affects specified Gemini uses | Google has separate fetchers for some products | YES |
| OpenAI / ChatGPT Search | `OAI-SearchBot` | `GPTBot` | separate user-triggered behavior may apply | YES |
| Anthropic / Claude | `Claude-SearchBot` | `ClaudeBot` | `Claude-User` | YES |
| Perplexity | provider-documented Perplexity crawler controls | provider says it does not build foundation models in the same way; re-check current docs | product behavior documented separately | YES |

Never copy a crawler list from a random repository directly into production robots.txt without checking the provider’s official current documentation.

## 9. Example policy patterns

### Allow AI search discovery but opt out of some training crawlers

This is conceptual; verify exact current bot names before deployment:

```text
# Search visibility
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

Google’s controls require separate consideration because Google-Extended is a product token and Googlebot remains the Search crawler.

## 10. Content characteristics likely to help retrieval/citation — evidence-safe framing

Do not call the following hidden “AI ranking factors.” They are robust content engineering principles that improve usability, retrieval clarity and source trust:

- precise page/topic scope;
- factual claims supported by primary evidence;
- original data, examples, expert experience or useful synthesis;
- clear entity names, definitions and relationships;
- descriptive headings that reflect actual sections;
- tables/lists where they genuinely make comparison easier;
- stable URLs and crawlable HTML;
- visible publication/update/authorship context when useful;
- clear sourcing and outbound citations to authoritative evidence;
- unique images/charts/data where they add information;
- consistent organization/contact/about/entity information;
- current information for freshness-sensitive topics.

These can make content easier for humans and retrieval systems to evaluate, but no item guarantees AI citation.

## 11. What NOT to overclaim about GEO/AEO

### `llms.txt`

Google Search explicitly says it does not use `llms.txt` as a special visibility mechanism. Other systems may experiment with it, but repository guidance must remain provider-specific.

### “AI schema”

There is no universal special schema required for AI citations. Continue using appropriate Schema.org/search-engine supported structured data for explicit facts/search features.

### Content chunk size

There is no universal optimal paragraph/word/token size. Google specifically rejects mandatory artificial chunking for generative Search.

### FAQ spam

Turning every article into dozens of formulaic Q&A blocks is not automatically better for AI. Content structure should serve intent; Google also changes rich-result eligibility over time.

### Mention spam

Fake Reddit/forum/listicle mentions are not a durable GEO strategy and can violate platform/search spam policies.

### Citation count ≠ business value

Track the full funnel:

**presence → citation → linked citation → referral → engagement → lead/revenue**

## 12. Measuring AI visibility

For each prompt set/model, record:

- provider/model/version when available;
- date/time;
- country/language/account context;
- prompt wording and paraphrases;
- whether web search was activated;
- brand mention yes/no;
- cited URL/domain;
- citation placement/prominence;
- response correctness/fidelity;
- referral traffic/conversion where measurable.

Repeat prompts. Generative results can vary run-to-run.

### Suggested KPIs

- prompt coverage rate;
- citation share / share of cited answers;
- distinct cited pages;
- competitor citation share;
- citation-to-referral rate;
- referral conversion rate;
- factual accuracy of generated brand descriptions;
- crawler access/error rate.

## 13. Research evidence caution

A current 2026 critical survey of GEO literature notes that evidence remains heterogeneous and that many reported optimization effects are conditional on content already being retrieved/placed in model context. Treat experimental “X% visibility gain” headlines cautiously unless the study proves organic discovery, repeated cross-platform effects and downstream outcomes.

Research reference discovered during this pass: [Optimizing Visibility in Generative Engines: A Critical Survey of Generative Engine Optimization (2023–2026)](https://arxiv.org/abs/2607.14035). This is research evidence, not provider documentation, and should be reviewed in full before extracting quantitative claims.

## 14. AI visibility deployment checklist

- [ ] Search engine pages are crawlable/indexable/canonical.
- [ ] Provider-specific search bots are intentionally allowed/blocked.
- [ ] Training preferences are set separately from search preferences.
- [ ] WAF/CDN does not accidentally challenge desired bots.
- [ ] Important facts are visible in accessible page content.
- [ ] Claims have trustworthy sources and dates where relevant.
- [ ] Organization/product/entity facts are consistent across owned properties.
- [ ] Pages provide unique value beyond commodity summaries.
- [ ] AI referrals are separately tracked.
- [ ] Prompt/citation monitoring uses repeated tests and stores dates/model context.
- [ ] Robots/crawler guidance is re-verified periodically because bot behavior changes quickly.

## 15. Bottom line

The most defensible 2026 strategy is not “replace SEO with GEO.” It is:

**strong search fundamentals + provider-specific crawler policy + differentiated source-quality content + measurable AI retrieval/citation monitoring.**

This repository will only label a tactic an AI-specific optimization when there is provider documentation or repeatable evidence supporting that narrower claim.