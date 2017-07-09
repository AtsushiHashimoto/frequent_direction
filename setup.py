#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages, Extension
from frequent_direction import __author__, __version__, __license__

setup(
        name             = 'frequent_direction',
        version          = __version__,
        description      = '.',
        license          = __license__,
        author           = __author__,
        author_email     = 'ahasimoto@mm.media.kyoto-u.ac.jp',
        url              = 'https://github.com/AtsushiHashimoto/frequent_direction.git',
        keywords         = 'spectral embedding, frequent direction, matrix sketch, large-scale matrix',
        packages         = find_packages(),
	include_package_data = True,
        install_requires = ['numpy','sklearn'],
        )
