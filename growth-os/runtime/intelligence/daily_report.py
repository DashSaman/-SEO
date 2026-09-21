#!/usr/bin/env python3
import argparse
import glob
import json
from datetime import datetime, timezone
from pathlib import Path

ISSUE_STATUSES = {"CRITICAL", "WARNING", "NOTICE"}


def summarize_crawl(crawl):
    scores = crawl.get("qualityScores") or {}
    categories = scores.get("categories") or []
    issues = []
    for item in (crawl.get("summary") or {}).get("items", []):
        if str(item.get("status", "")).upper() in ISSUE_STATUSES:
            issues.append({
                "code": item.get("aplCode"),
                "severity": str(item.get("status", "")).upper(),
                "text": item.get("text", ""),
            })
    return {
        "total_urls": (crawl.get("stats") or {}).get("totalUrls"),
        "status_counts": (crawl.get("stats") or {}).get("countByStatus", {}),
        "overall_score": (scores.get("overall") or {}).get("score"),
        "category_scores": {c.get("code"): c.get("score") for c in categories if c.get("code")},
        "issues": issues,
    }


def source_line(name, connected):
    return f"- {name}: {'CONNECTED' if connected else 'WAITING_FOR_CONNECTION'}"


def render_report(site_id, site_name, baseline, crawl_summary, data_sources=None, previous_baseline=None):
    data_sources = data_sources or {}
    root = baseline.get("root") or {}
    html = baseline.get("html") or {}
    now = datetime.now(timezone.utc).isoformat()
    issues = crawl_summary.get("issues") or []
    criticals = [x for x in issues if x["severity"] == "CRITICAL"]
    warnings = [x for x in issues if x["severity"] == "WARNING"]
    notices = [x for x in issues if x["severity"] == "NOTICE"]

    lines = [
        f"# {site_name} — Growth OS Daily Report",
        "",
        f"Generated: `{now}`",
        f"Site ID: `{site_id}`",
        "",
        "## Executive Summary",
        f"- Public HTTP status: `{root.get('status')}`",
        f"- Final URL: `{root.get('final_url')}`",
        f"- Sample response latency: `{root.get('elapsed_ms')} ms`",
        f"- Crawled HTML URLs: `{crawl_summary.get('total_urls')}`",
        f"- SiteOne overall score: `{crawl_summary.get('overall_score')}`",
        f"- Critical findings: `{len(criticals)}`; warnings: `{len(warnings)}`; notices: `{len(notices)}`",
        "",
        "## Current On-Page Snapshot",
        f"- Title: `{html.get('title')}`",
        f"- Meta description detected: `{'yes' if html.get('meta_description') else 'no'}`",
        f"- Canonical: `{html.get('canonical')}`",
        "",
        "## Data Sources",
        source_line("GSC", bool(data_sources.get("gsc"))),
        source_line("GA4", bool(data_sources.get("ga4"))),
        source_line("Telegram", bool(data_sources.get("telegram"))),
        "",
        "## Technical Findings",
    ]

    if not issues:
        lines.append("- No CRITICAL/WARNING/NOTICE findings in the current crawl summary.")
    else:
        for item in issues:
            lines.append(f"- **{item['severity']}** `{item['code']}` — {item['text']}")

    lines += [
        "",
        "## What Growth OS Did Today",
        "- Collected live public-site health evidence.",
        "- Ran a rate-limited technical crawl and stored machine-readable JSON + HTML evidence.",
        "- Classified current findings without making an unverified production change.",
        "",
        "## Verification / Failures / Retries",
        "- Collector/crawler results above come from live HTTP requests; missing external data sources are explicitly marked instead of fabricated.",
        "",
        "## Impact / Time-Waste Check",
        "- No production optimization action has been executed in this report cycle yet, so no ranking/traffic/revenue improvement is claimed.",
        "- Current value delivered: verified baseline + issue detection + repeatable monitoring state.",
        "- Search/conversion impact cannot be judged until GSC/GA4 are connected and a post-change measurement window exists.",
        "- Paid generative API cost: `0` by policy.",
        "",
        "## Before / After State",
    ]

    if previous_baseline:
        prev_root = previous_baseline.get("root") or {}
        lines.append(f"- Previous status/latency: `{prev_root.get('status')}` / `{prev_root.get('elapsed_ms')} ms`")
        lines.append(f"- Current status/latency: `{root.get('status')}` / `{root.get('elapsed_ms')} ms`")
        lines.append("- Latency samples are monitoring signals, not a statistically valid performance conclusion by themselves.")
    else:
        lines.append("- First daily baseline: no earlier comparable daily snapshot is available yet.")

    lines += [
        "",
        "## Next Cycle",
        "- Re-check public health automatically.",
        "- Re-run technical crawl on the 24-hour schedule.",
        "- Prioritize independently verified critical issues first.",
        "- Add GSC/GA4 evidence when direct free connectors are authorized.",
        "",
        "## Anti-Vanity Rule",
        "This report does not treat article count, change count, raw traffic, or a crawler score alone as business success. Qualified search visibility, leads, conversions and revenue become the primary outcome metrics when those data sources are connected.",
        "",
    ]
    return "\n".join(lines)


def latest_json(pattern):
    paths = sorted(glob.glob(pattern))
    if not paths:
        raise FileNotFoundError(pattern)
    return Path(paths[-1])


def previous_json(pattern):
    paths = sorted(glob.glob(pattern))
    return Path(paths[-2]) if len(paths) >= 2 else None


def load_json(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-id", required=True)
    parser.add_argument("--site-name", required=True)
    parser.add_argument("--state-root", default="/opt/growth-os/state/sites")
    parser.add_argument("--output-dir")
    args = parser.parse_args()

    site_root = Path(args.state_root) / args.site_id
    baseline_pattern = str(site_root / "baselines" / "*.json")
    crawl_pattern = str(site_root / "crawls" / "*" / "report.json")
    baseline_path = latest_json(baseline_pattern)
    prev_path = previous_json(baseline_pattern)
    crawl_path = latest_json(crawl_pattern)

    baseline = load_json(baseline_path)
    previous = load_json(prev_path) if prev_path else None
    crawl = summarize_crawl(load_json(crawl_path))
    sources = {"gsc": False, "ga4": False, "telegram": False}
    text = render_report(args.site_id, args.site_name, baseline, crawl, sources, previous)

    output_dir = Path(args.output_dir) if args.output_dir else site_root / "daily"
    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / (datetime.now(timezone.utc).date().isoformat() + ".md")
    output.write_text(text, encoding="utf-8")
    print(json.dumps({"site_id": args.site_id, "report": str(output), "baseline": str(baseline_path), "crawl": str(crawl_path)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
