import unittest
from pathlib import Path
import sys

MODULE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_DIR))

from public_baseline import extract_html_signals, sitemap_candidates


class PublicBaselineTests(unittest.TestCase):
    def test_extract_html_signals(self):
        html = '''<html><head>
        <title> Example Site </title>
        <meta name="description" content="Useful description">
        <link rel="canonical" href="https://example.com/page">
        </head><body></body></html>'''
        data = extract_html_signals(html)
        self.assertEqual(data["title"], "Example Site")
        self.assertEqual(data["meta_description"], "Useful description")
        self.assertEqual(data["canonical"], "https://example.com/page")

    def test_sitemap_candidates_keep_origin(self):
        self.assertEqual(
            sitemap_candidates("https://example.com/path?q=1"),
            ["https://example.com/sitemap.xml", "https://example.com/sitemap_index.xml"],
        )


if __name__ == "__main__":
    unittest.main()
