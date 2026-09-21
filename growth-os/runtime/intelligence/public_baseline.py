#!/usr/bin/env python3
import argparse
import json
import time
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit, urlunsplit
from urllib.request import Request, urlopen

USER_AGENT = "GrowthOS-PublicMonitor/0.1 (+site-owner-monitoring)"


class SignalParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.title_parts = []
        self.meta_description = None
        self.canonical = None

    def handle_starttag(self, tag, attrs):
        attrs = {k.lower(): v for k, v in attrs if k}
        tag = tag.lower()
        if tag == "title":
            self.in_title = True
        elif tag == "meta" and (attrs.get("name") or "").lower() == "description":
            self.meta_description = attrs.get("content")
        elif tag == "link" and "canonical" in (attrs.get("rel") or "").lower().split():
            self.canonical = attrs.get("href")

    def handle_endtag(self, tag):
        if tag.lower() == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title_parts.append(data)


def extract_html_signals(html):
    parser = SignalParser()
    parser.feed(html or "")
    title = " ".join(" ".join(parser.title_parts).split()) or None
    description = " ".join((parser.meta_description or "").split()) or None
    return {"title": title, "meta_description": description, "canonical": parser.canonical}


def origin(url):
    parts = urlsplit(url)
    return urlunsplit((parts.scheme, parts.netloc, "", "", ""))


def sitemap_candidates(url):
    base = origin(url).rstrip("/")
    return [f"{base}/sitemap.xml", f"{base}/sitemap_index.xml"]


def timestamped_output_path(output_dir, collected_at=None):
    stamp = collected_at or datetime.now(timezone.utc).isoformat()
    dt = datetime.fromisoformat(stamp.replace("Z", "+00:00")).astimezone(timezone.utc)
    return Path(output_dir) / dt.strftime("%Y%m%dT%H%M%SZ.json")


def fetch(url, timeout=20, body_limit=2_000_000):
    started = time.monotonic()
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,*/*;q=0.8"})
    try:
        with urlopen(req, timeout=timeout) as response:
            body = response.read(body_limit)
            charset = response.headers.get_content_charset() or "utf-8"
            text = body.decode(charset, errors="replace")
            return {
                "ok": True,
                "status": response.status,
                "final_url": response.geturl(),
                "content_type": response.headers.get("Content-Type"),
                "elapsed_ms": round((time.monotonic() - started) * 1000),
                "body": text,
                "bytes_sampled": len(body),
            }
    except HTTPError as exc:
        return {"ok": False, "status": exc.code, "final_url": exc.geturl(), "elapsed_ms": round((time.monotonic() - started) * 1000), "error": str(exc)}
    except URLError as exc:
        return {"ok": False, "status": None, "final_url": url, "elapsed_ms": round((time.monotonic() - started) * 1000), "error": str(exc.reason)}
    except Exception as exc:
        return {"ok": False, "status": None, "final_url": url, "elapsed_ms": round((time.monotonic() - started) * 1000), "error": f"{type(exc).__name__}: {exc}"}


def probe(url, timeout=20):
    result = fetch(url, timeout=timeout, body_limit=200_000)
    result.pop("body", None)
    return result


def collect(site_id, url, timeout=20):
    root = fetch(url, timeout=timeout)
    body = root.pop("body", "")
    html_signals = extract_html_signals(body) if root.get("ok") else {"title": None, "meta_description": None, "canonical": None}
    base = origin(root.get("final_url") or url).rstrip("/")
    robots = probe(f"{base}/robots.txt", timeout=timeout)
    sitemaps = [{"url": candidate, **probe(candidate, timeout=timeout)} for candidate in sitemap_candidates(base)]
    return {
        "schema_version": 1,
        "site_id": site_id,
        "requested_url": url,
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "root": root,
        "html": html_signals,
        "robots": {"url": f"{base}/robots.txt", **robots},
        "sitemaps": sitemaps,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-id", required=True)
    parser.add_argument("--url", required=True)
    output_group = parser.add_mutually_exclusive_group(required=True)
    output_group.add_argument("--output")
    output_group.add_argument("--output-dir")
    parser.add_argument("--timeout", type=int, default=20)
    args = parser.parse_args()

    data = collect(args.site_id, args.url, args.timeout)
    output = Path(args.output) if args.output else timestamped_output_path(args.output_dir, data["collected_at"])
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"site_id": args.site_id, "status": data["root"].get("status"), "final_url": data["root"].get("final_url"), "output": str(output)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
