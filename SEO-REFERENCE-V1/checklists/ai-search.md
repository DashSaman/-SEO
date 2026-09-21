# AI Search / GEO / AEO Checklist

## Provider controls
- [ ] Google Search crawl/index state clean.
- [ ] Google generative AI Search control intentionally set where available.
- [ ] Google-Extended training/grounding preference reviewed separately.
- [ ] `OAI-SearchBot` allowed/blocked intentionally.
- [ ] `GPTBot` training preference set independently.
- [ ] `Claude-SearchBot`, `Claude-User`, `ClaudeBot` reviewed separately.
- [ ] Perplexity crawler preference reviewed.
- [ ] Bing/Copilot discovery and IndexNow/sitemap setup reviewed.
- [ ] DuckAssistBot/Applebot/Applebot-Extended considered if relevant.
- [ ] WAF/CDN logs confirm intended bots are not accidentally denied.

## Content/evidence
- [ ] Important brand/product facts are explicit and current.
- [ ] Entity names/relationships are unambiguous.
- [ ] Original claims include sources/methodology.
- [ ] Authors/dates/limitations shown where relevant.
- [ ] Semantic headings/tables/lists improve user comprehension naturally.
- [ ] No artificial “LLM chunk size” rule used as ranking folklore.
- [ ] No AI-only schema/`llms.txt` presented as Google requirement.
- [ ] No fake Reddit/review/third-party mentions.

## Measurement
- [ ] ChatGPT referral traffic tracked (`utm_source=chatgpt.com` where present).
- [ ] Bing AI Performance citations/cited pages/grounding queries monitored where available.
- [ ] Google generative AI performance report monitored where available.
- [ ] Controlled prompt/query set defined per business topic.
- [ ] Multiple repeated runs used for stochastic systems.
- [ ] Citation, prominence, referral traffic and conversion measured separately.
- [ ] Provider/model/date/language recorded.
- [ ] Changes annotated; no one-run causal claims.

## PASS criteria

PASS when intended search/retrieval crawlers can access the intended public content, search vs training controls are explicitly separated, evidence/entity facts are accurate, measurement is provider-specific/repeated and no unsupported GEO myth is treated as a ranking factor.

## Common failures

- blocking a training bot and assuming search visibility is also blocked, or vice versa;
- WAF/CDN silently blocks intended search/retrieval bots despite permissive robots rules;
- `llms.txt`, FAQ spam or “AI schema” is presented as a Google requirement;
- one citation is reported as a ranking/authority/traffic win;
- fake Reddit/review/forum mentions are manufactured for supposed LLM signals;
- provider/model/date/language is omitted from citation tests;
- stochastic one-run prompt results are treated as deterministic;
- Bing citation metrics and ordinary search rank/clicks are merged into one KPI.

## Retest

1. Re-fetch provider-specific robots rules and first-party bot documentation before testing.
2. Check server/WAF logs for intended bot access and distinguish crawler identity/purpose.
3. Re-run a fixed prompt/query set multiple times with provider/model/date/language recorded.
4. Re-check Google/Bing AI reporting and ordinary Search Performance separately where available.
5. Verify referral analytics and conversions independently from citation counts.
6. Compare before/after observations without claiming causality unless the design supports it; mark `PASS`/`FAIL`/`MONITOR` with evidence.
