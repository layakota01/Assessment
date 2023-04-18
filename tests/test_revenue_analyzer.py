import unittest
from io import StringIO
from unittest.mock import patch
from revenue_analyzer.analyzer import RevenueAnalyzer
from configparser import ConfigParser

class TestRevenueAnalyzer(unittest.TestCase):
    def setUp(self):
        self.config = ConfigParser()
        self.config.read_string("""
            [general]
            chunk_size = 1024
            threads = 4
        """)
        
    @patch('builtins.open')
    def test_process_file(self, mock_open):
        input_data = "referrer\tproduct_list\n" \
                     "https://www.google.com/search?q=test1\tproduct1;1;2;3,product2;1;2;4\n" \
                     "https://www.google.com/search?q=test2\tproduct3;1;2;5,product4;1;2;6\n" \
                     "https://www.google.com/search?q=test1\tproduct5;1;2;3,product6;1;2;1\n" \
                     "https://www.google.com/search?q=test2\tproduct7;1;2;2,product8;1;2;2\n"
        output_data = "Search Engine Domain\tSearch Keyword\tRevenue\n" \
                      "www.google.com\ttest2\t15.0\n" \
                      "www.google.com\ttest1\t11.0\n"

        mock_open.side_effect = [
            StringIO(input_data),
            StringIO(),
            StringIO(output_data)
        ]

        analyzer = RevenueAnalyzer('input_file.tsv', self.config)
        analyzer.process_file()
        analyzer.write_output('output_file.tsv')

        with open('output_file.tsv', 'r') as f:
            result = f.read()

        self.assertEqual(output_data, result)

if __name__ == '__main__':
    unittest.main()

