# Growth OS — Autonomous Content, Video, Publishing & Reporting Design

**Date:** 2026-09-21  
**Status:** WRITTEN SPEC — awaiting owner review  
**Applies to:** MyTel, Tehran Network, and future tenant sites  
**Primary constraint:** owner should not be required to write, edit, render, upload, schedule, or manually publish routine content.

---

# بخش فارسی

## 1) هدف

Growth OS باید از یک سیستم SEO به یک سیستم یکپارچه رشد و درآمد تبدیل شود که به‌صورت 24/7:

- فرصت‌های SEO، مارکتینگ، محتوا، شبکه‌های اجتماعی، محصول/خدمت و رقابت را کشف کند؛
- برای هر فرصت تصمیم بگیرد چه اقداماتی بیشترین ارزش تجاری را دارند؛
- متن، تصویر، ویدیو، صدا، زیرنویس و نسخه‌های مخصوص هر شبکه را تولید کند؛
- محتوا را بدون درگیر کردن مالک در ادیت و آپلود، پس از عبور از QA داخلی منتشر کند؛
- نتیجه را با GSC، GA4، SERP، Analytics شبکه‌های اجتماعی، Lead و Conversion اندازه بگیرد؛
- از نتیجه یاد بگیرد و صف کار بعدی را اصلاح کند؛
- تمام اقدامات و نتایج قابل‌تحلیل را برای هر سایت در Repo همان سایت و Telegram Channel همان سایت ثبت کند.

مالک سیستم در حالت عادی فقط گزارش‌ها را می‌خواند، عملکرد را بررسی می‌کند و در صورت تمایل پیشنهاد یا جهت‌گیری جدید می‌دهد.

## 2) مدل تعامل مالک

### Owner Review-Only Mode — حالت پیش‌فرض

مالک برای عملیات روزمره لازم نیست:

- مقاله بنویسد؛
- Caption بنویسد؛
- سناریو بسازد؛
- Video Edit کند؛
- Voiceover ضبط کند؛
- Thumbnail بسازد؛
- محتوا را دستی Upload کند؛
- زمان انتشار را انتخاب کند؛
- هر Job را Approve کند.

سیستم باید مستقل کار کند و خروجی خود را گزارش دهد.

### پیشنهاد مالک

مالک می‌تواند هر زمان دستور سطح بالا بدهد، مانند:

- «این ماه روی فروش سرویس X تمرکز کن»
- «برای این مقاله یک Reel ترند بساز»
- «روی Lead بیشتر از Traffic تمرکز کن»
- «این شخصیت را بیشتر استفاده کن»
- «این سبک را دیگر استفاده نکن»

این Feedback باید در Brand/Strategy Memory همان سایت اعمال شود.

## 3) سطح خودکارسازی و Guardrail

هدف Autopilot کامل است، اما سیستم نباید برای رسیدن به خودکارسازی کارهای مخرب یا غیرقابل‌بازگشت را کورکورانه اجرا کند.

### Auto-execute

بعد از Pilot و عبور از QA داخلی:

- تولید/Refresh مقاله و FAQ؛
- Internal linking تأییدشده؛
- Meta/Title/Description؛
- Social post؛
- Carousel؛
- Reel/Short؛
- Thumbnail؛
- Voice/Subtitles؛
- Schedule/Publish؛
- اصلاحات کم‌ریسک سایت؛
- ایجاد Branch/PR/Test برای تغییرات کد؛
- گزارش و Measurement.

### Fail-closed / Report-only برای عملیات پرریسک

بدون دستور صریح مالک، سیستم نباید خودکار:

- URL مهم را حذف کند؛
- Sitewide Redirect/Canonical خطرناک اعمال کند؛
- Navigation اصلی را حذف یا بازطراحی مخرب کند؛
- Pricing/Financial claims حساس را جعل یا تغییر دهد؛
- محتوای مهم را پاک کند؛
- Fake review، fake engagement، PBN، cloaking، hacked links یا روش‌های مشابه اجرا کند.

در این موارد سیستم باید پیشنهاد را در گزارش ثبت کند و ادامه عملیات روزمره متوقف نشود.

## 4) جداسازی هر سایت

هر سایت یک Workspace مستقل دارد:

```text
sites/<site-id>/
  site.manifest.yaml
  brand/
  strategy/
  content/
  reports/
  campaigns/
  experiments/
  assets/
```

`site.manifest.yaml` شامل Reference به موارد زیر است و Secret خام داخل Git ذخیره نمی‌شود:

- Domain
- Git repository
- deployment method
- analytics source IDs
- GSC property
- Telegram reporting channel reference
- social channel references
- brand voice
- approved claims
- prohibited claims
- conversion goals
- competitors
- content languages
- autonomy policy

MyTel و Tehran Network هیچ Credential، Queue، Campaign یا Log خصوصی مشترکی ندارند.

## 5) معماری کلان

```text
Signals
  ├─ GSC / GA4
  ├─ SERP / Rankings
  ├─ Site Crawl / Logs
  ├─ Competitors
  ├─ Trends / RSS / Public signals
  ├─ Social analytics
  └─ Leads / Conversions
          ↓
Revenue Opportunity Engine
          ↓
Planner / Campaign Brain
          ↓
Task Queue
  ├─ SEO tasks
  ├─ Website tasks
  ├─ Content tasks
  ├─ Social tasks
  └─ Media/video tasks
          ↓
Local AI + Automation Workers
          ↓
QA / Brand / Fact / Duplicate / Safety Gates
          ↓
Publish / PR / Deploy
          ↓
Measure
          ↓
Learn + Reprioritize
```

## 6) Core Platform

Phase 2 باید Control Plane دائمی را ایجاد کند:

- workflow/orchestration engine؛
- PostgreSQL برای state/history/results؛
- Redis برای queue/cache/locks؛
- monitoring/health checks؛
- secret references؛
- backup jobs؛
- per-site job isolation؛
- retry/dead-letter queues؛
- audit ledger.

برای محصول آینده، Core باید تا حد ممکن به ابزارهای self-hosted با مجوز مناسب تجاری متکی باشد. هر ابزار قبل از Productization وارد License Ledger می‌شود.

## 7) Local AI Policy

**Paid generative API is disabled by default.**

```text
Text           → Local model
Embedding      → Local
Image          → Local
Video          → Local
TTS            → Local
Transcription  → Local
Editing        → Local
```

API رسمی رایگان/دارای quota برای اتصال و انتشار روی سرویس‌هایی مانند Search Console، Analytics، YouTube یا شبکه اجتماعی مجاز است؛ این با «API تولید محتوای پولی» متفاوت است.

اگر یک پلتفرم برای Publish نیازمند API پولی باشد، آن Connector به‌صورت پیش‌فرض غیرفعال می‌ماند تا سیاست محصول تغییر کند. سیستم نباید برای دور زدن محدودیت پلتفرم از Credential یا روش غیرمجاز استفاده کند.

## 8) GPU Scheduler

RTX 3070 Laptop با 8GB VRAM منبع مشترک است. Workerها نباید هم‌زمان VRAM را اشباع کنند.

```text
Text job → release GPU
Image job → release GPU
Video job → release GPU
Lip-sync job → release GPU
```

Queue باید:

- VRAM-heavy jobs را serialize کند؛
- priority داشته باشد؛
- timeout/retry داشته باشد؛
- دمای/خطای GPU و OOM را ثبت کند؛
- Job را بدون گم شدن state دوباره اجرا کند.

## 9) Content Factory

Agentهای منطقی:

- Opportunity Researcher
- Content Strategist
- SEO Writer
- Editor/Fact Checker
- Internal Link Agent
- Schema Agent
- Conversion Copy Agent
- Social Repurposing Agent

یک Source Topic باید خروجی channel-specific بسازد، نه Copy/Paste یکسان.

## 10) Trend + Video Factory

### Trend Scout

سیستم به‌صورت دوره‌ای Patternهای قابل‌استفاده را کشف می‌کند:

- Hook format
- storytelling structure
- video duration
- character style
- pacing
- caption pattern
- topic momentum
- competitor/public-content patterns
- performance history of our own posts

هدف تقلید عینی از یک ویدیوی شخص دیگر نیست؛ سیستم Pattern موفق را استخراج و اجرای Original مخصوص برند تولید می‌کند.

### Creative Director

برای هر Topic تصمیم می‌گیرد:

- Brand Character یا Trend Character؛
- Tone؛
- Hook؛
- Scene count؛
- CTA؛
- 9:16 / 1:1 / 16:9؛
- مدت مناسب؛
- نوع صدا/زیرنویس/موسیقی.

### Video pipeline

```text
Topic / Article / Offer
  ↓
Trend pattern
  ↓
Hook + Script
  ↓
Storyboard + Shot list
  ↓
Character / Visual generation
  ↓
Short scene generation
  ↓
Persian/local TTS
  ↓
Lip-sync when required
  ↓
Subtitle / Music / SFX / Logo / CTA
  ↓
Automated edit + render
  ↓
QA
  ↓
Platform-specific encode
  ↓
Auto-publish
```

ویدیوهای طولانی Diffusion یک‌تکه تولید نمی‌شوند. Sceneهای کوتاه تولید و سپس با renderer/FFmpeg مونتاژ می‌شوند تا مصرف GPU و زمان قابل‌کنترل باشد.

### Character Mode

سیستم هر دو حالت را پشتیبانی می‌کند:

1. **Brand Characters** — شخصیت‌های تکرارشونده برند؛
2. **Trend Characters** — شخصیت/Style جدید مناسب Trend.

در حالت `AUTO`، Agent بر اساس Topic، Brand و داده Performance انتخاب می‌کند. Trend Character موفق می‌تواند با ثبت در Brand Memory به شخصیت تکرارشونده تبدیل شود.

## 11) Publishing

Publisher Adapterها باید از API/روش رسمی و مجاز استفاده کنند.

کانال‌های هدف اولیه:

- Website
- Telegram
- Instagram
- YouTube / Shorts
- X در صورت وجود روش قابل‌قبول با سیاست هزینه پروژه
- سایر کانال‌های قابل اتصال

Publish Job فقط پس از QA موفق اجرا می‌شود. شکست Publish باید retry شود و اگر retry budget تمام شد به Dead Letter Queue برود و در گزارش همان سایت ثبت شود؛ مالک نباید مجبور شود Upload دستی انجام دهد.

## 12) QA بدون دخالت روزمره مالک

پیش از Publish، سیستم حداقل این Gateها را اجرا می‌کند:

- factual/claim check against approved sources;
- brand voice check;
- duplicate/sameness check;
- spelling/format check;
- link validation;
- unsafe/destructive action check;
- copyright/originality check where applicable;
- platform dimensions/codec validation;
- subtitle presence/readability;
- CTA validation;
- prohibited-claim check.

اگر QA شکست بخورد، Job به Agent اصلاح برمی‌گردد. مالک وارد چرخه Edit نمی‌شود.

## 13) گزارش‌دهی دوگانه برای هر سایت

این Requirement اجباری است.

### A. Repo Report

برای هر سایت:

```text
reports/
  YYYY/
    MM/
      DD-daily.md
      actions.jsonl
      incidents.md
  weekly/
  monthly/
```

Repo فقط اطلاعات قابل‌انتشار/غیرSecret را نگه می‌دارد. Raw analytics، token، email، phone، private customer data یا Secret در Git ثبت نمی‌شود.

هر Action مهم حداقل شامل:

- timestamp
- action id
- agent
- reason/opportunity
- asset/page/channel
- change summary
- publish/deploy result
- measurement target
- rollback/reference
- cost/time/GPU duration where useful

### B. Telegram Channel Report

هر سایت Channel گزارش مستقل دارد.

Telegram نباید با صدها Log کم‌ارزش Spam شود. سه سطح پیام داریم:

1. **Action Stream:** اقدام مهم مثل انتشار، deploy، campaign، incident؛
2. **Daily Digest:** کارهای انجام‌شده + اعداد کلیدی + مشکلات + برنامه بعدی؛
3. **Weekly/Monthly Executive Report:** فرصت‌ها، ROI/Lead/SEO/Social trend، برنده‌ها/بازنده‌ها و پیشنهاد استراتژیک.

هر پیام در صورت وجود به Report/Commit/PR مرتبط لینک می‌دهد.

## 14) Measurement & Learning

سیستم برای هر محتوا/کمپین باید قبل از اجرا Success Metric تعریف کند.

نمونه‌ها:

- qualified organic clicks
- lead/call/form conversion
- CTR
- target query movement
- social reach
- saves/shares
- video completion
- site clicks from social
- cost per produced asset
- GPU minutes
- autonomous success rate
- reverted/failed action rate

Traffic به تنهایی KPI نهایی نیست؛ Revenue/Lead/Conversion وزن بیشتری دارد.

## 15) Failure Handling

هر Workflow دائمی باید:

- idempotent باشد؛
- retry policy داشته باشد؛
- duplicate publish جلوگیری کند؛
- checkpoint داشته باشد؛
- dead-letter queue داشته باشد؛
- health status گزارش کند؛
- بعد از Windows/WSL restart قابل بازیابی باشد.

اگر سیستم local worker خاموش شود، Jobهای قابل‌صف باید از بین نروند و پس از برگشت worker ادامه پیدا کنند.

## 16) Security & Commercialization

- Secret خام در Git ممنوع؛
- PAT/tokenهای لو‌رفته باید rotate شوند؛
- هر Tenant isolation منطقی مستقل دارد؛
- Audit trail حفظ می‌شود؛
- License Ledger برای ابزارها/مدل‌ها اجباری است؛
- قبل از فروش محصول، licensing/redistribution/SaaS terms هر dependency بررسی می‌شود؛
- داده مشتری یا analytics خصوصی وارد Repo عمومی نمی‌شود.

## 17) معیار پذیرش

این زیرسیستم زمانی «کامل» محسوب می‌شود که برای حداقل یک سایت Pilot بتواند بدون ادیت یا Upload دستی مالک:

1. Opportunity را پیدا کند؛
2. Topic/Campaign را انتخاب کند؛
3. مقاله یا Asset متنی بسازد/بهبود دهد؛
4. نسخه Social بسازد؛
5. حداقل یک Video Short را از Script تا Render کامل تولید کند؛
6. QA خودکار انجام دهد؛
7. روی کانال مجاز منتشر کند؛
8. گزارش Repo تولید کند؛
9. گزارش Telegram تولید کند؛
10. نتیجه را اندازه بگیرد و در اولویت‌بندی بعدی استفاده کند؛
11. پس از restart بدون از دست دادن state ادامه دهد.

---

# English Summary / Canonical Requirements

## Purpose

Growth OS must operate as an autonomous, revenue-oriented growth system. Routine content writing, editing, rendering, uploading, scheduling and publishing must not require the owner. The owner primarily reviews reports and optionally gives strategic feedback.

## Mandatory capabilities

- continuous SEO/market/competitor/trend/social/revenue opportunity discovery;
- local-first text/image/video/voice generation;
- automated script, storyboard, character, scene, voice, subtitle, edit and render pipeline;
- brand-character and trend-character modes with automatic selection;
- automated QA and repair loop before publish;
- official/authorized publishing adapters;
- per-site workspace isolation;
- durable queues, retries, dead-letter handling and restart recovery;
- per-site Git repository reporting and per-site Telegram reporting;
- measurement feedback into the next opportunity cycle;
- no raw secrets or private analytics data in public Git repositories;
- license ledger before commercial productization.

## Default owner interaction

Normal operations are report-only for the owner. Destructive or high-risk actions fail closed and are reported rather than forcing the owner into a daily approval workflow.

## Zero-paid-generative-API policy

Generative text, image, video, TTS, transcription and editing are local-first. Official free/quota APIs may be used for analytics and publishing. Paid generative APIs are disabled unless the owner explicitly changes policy later.

## Reporting contract

Every site has:

- machine-readable local audit history;
- non-secret report artifacts in its repository;
- Telegram action notifications;
- daily digest;
- weekly/monthly executive summary.

## Completion criteria

A pilot must autonomously discover an opportunity, create text/social/video assets, QA them, publish through an authorized channel, report the work to repo and Telegram, measure results, learn from them, and recover from restarts without manual editing/uploading by the owner.
