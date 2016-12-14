#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='tb-api',
    version='1.0.3',
    description='Simple Flask API',
    author='Thong Dong',
    author_email='thongdong7@gmail.com',
    url='https://github.com/thongdong7/tb-api',
    packages=find_packages(exclude=["build", "dist", "tests*"]),
    install_requires=[
        'six==1.10.0',
    ],
    extras_require={
        'client': [
            'bravado~=8.4.0',
        ],
        'server': [
            'click==6.6',
            'flask~=0.11.1',
            'tb-ioc~=0.2.3',
            'flask-cors~=3.0.2',
        ]
    },
    entry_points={
        'console_scripts': [
            'api=tb_api.cli:cli_start'
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: Python Software Foundation License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    include_package_data=True,
)
