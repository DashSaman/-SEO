# TehNet MVP Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and deploy a production-ready first TehNet MVP on `91.107.138.246` with WordPress/WooCommerce, a custom TehNet presentation/integration layer, the four core journeys, and SEO/operations gates from the `DashSaman/-SEO` operating system.

**Architecture:** Nginx terminates origin HTTP(S) behind Cloudflare and serves WordPress through PHP-FPM with MariaDB. WooCommerce owns commerce; an LMS owns course delivery; focused custom TehNet theme/plugin code owns brand UI, content relationships, inquiry-mode products and site-specific behavior. Production changes are applied only after a host inventory and backup checkpoint.

**Tech Stack:** Ubuntu, Nginx, PHP-FPM, MariaDB, WordPress, WooCommerce, WP-CLI, PHP, CSS/JS, Cloudflare, Git.

**Spec:** `projects/tehnet/docs/superpowers/specs/2026-08-31-tehnet-platform-design.md`

## Global Constraints

- Preferred host is `https://tehnet.ir`; `www.tehnet.ir` must 301 to it.
- Production server is `91.107.138.246`.
- Preserve any existing production workload discovered on the host.
- Never commit credentials, API keys, database passwords or private keys.
- TehNet has four equal primary journeys: Learn, Lab, Services, Shop.
- Dark/light modes are required; dark is the visual anchor.
- Initial content priority is MikroTik/VPN, Linux/Server, Cisco, VoIP, then practical AI for Networking/IT.
- SEO implementation follows `DashSaman/-SEO`; SEO is a launch dependency, not a post-launch task.
- Avoid overlapping WordPress plugins; one owner per concern.
- Purchased files use entitlement-aware limited/expiring delivery; paid video is played in-site without an ordinary direct-download CTA.
- Launch services support direct packages, quote requests and hourly consulting.
- Shop supports direct-purchase stock and inquiry-mode special inventory.
- Launch authentication is email/password plus Google login.
- Iranian gateway first; payment architecture must permit future providers.

---

### Task 1: Production Host Safety Baseline

**Files:**
- Create: `projects/tehnet/ops/BASELINE.md`
- Create on server: `/opt/tehnet/backups/`

**Interfaces:**
- Consumes: production host `91.107.138.246`.
- Produces: dated inventory and backup checkpoint required by all deployment tasks.

- [ ] **Step 1: Collect read-only host inventory**

Run on the server:

```bash
set -euo pipefail
printf '## identity\n'; hostnamectl || true
printf '\n## os\n'; cat /etc/os-release
printf '\n## resources\n'; nproc; free -h; df -hT
printf '\n## listeners\n'; ss -lntup
printf '\n## web/db/php\n'; command -v nginx || true; nginx -v 2>&1 || true; command -v apache2 || true; command -v php || true; php -v 2>/dev/null || true; command -v mariadb || command -v mysql || true
printf '\n## containers\n'; command -v docker && docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Ports}}' || true
printf '\n## web roots\n'; find /var/www /opt -maxdepth 2 -mindepth 1 -type d 2>/dev/null | head -n 200
printf '\n## services\n'; systemctl --no-pager --type=service --state=running
```

Expected: enough evidence to decide whether ports 80/443, MariaDB or `/var/www` are already owned by another workload.

- [ ] **Step 2: Classify deployment mode**

Record exactly one in `ops/BASELINE.md`:

```text
MODE=GREENFIELD
```

or

```text
MODE=COEXIST
```

`GREENFIELD` requires no existing production workload on intended ports/paths. `COEXIST` requires a non-destructive virtual-host/container plan before installation.

- [ ] **Step 3: Create backup directory without overwriting application data**

```bash
sudo install -d -m 0700 /opt/tehnet/backups
```

- [ ] **Step 4: Snapshot relevant existing configuration before mutations**

```bash
STAMP="$(date +%Y%m%d-%H%M%S)"
sudo tar -C / -czf "/opt/tehnet/backups/pre-tehnet-${STAMP}.tgz" \
  etc/nginx etc/apache2 etc/php etc/mysql var/www 2>/dev/null || true
sudo sha256sum "/opt/tehnet/backups/pre-tehnet-${STAMP}.tgz" | sudo tee "/opt/tehnet/backups/pre-tehnet-${STAMP}.sha256"
```

Expected: tarball plus SHA-256 record. If a path is absent, tar may warn; existing data must not be deleted.

- [ ] **Step 5: Commit baseline record**

```bash
git add projects/tehnet/ops/BASELINE.md
git commit -m "ops: record TehNet production baseline"
```

---

### Task 2: WordPress Runtime Foundation

**Files:**
- Create: `projects/tehnet/ops/nginx/tehnet.conf`
- Create: `projects/tehnet/ops/install-wordpress.sh`
- Create: `projects/tehnet/ops/BACKUP_RESTORE.md`
- Server: `/var/www/tehnet/`

**Interfaces:**
- Consumes: Task 1 deployment mode and backups.
- Produces: healthy WordPress origin on the production host.

- [ ] **Step 1: Write shell syntax test first**

```bash
bash -n projects/tehnet/ops/install-wordpress.sh
```

Expected before script exists: FAIL because the file is missing.

- [ ] **Step 2: Create idempotent runtime installer**

The script must install only missing packages, create `/var/www/tehnet`, create a dedicated MariaDB database/user using environment-provided secrets, install WP-CLI, download WordPress, create `wp-config.php`, set salts, and never embed credentials in the repository.

Required environment contract:

```text
TEHNET_DB_NAME
TEHNET_DB_USER
TEHNET_DB_PASSWORD
TEHNET_ADMIN_USER
TEHNET_ADMIN_PASSWORD
TEHNET_ADMIN_EMAIL
```

The script must exit non-zero if any required variable is absent.

- [ ] **Step 3: Re-run shell syntax test**

```bash
bash -n projects/tehnet/ops/install-wordpress.sh
```

Expected: PASS.

- [ ] **Step 4: Validate Nginx config offline**

Deploy `ops/nginx/tehnet.conf` to a staging path and run:

```bash
sudo nginx -t
```

Expected: syntax successful. Configuration must make `tehnet.ir` canonical and redirect `www.tehnet.ir` to the apex host.

- [ ] **Step 5: Install WordPress runtime**

```bash
sudo -E bash projects/tehnet/ops/install-wordpress.sh
```

Expected: WordPress installed at `/var/www/tehnet`, DB reachable, no plaintext secrets added to Git.

- [ ] **Step 6: Verify local origin before Cloudflare**

```bash
curl -fsS -H 'Host: tehnet.ir' http://127.0.0.1/ >/dev/null
curl -sSI -H 'Host: www.tehnet.ir' http://127.0.0.1/ | grep -E '^HTTP/|^Location:'
```

Expected: apex responds successfully; `www` returns a permanent redirect to `https://tehnet.ir/...`.

- [ ] **Step 7: Commit foundation**

```bash
git add projects/tehnet/ops
git commit -m "ops: add TehNet WordPress production foundation"
```

---

### Task 3: TehNet Theme Skeleton and Dark/Light System

**Files:**
- Create: `projects/tehnet/site/wp-content/themes/tehnet/style.css`
- Create: `projects/tehnet/site/wp-content/themes/tehnet/functions.php`
- Create: `projects/tehnet/site/wp-content/themes/tehnet/theme.json`
- Create: `projects/tehnet/site/wp-content/themes/tehnet/front-page.php`
- Create: `projects/tehnet/site/wp-content/themes/tehnet/header.php`
- Create: `projects/tehnet/site/wp-content/themes/tehnet/footer.php`
- Create: `projects/tehnet/site/wp-content/themes/tehnet/assets/css/app.css`
- Create: `projects/tehnet/site/wp-content/themes/tehnet/assets/js/theme-toggle.js`
- Create: `projects/tehnet/site/tests/theme-smoke.php`

**Interfaces:**
- Produces: theme slug `tehnet`, four homepage journey cards, theme preference persisted client-side.

- [ ] **Step 1: Write failing smoke test**

`tests/theme-smoke.php` must assert the theme files exist and that `front-page.php` contains links to `/learn/`, `/labs/`, `/services/`, and `/shop/`.

- [ ] **Step 2: Run test and confirm failure**

```bash
php projects/tehnet/site/tests/theme-smoke.php
```

Expected: FAIL because theme files do not yet exist.

- [ ] **Step 3: Implement minimal theme**

Implement semantic RTL-first markup, responsive header, four equal hero journeys, dark/light tokens, accessible theme toggle, and no placeholder testimonials or fabricated metrics.

- [ ] **Step 4: Run syntax and smoke tests**

```bash
find projects/tehnet/site/wp-content/themes/tehnet -name '*.php' -print0 | xargs -0 -n1 php -l
php projects/tehnet/site/tests/theme-smoke.php
```

Expected: all PASS.

- [ ] **Step 5: Deploy and activate theme**

```bash
rsync -a --delete projects/tehnet/site/wp-content/themes/tehnet/ /var/www/tehnet/wp-content/themes/tehnet/
sudo -u www-data wp --path=/var/www/tehnet theme activate tehnet
```

- [ ] **Step 6: Commit theme skeleton**

```bash
git add projects/tehnet/site
git commit -m "feat: add TehNet responsive dark-light theme"
```

---

### Task 4: TehNet Core Content Model Plugin

**Files:**
- Create: `projects/tehnet/site/wp-content/plugins/tehnet-core/tehnet-core.php`
- Create: `projects/tehnet/site/wp-content/plugins/tehnet-core/src/content-types.php`
- Create: `projects/tehnet/site/wp-content/plugins/tehnet-core/src/relations.php`
- Create: `projects/tehnet/site/wp-content/plugins/tehnet-core/src/product-inquiry.php`
- Create: `projects/tehnet/site/tests/core-smoke.php`

**Interfaces:**
- Produces post types: `tn_lab`, `tn_service`.
- Produces taxonomies used by tutorials/labs/services for subject grouping.
- Produces product meta key `_tehnet_sale_mode` with allowed values `direct` or `inquiry`.
- Produces relationship metadata for tutorial→lab/course/product/service links.

- [ ] **Step 1: Write failing core smoke test**

Test expected file layout, allowed sale-mode constants and registered post-type slugs.

- [ ] **Step 2: Run test and verify failure**

```bash
php projects/tehnet/site/tests/core-smoke.php
```

Expected: FAIL.

- [ ] **Step 3: Implement focused plugin**

Implement only TehNet-specific data/behavior. Do not reimplement WooCommerce ordering, LMS entitlements or generic SEO-plugin functionality.

- [ ] **Step 4: Run PHP syntax and smoke tests**

```bash
find projects/tehnet/site/wp-content/plugins/tehnet-core -name '*.php' -print0 | xargs -0 -n1 php -l
php projects/tehnet/site/tests/core-smoke.php
```

Expected: PASS.

- [ ] **Step 5: Deploy and activate plugin**

```bash
rsync -a --delete projects/tehnet/site/wp-content/plugins/tehnet-core/ /var/www/tehnet/wp-content/plugins/tehnet-core/
sudo -u www-data wp --path=/var/www/tehnet plugin activate tehnet-core
```

- [ ] **Step 6: Commit core model**

```bash
git add projects/tehnet/site
git commit -m "feat: add TehNet lab service and product relationship model"
```

---

### Task 5: WooCommerce, LMS, Membership and Authentication Wiring

**Files:**
- Create: `projects/tehnet/ops/PLUGIN_MATRIX.md`
- Modify through WordPress configuration: WooCommerce/LMS/membership/Google-login plugins selected after license and maintenance validation.

**Interfaces:**
- Consumes: WordPress runtime and TehNet core plugin.
- Produces: checkout, course entitlement, monthly Pro entitlement and Google sign-in.

- [ ] **Step 1: Record one owner per concern in `PLUGIN_MATRIX.md`**

Required rows:

```text
Commerce | WooCommerce
LMS | <selected plugin>
Membership | <selected plugin>
Google Login | <selected plugin>
SEO | <selected plugin or deliberate custom/native choice>
Caching | <selected stack>
Ticketing | <selected plugin/integration>
```

Each selection records version, license, update activity, why chosen and overlapping features disabled.

- [ ] **Step 2: Install WooCommerce and selected components in staging/production**

Use WP-CLI where the plugin is available from WordPress.org; licensed plugins are installed only from legitimately supplied packages/licenses.

- [ ] **Step 3: Configure permalink and currency/checkout baseline**

```bash
sudo -u www-data wp --path=/var/www/tehnet rewrite structure '/%postname%/' --hard
sudo -u www-data wp --path=/var/www/tehnet rewrite flush --hard
```

- [ ] **Step 4: Verify account/checkout endpoints**

Use anonymous and authenticated HTTP/browser tests; confirm no privileged content is exposed to an unauthenticated user.

- [ ] **Step 5: Commit plugin matrix and reproducible configuration notes**

```bash
git add projects/tehnet/ops/PLUGIN_MATRIX.md
git commit -m "docs: lock TehNet WordPress component ownership"
```

---

### Task 6: Initial IA, Pages and SEO Query Map

**Files:**
- Create: `projects/tehnet/seo/BUSINESS_SEARCH_BRIEF.md`
- Create: `projects/tehnet/seo/SERP_MAP.md`
- Create: `projects/tehnet/seo/QUERY_URL_MAP.md`
- Create: `projects/tehnet/seo/LAUNCH_CHECKLIST.md`

**Interfaces:**
- Consumes: `RANKING_FRAMEWORK.md`, `TOP10_PLAYBOOK.md`, service/ecommerce playbooks.
- Produces: one preferred URL per launch intent and a controlled indexable architecture.

- [ ] **Step 1: Define business outcomes**

Record target conversions: paid course/file/lab purchase, Pro subscription, qualified service lead, hourly consultation request and hardware sale/inquiry.

- [ ] **Step 2: Build dated Iran/Persian SERP observations for launch clusters**

At minimum cover MikroTik training, MikroTik service/support, VPN/tunnel education, network support, network equipment/MikroTik purchase and AI-for-network-admin informational demand.

- [ ] **Step 3: Assign each stable intent to one preferred URL**

Reject duplicate synonym pages and fake-location pages.

- [ ] **Step 4: Create WordPress pages matching approved URL map**

Use WP-CLI to create only real launch pages with non-placeholder copy or a controlled `draft` status.

- [ ] **Step 5: Commit SEO artifacts**

```bash
git add projects/tehnet/seo
git commit -m "seo: add TehNet launch query and URL map"
```

---

### Task 7: Seed Sellable MVP Content Without Fabrication

**Files:**
- Create: `projects/tehnet/content/CONTENT_INVENTORY.md`
- Create: `projects/tehnet/content/YOUTUBE_REVIEW.md`

**Interfaces:**
- Produces: reviewed source inventory for target 3 courses, 10 tutorials, 5 labs, ~20 products and service pages.

- [ ] **Step 1: Inventory YouTube videos and available first-party files**

For each video mark `KEEP`, `REFRESH`, or `DROP`, with topic, date/freshness concern, supporting asset availability and intended URL.

- [ ] **Step 2: Publish only evidence-backed pages**

Do not create fake products, fake stock, fake reviews, invented customer cases or thin SEO filler. Missing commercial data remains draft until supplied.

- [ ] **Step 3: Cross-link real assets**

Every published tutorial should expose only relevant relationships among labs, courses, products and services.

- [ ] **Step 4: Commit inventory**

```bash
git add projects/tehnet/content
git commit -m "content: record TehNet launch inventory and YouTube migration"
```

---

### Task 8: Production SEO, Security and Launch Validation

**Files:**
- Create: `projects/tehnet/ops/LAUNCH_REPORT.md`
- Create: `projects/tehnet/ops/ROLLBACK.md`

**Interfaces:**
- Consumes: deployed MVP.
- Produces: explicit GO/NO-GO decision.

- [ ] **Step 1: Validate DNS and canonical hosts**

```bash
dig +short tehnet.ir A
dig +short www.tehnet.ir A
dig +short www.tehnet.ir CNAME
curl -sSI https://tehnet.ir/
curl -sSI https://www.tehnet.ir/
```

Expected: apex resolves to intended Cloudflare path; `www` resolves and permanently redirects to apex.

- [ ] **Step 2: Execute technical SEO launch gate**

Run applicable checks from `SEO_AUDIT_SOP.md` and `checklists/launch.md`: status, crawl/index directives, canonical, rendering, sitemap, internal links, schema truthfulness, mobile, CWV regression risks and analytics.

- [ ] **Step 3: Validate critical user journeys**

Test registration/login, Google login, direct-purchase checkout, inquiry product, protected download entitlement, paid video entitlement, course access, Pro entitlement, service request and support ticket entry.

- [ ] **Step 4: Test backup restoration procedure**

Restore into an isolated temporary DB/path or staging target; do not overwrite production merely to test restore.

- [ ] **Step 5: Write explicit release decision**

`ops/LAUNCH_REPORT.md` must contain one of:

```text
RELEASE=GO
```

or

```text
RELEASE=NO-GO
```

with failed critical checks listed for NO-GO.

- [ ] **Step 6: Commit launch evidence**

```bash
git add projects/tehnet/ops
git commit -m "ops: record TehNet production launch validation"
```
