#!/usr/bin/env bash
set -euo pipefail

STATE=/opt/growth-os/state/sites
LOCK=/opt/growth-os/state/daily-crawl.lock
STAMP=$(date -u +%Y%m%dT%H%M%SZ)

exec 9>"$LOCK"
flock -n 9 || { echo "DAILY_CRAWL_ALREADY_RUNNING"; exit 0; }

run_site() {
  local site_id="$1"
  local url="$2"
  local out="$STATE/$site_id/crawls/$STAMP"
  mkdir -p "$out"
  siteone-crawler \
    --url="$url" \
    --device=mobile \
    --disable-all-assets \
    --workers=2 \
    --max-reqs-per-sec=3 \
    --timeout=10 \
    --max-visited-urls=1000 \
    --output=json \
    --output-json-file="$out/report.json" \
    --output-html-report="$out/report.html" \
    --hide-progress-bar \
    --no-color \
    >"$out/stdout.json"
  echo "$site_id $out"
}

run_site mytel https://mytel.one/
run_site tehnet https://tehnet.ir/

echo DAILY_CRAWL_OK
