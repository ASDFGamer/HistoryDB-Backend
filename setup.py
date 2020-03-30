# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="HistoryDB API",
    author_email="historyDB@christoph-wildhagen.de",
    url="",
    keywords=["Swagger", "HistoryDB API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    This is an API which provides infos about historical events It provides info about events, countries, settlements and persons and also relations between different objects. In next versions it should also add art as an element. 
    """
)
