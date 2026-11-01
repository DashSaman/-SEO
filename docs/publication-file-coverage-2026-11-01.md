# Publication guard: complete tracked-file coverage

VERIFIED_LOCALLY; CI/integration recorded in the PR. Repository tooling only; MyTel production remains read-only and no URL/title/H1/performance change is authorized.

A fresh private TehNet history checkout had1513 tracked files. Ordinary Windows path lookup saw1276; an extended path saw1513. The old guard silently skipped missing paths. The independent Git-object known-value/path scan remained a separate full reachable-object check; the1276-file filesystem PASS is retained as incomplete coverage.

The identical guard update in all three repositories uses extended Windows paths for file reads, enables long-path handling only on its Git enumeration command, reports enumerated and successfully read counts, and fails with sanitized relative path/category when a tracked file cannot be read. OS exception text and file contents are not diagnostic output. Content rules and narrow contact exceptions are unchanged.

Actual regressions before the fix:12 tests,9 passed,2 failed and1 error (missing file, actual Windows deep path and unreadable file). After the fix:12 Windows tests passed. An unchanged deep checkout was rescanned without modifying its files:1513/1513 read, no findings in the scoped guard. Linux CI intentionally skips the Windows-only integration case; its result must not be described as12 Linux passes.

The separate local history preparation initially omitted unittest stderr despite exit0; complete capture was rerun without overwriting the snapshot/filter. A subsequent Git diff check also needed per-command long-path support; the original checkout remained unchanged. These preparation errors are not hidden as application failures or remote cleanup.

Shared history rewriting, retained PR/cache/fork removal and support submission remain NEEDS_APPROVAL. Historical credential validity/rotation stays UNKNOWN/NOT_ROTATED; Origin remains UNDETERMINED. No remote refs, accounts, production infrastructure or customer data were changed by this correction.
