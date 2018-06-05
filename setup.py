#!/usr/bin/env python
from setuptools import setup
import os

setup(
    name = 'simplewaze',
    version = 1.0,
    author = 'Rodrigo Ancavil',
    author_email = 'rancavil@gmail.com',
    description = "Get route times",
    license = 'GNU GPL v3',
    keywords = ['waze', 'route', 'times'],
    packages = ['simplewaze','config',]
)
