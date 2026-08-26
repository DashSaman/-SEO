# Image & Video SEO Reference (2026)

**Reviewed:** 2026-08-26  
**Primary sources:** current Google Search Central image/video documentation.

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
