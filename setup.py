#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('requirements_dev.txt') as requirements_file:
    requirements = requirements_file.read().splitlines()

setup(
    author="Jun Harashima",
    author_email='j.harashima@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="gsch is a tool for handling paper information in a Google Scholar results page.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='gsch',
    name='gsch',
    packages=find_packages(include=['gsch']),
    test_suite='tests',
    url='https://github.com/jun-harashima/gsch',
    version='0.2.3',
    zip_safe=False,
)
