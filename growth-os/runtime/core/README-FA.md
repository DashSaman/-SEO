# Runtime هسته Growth OS — Phase 2

این پوشه الگوهای Sanitized سرویس‌های Phase 2 را نگه می‌دارد. هیچ Secret خامی نباید وارد Git شود.

## مسیرهای روی Host

- Repo عملیاتی: `/opt/growth-os/repo`
- Backupها: `/opt/growth-os/backups`
- Logها: `/opt/growth-os/logs`
- State: `/opt/growth-os/state`
- Stackها: `/opt/stacks`

## پورت‌های محلی

- Activepieces: `127.0.0.1:8080`
- Uptime Kuma: `127.0.0.1:3001`
- Dockge: `127.0.0.1:5001`

این پورت‌ها در Pilot فقط روی localhost bind می‌شوند و نباید مستقیم روی LAN/Internet باز شوند.

## Secret Policy

فایل `/opt/stacks/activepieces/.env` فقط روی Host ساخته می‌شود، permission آن `600` است و هرگز commit نمی‌شود.

## وضعیت پایه تأییدشده

- Ubuntu 24.04 روی WSL2
- Docker Engine 29.8.1
- Docker Compose v5.5.1
- 20GB سقف RAM WSL، 12 CPU، 8GB Swap
- کاربر عملیاتی: `amirreza`
