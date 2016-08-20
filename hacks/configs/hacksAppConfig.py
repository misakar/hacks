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


# easy import to other file
project_path = path.abspath(path.join(path.dirname(__file__), '..'))
apis_path = path.join(project_path, 'blueprints/api_controllers/')
apps_path = path.join(project_path, 'blueprints/app_controllers/')
models_path = path.join(project_path, 'blueprints/models/')
views_path = path.join(project_path, 'blueprints/templates/')


class hacksAppConfig(object):
    """
    global configuration of hacks app
    """

    # secret key
    ## you'd better store your secret key in environment variable
    SECRET_KEY = os.getenv('SECRET_KEY') or 'hacking your SECRET_KEY..'

    # path finder
    ## the root path of your hacks project:)
    PROJECT_ROOT_PATH = project_path
    ## api controllers path
    APIS_PATH = apis_path
    ## app controllers path
    APPS_PATH = apps_path
    ## models path
    MODELS_PATH = models_path
    ## view templates path
    TEMPLATES_PATH = views_path

    # socketio message queue:
    ## default: redis 6379
    SOCKETIO_MESSAGE_QUEUE = os.getenv('SOCKETIO_MESSAGE_QUEUE', 'redis://')

    # celery configs
    ## learn more
    ## celery: http://www.celeryproject.org/
    ## celery configuration: http://docs.celeryproject.org/en/latest/configuration.html
    CELERY_CONFIGS = {
            'BROKER_URL': 'redis://',
            'CELERY_RESULT_BACKEND': 'redis://',
            'CELERY_ALWAYS_EAGER': False,
    }