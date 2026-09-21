# راهنمای عملیاتی Phase 2 — Growth OS

این سند برای مدیریت روزمره Core Platform روی `Amirreza-Pc` / Ubuntu 24.04 WSL2 است.

## آدرس‌های محلی

داخل Ubuntu/WSL:
- Activepieces: `http://localhost:8080`
- Uptime Kuma: `http://localhost:3001`
- Dockge: `http://localhost:5001`

Docker Engine مستقل داخل WSL پورت‌ها را با NAT کرنل publish می‌کند؛ بنابراین Windows localhost forwarding این پورت‌های Docker را همیشه مثل یک Process معمولی Forward نمی‌کند. برای Windows، Helper زیر IP خصوصی و فعلی WSL را خودش پیدا می‌کند، هر سه URL را با HTTP 200 بررسی می‌کند و در Browser باز می‌کند:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "\\wsl.localhost\Ubuntu-24.04\opt\growth-os\repo\growth-os\runtime\core\windows-open-uis.ps1"
```

در تست 2026-09-21 هر سه UI از Windows روی IP خصوصی WSL پاسخ 200 دادند و پورت‌های 8080/3001/5001 روی IP LAN ویندوز قابل دسترس نبودند. این Pilot نباید هیچ‌یک از این پنل‌ها را مستقیماً روی اینترنت منتشر کند.

## مسیرهای اصلی

- Repo: `/opt/growth-os/repo`
- Stackها: `/opt/stacks`
- Backupها: `/opt/growth-os/backups`
- Activepieces secrets: `/opt/stacks/activepieces/.env` — هرگز داخل Git قرار نگیرد.

## وضعیت سرویس‌ها

```bash
cd /opt/stacks/activepieces && docker compose -p activepieces ps
cd /opt/stacks/uptime-kuma && docker compose -p uptime-kuma ps
cd /opt/stacks/dockge && docker compose -p dockge ps
```

## لاگ‌ها

```bash
docker logs --tail 100 growthos-activepieces-app
docker logs --tail 100 growthos-activepieces-worker
docker logs --tail 100 growthos-postgres
docker logs --tail 100 growthos-redis
docker logs --tail 100 growthos-uptime-kuma
docker logs --tail 100 growthos-dockge
```

## تست سلامت کامل

```bash
bash /opt/growth-os/repo/growth-os/runtime/core/phase2-smoke.sh
```

خروجی نهایی سالم باید `PHASE2_SMOKE_OK` باشد. تست HTTP تا 60 ثانیه برای آماده‌شدن سرویس بعد از Cold Start صبر می‌کند.

## Backup

```bash
bash /opt/growth-os/repo/growth-os/runtime/core/phase2-backup.sh
```

Backup شامل PostgreSQL dump و کپی محافظت‌شده از تنظیمات Secret است و در `/opt/growth-os/backups` نگهداری می‌شود. `phase2-restore-check.sh` checksum و قابلیت خواندن dump با `pg_restore` داخل Container PostgreSQL را بررسی می‌کند.

## Autostart ویندوز

فایل زیر در Startup کاربر ساخته شده است:

`%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\GrowthOS-Start-WSL.cmd`

این Launcher هنگام Logon، Ubuntu WSL را Start می‌کند؛ systemd سپس Docker را بالا می‌آورد و Containerها به‌دلیل `restart: unless-stopped` برمی‌گردند. Sleep روی برق AC نیز برای Pilot غیرفعال شده است.

## نکات امنیتی

- Dockge به Docker socket دسترسی دارد و عملاً سطح دسترسی بسیار بالایی روی Docker host دارد؛ فقط در محیط محلی Pilot استفاده شود.
- Compose UI ports داخل WSL روی wildcard bind شده‌اند تا Windows host بتواند از IP خصوصی WSL به آن‌ها برسد؛ WSL در NAT mode است و تست LAN نشان داد این پورت‌ها از IP LAN ویندوز Forward نمی‌شوند.
- عضویت کاربر در گروه `docker` نیز privileged است؛ برای Pilot تک‌مالک پذیرفته شده ولی برای محصول multi-tenant مناسب نیست.
- Secretها، Tokenها و `.env` در GitHub ثبت نمی‌شوند.
- Phase 2 هیچ تغییری روی سایت Production MyTel یا Tehran Network انجام نمی‌دهد.

## اگر سرویس بالا نیامد

ابتدا smoke test را اجرا کن، سپس `docker compose ps` و Log همان Container را ببین. قبل از حذف Volume یا Database هیچ اقدام مخربی انجام نشود.
