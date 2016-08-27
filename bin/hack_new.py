# coding: utf-8

"""
	hacks~bin~new
	`````````````

	new a hacks scanffold project.
"""

import os
import shutil
import click


bin_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
prototype = os.path.abspath(os.path.join(bin_path, 'prototype'))


@click.route()
@click.argument('project_name')
def new():
	"""
	new a prototype hacks project
	"""
		