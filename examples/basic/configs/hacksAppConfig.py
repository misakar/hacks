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
apis_path = path.join(project_path, 'blueprints/controllers/')


class hacksAppConfig(object):

    # secret key
    # you'd better store your secret key in environment var
    SECRET_KEY = os.getenv('SECRET_KEY') or 'hacking SECRET_KEY...'

    # the root path of your hacks project:)
    PROJECT_ROOT_PATH = project_path

    # api controllers path
    APIS_PATH = apis_path
