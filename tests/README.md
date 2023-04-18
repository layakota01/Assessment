# Revenue Analyzer - Unit Tests

This README provides an overview of the unit tests for the Revenue Analyzer application.

## Prerequisites

	Python 3.6 or later
	Install the required packages listed in requirements.txt by running pip install -r requirements.txt.
	
## Running the tests

	To run the unit tests, use the following command from the root directory of the project:
	python -m unittest discover tests
	This command will discover and run all test cases in the tests directory.

## Test Coverage

	The unit tests cover the following functionalities of the Revenue Analyzer:

	Utility functions for parsing search engine and keyword information from the referrer URL, and extracting revenue from the product list.
	The RevenueAnalyzer class methods for parsing the input file, updating the revenue data, and writing the output file.
	Edge cases and input validation to ensure the application handles different types of input data correctly.

## Structure of the Unit Tests

	The tests directory contains the following files:

	__init__.py: An empty file indicating that the tests directory is a Python package.
	test_revenue_analyzer.py: Contains the unit tests for the RevenueAnalyzer class and utility functions.

	The test_revenue_analyzer.py file includes test cases for the following functionalities:

	Test the extract_search_info utility function with various referrer URLs.
	Test the extract_revenue utility function with various product lists.
	Test the parse_file method of the RevenueAnalyzer class for correct data parsing and revenue calculation.
	Test the write_output method of the RevenueAnalyzer class for correct output file generation.

## Adding New Tests

	To add new tests, simply create new test methods in the test_revenue_analyzer.py file, or create a new test file in the tests directory following the same structure. Make sure to prefix the test method names with test_ so that the unittest framework can discover and run them.

	When adding new functionality to the Revenue Analyzer application, make sure to also update the unit tests accordingly to maintain test coverage.
