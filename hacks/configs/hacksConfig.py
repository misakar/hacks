# coding: utf-8

import os
import os.path as path

# path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '...')
apis_path = path.abspath(path.join(path.dirname(__file__), '..'))
project_path = path.abspath(path.join(apis_path, '..'))


class hacksConfig(object):

    SECRET_KEY = os.getenv('SECRET_KEY') or 'hacking SECRET_KEY...'
    # APPLICATION_ROOT = '/api'
    PROJECT_ROOT_PATH = project_path
    APIS_PATH = apis_path
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.getenv("Hacks_SQLALCHEMY_DATABASE_URI") or \
                              'sqlite:///' + path.abspath(
                              path.join(project_path, 'defaultDB.sqlite'))
