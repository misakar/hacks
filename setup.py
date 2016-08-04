# encoding: utf-8

import re
import ast
import hacks.command
from setuptools import setup, find_packages

# version
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('hacks/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


# entry_points
entry_points = {
    'console_scripts':[
        'hack = hacks.command.cli:cli'
    ]
}


setup(
    name='hacks',
    version=version,
    include_package_data=True,
    packages=find_packages(),  # .gitignore
    url='https://github.com/neo1218/hacks',
    license='MIT',
    author='neo1218',
    author_email='neo1218@yeah.net',
    description='dead simple api framework',
    long_description=__doc__,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'click',
    ],
    entry_points=entry_points,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
