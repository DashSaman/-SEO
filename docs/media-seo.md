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
