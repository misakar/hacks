# coding: utf-8
"""
    configs~hacksAppConfig.py
    `````````````````````````

    global configuration of hacks app

        - secret_key
        - project_root_path
        - apis_path
"""

import os
import os.path as path


project_path = path.abspath(path.join(path.dirname(__file__), '..'))
apis_path = path.join(project_path, 'blueprints/api_controllers/')
apps_path = path.join(project_path, 'blueprints/app_controllers/')
models_path = path.join(project_path, 'blueprints/models/')
views_path = path.join(project_path, 'blueprints/templates/')


class hacksAppConfig(object):

    # secret key
    # you'd better store your secret key in environment var
    SECRET_KEY = os.getenv('SECRET_KEY') or 'hacking SECRET_KEY...'

    # the root path of your hacks project:)
    PROJECT_ROOT_PATH = project_path

    # api controllers path
    APIS_PATH = apis_path
    # app controllers path
    APPS_PATH = apps_path
    # models path
    MODELS_PATH = models_path
    # view templates path
    TEMPLATES_PATH = views_path

    # socketio message queue: redis default 6379
    SOCKETIO_MESSAGE_QUEUE = os.getenv('SOCKETIO_MESSAGE_QUEUE', 'redis://')

    # celery configs
    CELERY_CONFIGS = {
            'BROKER_URL': 'redis://',
            'CELERY_RESULT_BACKEND': 'redis://',
            'CELERY_ALWAYS_EAGER': False,
    }
