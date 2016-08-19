# coding: utf-8

from . import main


@main.route('/test/')
def test():
    return "just tell you everything is OK!"
