# Runtime هسته Growth OS — Phase 2

این پوشه الگوهای Sanitized سرویس‌های Phase 2 را نگه می‌دارد. هیچ Secret خامی نباید وارد Git شود.

## مسیرهای روی Host

- Repo عملیاتی: `/opt/growth-os/repo`
- Backupها: `/opt/growth-os/backups`
- Logها: `/opt/growth-os/logs`
- State: `/opt/growth-os/state`
- Stackها: `/opt/stacks`

## پورت‌های مدیریت

- Activepieces: پورت `8080`
- Uptime Kuma: پورت `3001`
- Dockge: پورت `5001`

Docker Engine مستقل داخل WSL این پورت‌ها را در namespace خصوصی WSL روی wildcard bind می‌کند تا Windows host بتواند از IP خصوصی WSL به آن‌ها برسد. در تست Phase 2 این پورت‌ها از IP LAN ویندوز قابل دسترس نبودند. هیچ‌یک از این UIها نباید مستقیماً روی Internet منتشر شوند.

داخل WSL از `localhost` استفاده کن. در Windows از `windows-open-uis.ps1` استفاده کن تا IP فعلی WSL به‌صورت خودکار پیدا و پنل‌ها باز شوند.

## Secret Policy

فایل `/opt/stacks/activepieces/.env` فقط روی Host ساخته می‌شود، permission آن `600` است و هرگز commit نمی‌شود.

## وضعیت پایه تأییدشده

- Ubuntu 24.04 روی WSL2
- Docker Engine 29.8.1
- Docker Compose v5.5.1
- 20GB سقف RAM WSL، 12 CPU، 8GB Swap
- کاربر عملیاتی: `amirreza`
- Cold-start نهایی Phase 2: `PHASE2_SMOKE_OK`
