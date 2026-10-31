# Bounded WordPress service release

Reviewed:2026-11-01. Classification: observed implementation evidence and scoped inferences; not search-engine requirements. Sources and limits: [service-intake synthesis](../docs/wordpress-service-intake-validation.md), OBS-TN-MIGRATION-20261031, OBS-TN-REHEARSAL-20261101 and OBS-TN-RELEASE-20261101.

- [ ] Identify the already authorized files, pages, parent paths and preserved data/options. Keep credentials/raw journals outside Git and the web root.
- [ ] Build immutable source blobs and old/new digests; reject a corrupted member, unsafe path, unknown runtime or foreign edit before target writes.
- [ ] Make and checksum a fresh backup. Independently restore WordPress/SQL into owned isolated resources with mail, external HTTP, cron and real payment blocked.
- [ ] Test restored HTTP as the actual web user. Privileged CLI success alone can conceal file/directory ownership problems.
- [ ] Validate native page/editor, exact CTA routing, nonce field ownership, no-JS and desktop/mobile behavior. Synthetic POST tests belong only in independently confirmed isolated staging, followed by owned-record cleanup and comparison of original data.
- [ ] Recheck live drift immediately before applying. Install required modules before the loader; use serial atomic file replacement and retain verified previous bytes/modes/ownership.
- [ ] Apply content under guarded transactions/journals with revision retention, native locking/revalidation and no adoption of foreign paths. Verify repeat operations create no duplicate work.
- [ ] Verify public status, canonical, H1, intentional robots policy, form ownership/context and actual loaded JS/download/reset. Production smoke must avoid customer/payment/form transactions.
- [ ] Rehearse content rollback before file rollback; restore the old loader before removing new modules. Preserve foreign changes and stop on drift or ambiguous commit, retaining private evidence for reconciliation.
- [ ] Remove only owned temporary resources by verified IDs/labels; verify original runtimes and protected state. Retain backup/release records privately.
- [ ] Record local/native/staging/live outcomes separately, with source commit, date, exact test scope, failures and untested fault modes. Deployment alone is not acceptance; acceptance alone is not an SEO result.

This checklist is a reusable gate, not a claim that another site's hooks, storage engines, cache or network recovery have been tested. A later authorized change needs fresh checks; a historical PASS does not authorize replay. Index-launch, credentials, shared history/network and payment gates remain separate.
