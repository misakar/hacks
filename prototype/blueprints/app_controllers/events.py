# coding: utf-8
"""
    blueprints~app_controllers~events.py
    `````````````````````````````````````

    server-side socketio

        -- server on/push message to client
"""

from blueprints import socketio
from flask_socketio import emit, send
from flask import request


sockets = []


@socketio.on('message')
def handle_message(msg):
    """
    message: 消息传递事件
    """
    print msg, ' ==> happy hacks hacking'


@socketio.on('connect')
def handle_connected():
    """
    connect: 连接事件
    """
    sockets.append(request.sid)


@socketio.on('disconnect')
def handle_disconnected():
    """
    disconnect: 连接断开事件
    """
    sockets.remove(request.sid)