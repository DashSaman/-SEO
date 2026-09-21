#!/usr/bin/env python3
import argparse
import glob
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

USER_AGENT = "GrowthOS-IndependentVerify/0.1"


def robots_directives(html, x_robots_header=None):
    values = []
    if x_robots_header:
        values.append(x_robots_header)
    pattern = re.compile(r"<meta[^>]+name\s*=\s*['\"]robots['\"][^>]*>", re.I)
    content_pattern = re.compile(r"content\s*=\s*['\"]([^'\"]*)['\"]", re.I)
    for tag in pattern.findall(html or ""):
        match = content_pattern.search(tag)
        if match:
            values.append(match.group(1))
    directives = set()
    for value in values:
        for part in re.split(r"[,\s]+", value.lower()):
            part = part.strip()
            if part:
                directives.add(part)
    return directives


def fetch_robots(url, timeout=15):
    started = time.monotonic()
    req = Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(req, timeout=timeout) as response:
            body = response.read(1_500_000)
            charset = response.headers.get_content_charset() or "utf-8"
            html = body.decode(charset, errors="replace")
            directives = sorted(robots_directives(html, response.headers.get("X-Robots-Tag")))
            return {
                "url": url,
                "status": response.status,
                "final_url": response.geturl(),
                "directives": directives,
                "noindex": "noindex" in directives,
                "elapsed_ms": round((time.monotonic() - started) * 1000),
                "error": None,
            }
    except Exception as exc:
        return {
            "url": url,
            "status": None,
            "final_url": None,
            "directives": [],
            "noindex": None,
            "elapsed_ms": round((time.monotonic() - started) * 1000),
            "error": f"{type(exc).__name__}: {exc}",
        }


def latest_crawl_report(site_root):
    paths = sorted(glob.glob(str(Path(site_root) / "crawls" / "*" / "report.json")))
    if not paths:
        raise FileNotFoundError(f"No crawl report under {site_root}")
    return Path(paths[-1])


def verify_site(site_id, site_root, timeout=15):
    report_path = latest_crawl_report(site_root)
    crawl = json.loads(report_path.read_text(encoding="utf-8"))
    urls = []
    for result in crawl.get("results", []):
        if str(result.get("status")) == "200" and result.get("url"):
            urls.append(result["url"])
    checked = [fetch_robots(url, timeout=timeout) for url in urls]
    successful = [x for x in checked if x["noindex"] is not None]
    noindex_count = sum(1 for x in successful if x["noindex"])
    return {
        "schema_version": 1,
        "site_id": site_id,
        "verified_at": datetime.now(timezone.utc).isoformat(),
        "source_crawl": str(report_path),
        "checked_count": len(checked),
        "successful_count": len(successful),
        "noindex_count": noindex_count,
        "all_successful_noindex": bool(successful) and noindex_count == len(successful),
        "results": checked,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-id", required=True)
    parser.add_argument("--site-root", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--timeout", type=int, default=15)
    args = parser.parse_args()

    data = verify_site(args.site_id, args.site_root, args.timeout)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "site_id": args.site_id,
        "checked": data["checked_count"],
        "successful": data["successful_count"],
        "noindex": data["noindex_count"],
        "all_successful_noindex": data["all_successful_noindex"],
        "output": str(output),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
