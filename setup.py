__author__ = 'Edinei'
from distutils.core import setup

setup(
    # Application name:
    name="pydaruma",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Edinei Colli",
    author_email="colli.edinei@gmail.com",

    # Packages
    packages=["pydaruma"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    #url="http://pypi.python.org/pypi/pydaruma_v010/",
    url="http://github.com/edineicolli/pydaruma",

    #
    license="GNU GPL",
    description="Wrapper for Daruma Framework library.",

    long_description=open("README.md").read(),

    # Dependent packages (distributions)
    install_requires=[
    ],
)
