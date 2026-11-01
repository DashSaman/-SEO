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

## Commercial service outcomes

Reviewed:2026-11-01. **OBSERVED — OBS-TN-COMMERCIAL-20261101:** An overnight technical acceptance run had not established a commercially useful service catalog or a direct request path. The subsequent change delivered seven browsable service categories at the existing Services owner, retained six nested service URLs and Home's Learn/Lab/Services/Shop identity, and added a short form to both existing pages. General specialist availability was explicitly owner-confirmed; vendor credentials, SLA, rates and deadlines were not inferred from that answer. Specialist PBX/IVR remained a contextual MyTel referral.

The short form reused the existing private ticket entity/action and staff dashboard. In isolated native WordPress, two synthetic requests actually persisted with distinct references; desktop and375px/no-JS receipts showed reference/status, and authorized staff saw the same two records and service context. Native validation, spam/rate and unauthorized-reply checks passed; original posts/meta/users/files/runtimes were restored. The public release then changed three files and two existing bodies, with fresh backup/checksum/drift and qualified payload/tool/guard equivalence. Public GET/browser verification confirmed the visible catalog/form/CTA results without submitting a live request. [Immutable production receipt and limits](https://github.com/DashSaman/TehNet/blob/17088b26ebaa2071bc66dc25cbcba0250755de80/qa/commercial-2026-11-01/production-verification.json).

**FACT-OFFICIAL — WP-TRANSIENTS-20261101:** WordPress transients have a maximum expiry and can disappear earlier; an expiring receipt must explain that boundary and fail without exposing a private conversation. [WordPress Transients API](https://developer.wordpress.org/apis/transients/). The observed implementation used an opaque token, no contact/thread disclosure, no-cache and no-referrer. Token entropy, authorization, access logging and cache behavior still require scoped review on another implementation; presence of a nonce is not authorization.

**FACT-OFFICIAL — GGL-CONTENT-003 / GGL-LINKS-20261101:** Google's people-first questions support original useful synthesis and clear sourcing; crawlable links use actual href destinations with relevant descriptive text. [Helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content), [link guidance](https://developers.google.com/search/docs/crawling-indexing/links-crawlable). **INFERENCE:** For a service business, a useful catalog should help visitors choose scope, understand deliverables and reach the appropriate existing workflow. A keyword-link wall, a large topic list or passing CI does not establish that customer outcome.

Reusable acceptance should separate:

- **Visible delivery:** before/after evidence at exact public owners, mobile/no-JS navigation, appropriate scope and direct CTA.
- **Canonical request:** actual private persistence, actual reference/status and authorized staff traceability in isolated staging; reuse existing entities rather than adding a parallel CRM.
- **Operational qualification:** precise backups, immutable payload, drift protection, restoration and public smoke. Earlier failed attempts remain disclosed; a QA staff dashboard auto-draft needed explicit owned-fixture cleanup rather than broad deletion.
- **Business/search evidence:** actual consented projects, response SLA, leads, indexing and search outcomes are independent. Synthetic request IDs and browser counts are not conversion or competitive-parity measurements.

The site's intentional noindex and closed physical-commerce gates remained; no production QA submission, payment or MyTel runtime write was performed. Issue63 stayed open for commercial depth, trust, researched content and measurement. This lesson updates acceptance criteria without changing the central71% research baseline or closing credential/history/Origin gates.

## Remaining scope

The original intake receipt above did not prove production release or editor acceptance. Subsequent evidence is separately dated below. New article research, live intake outcomes and search effects remain outside these receipts. Other plugins/sites may register different query variables; the key above is an example to verify locally, not a globally reserved safe name. TehNet operational identifiers, private backups and MyTel metrics are deliberately absent. The central reference baseline remains71%.

## Subsequent migration and release evidence

**OBSERVED — OBS-TN-MIGRATION-20261031:** A narrowly bounded migration passed37 native assertions, including apply/repeat/rollback, exact Persian storage, failed-transaction cleanup, concurrent edits through a second connection and preservation of earlier revisions under a retention cap. A prototype rollback race and revision-pruning issue were reproduced and fixed before production. Thirteen owned fixtures were cleaned and original post/meta rows matched. This does not establish that every WordPress hook is transactional or that a future drifted page can be blindly restored. [Immutable migration receipt](https://github.com/DashSaman/TehNet/blob/2a44f1e62cb5829b66e61d91045c9803342e769a/qa/growth-2026-10-31/migration-verification.json).

**OBSERVED — OBS-TN-REHEARSAL-20261101:** A fresh independent restore initially booted successfully under root CLI, while HTTP omitted the store plugin's forms. Restrictive restored directories belonged to root, preventing traversal by the web user. Ownership was corrected only in the owned clone and the private restore procedure. Eight HTTP paths then passed, followed by content-before-files rollback/repeat, baseline checksums and protected-state equality. Both temporary containers/network were removed; existing runtimes were unchanged. A corrupted bundle was rejected before target writes. This is a failure and repair in the restore method, not evidence that production permissions were faulty. [Immutable rehearsal receipt](https://github.com/DashSaman/TehNet/blob/4c6e93864c337251074341ae0fdef510a8166fba/qa/growth-2026-10-31/release-rehearsal.json).

**OBSERVED — OBS-TN-RELEASE-20261101:** A normal protected PR merge and fresh backup/checksum/drift preceded the six-file release, two editable Services/Lab pages and two hub appendices. Eight public GETs with validated TLS and25 read-only production-browser checks passed, covering1440px/375px/no-JS, local manual JSON/reset and owning-form nonce/context. Intentional noindex,25 inquiry-only products, closed ERP/payment and protected data/runtime remained unchanged; no production form was submitted or MyTel runtime written. Production rollback was not needed; its path was rehearsed in the clone. [Immutable production receipt](https://github.com/DashSaman/TehNet/blob/1caef30f5d3bf9ef62c74b6987d40ad7183e0fe8/qa/growth-2026-10-31/production-release.json).

**INFERENCE:** Recovery acceptance must exercise the actual web-user HTTP path as well as privileged CLI/database checks. **INFERENCE:** Release dependency order matters: new modules before their loader; content rollback before removing the modules it requires. These operational controls reduce an observed failure mode; they establish no ranking, indexing, citation or conversion gain. Abrupt host loss/ambiguous COMMIT was not fault-injected and remains an explicit reconciliation gate. See the [release checklist](../checklists/wordpress-service-release.md).

## Corporate navigation and honest CAPTCHA acceptance

Reviewed:2026-11-01. Workstream:`tehnet-corporate-navigation-captcha-20261101`. This is a scoped implementation lesson; baseline71% and18 dashboard destinations do not change.

**OBSERVED — OBS-TN-CORPORATE-20261101:** A production screenshot and browser geometry reproduced a24px offset between the first workflow card and its siblings, caused by inherited WordPress flow margins. An explicit scoped grid-child margin fixed the offset to under1px in isolated native staging. Locally served licensed Estedad loaded successfully; navigation increased from12px to at least15px. Seven top-level destinations and actual editable WordPress children replaced the flat10-item menu. Desktop/mobile, keyboard disclosure/Escape, no-JS links and saved dark preference were exercised. Two synthetic private requests still reached the existing ticket store and staff interface; all fixture data/files/runtime were restored. [Immutable staging evidence and screenshots](https://github.com/DashSaman/TehNet/blob/a56d2916b89194c6b6cd7fc6df98a3755d219357/qa/corporate-ui-2026-11-01/staging-verification.json).

**OBSERVED:** `wp_get_nav_menu_items` returned normalized display orders, while the actual stored home-item order was0. The bounded migration's guard must compare the database representation, not assume the displayed ordinal is the stored value. Routine navigation remains editable; a hidden permanent theme filter must not undo future admin edits. This is an implementation-specific finding, not an engine ranking rule.

**FACT-OFFICIAL — GGL-CAPTCHA-DISPLAY-20261101 / GGL-CAPTCHA-VERIFY-20261101:** Google v2 supports explicit widget rendering; its server-side token is short-lived and single-use. Keep renderer and server verification in the existing intake path, enforce exact hostname and provider success, handle expiry/network failure clearly, keep secrets outside Git and do not forward optional customer information unnecessarily. [Display](https://developers.google.com/recaptcha/docs/display), [verify](https://developers.google.com/recaptcha/docs/verify). A provider-response fixture validates local integration logic, not Google's actual service availability or a human challenge.

**OBSERVED:** Key creation was actually attempted but blocked by Google project quota and account country/region restrictions. No key, billing or quota request was created. The adapter is prepared but remains DISABLED; existing nonce/honeypot/throttle controls persist. Do not label an unconfigured integration as active protection. [Operations and limits](https://github.com/DashSaman/TehNet/blob/a56d2916b89194c6b6cd7fc6df98a3755d219357/docs/recaptcha-operations.fa.md).

**OBSERVED:** The first qualified production attempt fully rolled back because its wrapper incorrectly required noindex on an existing standalone utility with a different measured robots baseline. Preserve actual per-route controls and correct the acceptance assumption; do not alter indexing merely to make a test green. [Rollback receipt](https://github.com/DashSaman/TehNet/blob/3bee3913b6aa8623b856b98773e380ab0b55cd85/qa/corporate-ui-2026-11-01/first-release-rollback.json). A subsequent release requires a fresh source/journal, identical native-qualified payload and fresh backup/drift guard. This paragraph does not assert a later deployment.

**INFERENCE:** User-visible geometry, readable navigation and a canonical functioning request journey are useful acceptance criteria. CI counts, font choice, screenshots and CAPTCHA integration alone prove no ranking, indexing, AI-citation, conversion or competitor-parity improvement. MyTel remains independent and intentional noindex/payment/security gates stay explicit.
