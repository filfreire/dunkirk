"""Packaging settings."""

from setuptools import setup
from codecs import open
from os import path
from dunkirk import __version__

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'dunkirk',
    version = __version__,
    description = 'Export all your Apple iCloud Notes to text files',
    long_decription = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/filfreire/dunkirk',
    author = 'Filipe Freire',
    author_email = 'livrofubia@gmail.com',
    license = 'MIT',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Utilities',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords = 'apple icloud notes text files',
    entry_points = {
        'console_scripts': ['dunkirk = dunkirk.dunkirk:main']
    },
    packages = ['dunkirk'],
    install_requires = [
        'biplist >= 1.0.3',
        'beautifulsoup4 >= 4.6.0',
        'docopt >= 0.6.2'
    ],
)
