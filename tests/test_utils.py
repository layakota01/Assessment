import unittest
from urllib.parse import urlparse, parse_qs
from revenue_analyzer.utils import extract_search_info, extract_revenue

class TestUtils(unittest.TestCase):
    def test_extract_search_info(self):
        # Test for Google
        url = "https://www.google.com/search?q=test+query"
        search_engine, keyword = extract_search_info(url)
        self.assertEqual(search_engine, "www.google.com")
        self.assertEqual(keyword, "test query")

        # Test for Yahoo
        url = "https://search.yahoo.com/search?p=test+query"
        search_engine, keyword = extract_search_info(url)
        self.assertEqual(search_engine, "search.yahoo.com")
        self.assertEqual(keyword, "test query")

        # Test for Bing
        url = "https://www.bing.com/search?q=test+query"
        search_engine, keyword = extract_search_info(url)
        self.assertEqual(search_engine, "www.bing.com")
        self.assertEqual(keyword, "test query")

        # Test for non-search engine referrer
        url = "https://www.example.com/"
        search_engine, keyword = extract_search_info(url)
        self.assertIsNone(search_engine)
        self.assertIsNone(keyword)

    def test_extract_revenue(self):
        # Test with valid product list
        product_list = "id1;name1;price1;10,id2;name2;price2;20"
        revenue = extract_revenue(product_list)
        self.assertEqual(revenue, 30)

        # Test with empty product list
        product_list = ""
        revenue = extract_revenue(product_list)
        self.assertEqual(revenue, 0)

        # Test with malformed product list
        product_list = "id1;name1;price1;10,id2;name2;price2;"
        revenue = extract_revenue(product_list)
        self.assertEqual(revenue, 10)

if __name__ == '__main__':
    unittest.main()
