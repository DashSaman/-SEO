# Troubleshooting / عیب‌یابی

Purpose: keep reproducible incident records containing symptoms, detection method, root cause, fix, verification, prevention, and rollback.

هدف: ثبت خطاها به‌صورت قابل‌تکرار شامل نشانه، روش تشخیص، علت ریشه‌ای، راه‌حل، Verify، پیشگیری و Rollback.

## Operator documentation contract / قرارداد مستندسازی
Each component/incident guide must record: purpose; why selected; version; prerequisites; installation; configuration; ports/network exposure; secret variable names only; verification; normal operation; update procedure; backup/restore; rollback; common failures; removal procedure; upstream repository and license.

هر راهنما باید هدف، دلیل انتخاب، نسخه، پیش‌نیاز، نصب، تنظیمات، پورت/شبکه، فقط نام Secretها، Verify، عملیات عادی، آپدیت، بکاپ/ریستور، Rollback، خطاهای رایج، حذف و ریپو/License اصلی را ثبت کند.

## Incident rule
Never delete a useful failure from history after fixing it. Preserve the cause and verified remedy so later sites/customers do not pay the same debugging cost again.
