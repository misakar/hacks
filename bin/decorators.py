# coding: utf-8

import os
import functools


def run_in_root(f):
	"""
	'wsgi.py' for command run in root
	"""
	def decorators(*args, **kwargs):
		current_path = os.getcwd()


		
		if os.isdir()
