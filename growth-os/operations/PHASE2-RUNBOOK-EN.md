# Phase 2 Operations Runbook — Growth OS

This runbook covers the Core Platform on `Amirreza-Pc` / Ubuntu 24.04 WSL2.

## Local URLs

- Activepieces: `http://localhost:8080`
- Uptime Kuma: `http://localhost:3001`
- Dockge: `http://localhost:5001`

During the local pilot all three management UIs bind only to `127.0.0.1` and must not be exposed directly to the public Internet.

## Main paths

- Repository: `/opt/growth-os/repo`
- Compose stacks: `/opt/stacks`
- Backups: `/opt/growth-os/backups`
- Activepieces secrets: `/opt/stacks/activepieces/.env` — never commit this file.

## Service status

```bash
cd /opt/stacks/activepieces && docker compose -p activepieces ps
cd /opt/stacks/uptime-kuma && docker compose -p uptime-kuma ps
cd /opt/stacks/dockge && docker compose -p dockge ps
```

## Logs

```bash
docker logs --tail 100 growthos-activepieces-app
docker logs --tail 100 growthos-activepieces-worker
docker logs --tail 100 growthos-postgres
docker logs --tail 100 growthos-redis
docker logs --tail 100 growthos-uptime-kuma
docker logs --tail 100 growthos-dockge
```

## Full health test

```bash
/opt/growth-os/repo/growth-os/runtime/core/phase2-smoke.sh
```

A healthy run ends with `PHASE2_SMOKE_OK`.

## Backup

```bash
/opt/growth-os/repo/growth-os/runtime/core/phase2-backup.sh
```

Backups contain a PostgreSQL dump plus a protected copy of the host-only secret configuration and are stored under `/opt/growth-os/backups`.

## Security notes

- Dockge mounts the Docker socket and therefore has highly privileged control of the Docker host; keep it localhost-only.
- Membership in the `docker` group is privileged and is acceptable only for this single-owner pilot, not as a multi-tenant permission model.
- Secrets, tokens and `.env` files are never committed to GitHub.
- Phase 2 does not modify the MyTel or Tehran Network production sites.

## If a service is down

Run the smoke test first, then inspect `docker compose ps` and the affected container logs. Do not delete volumes or databases as a troubleshooting shortcut.
