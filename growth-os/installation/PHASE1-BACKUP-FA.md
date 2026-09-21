# بکاپ پایه Phase 1 — WSL2 / Ubuntu / Docker

این مرحله درست قبل از ورود به Phase 2 انجام می‌شود تا یک نقطه بازگشت سالم از Ubuntu 24.04 + WSL2 + Docker داشته باشیم.

## چرا این بکاپ را می‌گیریم؟

تا اینجا Ubuntu، GPU، محدودیت منابع، systemd و Docker تست شده‌اند. از Phase 2 به بعد سرویس‌های دائمی، دیتابیس و Automation اضافه می‌شوند. اگر در آینده چیزی خراب شد، این Export امکان می‌دهد به وضعیت تمیز پایان Phase 1 برگردیم.

## مرحله 1 — خروج از Ubuntu

داخل Ubuntu:

```bash
exit
```

## مرحله 2 — ساخت پوشه بکاپ در Windows

در PowerShell:

```powershell
New-Item -ItemType Directory -Force -Path C:\GrowthOS-Backups
```

## مرحله 3 — خاموش کردن کامل WSL

```powershell
wsl --shutdown
```

## مرحله 4 — Export کامل Ubuntu

```powershell
wsl --export Ubuntu-24.04 C:\GrowthOS-Backups\Ubuntu-24.04-phase1-2026-09-21.tar
```

ممکن است چند دقیقه طول بکشد. تا برگشتن Prompt پنجره را نبندید.

## مرحله 5 — بررسی فایل

```powershell
Get-Item C:\GrowthOS-Backups\Ubuntu-24.04-phase1-2026-09-21.tar | Format-List FullName,Length,LastWriteTime
```

## مرحله 6 — ثبت SHA256

```powershell
Get-FileHash C:\GrowthOS-Backups\Ubuntu-24.04-phase1-2026-09-21.tar -Algorithm SHA256
```

Hash و اندازه فایل در Execution Ledger ثبت می‌شوند؛ خود فایل بکاپ وارد GitHub نمی‌شود.

## نکته امنیتی

فایل Export می‌تواند تنظیمات و داده‌های داخل Ubuntu را در خود داشته باشد. آن را عمومی نکنید و داخل repository commit نکنید.

## بازیابی اضطراری

بازیابی باید فقط با تصمیم آگاهانه و بعد از بررسی نسخه موجود انجام شود؛ چون `wsl --unregister` مخرب است. در Runbook بازیابی، ابتدا از وضعیت فعلی Backup گرفته می‌شود و سپس import روی نام جدا انجام می‌شود تا از حذف ناخواسته جلوگیری شود.
