from setuptools import setup, find_packages

setup(
    name="bioseq_analyzer",
    version="0.1.0",
    description="A Python library for genome analysis and motif searching.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "biopython",
        "matplotlib"
    ],
)