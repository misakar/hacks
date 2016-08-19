# coding: utf-8

import random
# from blueprints.app_controllers.events import clients
from blueprints.app_controllers.events import  sockets
from blueprints import socketio


def render_realtime_msg(event, msg):
    def decorator(f):
        def wraper(*args, **kwargs):
            rv = f(*args, **kwargs)
            # k =  random.randint(0, len(sockets)-1)
            socketio.emit(event, msg, broadcast=True)
            return rv
        return wraper
    return decorator
