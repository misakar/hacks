# coding: utf-8

import os
import os.path as path


apis_path = path.abspath(path.join(path.dirname(__file__), '..'))
project_path = path.abspath(path.join(apis_path, '..'))


class hacksConfig(object):

    SECRET_KEY = os.getenv('SECRET_KEY') or 'hacking SECRET_KEY...'
    PROJECT_ROOT_PATH = project_path
    APIS_PATH = apis_path
