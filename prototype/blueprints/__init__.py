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

import os
from flask import Flask, url_for
from flask_socketio import SocketIO
from celery import Celery


socketio = SocketIO()
celery = Celery()
# Import celery task so that it is registered with the Celery workers
from tasks.post_resources import post_resources
from tasks.run_ctx_request import run_ctx_request


def create_app(configs=[], main=True):

    app = Flask(__name__)

    for config in configs:
        app.config.from_object(config)

    socketio.init_app(app, message_queue=app.config['SOCKETIO_MESSAGE_QUEUE'])
    celery.conf.update(hacksAppConfig.CELERY_CONFIGS)

    from .app_controllers import main
    app.register_blueprint(main, url_prefix='/')

    from .api_controllers import api
    app.register_blueprint(api, url_prefix='/api')

    return app