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


# clients = []  # all connected clients, may be a huge number
sockets = []   # all auto connected sockets


@socketio.on('send_msg')
def handle_send_msg(msg):
    print "hacks got the message: ", msg


@socketio.on('message')
def handle_message(msg):
    """
    服务器端接受客户端socket发送的信息
    """
    print msg, ' ==> happy hacks hacking'

@socketio.on('connect')
def handle_connected():
    # clients.append(request.namespace)
    sockets.append(request.sid)


@socketio.on('disconnect')
def handle_disconnected():
    # clients.remove(request.namespace)
    sockets.remove(request.sid)
