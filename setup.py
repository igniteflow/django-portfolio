#!/usr/bin/env python
"""
Installation script:

To release a new version to PyPi:
- Ensure the version is correctly set in django-portfolio.__init__.py
- Run: python setup.py sdist upload
"""

from setuptools import setup, find_packages

VERSION = (0, 0, 2, 'alpha', 0)

def get_short_version():
    return '%s.%s' % (VERSION[0], VERSION[1])

def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        # Append 3rd digit if > 0
        version = '%s.%s' % (version, VERSION[2])
    if VERSION[3:] == ('alpha', 0):
        version = '%s pre-alpha' % version
    elif VERSION[3] != 'final':
        version = '%s %s %s' % (version, VERSION[3], VERSION[4])
    return version


setup(name='django-portfolio',
    version=get_version().replace(' ', '-'),
    url='https://igniteflow@github.com/igniteflow/django-portfolio.git',
    author="Phil Tysoe",
    author_email="philtysoe@gmail.com",
    description="A simple set of abstract models and functionality to speed up the development of a portfolio type site in Django 1.3+",
    long_description="A simple set of abstract models and functionality to speed up the development of a portfolio type site in Django 1.3+",
    keywords="Django, portfolio, blog, artist",
    license='BSD',
    platforms=['linux'],
    packages=find_packages(exclude=["*.tests"]),
    install_requires=[
        'django-extensions==0.7.1',
        'django-tagging==0.3.1',
        'django-tinymce==1.5.1b2'
        ],
    # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=['Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: Unix',
                 'Programming Language :: Python']
)
