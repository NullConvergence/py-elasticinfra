import os
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='pyeasticinfrastructure',
    version='1.0',
    description='A small utilty to index infrastructure metrics to elasticsearch',
    author='NullConvergence',
    packages=['py_elasticinfra'],
    install_requires=required
)
