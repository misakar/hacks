# coding: utf-8

"""
	blueprints~app_controllers~views.py
	```````````````````````````````````

	视图:)

"""

from . import main


@main.route('/test/')
def test():
    return "just tell you everything is OK!"