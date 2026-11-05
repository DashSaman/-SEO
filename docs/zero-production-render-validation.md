# Zero-Production Render Validation — inject-in-own-session method (2026-11-05)

**Evidence class:** OBSERVED on one property; method is engine-agnostic (any Chromium-driven session).

**Technique:** to pre-validate content-insertion drafts against live pages without production changes, load the live page in your own browser session, inject the draft HTML fragment client-side (DOM only) into the content container, then run programmatic checks — duplicate-text detection against existing innerText (distinctive phrase probes), H1 count stability, computed direction/style of injected nodes (e.g., a component class that exists only in other templates will render unstyled: backgroundColor === transparent), link targets collection, mobile-viewport visibility and horizontal-overflow check, plus screenshots of the injected region. Navigate away/reload discards everything; the server never sees the change.

**Caveats:** injection point in a test (parent of H1 vs final editorial position) can differ from the production insertion slot; component classes scoped to other templates render unstyled — prefer inline styles in draft fragments; DOM injection proves rendering compatibility, NOT editor/Elementor storage compatibility.

**Confidence:** method-level PASS criteria transferable; page-level results are property-specific.
