# -*- coding: utf-8 -*-

"""
setup.py - Package and distribution management

Copyright (c) 2024 Suriyaa Sundararuban
Copyright (c) 2024 Elara Aerospace team
"""

from setuptools import setup, find_packages

# Read the long description from the README.md file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Read the requirements from the requirements.txt file
with open('requirements.txt', 'r', encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name='elara-grace',
    version='1.0.0',
    packages=find_packages(),
    install_requires=requirements,
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
    long_description=long_description,
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
