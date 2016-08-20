# coding: utf-8

"""
	hacks~bin~generate
	``````````````````

	generate a full crud restful api with
	search and pagination stuff.
"""

import click


@click.command()
@click.option('-api', nargs=1)
def generate(api):
	pass