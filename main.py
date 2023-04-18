import argparse
from datetime import datetime
from configparser import ConfigParser
from revenue_analyzer.analyzer import RevenueAnalyzer

def main(args, config):
    analyzer = RevenueAnalyzer(args.input_file, config)
    analyzer.process_file()

    output_filename = f'output/{datetime.now().strftime("%Y-%m-%d")}_SearchKeywordPerformance.tab'
    analyzer.write_output(output_filename)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analyze revenue from search engines and keywords.')
    parser.add_argument('input_file', help='Input file containing hit level data.')
    args = parser.parse_args()

    config = ConfigParser()
    config.read('config.ini')

    main(args, config)
