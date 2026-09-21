# Growth OS Core Runtime — Phase 2

This directory stores sanitized Phase 2 service templates. Raw secrets must never enter Git.

## Host paths

- Operational repo: `/opt/growth-os/repo`
- Backups: `/opt/growth-os/backups`
- Logs: `/opt/growth-os/logs`
- State: `/opt/growth-os/state`
- Compose stacks: `/opt/stacks`

## Local ports

- Activepieces: `127.0.0.1:8080`
- Uptime Kuma: `127.0.0.1:3001`
- Dockge: `127.0.0.1:5001`

During the pilot these ports bind to localhost only and must not be exposed directly to the LAN or Internet.

## Secret policy

`/opt/stacks/activepieces/.env` is created only on the host, uses permission `600`, and is never committed.

## Verified baseline

- Ubuntu 24.04 on WSL2
- Docker Engine 29.8.1
- Docker Compose v5.5.1
- WSL capped at 20GB RAM, 12 CPUs, 8GB swap
- Operational user: `amirreza`
