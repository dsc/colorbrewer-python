#!python
# -*- coding: utf-8 -*-
import sys, os, re
from os.path import dirname, abspath, join
from setuptools import setup, find_packages

HERE = abspath(dirname(__file__))
readme = open(join(HERE, 'README.md'), 'rU').read()

version_file = open(join(HERE, 'colorbrewer.py'), 'rU')
__version__ = re.sub(
    r".*\b__version__\s+=\s+'([^']+)'.*",
    r'\1',
    [ line.strip() for line in version_file if '__version__' in line ].pop(0)
)


setup(
    name             = 'colorbrewer',
    version          = __version__,
    description      = 'A tool for selecting colorschemes, by Cynthia Brewer',
    long_description = readme,
    url              = 'http://github/dsc/colorbrewer',
    
    author           = 'David Schoonover',
    author_email     = 'dsc@less.ly',
    
    py_modules       = [ 'colorbrewer', ],
    
    # install_requires = [
    #     "bunch  >= 1.0",
    # ],
    
    keywords         = 'colorbrewer color maps tools',
    classifiers      = [
        "Development Status :: 5 - Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Utilities"
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    zip_safe = False,
    license  = "MIT",
)
