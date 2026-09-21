# Phase 1 — نصب WSL2 و Ubuntu 24.04 روی Windows 11

این راهنما برای کاربری نوشته شده که هیچ تجربه قبلی با Linux، WSL یا Docker ندارد. هدف این مرحله فقط ساخت محیط Linux تمیز داخل Windows است؛ هنوز Docker، Agentها یا ابزارهای SEO نصب نمی‌شوند.

## WSL2 چیست؟

WSL2 یعنی یک محیط Linux واقعی داخل Windows بدون نیاز به VMware یا نصب دوگانه سیستم‌عامل.

```mermaid
flowchart TD
    A[Windows 11] --> B[WSL2]
    B --> C[Ubuntu 24.04 LTS]
    C --> D[بعداً Docker]
    D --> E[Growth OS Services]
```

تو همچنان با Windows کار می‌کنی و Ubuntu پشت‌صحنه برای سرویس‌های سروری استفاده می‌شود.

## وضعیت این سیستم در 2026-09-21

نتیجه Preflight ثبت‌شده:

```text
WSL: نصب نیست
Ubuntu: نصب نیست
GPU: NVIDIA GeForce RTX 3070 Laptop GPU
VRAM: 8192 MiB
Windows NVIDIA Driver: 616.92
CUDA UMD reported by Windows: 13.4
```

پس مسیر درست این سیستم، نصب WSL2 از صفر است.

---

# قدم 1 — باز کردن PowerShell با دسترسی Administrator

1. روی Start کلیک کن.
2. بنویس `PowerShell`.
3. روی **Windows PowerShell** راست‌کلیک کن.
4. **Run as administrator** را بزن.
5. اگر پنجره تأیید Windows باز شد، **Yes** را بزن.

باید چیزی شبیه این ببینی:

```text
Windows PowerShell
PS C:\WINDOWS\system32>
```

---

# قدم 2 — نصب WSL2 و Ubuntu 24.04

در همان PowerShell Administrator این دستور را دقیقاً وارد کن:

```powershell
wsl --install -d Ubuntu-24.04
```

این دستور باید WSL، Virtual Machine Platform، Linux kernel و Ubuntu 24.04 را نصب کند.

طبق مستندات رسمی Microsoft، `wsl --install` روش توصیه‌شده نصب WSL روی Windows 11 است و با `-d` می‌توان توزیع موردنظر را تعیین کرد.

## نتیجه مورد انتظار

ممکن است پیام‌هایی درباره فعال‌شدن Featureها، Download و Install ببینی. در پایان معمولاً Windows می‌گوید برای کامل‌شدن نصب سیستم را Restart کن.

اگر Restart خواست:

1. همه فایل‌های بازت را ذخیره کن.
2. Windows را Restart کن.
3. بعد از بالا آمدن Windows ادامه همین راهنما را انجام بده.

> اگر نصب روی `0.0%` گیر کرد، فعلاً چیزی را حذف نکن. خطا را ثبت کن. راه جایگزین رسمی Microsoft این است:
>
> ```powershell
> wsl --install --web-download -d Ubuntu-24.04
> ```
>
> اما فقط وقتی از مسیر عادی خطا گرفتیم از آن استفاده می‌کنیم.

---

# قدم 3 — اولین اجرای Ubuntu

بعد از Restart ممکن است Ubuntu خودکار باز شود. اگر باز نشد:

1. Start را باز کن.
2. بنویس `Ubuntu 24.04`.
3. برنامه را اجرا کن.

اولین اجرا ممکن است چند دقیقه برای آماده‌سازی فایل‌ها زمان بخواهد.

سپس از تو Username می‌خواهد:

```text
Enter new UNIX username:
```

یک نام ساده انگلیسی انتخاب کن؛ مثال:

```text
saman
```

بعد Password می‌خواهد.

نکته مهم: هنگام تایپ Password در Linux هیچ ستاره یا کاراکتری روی صفحه نمی‌بینی. این طبیعی است. Password را تایپ کن و Enter بزن.

Password را دوباره تکرار کن.

وقتی تمام شد چیزی شبیه این می‌بینی:

```text
saman@COMPUTER:~$
```

این یعنی وارد Ubuntu شده‌ای.

---

# قدم 4 — Verify نصب از داخل Windows

PowerShell را باز کن و بزن:

```powershell
wsl --status
```

سپس:

```powershell
wsl --list --verbose
```

نتیجه مورد انتظار باید چیزی شبیه این باشد:

```text
NAME              STATE           VERSION
* Ubuntu-24.04    Running         2
```

مهم‌ترین قسمت:

```text
VERSION = 2
```

اگر VERSION برابر 1 بود، ادامه نده و مشکل را ثبت کن.

---

# قدم 5 — Verify GPU داخل Ubuntu

داخل پنجره Ubuntu این دستور را اجرا کن:

```bash
nvidia-smi
```

باید RTX 3070 را ببینی. لازم نیست CUDA Toolkit را داخل Ubuntu نصب کنیم فقط برای اینکه `nvidia-smi` کار کند؛ WSL از درایور Windows استفاده می‌کند.

اگر `nvidia-smi` کار کرد، GPU Pass-through برای WSL آماده است.

---

# قدم 6 — فعلاً توقف

بعد از موفقیت قدم‌های بالا هنوز این‌ها را نصب نکن:

```text
Docker
Ollama
LiteLLM
n8n
PostgreSQL
Redis
OpenHands
Postiz
OpenGSC
DispatchSEO
```

اول خروجی Verifyها باید ثبت شود، بعد Phase 1 ادامه پیدا می‌کند.

---

# خطاهای رایج

## خطا: WSL نصب نیست

```text
The Windows Subsystem for Linux is not installed
```

راه‌حل مرحله فعلی:

```powershell
wsl --install -d Ubuntu-24.04
```

## نصب روی 0.0% گیر کرده

بعد از ثبت خطا می‌توان از مسیر رسمی جایگزین استفاده کرد:

```powershell
wsl --install --web-download -d Ubuntu-24.04
```

## بعد از نصب Ubuntu باز نمی‌شود

ابتدا Windows را Restart کن، سپس:

```powershell
wsl --list --verbose
```

و نتیجه را بررسی کن.

## Password دیده نمی‌شود

طبیعی است. Linux هنگام تایپ Password چیزی نشان نمی‌دهد.

---

# چک‌لیست اپراتور

- [ ] PowerShell به صورت Administrator باز شد.
- [ ] `wsl --install -d Ubuntu-24.04` اجرا شد.
- [ ] Windows در صورت نیاز Restart شد.
- [ ] Ubuntu 24.04 اولین بار اجرا شد.
- [ ] Linux username ساخته شد.
- [ ] `wsl --status` بدون خطا اجرا شد.
- [ ] `wsl --list --verbose` نشان داد Ubuntu روی VERSION 2 است.
- [ ] `nvidia-smi` داخل Ubuntu کارت RTX 3070 را نشان داد.
- [ ] نتیجه Verify در `AGENT.md` ثبت شد.

## Rollback / حذف اضطراری

در این مرحله اگر نصب ناقص شد، قبل از حذف یا `unregister` کردن Ubuntu ابتدا خطا باید ثبت و بررسی شود. دستورهای حذف عمداً در این راهنمای شروع قرار داده نشده‌اند تا کاربر تازه‌کار تصادفاً داده Linux را پاک نکند.

## منابع رسمی

- Microsoft Learn — Install WSL
- Microsoft Learn — Basic commands for WSL

این راهنما با هر تغییر واقعی در نصب، خطا یا راه‌حل روی سیستم Pilot به‌روزرسانی می‌شود تا بعداً به Runbook قابل استفاده برای مشتری تبدیل شود.
