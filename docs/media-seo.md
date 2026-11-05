# Image & Video SEO Reference (2026)

**Reviewed:** 2026-08-26  
**Primary sources:** current Google Search Central image/video documentation.

**Scoped review2026-11-04:** the recorded-course attribution section below rechecks Google video guidance and transfers a bounded implementation; it does not refresh every image/media claim on this page.

## 1. Media SEO is retrieval + context + delivery

Images and videos are not isolated ranking objects. Their visibility depends on:

- a crawlable/indexable host page;
- crawlable media URLs;
- useful surrounding context;
- accurate titles/descriptions/alt text/metadata;
- media prominence when the page is actually about the media;
- performance and rendering;
- supported structured data/sitemaps where relevant;
- stable URLs and lifecycle management.

## 2. Image SEO

Primary source: [Google image SEO best practices](https://developers.google.com/search/docs/appearance/google-images)

### Discovery

Use standard HTML image elements for important content where possible:

```html
<img src="/images/widget-installation.webp" alt="Widget mounted on the left rail" width="1200" height="800">
```

Ensure:

- Googlebot can crawl the host page;
- image URLs are not blocked unintentionally;
- images are not available only as CSS backgrounds when they are essential discoverable content;
- lazy loading still exposes discoverable URLs/content;
- image URLs are stable rather than regenerated unnecessarily.

For large image estates, image sitemaps can help discovery.

### Context

Search systems use the page and nearby text to understand an image. Put important images near relevant descriptive content. Avoid generic stock images that add no information when an original diagram/photo would be more useful.

### Alt text

Good `alt` text describes the informative content/function of the image in context.

Good:

```html
<img src="kuka-kr6-axis2.jpg" alt="KUKA KR6 robot arm with axis 2 highlighted">
```

Bad:

```html
<img src="kuka.jpg" alt="robot robot arm industrial robot best robot KUKA robot">
```

For purely decorative images, use an empty alt attribute where appropriate:

```html
<img src="divider.svg" alt="">
```

Alt text primarily serves accessibility and understanding; do not keyword-stuff it.

### File names

Descriptive filenames can add weak contextual clarity for humans/systems, but renaming thousands of already-indexed image URLs without a migration reason can create unnecessary churn. Stable URLs matter.

### Image quality and originality

Use sufficiently high-quality images for the intended display. Original photographs, screenshots, charts and diagrams can provide differentiated information unavailable in commodity stock imagery.

### Preferred image signals

Google's current 2026 image guidance documents several ways publishers can indicate a representative/preferred image, including relevant Schema.org image relationships and `og:image` in applicable contexts. These are selection clues, not guarantees.

## 3. Image performance

Images are frequent LCP bottlenecks.

Practices:

- serve appropriately sized responsive images;
- use modern efficient formats where supported;
- compress without unacceptable quality loss;
- specify dimensions/aspect ratio to reduce CLS;
- lazy-load below-the-fold media;
- do **not** delay the likely LCP/hero image with inappropriate lazy loading;
- use CDN caching thoughtfully;
- minimize redirect chains on image assets.

Example responsive markup:

```html
<img
  src="product-800.webp"
  srcset="product-400.webp 400w, product-800.webp 800w, product-1600.webp 1600w"
  sizes="(max-width: 700px) 100vw, 800px"
  width="1600"
  height="1067"
  alt="Front and side view of Product X">
```

## 4. Image rights and metadata

When useful, expose accurate creator/license/credit information. Do not claim ownership/license rights you do not possess. For original media, preserve a clear first-party source page and useful contextual metadata.

## 5. Video SEO

Primary source: [Google video SEO best practices](https://developers.google.com/search/docs/appearance/video)

### Video watch page principle

For strongest dedicated video eligibility, use a page whose main purpose is watching that video. A video embedded incidentally far below an unrelated article may not be treated as a video watch page.

A good watch page has:

- unique crawlable URL;
- prominent playable video;
- descriptive title/context;
- accessible thumbnail;
- useful supporting text/transcript/chapters where appropriate;
- appropriate `VideoObject` data when eligible;
- no robots/noindex/resource blocks that prevent understanding.

### Stable media and thumbnail URLs

Use stable crawlable thumbnail/video/embed URLs. Do not place required video resources behind authentication, expiring URLs or anti-bot rules that search crawlers cannot access.

### Video structured data

Accurate `VideoObject` markup may describe facts such as:

- `name`;
- `description`;
- `thumbnailUrl`;
- `uploadDate`;
- `duration`;
- `contentUrl` or `embedUrl` where appropriate;
- livestream/clip/key-moment properties when truly applicable.

Follow current Google feature requirements; Schema.org validity alone does not guarantee video-result eligibility.

## 6. Video key moments

When a video has meaningful sections, key-moment information can improve navigation/search presentation when supported. Use real timestamps/labels; do not auto-generate meaningless chapter spam.

## 7. Video transcript

A transcript can improve accessibility and make spoken information available as text. It should be accurate enough to be useful. Do not hide huge keyword-stuffed transcripts solely for bots.

### Recorded-course attribution gate — reviewed2026-11-04

**FACT-OFFICIAL:** [Google's current video guidance](https://developers.google.com/search/docs/appearance/video) calls for video metadata consistent with the actual video. [Video structured data](https://developers.google.com/search/docs/appearance/structured-data/video) describes eligible video content; an incidental video does not turn a written tutorial into a dedicated watch page. These requirements do not override an intentional noindex control.

**Operational policy, not an additional Google requirement:** keep three separate records: source availability, verified teaching coverage, and independent written material. A syllabus, video title, generated transcript, or instructor's intended future lesson cannot alone establish what the recording actually teaches. Record the source ID, review method, real time range when established, reviewer, editorial disposition and relevant URL. Unknown coverage stays UNVERIFIED. Distinguish “no detailed lesson taught” from “no brief mention anywhere”; preserve contradictory evidence rather than flattening it.

For an existing course, repair titles, introductions, lesson order, nearby links and metadata together. Keep valuable written examples, label them as independent material, and retain stable URLs/IDs. A supplement can remain at its existing historical URL with an accurate role label; moving it solely to improve a slug can create needless migration work. Publish timestamps and VideoObject/Clip claims only when supported. A repository input gate is not an admin-save guard or a complete semantic fact checker.

**MEASURED case: TehNet PR76.** Eight existing records were corrected; Queue became a clearly independent supplement instead of episode6 teaching. Seven auto-caption exports and selected passages were examined; full audio/screen verification of all eight sources remains incomplete. The source matrix explicitly separates instructor-reported absence of a detailed Queue lesson from a brief caption reference. Native42 and browser536 checks validated the bounded content migration and rollback, not the underlying completeness of the course review. The published correction is visible at [the Queue supplement](https://tehnet.ir/learn/mikrotik/mtcna/queues-troubleshooting/) and [course archive](https://tehnet.ir/learn/mikrotik/mtcna/); [PR76](https://github.com/DashSaman/TehNet/pull/76) preserves implementation and staged before/after evidence. No ranking, traffic, AI citation, conversion or competitive-parity outcome was measured.

An important WordPress boundary was observed: one target was a `post`, not a `page`. Its update invoked [the core ping/enclosure publication hook](https://developer.wordpress.org/reference/functions/_publish_post_hook/), adding metadata outside the allowed migration. The CLI process temporarily suppressed that hook and restored its original registration in finally; tests checked metadata, cron, repeat, intervening edits and exact rollback. Never widen a field-change guard merely to pass a migration. This is a scoped release lesson, not a recommendation to disable normal site ping behavior globally.

Before declaring completion, distinguish: corrected attribution, full source review, repository/CI input enforcement, admin-edit enforcement, staged release qualification and visible production behavior. None substitutes for another. The [immutable public production receipt](https://github.com/DashSaman/TehNet/blob/a940e2cebbece5027dd3cb8c1daeb03089f5b206/docs/evidence/2026-11-04/production-verification.json) records separate live536 read-only assertions and zero submissions; this does not complete the eight-source review. TehNet's source-review issue and broader commercial issue remain open despite the published correction.

### Later redacted text review is still not audiovisual approval

**OBSERVED — OBS-TN-CAPTION-TEXT-20261104:** All available displayable text in seven hash-pinned automatic caption exports was subsequently read with known private values and credential contexts redacted. Redacted passages were not reviewed; source5.5 still lacked an available export. All eight audiovisual sources remained UNVERIFIED, topic claims and editor approval remained empty, and no chapters/schema/video association was published from this text pass. Three read-only Descript searches found no matching ready transcript; no import, ASR or export was performed. [Immutable bounded review](https://github.com/DashSaman/TehNet/blob/4a060ea642cc282df0c39292ae087b8452e0767b/seo/MTCNA_CAPTION_REVIEW_2026-11-04.fa.md).

**Reusable editorial distinction:** a production script's proposed narration, click highlights and target shot timing are a separate artifact from a transcript, observed teaching coverage or actual recorded duration. Missing real interface captures must stay pending; a conceptual teaching-model screenshot is not a fabricated router screenshot. This distinction is an editorial/evidence control, not a new Google ranking factor.

### Original illustrated workflow and recording scripts —2026-11-04

**FACT-OFFICIAL — GGL-IMAGE-WORKFLOW-20261104:** [Google's current image guidance](https://developers.google.com/search/docs/appearance/google-images), read2026-11-04, supports ordinary img/src, descriptive contextual alt/captions and images adjacent to the relevant text. A full-size link helps the user read small UI labels; it is not an indexing guarantee and does not override noindex.

**OBSERVED — OBS-TN-ILLUSTRATED-LIVE-20261104:** TehNet improved one existing routing owner with four numbered image/option/result steps. Screenshots were captured from the actual browser teaching model; originals, annotation purpose and hashes were preserved. They were explicitly not WinBox captures or actual RouterOS output. Native49/renderer7/site200 and exact restoration preceded PR85 publication fromf1a6764, byte-equal to qualified795c4a1. A further independent live200 checked image bytes, mobile full-size click, real article-to-Lab navigation and the stated exercise results. Fresh backup/checksum/drift/rollback and all protected data/runtime/noindex/payment controls held, zero customer submissions. [Actual receipt and in-context images](https://github.com/DashSaman/TehNet/blob/1367ed96473986e80cf02fecb3e137b99b97b65c/docs/evidence/2026-11-04/illustrated-routing/production-verification.json).

**Reusable implementation lessons:** validate the serialized article through real WordPress before multiplying it. Unsupported inline markup and image serialization were corrected to match the native sanitizer; its guard was not weakened. Nested image-parent creation required a scoped operator fix, journaling only directories actually created and removing only empty owned directories on rollback; a foreign file is preserved. Earlier nonqualified attempts and exact recovery remain separate evidence.

**Editorial handoff:** nine per-recording production files specify tone, narration, screen actions, click highlighting and target shot times. Actual duration/rehearsal/editor approval remain null, and source5.5's proposed new Bridge topic is explicitly not a verified old-video topic. Real WinBox captures and all eight audiovisual source approvals remain open. A script, screenshot count, test count or published page does not establish filmed coverage, a real customer result, search uplift or competitor parity.

### Actual tool capture and desktop independence —2026-11-05

**FACT-OFFICIAL — GGL-IMAGE-NOINDEX-20261105:** Google's [image guidance](https://developers.google.com/search/docs/appearance/google-images) was refreshed2026-11-05: keep instructional screenshots in ordinary HTML img/src with relevant alt and nearby explanation. CSS callout decoration is not the indexed image. Google's [noindex guidance](https://developers.google.com/search/docs/crawling-indexing/block-indexing), read the same day, makes indexing control independent of image/content quality: an accessible page's noindex excludes it when Google crawls and processes that directive. Preserve an intentional launch gate; useful images are not permission to remove it.

**OBSERVED — OBS-TN-WINBOX-STAGING-20261105:** Two existing TehNet article owners gained39 original captures from an actual isolated CHR7.25.1 / WinBox4.5 lab, with bold click labels, proportional CSS callouts and full-size original links. Native migration60/renderer16, browser1590 and exact staging restoration are documented in the [bounded receipt](https://github.com/DashSaman/TehNet/blob/2572709fa18a0d3f8982bad44ede4d4402b34087/docs/evidence/2026-11-05/winbox-core/native-staging.json). These are software acceptance assertions, not independent visitors, recordings or evidence of SEO gains. Production publication is pending owner approval in [PR88](https://github.com/DashSaman/TehNet/pull/88).

**Reusable lessons:** keep original UI pixels/hash/version and label overlays as explanation. Distinguish a GUI form observed from its final action actually executed in CLI; distinguish a synthetic DHCP result from Internet/DNS/hardware acceptance. Test both target rows before writing either and refuse rollback over a newer editor change. Headless browser QA should actually open the full-size picture, verify the served bytes and test callout bounds/RTL/no-JS on mobile. When desktop control is withdrawn, move capture to a separate guest framebuffer; do not change host sleep/lock/display policy to keep the task running.

**Limits:** source recordings still need complete audiovisual review; proposed scripts retain null actual timing/editor approval. Native/staging qualification does not mean deployment, competitive parity, indexing, traffic, conversion or an AI recommendation. This case is a bounded implementation observation; the central71% research baseline and20 dashboard destinations are unchanged.

## 8. Embedded third-party video

If YouTube/Vimeo/etc is embedded on your site:

- the platform video may rank independently;
- your page can still rank if it provides useful original context;
- avoid making your page a thin wrapper around someone else's video;
- include substantive commentary/data/instructions when appropriate.

## 9. Image/video sitemap strategy

Use sitemaps when they materially improve discovery/diagnostics, particularly for large media-heavy sites. Keep sitemap URLs canonical and live. Sitemaps do not guarantee indexing.

## 10. CDN / hotlink considerations

If media is served on a CDN/subdomain:

- ensure crawler access;
- stable HTTPS URLs;
- correct MIME types;
- sensible caching;
- no unauthorized hotlink-protection challenge against search bots;
- ownership/site relationships clear operationally.

## 11. JavaScript-rendered galleries/video

Test raw response and rendered DOM. If an important gallery/video URL appears only after several user interactions, crawlers may not discover it reliably. Prefer crawlable links/media references in initial/rendered HTML.

## 12. Media duplication

Repeated same image/video across many pages is not automatically harmful, but only index/optimize pages that have distinct user value. Avoid creating one near-empty page per image solely to multiply indexable URLs.

## 13. AI-search implications

Google's 2026 generative Search guidance specifically encourages useful multimodal content where it helps users. Original charts/images/video can also give AI/search systems more first-party evidence to reference.

This does **not** mean that adding arbitrary media is an AI ranking factor. Media must contribute information.

## 14. Image audit checklist

- [ ] Host page indexable/canonical.
- [ ] Important image URLs crawlable.
- [ ] Standard image markup exposes the asset.
- [ ] Alt text accurate and not stuffed.
- [ ] Informative images sit near relevant text.
- [ ] Dimensions reserved to reduce CLS.
- [ ] Responsive source sizes appropriate.
- [ ] LCP/hero image prioritized.
- [ ] Below-fold images lazy-loaded appropriately.
- [ ] Original images/charts used where they add value.
- [ ] Image sitemap considered for large media estates.
- [ ] Rights/licensing/credits accurate.

## 15. Video audit checklist

- [ ] Dedicated videos have stable crawlable watch pages where appropriate.
- [ ] Video is prominent/playable.
- [ ] Thumbnail accessible and relevant.
- [ ] Main video resources aren't blocked by robots/WAF/auth.
- [ ] Page has useful descriptive context.
- [ ] Accurate `VideoObject` markup used when eligible.
- [ ] Transcript/chapters provided when useful.
- [ ] Key moments accurate.
- [ ] Video sitemap considered for large libraries.
- [ ] Performance/player scripts do not destroy CWV.
- [ ] Embedded third-party videos are supplemented by original value.

## Primary sources

- https://developers.google.com/search/docs/appearance/google-images
- https://developers.google.com/search/docs/appearance/video
- https://developers.google.com/search/docs/appearance/structured-data/video
- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
