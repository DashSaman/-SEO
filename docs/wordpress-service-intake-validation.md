# WordPress service journeys: validate routing and intake together

Reviewed/observed: **2026-11-01**. Scope: WordPress shortcode forms, a networking-service journey, isolated previews and bounded production acceptance. This is implementation evidence, not a ranking experiment or a universal conversion claim.

## Official mechanics

**FACT-OFFICIAL — WP-NONCE-20261031:** `wp_nonce_field()` returns markup and echoes it by default. In a callback that builds a string, use its return mode and concatenate it inside the actual form. A nonce is one validation control; its presence does not establish authorization or comprehensive security. [WordPress reference](https://developer.wordpress.org/reference/functions/wp_nonce_field/).

**FACT-OFFICIAL — WP-SHORTCODE-20261031:** Shortcode callbacks should return their output. Directly emitted fragments can appear outside the intended replacement location. [WordPress reference](https://developer.wordpress.org/reference/functions/add_shortcode/).

**FACT-OFFICIAL — WP-CPT-20261031:** A public custom post type normally uses its post-type key as a query variable. Intake/tracking parameters must be checked against the site's registered query variables. [WordPress reference](https://developer.wordpress.org/reference/functions/register_post_type/).

## Scoped observed case

**OBSERVED — OBS-TN-INTAKE-20261031:** TehNet's support/B2B callbacks emitted nonce markup outside their returned forms. Local regression reproduced the boundary; actual preview FormData and HTTP submission later confirmed the repair. A proposed context key, `tn_service`, also selected the existing service CPT: the support page existed and resolved by ID, yet the request with that parameter returned404. The fix used the distinct `tn_service_context` key. This new-link defect was caught before production publication, not presented as a search-ranking loss.

The final isolated run passed24 browser/HTTP checks. Backend verification confirmed two synthetic private tickets, one private B2B request, the approved context, array-context rejection and preserved decimal quantity; invalid nonce made no record. All three owned records were removed and the previous-record fingerprint matched. No real customer, payment, order, ERP or MyTel production operation was performed. [Immutable receipt](https://github.com/DashSaman/TehNet/blob/0fbf6e8216fa5a8dcba85d8551d4040e2dfe1d3b/qa/growth-2026-10-31/native-verification.json).

The accompanying eight-question tool exports a local **manual** report with `measured:false`; selecting answers is not network measurement, a readiness score or certification. Its26 component checks included keyboard, reset/focus, two instances,375px layout, no-JS guidance, download and absence of external requests/storage. Two page drafts and41 block roundtrips were staged; that is not live publication or browser-editor acceptance. Intentional noindex was retained.

## Reusable acceptance checklist

1. **INFERENCE:** Verify the complete service-to-request journey before sending a new content campaign to it; this prevents a plausible operational failure, without claiming an SEO ranking effect.
2. Inspect the rendered form's actual `FormData` and field ownership. A nonce somewhere in the document is insufficient evidence.
3. Check context/query keys against registered CPT/taxonomy/core query variables; navigate the exact CTA URL through native routing. Pure HTML fixtures cannot prove this integration.
4. In independently confirmed isolated staging, test successful submission, malformed/array context, rejected nonce, private persistence and cleanup of owned synthetic records. Block outbound mail/HTTP, real payment and cron before testing.
5. Keep unit, component, native, production and field-performance evidence separate. Verify protected records after cleanup; do not publish raw form tokens or customer data.
6. Preserve intentional noindex and commerce gates. A functional route or truthful schema does not demonstrate indexing, AI citations, traffic or conversion uplift.

## Remaining scope

The original intake receipt above did not prove production release or editor acceptance. Subsequent evidence is separately dated below. New article research, live intake outcomes and search effects remain outside these receipts. Other plugins/sites may register different query variables; the key above is an example to verify locally, not a globally reserved safe name. TehNet operational identifiers, private backups and MyTel metrics are deliberately absent. The central reference baseline remains71%.

## Subsequent migration and release evidence

**OBSERVED — OBS-TN-MIGRATION-20261031:** A narrowly bounded migration passed37 native assertions, including apply/repeat/rollback, exact Persian storage, failed-transaction cleanup, concurrent edits through a second connection and preservation of earlier revisions under a retention cap. A prototype rollback race and revision-pruning issue were reproduced and fixed before production. Thirteen owned fixtures were cleaned and original post/meta rows matched. This does not establish that every WordPress hook is transactional or that a future drifted page can be blindly restored. [Immutable migration receipt](https://github.com/DashSaman/TehNet/blob/2a44f1e62cb5829b66e61d91045c9803342e769a/qa/growth-2026-10-31/migration-verification.json).

**OBSERVED — OBS-TN-REHEARSAL-20261101:** A fresh independent restore initially booted successfully under root CLI, while HTTP omitted the store plugin's forms. Restrictive restored directories belonged to root, preventing traversal by the web user. Ownership was corrected only in the owned clone and the private restore procedure. Eight HTTP paths then passed, followed by content-before-files rollback/repeat, baseline checksums and protected-state equality. Both temporary containers/network were removed; existing runtimes were unchanged. A corrupted bundle was rejected before target writes. This is a failure and repair in the restore method, not evidence that production permissions were faulty. [Immutable rehearsal receipt](https://github.com/DashSaman/TehNet/blob/4c6e93864c337251074341ae0fdef510a8166fba/qa/growth-2026-10-31/release-rehearsal.json).

**OBSERVED — OBS-TN-RELEASE-20261101:** A normal protected PR merge and fresh backup/checksum/drift preceded the six-file release, two editable Services/Lab pages and two hub appendices. Eight public GETs with validated TLS and25 read-only production-browser checks passed, covering1440px/375px/no-JS, local manual JSON/reset and owning-form nonce/context. Intentional noindex,25 inquiry-only products, closed ERP/payment and protected data/runtime remained unchanged; no production form was submitted or MyTel runtime written. Production rollback was not needed; its path was rehearsed in the clone. [Immutable production receipt](https://github.com/DashSaman/TehNet/blob/1caef30f5d3bf9ef62c74b6987d40ad7183e0fe8/qa/growth-2026-10-31/production-release.json).

**INFERENCE:** Recovery acceptance must exercise the actual web-user HTTP path as well as privileged CLI/database checks. **INFERENCE:** Release dependency order matters: new modules before their loader; content rollback before removing the modules it requires. These operational controls reduce an observed failure mode; they establish no ranking, indexing, citation or conversion gain. Abrupt host loss/ambiguous COMMIT was not fault-injected and remains an explicit reconciliation gate. See the [release checklist](../checklists/wordpress-service-release.md).
