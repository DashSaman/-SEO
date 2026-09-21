# Phase 3 — Local AI Layer Implementation Plan

## Goal
Build a zero-paid-generative-API AI layer on `Amirreza-Pc` that can serve text/reasoning jobs for Growth OS while protecting the RTX 3070 8GB from VRAM overcommit. This phase does not modify production sites.

## Operating requirements carried forward
- 24/7 monitoring is a product requirement; the AI worker must recover cleanly after WSL/Windows restart.
- Every site will later receive one isolated daily report every 24 hours showing what the system observed, what it changed, what failed, what improved and what is planned next.
- Every site will later run a measured optimization cycle every 7 days with before/after evidence, impact analysis and keep/adjust/rollback decisions.
- Reports must be written both to the relevant site repository and that site's Telegram reporting destination.
- Routine owner workflow is review-only; no manual content/video editing or uploading should be required in normal operation.
- Paid generative APIs remain disabled. Local models are primary; official free platform APIs may later be used only for analytics/publishing where appropriate.
- The business objective is to maximize qualified visibility, leads, conversions and revenue with evidence-based white-hat SEO/marketing. First-page rankings are a target, not a guarantee.

## Architecture
```text
Activepieces / Agents
        ↓
LiteLLM local gateway :4000
        ↓
Ollama local inference :11434
        ↓
RTX 3070 8GB
        ↓
Primary model + Fast fallback model
```

## Resource policy
Because the host has one 8GB GPU, run one loaded model and one inference stream at a time by default. Queue excess work instead of competing for VRAM. Video/image GPU jobs added later must share the same serialized GPU-job policy.

Set the local inference defaults conservatively:
- `OLLAMA_MAX_LOADED_MODELS=1`
- `OLLAMA_NUM_PARALLEL=1`
- bounded `OLLAMA_MAX_QUEUE`
- `OLLAMA_CONTEXT_LENGTH=8192` initially
- short keep-alive so VRAM can be released for future image/video jobs
- Ollama cloud inference disabled

## Tasks

### P3-AI-01 — Read-only preflight
Verify GPU visibility, free disk/RAM, ports 11434/4000, existing Ollama/LiteLLM state, and Phase 2 health.

### P3-AI-02 — Install Ollama natively in WSL
Use the current official Linux installer. Keep it under systemd so it recovers after WSL start. Configure the resource policy above and keep the API local/private; never expose it directly to the public Internet.

Verification:
- service active
- API version responds
- resource policy visible in the service environment
- GPU detected during inference

### P3-AI-03 — Pull resource-safe local models
Primary: `qwen3.5:9b` Q4_K_M (~6.6GB model payload), current stronger local-fit option with tool/thinking/vision capability and 256K model context, run initially with an 8K server context for VRAM safety.
Fast fallback: `qwen3.5:4b` Q4_K_M (~3.4GB).
Record exact model digests/licenses in the license ledger after pull.

Verification:
- both models listed locally
- Persian and English production-style smoke prompts succeed
- primary inference uses GPU without OOM
- benchmark latency/tokens-per-second is recorded for later model comparison

### P3-AI-04 — Deploy LiteLLM local gateway
Deploy a pinned/self-hosted gateway configured only for local Ollama models. Expose one OpenAI-compatible endpoint to later agents and Activepieces. No paid provider keys are configured.

Routes:
- `growth-primary` → `qwen3.5:9b`
- `growth-fast` → `qwen3.5:4b`
- fallback from primary to fast for retryable local-model failures where safe

### P3-AI-05 — GPU-safe queue and health policy
Implement serialized GPU execution policy, readiness checks, timeout/retry limits and queue state. Later image/video jobs must consume the same GPU lock rather than running concurrently with a loaded LLM when VRAM is insufficient.

### P3-AI-06 — Restart/cold-start verification
Run full WSL shutdown/relaunch. Verify Ollama, gateway, Phase 2 core services and model API recover. No completion claim without a fresh smoke test.

### P3-AI-07 — Bilingual runbook + baseline backup
Document FA/EN operator steps, model inventory, resource limits, rollback and troubleshooting. Take a fresh baseline after verification.

## Phase 3 completion gate
Phase 3 is complete only when:
- Phase 2 remains healthy;
- Ollama is active after cold start;
- `qwen3.5:9b` and `qwen3.5:4b` are callable locally;
- LiteLLM exposes a stable OpenAI-compatible local-only gateway;
- a Persian SEO/revenue-analysis style prompt succeeds through the gateway;
- GPU memory stays within safe limits during the smoke test;
- no paid generative API credential is configured;
- docs/license ledger/baseline are updated.

## Next phase
Phase 4 connects real MyTel and Tehran Network data sources and begins the 24/7 Revenue/SEO Intelligence loop, daily per-site reporting, and the measured 7-day optimization cadence defined in `growth-os/architecture/24X7-OPTIMIZATION-CADENCE-FA.md` / `-EN.md`.
