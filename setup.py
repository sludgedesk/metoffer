#!/usr/bin/env python
import setuptools


with open("README.rst", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="MetOffer",
    version="2.0",
    author="Stephen B. Murray",
    author_email="sbm199@gmail.com",
    description="Simple wrapper for the Met Office DataPoint API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sludgedesk/metoffer",
    license="LGPLv3+",
    packages=setuptools.find_packages(),
    package_data={"": ["*.txt", "*.rst"]},
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
    ),
)
