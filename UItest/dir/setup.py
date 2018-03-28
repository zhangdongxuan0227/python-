#!/usr/bin/python
# -*- coding: utf-8 -*-
_author__ = 'zhangxingchen'

from setuptools import setup

setup(
    name='tickets',
    py_modules=['tickets', 'station'],
    install_requires=['requests', 'docopt', 'prettytable', 'colorama'],
    entry_points={
        'console_scripts': ['tickets=tickets:cli']
    }
)

