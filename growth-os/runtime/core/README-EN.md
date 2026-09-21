# Growth OS Core Runtime — Phase 2

This directory stores sanitized Phase 2 service templates. Raw secrets must never enter Git.

## Host paths

- Operational repo: `/opt/growth-os/repo`
- Backups: `/opt/growth-os/backups`
- Logs: `/opt/growth-os/logs`
- State: `/opt/growth-os/state`
- Compose stacks: `/opt/stacks`

## Management ports

- Activepieces: port `8080`
- Uptime Kuma: port `3001`
- Dockge: port `5001`

The standalone Docker Engine inside WSL binds these ports on the private WSL namespace wildcard interface so the Windows host can reach them through WSL's private address. Phase 2 verification showed the ports were not reachable through the Windows LAN address. None of these management UIs should be exposed directly to the public Internet.

Inside WSL use `localhost`. On Windows use `windows-open-uis.ps1` so the current WSL address is resolved automatically and the panels are opened for the operator.

## Secret policy

`/opt/stacks/activepieces/.env` is created only on the host, uses permission `600`, and is never committed.

## Verified baseline

- Ubuntu 24.04 on WSL2
- Docker Engine 29.8.1
- Docker Compose v5.5.1
- WSL capped at 20GB RAM, 12 CPUs, 8GB swap
- Operational user: `amirreza`
- Final Phase 2 cold-start: `PHASE2_SMOKE_OK`
