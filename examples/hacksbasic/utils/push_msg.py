# coding: utf-8

from blueprints import socketio


def push_msg(msg):
    """broadcast = True"""
    print 'FFF -> ', msg
    socketio.emit(msg)
