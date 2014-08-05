#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='cloudwatch2graphite',
    version='0.0.0',
    description='This application will output graphite counters for a list of AWS CloudWatch metrics',
    author='msshin',
    url='https://gitlab.enswer.net/devops/cloudwatch2graphite',
    parsers=find_packages(),
    zip_safe=False,
    entry_points="""
    [console_scripts]
    cloudwatch2graphite = cloudwatch2graphite.main:main
    """
)
