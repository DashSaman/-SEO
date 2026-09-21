# Sites / سایت‌ها

Purpose: keep each website/customer context isolated while allowing intentionally generic system learning to be reused across sites.

هدف: نگهداری Context هر سایت/مشتری به‌صورت جدا، در حالی که یادگیری‌های عمومی و غیرمحرمانه سیستم بتوانند به‌صورت کنترل‌شده بین سایت‌ها استفاده شوند.

## Isolation rules / قوانین جداسازی
- No credentials in site files.
- MyTel data must not be copied into Tehran Network context unless intentionally shared as generic system learning.
- Tehran Network data must not be copied into MyTel context unless intentionally shared as generic system learning.
- Each site gets its own manifest, brand profile, competitors, channels, experiments, reports and history.
- Secret values belong in the approved secret-management layer, never in this directory.

- هیچ Credential یا Secret واقعی داخل فایل‌های سایت ذخیره نمی‌شود.
- داده اختصاصی MyTel نباید وارد Context تهران نتورک شود مگر اینکه آگاهانه به یک یادگیری عمومی تبدیل شده باشد.
- داده اختصاصی تهران نتورک نباید وارد Context MyTel شود مگر اینکه آگاهانه به یک یادگیری عمومی تبدیل شده باشد.
- هر سایت Manifest، Brand Profile، رقبا، Channelها، آزمایش‌ها، Reportها و History مستقل دارد.

## Future site structure
```text
<site>/
├── site.manifest.yaml
├── brand.yaml
├── competitors.yaml
├── channels.yaml
├── experiments/
├── reports/
└── history/
```

## Operator documentation contract / قرارداد مستندسازی
Any reusable per-site connector/component must document: purpose; why selected; version; prerequisites; installation; configuration; ports/network exposure; secret variable names only; verification; normal operation; update procedure; backup/restore; rollback; common failures; removal procedure; upstream repository and license.
