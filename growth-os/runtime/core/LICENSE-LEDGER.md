# Growth OS — Phase 2 License Ledger

Verified: 2026-09-21

This ledger tracks the exact Phase 2 runtime components used by the local pilot. It is operational documentation, not legal advice. Re-check licenses before redistribution, embedding, or commercial product release.

| Component | Runtime version/tag | Verified image digest | Upstream license | Commercialization note | Official source |
|---|---|---|---|---|---|
| Activepieces Community Edition | `ghcr.io/activepieces/activepieces:0.86.3` | `sha256:208517c4f0d798a477a0c594bf432dd0f4918433f4b6f5b5f188a6e10e638c6c` | MIT for non-EE code; enterprise directories have separate terms | Pilot uses CE only. Do not depend on enterprise-only code/features without a separate review. | https://github.com/activepieces/activepieces/blob/main/LICENSE |
| pgvector / PostgreSQL image | `pgvector/pgvector:0.8.0-pg14` | `sha256:c55d7e7deac05dde62139e0ded4fcf4f58363656cbc382dbea82fbed995aa767` | PostgreSQL License | Permissive; retain copyright/license notices when redistributing. | https://github.com/pgvector/pgvector/blob/master/LICENSE |
| Redis | `redis:7.0.7` | `sha256:bb474c35022ca2c5618f4c49ca759bd2c0eea1daf5d934c560bd30092b97b498` | BSD 3-Clause style license in Redis 7.0.7 COPYING | Permissive for this pinned 7.0.7 release; future Redis major/version changes require a fresh license review. | https://github.com/redis/redis/blob/7.0.7/COPYING |
| Uptime Kuma | `louislam/uptime-kuma:2` | `sha256:c74379ac4509ce2d2c2633f509e67003ee2e45b6e995c5e43fc101f45a0e1fbe` | MIT | Permissive; retain license notice when redistributing. | https://github.com/louislam/uptime-kuma/blob/master/LICENSE |
| Dockge | `louislam/dockge:1` | `sha256:335c6368b880ecc203236ed89e6e5232e0d6578e8ef5920e4a502390451502bf` | MIT | Permissive; Dockge's Docker socket privilege is a security concern, not a license issue. | https://github.com/louislam/dockge/blob/master/LICENSE |
| Docker Engine / Moby | Engine `29.8.1` | n/a — host package | Apache-2.0 upstream | Permissive upstream engine license; packaged distribution terms must also be respected. | https://github.com/moby/moby/blob/master/LICENSE |
| Docker CLI | `29.8.1` | n/a — host package | Apache-2.0 | Permissive upstream CLI license. | https://github.com/docker/cli/blob/master/LICENSE |
| Docker Compose | `v5.5.1` | n/a — host plugin | Apache-2.0 | Permissive upstream Compose license. | https://github.com/docker/compose/blob/main/LICENSE |

## Productization gate

Before Phase 9 commercialization, re-verify every exact deployed tag/digest and all local AI model licenses. In particular:

- Never assume a model license follows the license of the inference tool that runs it.
- Record model weights, voice packs, checkpoints, LoRAs, media assets and fonts separately.
- Do not use enterprise-only Activepieces code as if it were MIT Community Edition.
- Re-check Redis licensing if the pinned 7.0.7 line is upgraded to a materially different release/license generation.
- Keep attribution/license files required by each dependency in any redistributed product bundle.
