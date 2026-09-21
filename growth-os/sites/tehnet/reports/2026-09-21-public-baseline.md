# Tehran Network — Public Baseline — 2026-09-21

Source: live Growth OS public baseline collector on `Amirreza-Pc`.

## Observed
- Requested URL: `https://tehnet.ir`
- HTTP status: `200`
- Final URL: `https://tehnet.ir`
- Root response sample latency: `928 ms`
- Title: `تهران نتورک | TehNet – آموزش، خدمات و تجهیزات شبکه`
- Meta description: **not detected on homepage**
- Canonical: `https://tehnet.ir/`
- `robots.txt`: HTTP `200`
- `/sitemap.xml`: HTTP `404`
- `/sitemap_index.xml`: HTTP `404`

## Evidence-backed opportunities
1. Homepage meta description is missing in the fetched HTML. Prepare an intent-aligned description in the later execution phase; verify rendered/live HTML after any change.
2. Both standard sitemap candidate paths returned 404. Do not assume no sitemap exists yet; next crawl must inspect `robots.txt`, site links and CMS configuration for any non-standard sitemap location before proposing a fix.

## Ruling
The public homepage is reachable, but the baseline shows two technical/content checks requiring investigation. No production change is made in Phase 4 public-baseline collection.

Raw runtime evidence is stored host-side under `/opt/growth-os/state/sites/tehnet/baselines/20260921T044024Z.json` and is not a credential file.
