#!/usr/bin/env python
# -*- coding: utf8 -*-
from setuptools import setup, find_packages

NAME = "lambda2color"
# import lambda2color
# VERSION = lambda2color.__version__ # << to change in __init__.py
VERSION = "0.7"

setup(
    name = NAME,
    version = VERSION,
    packages = find_packages(exclude=['contrib', 'docs']),
     author = "Laurent Perrinet INT - CNRS",
    author_email = "Laurent.Perrinet@univ-amu.fr",
    description = "This is a simple library to transform a given light wavelength into the corresponding RGB color.",
    long_description=open("README.md", 'r', encoding='utf-8').read(),
    license = "GPLv2",
    install_requires=['numpy'],
    extras_require={
                'html' : [
                         'matplotlib'
                         'jupyter>=1.0']
    },
    keywords = ('computational neuroscience', 'simulation', 'analysis', 'visualization', 'biologically-inspired', 'computer vision'),
    url = 'https://github.com/laurentperrinet/' + NAME, # use the URL to the github repo
    download_url = 'https://github.com/laurentperrinet/' + NAME + '/tarball/' + VERSION,
    classifiers = ['Development Status :: 3 - Alpha',
                   'Environment :: Console',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Operating System :: POSIX',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Utilities',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.10',
                  ],
     )
