#!/usr/bin/env python
from os import path
from setuptools import setup, find_packages


def read(name):
    return open(path.join(path.dirname(__file__), name)).read()

setup(
    name='django-basic-stats',
    description=("django-basic-stats is a simple traffic statistics application. "
                 "It show latest referrer, google queried terms or overall hits count. "
                 "It also provides optional logging and statistics for mobile devices."),
    long_description=read("README.md"),
    version='0.1',
    maintainer="Piotr Malinski",
    maintainer_email="riklaunim@gmail.com",
    install_requires=(
        'django',
    ),
    packages=find_packages(),
)
