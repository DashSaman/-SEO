# Public repositories and operational evidence

Reviewed: 2026-10-31. Evidence classes: FACT-OFFICIAL (GitHub), OBSERVED (repository cleanup), INFERENCE (recommended workflow). No ranking or growth causality claim.

An SEO/code handoff must remain useful without publishing origin addresses, credentials, raw SQL, form dumps, private console exports or identifying logs. Keep private originals outside public Git; publish narrowly sanitized findings with date, method, scope and limits. Redacted receipts have different bytes from originals: retain private originals/hashes and label replacements. A public source URL or third-party security CIDR is distinct from a private operational target.

Deleting a tracked file removes it from a tree; earlier commits, branches, pull-request references, forks and clones can retain it. GitHub's official removal workflow calls for coordination and explains these limits. Rotate/revoke exposed credentials first if real credential exposure is confirmed. Treat changing visibility and rewriting shared history as separate controlled actions. [GitHub source](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).

Observed case: an operational repository contained origin addresses and workstation-specific module paths; another tracked raw backup/console files. Current-tree cleanup, private preservation, standard module resolution and a diagnostics-redacted publication guard were implemented on review branches. This observation is not a comprehensive security audit, an all-history purge or evidence of search growth. No private site metrics/customer identifiers are reproduced here.

Guard exceptions should name a narrow category, reason and content digest, with only CRLF/LF normalization where needed. Intentional public TLS fixtures and URL-rejection test inputs require explicit distinction from real credentials. A dedicated scanner can flag public signature fingerprints and source variable names: classify originals before alleging compromised keys. Do not hide unclassified scanner findings through broad exclusions.

Manual diff review in this case found a plaintext staged-account password in prose after the initial scanner/guard checks. It was removed and a failing regression against the previous guard was captured before the new rule passed. This is a confirmed example of a scanner miss, not evidence that later scans find everything. No credential value or private forwarding address is reproduced here. Removal from files and revocation of an account password are independent operations.

## Publication gate

1. Inspect tracked paths and all fetched history; do not print discovered values.
2. Preserve private originals outside the repository and avoid leaking the private archive path.
3. Remove raw private evidence; redact current prose and parameterize workstation settings.
4. Validate JSON/source/test behavior and negative guard cases.
5. Recheck remote refs, coordinate old clones and rehearse a history purge in a separate backed-up clone.
6. After approval, verify remote branches/tags plus PR/cache/fork limitations; never equate a clean HEAD with complete removal.

## Mandatory publication checks —2026-10-31

**OBSERVED:** Actual API review found native secret scanning/push protection enabled on the two public repositories, while main had no protection and the accessible ruleset list was empty. A passing workflow alone was therefore not mandatory publication enforcement. The private repository's protection API returned403 and security fields were absent: its state remains UNKNOWN, not “disabled”; no subscription, visibility or policy change was attempted there.

After verifying the successful `tracked-file-privacy` job and its actual GitHub Actions app, main protection was configured on the two public repositories. Readback200 confirmed: pull request required, that app-bound check required, branch up-to-date required, administrator enforcement on, force-push/deletion off. Required approving-review count is0 to avoid claiming independent review or locking a sole-owner workflow. Main commit IDs remained unchanged. Prior settings and a drift-guarded rollback procedure are private.

The first PUT returned422 because both `contexts` and `checks` were supplied to a mutually exclusive schema. Full error was reviewed; fresh preflight confirmed no policy change, and the corrected checks-only request/readback succeeded. This was validation failure, not an authorization or automatic-approval rejection; no access control was bypassed.

**FACT-OFFICIAL:** GitHub provides separate settings for required checks, their app, administrator enforcement and pull-request reviews. Use the actual observed check identity and reconcile existing policies before replacing them. [Official branch-protection API](https://docs.github.com/en/rest/branches/branch-protection#update-branch-protection), reviewed2026-10-31.

**LIMIT:** This makes the bounded guard mandatory in the configured workflow. It does not prove no leak, prevent an owner from later changing policy, purge retained history, rotate credentials or validate Origin protection. Known-value/manual/media audits remain separate. This configuration step changed no production infrastructure and rewrote no shared Git history.
