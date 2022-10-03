#!/usr/bin/python
# -*- coding: utf-8 -*-
# DATE: 2022/7/28
# Author: Irfan TOOR

"""
Utility classes
"""

from typing import List

from util.downloader import Downloader
from util.cache import Cache
from util.setting import PROJECT, VERSION

__author__: str = 'Irfan TOOR'
__name__: str = PROJECT
__email__: str = 'email@irfantoor.com'
__version__: str = '.'.join(map(str, VERSION))

__all__: List[str] = [
    'Downloader', 'Cache'
]
