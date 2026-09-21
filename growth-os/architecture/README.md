# Architecture / معماری

Purpose: record long-lived system architecture, interfaces, boundaries, resource decisions, and Architecture Decision Records (ADRs).

هدف: ثبت معماری ماندگار، مرز سرویس‌ها، اینترفیس‌ها، تصمیم‌های منابع و ADRها.

## Operator documentation contract / قرارداد مستندسازی
Every reusable component document must record: purpose; why selected; version; prerequisites; installation; configuration; ports/network exposure; secret variable names only; verification; normal operation; update procedure; backup/restore; rollback; common failures; removal procedure; upstream repository and license.

هر جزء قابل‌استفاده‌مجدد باید این موارد را ثبت کند: هدف، دلیل انتخاب، نسخه، پیش‌نیاز، نصب، تنظیمات، پورت/شبکه، فقط نام Secretها، روش Verify، عملیات عادی، آپدیت، بکاپ/ریستور، Rollback، خطاهای رایج، حذف و ریپوی اصلی/License.

## ADR rule
Create an ADR whenever a meaningful alternative was rejected and the decision matters to future operation, migration, security, cost, or productization.
