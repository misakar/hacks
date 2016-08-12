# coding: utf-8

import os
import os.path as path


project_path = path.abspath(path.join(path.dirname(__file__), '..'))
apis_path = path.join(project_path, 'blueprints/apis')



class apisConfig(object):

    SECRET_KEY = os.getenv('SECRET_KEY') or 'hacking SECRET_KEY...'
    PROJECT_ROOT_PATH = project_path
    APIS_PATH = apis_path
