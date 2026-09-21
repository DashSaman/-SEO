# Start Here — Growth OS

This page is for an operator who may know nothing about Linux, WSL, Docker, agents, or SEO tooling. If this system must later be rebuilt, repaired, handed to another operator, or commercialized, start here.

![Growth OS roadmap](./assets/roadmap-en.svg)

## Where are we now?

The live source of truth is [`../AGENT.md`](../AGENT.md). A step is marked `[x]` only after verification.

Current pilot state on 2026-09-21:

- Phase 0: repository bootstrap/docs prepared; PR is open.
- Phase 1: WSL2 and Ubuntu 24.04 are installed.
- Ubuntu runs as WSL VERSION 2.
- RTX 3070 with 8GB VRAM is visible inside Ubuntu.
- Ubuntu repositories are reachable and base package maintenance is in progress/completing.
- Next: WSL resource limits, systemd, then Docker.

## Visual Phase 1 guide

![WSL2 web-download success](./installation/assets/wsl2-step-02-web-download-success.svg)

Persian guide:
- [`installation/PHASE1-WSL2-FA.md`](./installation/PHASE1-WSL2-FA.md)

English guide:
- [`installation/PHASE1-WSL2-EN.md`](./installation/PHASE1-WSL2-EN.md)

Real HTTP 500 incident and recovery:
- [`troubleshooting/INC-WSL2-0001-HTTP-500.md`](./troubleshooting/INC-WSL2-0001-HTTP-500.md)

## Full project path

1. Phase 0 — Repository Foundation
2. Phase 1 — Windows / WSL2
3. Phase 2 — Core Platform
4. Phase 3 — AI Layer
5. Phase 4 — SEO Intelligence
6. Phase 5 — Agent Execution
7. Phase 6 — Trends / Competitors
8. Phase 7 — Social Automation
9. Phase 8 — MyTel + Tehran Network Pilot
10. Phase 9 — Productization / SaaS

## When do the sites enter the loop?

- Phase 4: real MyTel and Tehran Network data ingestion/auditing starts.
- Phase 5: agents may make controlled code/content changes through branch/PR/QA gates.
- Phase 8: full 24/7 pilot loop runs and is measured on both sites.

## Security rule

Never commit real passwords, PATs, API keys, OAuth secrets, cookies, or tokens. Documentation records secret variable names only.

## If you get stuck

1. Read `AGENT.md` and locate `CURRENT_TASK`.
2. Open the guide for that phase/task.
3. Check `troubleshooting/` for a matching incident.
4. Never repeat a verified step unless the runbook explicitly calls for an upgrade or recovery action.
