# معماری یکپارچه Content + Social Autopilot

هدف این بخش این است که Growth OS فقط SEO را بررسی نکند؛ بلکه از کشف فرصت تا تولید محتوا، بازاستفاده چندکاناله، انتشار، اندازه‌گیری نتیجه و بهبود بعدی را در یک چرخه واحد مدیریت کند.

## چرخه اصلی

```text
Signals
  ├─ GSC
  ├─ GA4
  ├─ Rank/SERP
  ├─ Website crawl
  ├─ Server/log signals
  ├─ Competitor changes
  ├─ Trends/RSS
  └─ Social performance
       ↓
Opportunity Engine
       ↓
Content Planner
       ↓
Content + Media Production
       ↓
QA / Brand / SEO / Safety Gates
       ↓
Publish
  ├─ Website
  ├─ Telegram
  ├─ Instagram
  ├─ YouTube
  ├─ X
  └─ other supported channels
       ↓
Measure
       ↓
Learn / reprioritize / repeat
```

## اصل مهم: یک محتوا را کورکورانه همه‌جا کپی نکن

یک موضوع مرکزی می‌تواند چند خروجی متفاوت داشته باشد:

- Website: مقاله عمیق، صفحه خدمات، FAQ، Schema و Internal Links
- Telegram: خلاصه کاربردی + CTA + لینک
- Instagram: Carousel/Reel script/caption
- YouTube: ویدیوی آموزشی بلند + Short
- X: Thread فنی کوتاه

Agent باید محتوا را برای Intent و Format هر کانال بازطراحی کند، نه اینکه همان متن را Paste کند.

## اجزای سیستم

### 1. Research / Opportunity Agent
ورودی: GSC، GA4، SERP، Crawl، Competitor، Trends
خروجی: لیست فرصت‌های اولویت‌دار با دلیل، ارزش تجاری و Effort

### 2. Content Strategist Agent
برای هر Opportunity تصمیم می‌گیرد:
- صفحه موجود Refresh شود یا صفحه جدید ساخته شود؟
- نوع محتوا چیست؟
- چه Keyword/Intentهایی پوشش داده شوند؟
- چه Assetهای Social از آن ساخته شوند؟

### 3. Writer / Editor Agent
تولید یا اصلاح:
- مقاله
- Landing page
- Service page
- FAQ
- Title/Meta
- Schema data
- Internal-link copy
- Email/social copy در صورت نیاز

### 4. Media Agent
در فازهای بعدی:
- تصویر
- Thumbnail
- Carousel
- Short/Reel storyboard
- Video script
- Subtitle/transcript

برای Pilot، Media generation باید job-based باشد تا GPU 8GB با Local LLM همزمان اشباع نشود.

### 5. Publisher Agent
کانال‌ها را از طریق Adapter مدیریت می‌کند:
- Website: GitHub PR / SSH deploy / CMS API
- Social: Postiz یا API رسمی هر پلتفرم
- Telegram: Bot/API

### 6. Measurement Agent
بعد از انتشار:
- index/crawl status
- GSC impressions/clicks/CTR/position
- GA4 sessions/conversions
- social reach/clicks/engagement
- uptime/errors

نتیجه دوباره وارد Opportunity Engine می‌شود.

## Approval Tiers

### Low Risk — قابل خودکارسازی بعد از Pilot
- Meta/formatting اصلاحی
- verified internal links
- alt/structured housekeeping
- social scheduling از محتوای Approved
- refreshهای کوچک با QA کامل

### Medium Risk — ابتدا PR/Review
- مقاله جدید
- Landing page
- بازنویسی بزرگ
- FAQ/schema عمده
- انتشار campaign جدید

### High Risk — تأیید انسانی اجباری
- حذف یا تغییر URL
- canonical/redirect سایت‌گسترده
- تغییر navigation/architecture
- تغییرات حساس قیمت/ادعاهای تجاری
- حذف محتوای مهم

## هدف محصول تجاری

هر Site یک Tenant/Workspace منطقی مستقل خواهد داشت:

```text
site.manifest.yaml
brand profile
content policy
channel credentials references
approved claims
conversion goals
competitors
history
cost ledger
result ledger
```

Agent باید فقط اطلاعاتی را از کاربر سؤال کند که از سایت، Repo، منابع متصل یا Manifest نتوانسته با اطمینان پیدا کند.

## Pilotها

### MyTel
Growth Mode:
- Existing site audit
- GSC/GA4 opportunity mining
- content refresh
- lead/conversion focus
- social repurposing

### Tehran Network
Build + Growth Mode:
- discover missing business/site inputs
- ask targeted questions
- complete information architecture/pages/content
- launch QA
- then switch to ongoing Growth Mode

## معیار موفقیت

سیستم نباید فقط تعداد محتوا را زیاد کند. KPIها شامل:
- qualified organic clicks
- conversions/leads
- CTR improvement
- rankings for tracked queries
- content production cost
- time to publish
- social-to-site traffic
- successful autonomous actions vs reverted actions

رتبه صفحه اول Google تضمین نمی‌شود؛ سیستم باید فرصت‌هایی را که از نظر داده سریع‌تر و منطقی‌تر قابل‌برد هستند اولویت‌بندی و آزمایش کند.
