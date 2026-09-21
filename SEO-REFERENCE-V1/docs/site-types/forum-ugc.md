# Forum / UGC SEO Playbook

## Goal

Preserve useful community knowledge while preventing spam, thin profile/tag/search pages and infinite crawl spaces from overwhelming the index.

## Indexability classes

Potentially indexable:
- substantive question/thread pages with unique user value;
- high-quality topic/category hubs;
- curated knowledge summaries.

Usually non-indexable/low priority:
- empty/one-line threads;
- login/account/action URLs;
- internal search results;
- duplicate sort/filter views;
- thin user profiles;
- moderation/admin endpoints;
- pagination beyond useful discovery patterns when no unique value.

## Thread quality

Useful threads have:
- clear question/topic title;
- enough context to understand problem;
- substantive answers;
- timestamps;
- accepted/best answer signals if genuine;
- moderation against spam/abuse;
- stable canonical URL.

## Links

UGC links should use appropriate platform policies and often `rel="ugc"`/`nofollow` where suitable. Do not let forums become automated link-building infrastructure.

## Spam controls

Use:
- rate limits;
- trust/reputation systems;
- moderation queues;
- duplicate detection;
- abuse reporting;
- bot/account defenses;
- URL/link thresholds;
- malware/phishing scanning.

Remove hacked/spam pages quickly and return correct status when gone.

## Architecture

Create meaningful topic hubs and breadcrumbs. Avoid tag clouds generating thousands of overlapping archives. Keep thread URLs stable even when titles are edited; redirect old slugs if architecture changes.

## Structured data

Use forum/Q&A structured data only when the page genuinely matches supported content and visible data. Current Google supported-property requirements win over generic Schema.org vocabulary.

## AI/search value

Authentic UGC can contain first-hand experience and niche answers, but do not manipulate the community to manufacture AI citations. Measure which topics earn search/AI referrals and improve moderation/knowledge extraction around real demand.

## KPI stack

- indexable substantive-thread count;
- indexed/submitted ratio by thread quality class;
- spam/abuse rate;
- organic visits per quality cohort;
- solved-question rate;
- repeat/community engagement;
- bot crawl spent on actions/search/tags;
- referral/conversion value.

## PASS gate

PASS when useful threads are crawlable, action/search/spam spaces are controlled, links are policy-safe, moderation is strong and page-count growth follows community value rather than SEO generation targets.
