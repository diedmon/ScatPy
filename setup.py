# -*- coding: utf-8 -*-

#from distutils.core import setup
from setuptools import setup, find_packages
from git_version import sdist, get_version
import re

with open('README.txt', encoding='utf-8') as f:
    long_description = f.read()

def pep440_compliant_version(version_str):
    """
    Convert a git describe version string (e.g., '0.1.1-10-gccd84ed')
    to a PEP 440-compliant version (e.g., '0.1.1.post10+gccd84ed').
    If already compliant, return as is.
    """
    m = re.match(r'^(\d+\.\d+\.\d+)-(\d+)-g([0-9a-f]+)$', version_str)
    if m:
        base, commits, sha = m.groups()
        return f"{base}.post{commits}+g{sha}"
    return version_str

setup(
    name='ScatPy',
    version=pep440_compliant_version(get_version().decode('utf-8')),
    author='Andrew G. Mark',
    author_email='mark@is.mpg.de',
    packages=['ScatPy'],  # Or use find_packages() if you want to auto-discover
    url='https://github.com/hohlraum/ScatPy',
    platforms='All',
    license='GNU GPLv3',
    description='A Python package for setting up DDSCAT jobs and analysing the results.',
    long_description=long_description,
    cmdclass={"sdist": sdist},
    package_data={'ScatPy': ['profiles/*']},
    package_dir={'ScatPy': 'ScatPy'},
    zip_safe=True,
    install_requires=[
        'numpy', 'scipy', 'matplotlib',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Chemistry',
    ]
)