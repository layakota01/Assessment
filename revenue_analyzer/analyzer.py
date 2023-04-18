import threading
from collections import defaultdict
from urllib.parse import urlparse, parse_qs

class RevenueAnalyzer:
    def __init__(self, input_file, config):
        self.input_file = input_file
        self.config = config
        self.revenue_data = defaultdict(float)

    def process_file(self):
        with open(self.input_file, 'r') as f:
            headers = f.readline().strip().split('\t')
            referrer_idx = headers.index('referrer')
            product_list_idx = headers.index('product_list')

            chunk_size = int(self.config.get("general", "chunk_size"))
            threads = int(self.config.get("general", "threads"))

            while True:
                lines = f.readlines(chunk_size)
                if not lines:
                    break

                chunks = self.split_into_chunks(lines, threads)
                thread_list = []

                for chunk in chunks:
                    t = threading.Thread(target=self.process_chunk, args=(chunk, referrer_idx, product_list_idx))
                    t.start()
                    thread_list.append(t)

                for t in thread_list:
                    t.join()

    def process_chunk(self, chunk, referrer_idx, product_list_idx):
        for line in chunk:
            columns = line.strip().split('\t')
            referrer = columns[referrer_idx]
            product_list = columns[product_list_idx]

            search_engine, keyword = self.extract_search_info(referrer)
            if search_engine and keyword:
                revenue = self.extract_revenue(product_list)
                self.revenue_data[(search_engine, keyword)] += revenue

    @staticmethod
    def split_into_chunks(lines, num_chunks):
        avg_chunk_size = len(lines) // num_chunks
        return [lines[i:i + avg_chunk_size] for i in range(0, len(lines), avg_chunk_size)]


    @staticmethod
    def extract_search_info(referrer):
        parsed_url = urlparse(referrer)
        search_engine = parsed_url.hostname
        query_params = parse_qs(parsed_url.query)

        if search_engine in ['www.google.com', 'search.yahoo.com', 'www.bing.com']:
            keyword = query_params.get('q') or query_params.get('p')
            if keyword:
                return search_engine, keyword[0]
        return None, None

    @staticmethod
    def extract_revenue(product_list):
        if not product_list:
            return 0

        products = product_list.split(',')
        revenue = 0
        for product in products:
            attributes = product.split(';')
            if len(attributes) >= 4:
                revenue += float(attributes[3])

        return revenue

    def write_output(self, output_file):
        with open(output_file, 'w') as f:
            f.write('Search Engine Domain\tSearch Keyword\tRevenue\n')
            for (search_engine, keyword), revenue in sorted(self.revenue_data.items(), key=lambda x: x[1], reverse=True):
                f.write(f'{search_engine}\t{keyword}\t{revenue}\n')
