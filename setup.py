# -*- coding: utf-8 -*-

"""
setup.py - Package and distribution management

Copyright (c) 2024 Suriyaa Sundararuban
Copyright (c) 2024 Elara Aerospace team
"""

from setuptools import setup, find_packages

setup(
    name='elara-grace',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pylint',
        'numpy',
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'elara-grace = src.main:main'
        ]
    },
    test_suite='tests',
    include_package_data=True,
    package_data={
        '': ['logs/*.log', 'config/*.py']
    },
    author='Suriyaa Sundararuban',
    author_email='suriyaa.sundararuban@elara-aerospace.com',
    description='Rocket Fault Detection and Handling Software by Elara Aerospace',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/elara-aerospace/elara-grace',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    keywords='rocket monitoring student project',
    python_requires='>=3.8'
)
