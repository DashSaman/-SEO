# TehNet Platform Design

**Date:** 2026-08-31  
**Domain:** `tehnet.ir`  
**Production server:** `91.107.138.246`  
**SEO operating system:** `DashSaman/-SEO`

## Product

TehNet is a unified Persian networking brand with four equal primary journeys:

1. **Learn** — free tutorials and paid courses.
2. **Lab** — downloadable labs, scripts, diagrams, configs and premium assets.
3. **Services** — remote and on-site networking work plus hourly consulting.
4. **Shop** — networking hardware with direct purchase for stocked items and inquiry for special items.

The homepage hero gives all four journeys equal prominence. Content and commerce are deliberately cross-linked so a useful tutorial can lead to a lab, course, product, configuration service or project request.

## Commercial model

- Paid courses: initial price band roughly 300,000–3,000,000 IRR toman-equivalent display values configured in the shop currency model.
- TehNet Pro: monthly subscription only at launch.
- Labs: free, individually paid, and Pro-only tiers.
- Services: fixed-price standard packages, quote-based custom projects, and hourly consulting.
- Shop: mixed real-stock checkout plus price/availability inquiry for special inventory.
- Initial revenue emphasis: courses, files/labs/scripts and Pro; services and hardware increase LTV.

## Audience and content priorities

Audience includes network professionals, companies, beginners and equipment buyers. Initial editorial priority:

`MikroTik/VPN → Linux/Server → Cisco → VoIP → practical AI for Networking/IT`

AI content must be applied and project-driven: network-admin tooling, automation, monitoring, troubleshooting, log analysis, AI helpdesk and network assistants.

## Brand and UX

- TehNet is the primary independent brand.
- Founder/instructor identity is used where it increases trust or teaching credibility, but the site is not a personal-brand-only site.
- Dark/light modes are supported; dark is the visual anchor.
- Visual language should modernize the existing Tehran Network YouTube identity rather than invent an unrelated brand.
- Services/shop copy is formal and trust-oriented; education/labs copy is technical, clear and friendlier.
- Mobile experience is first-class.

## Core conversion loop

`YouTube / Google → Tutorial → Lab/File → Course/Pro → Product → Service`

A tutorial page can contain video, article, commands, screenshots/diagram, downloadable assets, related lab/course, related hardware and service CTA.

## Information architecture

### Primary routes

- `/` — homepage
- `/learn/` — academy hub
- `/tutorials/` — free tutorial hub
- `/labs/` — labs and files
- `/services/` — services hub
- `/shop/` — equipment store
- `/pro/` — monthly membership
- `/account/` — customer account
- `/support/` — support/tickets
- `/about/`
- `/contact/`

### Initial Learn taxonomy

- MikroTik & VPN/Tunnel
- Linux & Servers
- Cisco & Routing/Switching
- VoIP & Call Center
- AI for Network/IT

### Service architecture

Follow the service-business playbook:

`Home → Service hub → Individual service → Use case → Genuine location/service area → Case study/resource/contact`

Initial service landing pages:

- MikroTik configuration
- Network support
- VPN/tunneling
- Server/Linux
- VoIP/call center
- Virtualization
- Firewall/security
- Hourly consulting

Remote service is available nationwide. On-site work covers Tehran and nearby cities by arrangement; do not create fake city-office pages.

### Ecommerce architecture

Follow the ecommerce playbook:

`Home → Department → Category → Subcategory → Product`

Initial categories prioritize MikroTik, Cisco, routing/switching, Wi-Fi/access points, SFP/transceivers, racks/cabling and related network equipment. Product pages should connect specs to practical selection guidance, tutorials, labs and optional configuration service.

## Account and authentication

Launch authentication:

- email/password
- Google login

Account areas:

- courses
- downloads/labs
- Pro status
- orders/invoices
- support tickets
- service requests

## Payment

- Launch with Iranian payment gateway integration.
- Payment layer must not hard-code a single provider so international payment can be added later without redesigning commerce data.

## Protected digital delivery

- Purchased downloadable files use expiring/limited download links.
- Paid video is streamed in-site without exposing a normal direct-download link.
- No DRM claims; protection is deterrence/access-control rather than a guarantee against copying.

## Support

Launch channels:

- account ticketing
- Telegram/WhatsApp quick contact
- contact form/email

Live chat is deferred.

## YouTube migration

Legacy Tehran Network videos are reviewed, not blindly imported. Useful content is retained and updated; obsolete/weak content is excluded or refreshed. Each retained video should gain a useful site page with original supporting content and clear next actions.

## SEO and search requirements

`DashSaman/-SEO` governs planning and validation from the start. SEO is not a post-build phase.

Mandatory workflow:

`Business → Market/SERP → Feasibility → Query/Intent mapping → Architecture → Technical → Brief → Content → On-page → Entity/Trust → Structured Data → Internal Links → Authority → AI Search → Launch → Validation → Measurement → Iteration`

Required constraints:

- one preferred page per coherent stable intent;
- no synonym/location doorway page factories;
- crawlable finite architecture;
- canonical URL policy defined before publishing at scale;
- genuine product/service facts and reviews only;
- structured data must match visible content;
- technical launch gate includes HTTPS/status/crawl/index/canonical/rendering/internal links/schema/mobile/performance/analytics;
- AI search work remains provider-specific and evidence-based;
- success is tied to qualified traffic, leads and revenue rather than plugin scores.

## Technical architecture

Launch stack:

- Ubuntu host at `91.107.138.246`
- Nginx
- PHP-FPM
- MariaDB
- WordPress
- WooCommerce
- one selected LMS
- custom TehNet theme and small focused custom plugin(s)
- object/page caching where validated
- Cloudflare in front of the origin

Avoid a large pile of overlapping WordPress plugins. Prefer one owner per concern. Custom TehNet code owns brand components, cross-linking/content metadata and product/service/lab integrations that are part of the differentiator.

## DNS/canonical policy

- Preferred canonical host: `https://tehnet.ir`
- `www.tehnet.ir` redirects permanently to `https://tehnet.ir`
- Root A currently points to `91.107.138.246` through Cloudflare.
- A DNS record for `www` still needs to exist before the redirect can work globally.

## Launch scope

The first public release should be professional and sellable without waiting for every future capability:

- homepage
- Academy/Learn
- Tutorials
- Labs
- Services
- Shop
- Pro landing/membership wiring
- account/checkout
- support/ticket entry
- initial target: 3 courses, 10 useful tutorials, 5 labs, ~20 products and core service pages

Content counts are launch targets, not permission to publish placeholder or thin content.

## Security and operations

- preserve any pre-existing production workload discovered on the host;
- make a before-change inventory and backup before destructive migration;
- least-privilege DB/app credentials;
- secrets never committed to Git;
- regular DB/uploads/config backups;
- HTTP security headers validated for WordPress compatibility;
- WordPress/plugin/theme updates controlled and tested;
- admin access hardened and rate-limited at the edge/origin where appropriate;
- health/backup/restore procedure documented.

## Success criteria for MVP

MVP is ready only when:

1. Core journeys work on desktop and mobile.
2. A user can register/login, purchase an eligible product/digital item and access entitled content.
3. A service lead can be submitted and support entry is available.
4. Shop supports both direct-purchase and inquiry-mode products.
5. Dark/light themes are coherent.
6. Priority pages pass technical SEO launch checks.
7. Analytics and Search Console-ready measurement hooks are present.
8. Production is served over HTTPS with canonical redirect policy working.
9. Backups and a rollback path exist.
