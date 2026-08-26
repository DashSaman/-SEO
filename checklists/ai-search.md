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

## PASS
PASS when intended crawlers can retrieve content, training/search controls are separated, first-party evidence/entity clarity are strong, measurements are provider-specific and no unsupported GEO myth is treated as a ranking factor.
