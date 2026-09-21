# توپولوژی Agentهای Growth OS — Free / Local First

## اصل
هدف، یک تیم Agent خودکار برای SEO، Revenue، رقبا، محتوا، CRO، سایت و Social است. مالک Routine Production را انجام نمی‌دهد و فقط گزارش/پیشنهاد/نتیجه را بررسی می‌کند.

## Orchestrator
**Activepieces Community Core**
- Scheduler و workflow engine
- صف Jobها، Retry، Dead-letter و اجرای 24/7
- اتصال Agentها و گزارش‌ها

## Local AI Brain
**LiteLLM + Ollama**
- Gateway واحد OpenAI-compatible برای تمام Agentها
- Primary: Qwen3.5 9B روی RTX 3070 8GB
- Fast fallback: Qwen3.5 4B
- Paid generative APIs disabled
- GPU jobs serialized تا LLM/Image/Video همزمان VRAM را پر نکنند

## Search Intelligence Agent
داده‌ها:
- Google Search Console
- GA4
- Bing Webmaster در صورت اتصال
- Crawl/Indexability
وظایف:
- query/page opportunity detection
- CTR gaps
- content decay
- cannibalization
- page-1/near-page-1 opportunities
- commercial-intent clustering

## Technical SEO Agent
ابزارها:
- SiteOne Crawler
- Crawl4AI
- Lighthouse CI
وظایف:
- crawlability/indexability
- status codes / redirects / canonicals
- metadata/schema/internal links
- performance/Core Web Vitals signals
- regression detection

## Revenue Opportunity Agent
Signalهای SEO + Analytics + Lead + Conversion + Competitor را ترکیب می‌کند و فرصت‌ها را با Revenue potential، intent، demand، speed، confidence، effort و risk اولویت‌بندی می‌کند.

## Competitor & Trend Scout
ابزارها/منابع:
- changedetection.io
- RSSHub / RSS / public feeds
- competitor website crawl/diff
- public trend/news/search signals
خروجی:
- صفحات/خدمات/Offerهای جدید رقبا
- Topic/format trends
- فرصت‌های محتوایی و تجاری قابل اقدام

## Content Strategy Agent
- topic/entity cluster planning
- search intent matching
- brief + outline + FAQ + schema plan
- refresh-vs-new-page decision
- جلوگیری از mass low-value content

## Website Execution Agent
- branch/PR based edits
- page/content/schema/internal-link changes
- tests + QA + deploy adapters
- destructive/high-impact actions fail-closed

## CRO / Revenue Agent
- CTA/form/funnel analysis
- high-traffic low-conversion detection
- offer/landing-page experiments
- before/after conversion measurement

## Content + Social Agent
- web article/service/FAQ
- Telegram-specific post
- Instagram caption/carousel/reel script
- YouTube/Short plan
- X/thread where usable
- no blind copy-paste across channels

## Local Media / Video Agent
- script + hook + storyboard
- ComfyUI/local image generation
- FramePack/LTX-class local video workflow where hardware allows
- local Persian TTS
- subtitle/edit/render with FFmpeg/renderer
- automatic QA and upload/scheduling through free official connectors where available

## Reporting & Learning Agent
هر سایت مستقل:
- Action log در Repo
- Daily report در Repo + Telegram
- Weekly 7-day optimization review
- Before/After impact ledger
- failed/retried/rolled-back work
- cost/compute/time accounting
- feed results back to Opportunity scoring

## Ranking objective
هدف عملیاتی افزایش سهم Queryهای تجاری منتخب در صفحه اول و رشد Qualified Traffic/Lead/Revenue است. هیچ Rank/Page-1/Top-10 نتیجه‌ای تضمین نمی‌شود؛ تصمیم‌ها و ادامه/rollback فقط با داده و Verification انجام می‌شوند.
