# راهنمای عملیاتی Phase 2 — Growth OS

این سند برای مدیریت روزمره Core Platform روی `Amirreza-Pc` / Ubuntu 24.04 WSL2 است.

## آدرس‌های محلی

- Activepieces: `http://localhost:8080`
- Uptime Kuma: `http://localhost:3001`
- Dockge: `http://localhost:5001`

هر سه UI در فاز Pilot فقط روی `127.0.0.1` منتشر می‌شوند و نباید مستقیماً روی اینترنت باز شوند.

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
/opt/growth-os/repo/growth-os/runtime/core/phase2-smoke.sh
```

خروجی نهایی سالم باید `PHASE2_SMOKE_OK` باشد.

## Backup

```bash
/opt/growth-os/repo/growth-os/runtime/core/phase2-backup.sh
```

Backup شامل PostgreSQL dump و کپی محافظت‌شده از تنظیمات Secret است و در `/opt/growth-os/backups` نگهداری می‌شود.

## نکات امنیتی

- Dockge به Docker socket دسترسی دارد و عملاً سطح دسترسی بسیار بالایی روی Docker host دارد؛ فقط localhost.
- عضویت کاربر در گروه `docker` نیز privileged است؛ برای Pilot تک‌مالک پذیرفته شده ولی برای محصول multi-tenant مناسب نیست.
- Secretها، Tokenها و `.env` در GitHub ثبت نمی‌شوند.
- Phase 2 هیچ تغییری روی سایت Production MyTel یا Tehran Network انجام نمی‌دهد.

## اگر سرویس بالا نیامد

ابتدا smoke test را اجرا کن، سپس `docker compose ps` و Log همان Container را ببین. قبل از حذف Volume یا Database هیچ اقدام مخربی انجام نشود.
