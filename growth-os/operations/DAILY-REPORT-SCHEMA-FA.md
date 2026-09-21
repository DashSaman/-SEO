# Schema گزارش روزانه Growth OS

هر سایت باید هر 24 ساعت یک گزارش مستقل در Repo و Telegram خودش داشته باشد.

## 1) Executive Summary
- وضعیت کلی: Healthy / Degraded / Attention
- مهم‌ترین تغییر 24 ساعت گذشته
- مهم‌ترین اثر مثبت/منفی
- مهم‌ترین تصمیم برای 24 ساعت بعد

## 2) KPI Snapshot
در صورت دسترسی به داده:
- GSC Clicks / Impressions / CTR / Average Position
- Queryهای تجاری منتخب و تغییر Position
- صفحات برتر / افت‌کرده
- Indexed/Crawl/404/5xx/redirect/canonical issues
- Lighthouse/performance regressions
- Sessions / engaged traffic
- Leads / calls / forms / conversions / revenue signals
- Social reach / engagement / site clicks

هم تغییر 24h و هم مقایسه 7-day baseline نمایش داده شود؛ داده کم یا lagدار باید صریح مشخص شود.

## 3) What Growth OS Did Today
برای هر Action:
```yaml
action:
  id: "..."
  reason: "..."
  evidence_before: "..."
  change: "..."
  verification: pass|fail|pending
  impact_now: "..."
  next_measurement_date: "..."
  status: keep|observe|adjust|rollback|queued
```

## 4) Opportunity Queue
- فرصت‌های جدید SEO
- فرصت‌های Competitor/Trend
- CRO/Offer/Revenue opportunities
- Content/Social/Video opportunities
- priority score + evidence + expected measurement metric

## 5) Failures / Retries / Incidents
- چه چیزی Fail شد؟
- علت شناخته‌شده چیست؟
- Retry انجام شد یا Queue شد؟
- آیا کاربر باید کاری انجام دهد؟ در حالت عادی: خیر.

## 6) Impact / Time-Waste Check
این بخش اجباری است تا مشخص شود سیستم ارزش ایجاد می‌کند یا خیر:
- کارهای انجام‌شده که هنوز برای نتیجه زود است
- کارهایی که اثر اولیه مثبت دارند
- کارهایی که اثر منفی/صفر دارند
- Experiments متوقف یا Rollback شده
- Compute time / local GPU usage / paid API cost (هدف generative API = صفر)
- Lead/Conversion/Revenue impact در صورت وجود داده

## 7) Tomorrow / Next Cycle
حداکثر چند اقدام اولویت‌دار با دلیل و Metric هدف.

## 8) Weekly marker
در روز پایان چرخه 7 روزه، Daily Report به Weekly Optimization Review لینک دهد و Before/After هفتگی را خلاصه کند.

## Anti-vanity rule
گزارش نباید موفقیت را فقط با تعداد مقاله، تعداد تغییر یا Traffic خام اعلام کند. اثر روی Search quality، qualified traffic، conversion و commercial outcome باید هرجا داده وجود دارد گزارش شود.
