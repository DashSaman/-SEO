# Installation / نصب

Purpose: step-by-step installation guides beginning with Phase 1 (Windows/WSL2) and continuing through every Growth OS service.

هدف: راهنماهای مرحله‌به‌مرحله نصب از WSL2 تا تمام سرویس‌های Growth OS، طوری که کاربر بدون دانش قبلی بتواند نصب و عیب‌یابی را دنبال کند.

## Phase 1 guides / راهنماهای فاز ۱

- [راهنمای فارسی نصب WSL2 و Ubuntu 24.04](PHASE1-WSL2-FA.md)
- [English WSL2 and Ubuntu 24.04 setup guide](PHASE1-WSL2-EN.md)

راهنمای فارسی شامل دیاگرام Mermaid، خروجی مورد انتظار، خطاهای رایج، چک‌لیست Verify و مسیر امن توقف است. با هر خطای واقعی Pilot این راهنما به‌روزرسانی می‌شود تا بعداً قابل استفاده برای مشتری یا اپراتور جدید باشد.

## Operator documentation contract / قرارداد مستندسازی
Every component guide must record: purpose; why selected; version; prerequisites; installation; configuration; ports/network exposure; secret variable names only; verification; normal operation; update procedure; backup/restore; rollback; common failures; removal procedure; upstream repository and license.

هر راهنما باید هدف، دلیل انتخاب، نسخه، پیش‌نیاز، نصب، تنظیمات، پورت/شبکه، فقط نام Secretها، Verify، عملیات عادی، آپدیت، بکاپ/ریستور، Rollback، خطاهای رایج، حذف و ریپو/License اصلی را ثبت کند.

## Installation rule
No installation step is marked complete until its verification command/result is recorded in `AGENT.md` or the relevant phase runbook.
