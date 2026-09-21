# Growth OS Documentation / مستندات Growth OS

This directory contains the reusable architecture, installation, operation, troubleshooting, product-learning, experiment, benchmark, compliance, and per-site records for Growth OS.

این پوشه مرجع عملیاتی سیستم Growth OS است؛ هر نصب، تغییر معماری، خطا، آزمایش و نتیجه‌ای که قابلیت استفاده مجدد داشته باشد باید در مسیر مناسب اینجا ثبت شود.

## Map / نقشه
- `architecture/` — long-lived architecture and ADRs / معماری و تصمیم‌های ADR
- `installation/` — installation guides beginning in Phase 1 / راهنماهای نصب از فاز ۱
- `operations/` — start, stop, update, backup, restore, runbooks / عملیات روزمره و بازیابی
- `troubleshooting/` — incidents, symptoms, causes, fixes / خطاها، علت و راه‌حل
- `product/` — onboarding, cost model, pricing, multi-tenant evolution / مسیر محصول و درآمدزایی
- `experiments/` — hypotheses, actions, metrics, results / آزمایش‌ها و نتایج اندازه‌گیری‌شده
- `benchmarks/` — LLM, task, cost, performance measurements / مقایسه مدل‌ها، هزینه و کارایی
- `compliance/` — licenses, provider policies, privacy/security constraints / مجوزها، قوانین سرویس‌ها و حریم خصوصی
- `sites/` — non-secret per-site manifests, reports, history and pilot notes / اطلاعات غیرمحرمانه هر سایت

## Rule / قانون
Do not create undocumented production state. If a reusable component is installed or changed, its operator documentation and `AGENT.md` state must be updated.

هیچ وضعیت Production بدون مستندات ایجاد نمی‌شود. نصب یا تغییر هر جزء قابل‌استفاده‌مجدد باید هم در مستندات و هم در `AGENT.md` ثبت شود.
