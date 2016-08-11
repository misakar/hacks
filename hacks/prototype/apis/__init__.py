# coding: utf-8

from flask import Flask, url_for
from flask_socketio import SocketIO
from pony import orm
from configs.hacksConfig import hacksConfig
#{=> configs|import <=}


db = orm.Database()
socket = SocketIO()  # server side socketIO


def create_api(configs=[], main=True):
    api = Flask(__name__)

    for config in configs:
        api.config.from_object(config)

    socket.init_app(api)

    from .hacks import hacks
    api.register_blueprint(hacks, url_prefix='/api')

    #{=> register|blueprint <=}

    return api


configs = [hacksConfig]
#{=> configs|append <=}
api = create_api(configs)
