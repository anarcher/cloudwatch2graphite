#!/usr/bin/env python
import sys
import os
import re

from setuptools import setup, find_packages

#To parse package version 
for line in open("cw2graphite/version.py"):
    m = re.match('__version__ = "(.*)"', line)
    if m:
       version = m.group(1)
       break
    else:
        sys.exit("error: can't find version information")

requires = [
    "boto"
]

setup(
    name='cloudwatch2graphite',
    version=version,
    description='This application will output graphite counters for a list of AWS CloudWatch metrics',
    author='msshin',
    url='https://gitlab.enswer.net/devops/cloudwatch2graphite',
    parsers=find_packages(),
    zip_safe=False,
    install_requires=requires,
    entry_points="""
    [console_scripts]
    cw2graphite = cw2graphite.main:main
    """
)
