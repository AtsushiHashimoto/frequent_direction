#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages, Extension
from spectral_embedding_with_frequent_direction import __author__, __version__, __license__

setup(
        name             = 'spectral_embedding_with_frequent_direction',
        version          = __version__,
        description      = '.',
        license          = __license__,
        author           = __author__,
        author_email     = 'ahasimoto@mm.media.kyoto-u.ac.jp',
        url              = 'https://github.com/AtsushiHashimoto/spectral_embedding4large_scale_matrix.git',
        keywords         = 'spectral embedding, frequent direction, matrix sketch, large-scale matrix',
        packages         = find_packages(),
	include_package_data = True,
        install_requires = ['numpy','sklearn'],
        )
