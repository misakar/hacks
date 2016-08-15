# coding: utf-8
"""
    blueprint~__init__.py
    `````````````````````

    hacks app

        - create app
        - setup app configurations
        - initial flask extensions
        - register app blueprint
        - register api blueprint
"""

from flask import Flask, url_for
from flask_socketio import SocketIO
from configs.hacksAppConfig import hacksAppConfig
from configs.usersConfig import usersConfig


socket = SocketIO()


def create_app(configs=[], main=True):

    app = Flask(__name__)

    for config in configs:
        app.config.from_object(config)

    socket.init_app(app)

    from .main import main
    app.register_blueprint(main, url_prefix='/')

    from .api import api
    app.register_blueprint(api, url_prefix='/api')

    return app


configs = [hacksAppConfig]
configs.append(usersConfig)
#{{ append_cfg }}


app = create_app(configs)
