from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='agenda',
    version='1.0.1',
    license='MIT',

    description='Module for pretty task logging',
    long_description=long_description,

    url='https://github.com/jonhoo/python-agenda',
    author='Jon Gjengset',
    author_email='jon@thesquareplanet.com',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: System :: Logging',
        'Environment :: Console',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='logging console pretty-print',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['future', 'termcolor'],
)
