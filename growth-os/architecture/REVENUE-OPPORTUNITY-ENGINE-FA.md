# معماری Revenue Opportunity Engine

هدف این بخش این است که Growth OS فقط «سئو» یا «انتشار محتوا» نباشد؛ بلکه موتور کشف، امتیازدهی، اجرا و اندازه‌گیری فرصت‌های درآمدی و رقابتی باشد.

## اصل محصول

سیستم باید دائماً داده‌های بازار و عملکرد کسب‌وکار را جمع کند، فرصت‌ها را به اقدام قابل اجرا تبدیل کند، نتیجه را اندازه بگیرد و از آن یاد بگیرد.

```text
Signals
  ├─ GSC / Search queries / CTR / positions
  ├─ GA4 / conversions / landing performance
  ├─ SERP / competitors / content gaps
  ├─ Website crawl / technical SEO / internal linking
  ├─ Competitor pages / pricing / offers / launches
  ├─ Trends / RSS / news / communities
  ├─ Social reach / engagement / search visibility
  ├─ Leads / forms / calls / CRM signals (when connected)
  ├─ Product/service margin and business priority
  └─ Server / logs / indexation / uptime
          ↓
Revenue Opportunity Engine
          ↓
Score = Revenue potential + intent + demand + speed + confidence - effort - risk
          ↓
Action Plan
          ↓
Website / Content / Social / Offer / Conversion / Product / Outreach
          ↓
QA + Approval Tier
          ↓
Publish / Deploy / Schedule
          ↓
Measure revenue-oriented outcome
          ↓
Learn / Re-score / Repeat
```

## دسته‌های فرصت که باید رصد شوند

### Search / SEO
- Queryهای دارای impression بالا و رتبه نزدیک صفحه اول
- CTR پایین نسبت به جایگاه
- Content decay
- Cannibalization
- صفحات بدون internal-link کافی
- موضوعات و سوالاتی که رقبا پوشش داده‌اند و ما نداریم
- SERPهایی که ابزار، FAQ، ویدیو یا صفحه خدمات می‌تواند مزیت ایجاد کند
- مشکلات crawl/index/schema/performance که جلوی رشد صفحات درآمدزا را می‌گیرند

### Commercial / Revenue
- صفحات و Queryهای با intent خرید، تماس، قیمت، مقایسه یا درخواست خدمات
- خدماتی که تقاضای بالا ولی پوشش ضعیف در سایت دارند
- فرصت ساخت Landing Page یا Tool برای Lead generation
- Upsell / cross-sell بین خدمات مرتبط
- Offer و CTAهایی که نیاز به تست دارند
- فرصت ساخت بسته یا محصول جدید بر اساس تقاضای واقعی

### Competitor Intelligence
- صفحه یا سرویس جدید رقیب
- تغییر قیمت، Offer، CTA یا ساختار Landing Page
- Topic cluster جدید
- ابزار رایگان یا Lead Magnet جدید
- محتوایی که سریع در SERP رشد می‌کند
- تغییرات مهم navigation / schema / content format
- شکاف‌هایی که رقبا هنوز پوشش نداده‌اند

### Content / Social
- موضوعات ترند و تازه
- محتوای وبی که قابلیت تبدیل به Reel/Short/Carousel/Thread دارد
- Social postهایی که باید به مقاله یا Landing Page تبدیل شوند
- ویدیوها یا پست‌هایی که engagement یا search discovery خوبی دارند و باید تقویت شوند
- زمان و کانالی که برای هر نوع محتوا بهتر جواب داده است بر اساس داده خودمان

### Conversion / CRO
- صفحات با traffic ولی conversion پایین
- CTA ضعیف یا نامشخص
- فرم طولانی یا خراب
- مسیرهای کاربری که lead را از دست می‌دهند
- فرصت A/B test برای title, hero, CTA, offer و form

### Product / Business Discovery
- سوال‌ها و درخواست‌های تکرارشونده کاربران
- Search demand برای خدمت/محصولی که هنوز ارائه نمی‌کنیم
- مشکلات پرتکرار جامعه هدف که می‌توانند به Tool, SaaS, service package یا downloadable asset تبدیل شوند
- موضوعاتی که هم search demand دارند و هم به قابلیت‌های فعلی کسب‌وکار نزدیک‌اند

## مدل امتیازدهی فرصت

هر Opportunity باید حداقل این فیلدها را داشته باشد:

```yaml
opportunity:
  site: mytel | tehnet
  source: gsc | serp | competitor | trend | social | analytics | crm
  type: seo | content | offer | cro | product | social | technical
  title: "..."
  evidence: "..."
  revenue_potential: 0-100
  commercial_intent: 0-100
  demand: 0-100
  speed_to_result: 0-100
  confidence: 0-100
  effort: 0-100
  risk: 0-100
  priority_score: calculated
  recommended_action: "..."
  approval_tier: auto | review | manual
  owner_agent: "..."
  status: detected | planned | executing | measuring | closed
```

## اصل مهم: پول معیار اصلی است، نه صرفاً Traffic

Growth OS باید تفاوت بین این دو را بفهمد:

- 10,000 بازدید بدون Lead
- 300 بازدید با 20 Lead باکیفیت

پس Dashboard نهایی باید علاوه بر Rank/Traffic، مواردی مثل Lead، تماس، Conversion، ارزش تجاری، هزینه تولید/AI و ROI را نیز نشان دهد؛ هر جا اتصال داده ممکن باشد.

## سطح‌های اتوماسیون

### Auto
کارهای کم‌ریسک و برگشت‌پذیر بعد از تثبیت Pilot، مثل schedule محتوا، گزارش، بعضی internal-linkها یا refreshهای از قبل تأییدشده.

### Review
محتوا، Landing Page، تغییر CTA، Social campaign و PRهای معمولی ابتدا با Review انسانی یا Agent Review چندمرحله‌ای.

### Manual
حذف URL، تغییر canonical گسترده، redirect site-wide، تغییر معماری اصلی، تغییر قیمت/Offer حساس، هزینه تبلیغات و اقدامات مالی بدون تأیید صریح اجرا نشوند.

## خروجی محصول آینده

کاربر سایت و کانال‌هایش را متصل می‌کند؛ سیستم Business Manifest را می‌سازد، Opportunityها را کشف می‌کند، آن‌ها را بر اساس درآمد بالقوه اولویت‌بندی می‌کند، Agent مناسب را اجرا می‌کند و نتیجه را در Revenue Dashboard نشان می‌دهد.

MyTel و Tehran Network دو Pilot اولیه برای ساخت دیتای واقعی این موتور هستند. موفقیت یا شکست هر Opportunity باید ذخیره شود تا مدل تصمیم‌گیری محصول از تجربه واقعی خودمان بهتر شود.
