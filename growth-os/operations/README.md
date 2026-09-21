# Operations / عملیات

Purpose: production runbooks for start/stop/restart, health checks, updates, backup/restore, scheduled maintenance, and disaster recovery.

هدف: ثبت Runbookهای عملیاتی برای Start/Stop/Restart، Health Check، آپدیت، Backup/Restore، نگهداری دوره‌ای و Disaster Recovery.

## Operator documentation contract / قرارداد مستندسازی
Each runbook/component document must record: purpose; why selected; version; prerequisites; installation; configuration; ports/network exposure; secret variable names only; verification; normal operation; update procedure; backup/restore; rollback; common failures; removal procedure; upstream repository and license.

هر Runbook باید هدف، دلیل انتخاب، نسخه، پیش‌نیاز، نصب، تنظیمات، پورت/شبکه، فقط نام Secretها، Verify، عملیات عادی، آپدیت، بکاپ/ریستور، Rollback، خطاهای رایج، حذف و ریپو/License اصلی را ثبت کند.

## Operations rule
A backup is not considered valid until a restore test has been performed and recorded.
