import unittest
from pathlib import Path
import sys

MODULE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_DIR))

from independent_verify import robots_directives


class IndependentVerifyTests(unittest.TestCase):
    def test_robots_directives_from_meta_and_header(self):
        html = "<html><head><meta name='robots' content='noindex, follow'></head></html>"
        directives = robots_directives(html, "noarchive, nosnippet")
        self.assertEqual(directives, {"noindex", "follow", "noarchive", "nosnippet"})

    def test_empty_robots_is_empty(self):
        self.assertEqual(robots_directives("<html></html>", None), set())


if __name__ == "__main__":
    unittest.main()
