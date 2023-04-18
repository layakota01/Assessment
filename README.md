# Revenue Analyzer

Revenue Analyzer is a Python-based tool for analyzing revenue generated from search engines and keywords. The tool reads hit-level data from an input file, extracts search engine and keyword information, calculates revenue, and outputs a summary file.

## Table of Contents

	Directory structure
	Features
	Installation
	Configuration
	Usage
	Support
	License

## Directory structure

	revenue_analyzer/
	    ├── revenue_analyzer
	    │   ├── __init__.py
	    │   ├── analyzer.py
	    │   └── utils.py
	    ├── config.ini
	    ├── main.py
	    └── requirements.txt

## Features

	Extracts search engine and keyword information from hit-level data
	Calculates revenue for each search engine and keyword combination
	Outputs a summary file containing search engine domain, keyword, and revenue
	Efficient handling of large input files using multi-threading and memory optimization
	Customizable configuration

## Installation

1. Clone the repository:

	git clone https://github.com/yourusername/revenue_analyzer.git

2. Change to the project directory:

	cd revenue_analyzer

3. Install the required packages:

	pip install -r requirements.txt

## Configuration

1. Edit the config.ini file to set the desired configuration:

	[input]
	delimiter = \t


	[output]
	directory = output
	delimiter = \t
	extension = tab


	delimiter: The delimiter used in the input and output files (e.g., tab, comma)
	directory: The directory where output files will be saved
	extension: The file extension for output files (e.g., tab, csv)

2. Save the config.ini file.

## Usage

Run the Revenue Analyzer:

	python main.py <input_file>

Replace <input_file> with the path to your input file containing hit-level data.

The output file will be saved in the specified output directory with a name like YYYY-MM-DD_SearchKeywordPerformance.tab.

## Support

For any questions or issues, please contact the repository owner or open a new issue on the GitHub repository.

## License
