from setuptools import setup, find_packages

setup(
    name="thrift-data-pipeline",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "scrapy"
    ]
)
