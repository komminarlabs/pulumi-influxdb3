# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import errno
import os
from setuptools import setup, find_packages
from setuptools.command.install import install
from subprocess import check_call


VERSION = os.getenv("PULUMI_PYTHON_VERSION", "0.0.0")
def readme():
    try:
        with open('README.md', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "influxdb3 Pulumi Package - Development Version"


setup(name='komminarlabs_influxdb3',
      python_requires='>=3.8',
      version=VERSION,
      description="A Pulumi package for creating and managing InfluxDB V3 resources.",
      long_description=readme(),
      long_description_content_type='text/markdown',
      keywords='pulumi influxdb3 category/database',
      url='https://www.influxdata.com',
      project_urls={
          'Repository': 'https://github.com/komminarlabs/pulumi-influxdb3'
      },
      license='Apache-2.0',
      packages=find_packages(),
      package_data={
          'komminarlabs_influxdb3': [
              'py.typed',
              'pulumi-plugin.json',
          ]
      },
      install_requires=[
          'parver>=0.2.1',
          'pulumi>=3.0.0,<4.0.0',
          'semver>=2.8.1'
      ],
      zip_safe=False)
