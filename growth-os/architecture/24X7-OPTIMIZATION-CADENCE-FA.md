# ریتم عملیاتی 24/7 Growth OS

## هدف
Growth OS باید برای هر سایت به‌صورت پیوسته کار کند؛ مالک درگیر اجرای روزانه نباشد و فقط گزارش، نتیجه و پیشنهادها را مرور کند.

## چرخه دائمی

```text
Signals / Health / Search / Competitors / Social / Leads
        ↓
24/7 Monitoring
        ↓
Opportunity Queue + Alerts
        ↓
Daily Analysis + Daily Report
        ↓
7-Day Optimization Cycle
        ↓
Execute low-risk approved work
        ↓
Measure Before/After
        ↓
Learn + Re-score + Repeat
```

## 24/7 Monitoring
- پایش وضعیت سرویس‌ها، Crawl، indexability، خطاهای فنی، GSC/GA4، SERP/Rank، رقبا، Trendها، Social و Lead/Conversion هر زمان که Connector مربوطه فعال باشد.
- Signalهای سریع می‌توانند در بازه‌های کوتاه‌تر بررسی شوند؛ سیستم نباید برای کشف Incident تا گزارش روزانه صبر کند.
- اگر لپ‌تاپ/Worker موقتاً خاموش باشد، Jobها باید قابل صف‌شدن و Resume باشند. برای SLA تجاری واقعی، Control Plane همیشه‌روشن در فاز Productization لازم است.

## Daily Report — هر 24 ساعت
برای هر سایت یک گزارش مستقل تولید شود و به Repo همان سایت و Telegram همان سایت ارسال شود. گزارش حداقل شامل این موارد باشد:
- وضعیت سلامت و Incidentها؛
- تغییرات Ranking/Impression/CTR/Traffic/Conversion در صورت دسترسی به داده؛
- فرصت‌های جدید SEO/Marketing/Competitor/Content/CRO/Revenue؛
- کارهای انجام‌شده در 24 ساعت گذشته؛
- نتیجه/Verification هر کار؛
- کارهای Fail/Retry/Queued؛
- هزینه محاسباتی/API در صورت وجود؛
- مهم‌ترین اقدام‌های برنامه‌ریزی‌شده برای چرخه بعدی.

## 7-Day Optimization Cycle
هر 7 روز برای هر سایت یک چرخه کامل بهینه‌سازی اجرا شود:
1. Snapshot قبل از تغییرات.
2. Re-score فرصت‌ها با داده جدید.
3. انتخاب کارهای کم‌ریسک و دارای اولویت تجاری بالاتر.
4. اجرای SEO/Content/Internal-link/CRO/Social/Technical actions متناسب با فاز فعال سیستم.
5. QA و Verification.
6. Snapshot بعد از تغییرات.
7. ثبت Before/After و اثر اولیه.
8. نگه‌داشتن تغییر، اصلاح، Rollback یا ادامه آزمایش بر اساس شواهد.

## اصل اندازه‌گیری
بهینه‌سازی موفق فقط با «تعداد کار انجام‌شده» سنجیده نمی‌شود. Metrics بسته به سایت شامل Search visibility، CTR، qualified traffic، leads، calls، conversions، commercial value و revenue/ROI است. افزایش Rank یا Traffic به‌تنهایی تضمین موفقیت تجاری نیست.

## Automation Policy
- Monitoring، جمع‌آوری داده، گزارش‌سازی، Queue management و کارهای کم‌ریسک قابل اتوماسیون هستند.
- کارهای مخرب/پرریسک مانند حذف URL، redirect/canonical گسترده، تغییر معماری اصلی، قیمت‌گذاری حساس یا هزینه تبلیغاتی بدون مجوز در حالت fail-closed باقی می‌مانند.
- Owner workflow باید review-first باشد: مالک گزارش و پیشنهادها را می‌بیند و برای Routine Operations مجبور به تولید محتوا، ادیت، Upload یا اجرای دستی نیست.

## Reporting Isolation
MyTel و Tehran Network باید state، action log، experiment log، Repo report و Telegram destination مستقل داشته باشند تا تحلیل نتایج با هم مخلوط نشود.
