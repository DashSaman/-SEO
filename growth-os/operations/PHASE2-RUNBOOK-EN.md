# Phase 2 Operations Runbook — Growth OS

This runbook covers the Core Platform on `Amirreza-Pc` / Ubuntu 24.04 WSL2.

## Local URLs

Inside Ubuntu/WSL:
- Activepieces: `http://localhost:8080`
- Uptime Kuma: `http://localhost:3001`
- Dockge: `http://localhost:5001`

The standalone Docker Engine inside WSL publishes ports through kernel NAT, so WSL localhost forwarding does not always surface those Docker-published ports on Windows localhost the same way it surfaces a normal listening process. On Windows, use the helper below: it resolves the current private WSL address, verifies HTTP 200 for all three UIs, and opens them in the browser.

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "\\wsl.localhost\Ubuntu-24.04\opt\growth-os\repo\growth-os\runtime\core\windows-open-uis.ps1"
```

On 2026-09-21 all three UIs returned HTTP 200 from Windows through the private WSL address, while ports 8080/3001/5001 were not reachable through the Windows LAN address. Do not expose any of these pilot management UIs directly to the public Internet.

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
bash /opt/growth-os/repo/growth-os/runtime/core/phase2-smoke.sh
```

A healthy run ends with `PHASE2_SMOKE_OK`. HTTP checks retry for up to 60 seconds to allow services to become ready after a cold start.

## Backup

```bash
bash /opt/growth-os/repo/growth-os/runtime/core/phase2-backup.sh
```

Backups contain a PostgreSQL dump plus a protected copy of the host-only secret configuration and are stored under `/opt/growth-os/backups`. `phase2-restore-check.sh` verifies checksums and confirms the dump is readable with the PostgreSQL container's `pg_restore`.

## Windows autostart

The following user Startup launcher is created:

`%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\GrowthOS-Start-WSL.cmd`

At logon it starts Ubuntu WSL; systemd starts Docker, then the containers return because they use `restart: unless-stopped`. AC sleep is also disabled for the local 24/7 pilot.

## Security notes

- Dockge mounts the Docker socket and therefore has highly privileged control of the Docker host; use it only in the local pilot environment.
- Compose UI ports bind to the WSL wildcard interface so the Windows host can reach them via WSL's private address. WSL is operating in NAT mode and the LAN verification showed these ports are not forwarded through the Windows LAN address.
- Membership in the `docker` group is privileged and is acceptable only for this single-owner pilot, not as a multi-tenant permission model.
- Secrets, tokens and `.env` files are never committed to GitHub.
- Phase 2 does not modify the MyTel or Tehran Network production sites.

## If a service is down

Run the smoke test first, then inspect `docker compose ps` and the affected container logs. Do not delete volumes or databases as a troubleshooting shortcut.
