# encoding: utf-8

from setuptools import setup, find_packages
import hacks.command

# version
version = '0.10'


# entry_points
entry_points = {
    'console_scripts':[
        'hack = hacks.command.cli:cli'
    ]
}


setup(
    name='hacks',
    version=version,
    packages=find_packages(),
    url='https://github.com/neo1218/hacks',
    license='MIT',
    author='neo1218',
    author_email='neo1218@yeah.net',
    description='dead simple api framework',
    long_description=__doc__,
    zip_safe=False,
    include_package_data=True,
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
