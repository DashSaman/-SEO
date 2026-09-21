import unittest
from pathlib import Path
import sys

MODULE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_DIR))

from daily_report import summarize_crawl, render_report


class DailyReportTests(unittest.TestCase):
    def test_crawl_summary_keeps_critical_evidence(self):
        crawl = {
            "stats": {"totalUrls": 19, "countByStatus": {"200": 19}},
            "qualityScores": {"overall": {"score": 7.9}, "categories": [{"code": "seo", "score": 6.1}]},
            "summary": {"items": [
                {"aplCode": "seo-noindex-sitewide", "status": "CRITICAL", "text": "19 of 19 pages are noindex"},
                {"aplCode": "404", "status": "OK", "text": "no 404"},
            ]},
        }
        summary = summarize_crawl(crawl)
        self.assertEqual(summary["total_urls"], 19)
        self.assertEqual(summary["issues"][0]["code"], "seo-noindex-sitewide")
        self.assertEqual(len(summary["issues"]), 1)

    def test_report_contains_impact_check_and_data_gaps(self):
        baseline = {"root": {"status": 200, "elapsed_ms": 900, "final_url": "https://example.com"}, "html": {"title": "Example", "meta_description": None, "canonical": "https://example.com/"}}
        crawl_summary = {"total_urls": 1, "overall_score": 8.0, "category_scores": {"seo": 7.0}, "issues": []}
        text = render_report("example", "Example", baseline, crawl_summary, data_sources={"gsc": False, "ga4": False, "telegram": False})
        self.assertIn("Impact / Time-Waste Check", text)
        self.assertIn("GSC: WAITING_FOR_CONNECTION", text)
        self.assertIn("No production optimization action", text)


if __name__ == "__main__":
    unittest.main()
