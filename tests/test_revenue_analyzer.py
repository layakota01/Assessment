import unittest
from io import StringIO
from revenue_analyzer.analyzer import RevenueAnalyzer
from revenue_analyzer.utils import extract_search_info, extract_revenue

class TestRevenueAnalyzer(unittest.TestCase):

    def test_extract_search_info(self):
        url = 'https://www.google.com/search?q=test'
        search_engine, keyword = extract_search_info(url)
        self.assertEqual(search_engine, 'www.google.com')
        self.assertEqual(keyword, 'test')

        url = 'https://search.yahoo.com/search?p=test'
        search_engine, keyword = extract_search_info(url)
        self.assertEqual(search_engine, 'search.yahoo.com')
        self.assertEqual(keyword, 'test')

        url = 'https://www.bing.com/search?q=test'
        search_engine, keyword = extract_search_info(url)
        self.assertEqual(search_engine, 'www.bing.com')
        self.assertEqual(keyword, 'test')

    def test_extract_revenue(self):
        product_list = 'P1;C1;10.0;50.0,P2;C2;5.0;25.0'
        revenue = extract_revenue(product_list)
        self.assertEqual(revenue, 75.0)

        product_list = 'P1;C1;10.0'
        revenue = extract_revenue(product_list)
        self.assertEqual(revenue, 0)

        product_list = ''
        revenue = extract_revenue(product_list)
        self.assertEqual(revenue, 0)

    def test_revenue_analyzer(self):
        input_data = StringIO('''referrer\tproduct_list
https://www.google.com/search?q=test1\tP1;C1;10.0;50.0,P2;C2;5.0;25.0
https://search.yahoo.com/search?p=test2\tP1;C1;10.0;75.0
https://www.bing.com/search?q=test3\tP1;C1;10.0;60.0,P2;C2;5.0;15.0
''')
        analyzer = RevenueAnalyzer(input_data)
        analyzer.parse_file()

        expected_data = {
            ('www.google.com', 'test1'): 75.0,
            ('search.yahoo.com', 'test2'): 75.0,
            ('www.bing.com', 'test3'): 75.0
        }

        self.assertEqual(analyzer.revenue_data, expected_data)

if __name__ == '__main__':
    unittest.main()

