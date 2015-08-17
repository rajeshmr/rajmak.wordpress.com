from setuptools import setup, find_packages
import os
version = os.environ.get("GO_PIPELINE_LABEL", "1.0")
setup(
	name="wordcount-job",
	version=version,
	packages=find_packages(),
	zip_safe=True,
	install_requires=[
		'dumbo'
	]
)
