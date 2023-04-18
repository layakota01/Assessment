from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="revenue_analyzer",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool to analyze revenue from search engines and keywords.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/revenue_analyzer",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[
        "argparse",
    ],
    entry_points={
        "console_scripts": [
            "revenue_analyzer=revenue_analyzer.analyzer:main",
        ],
    },
)
