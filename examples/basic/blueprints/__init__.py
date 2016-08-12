# coding: utf-8

from flask import Flask, url_for
from flask_socketio import SocketIO
from configs.apisConfig import apisConfig
from configs.usersConfig import usersConfig


socket = SocketIO()


def create_app(configs=[], main=True):

    app = Flask(__name__)

    for config in configs:
        app.config.from_object(config)

    socket.init_app(app)

    from .apis import api
    app.register_blueprint(api, url_prefix='/api')

    #{{ register_bp }}

    return app


configs = [apisConfig]
configs.append(usersConfig)
#{{ append_cfg }}


app = create_app(configs)
