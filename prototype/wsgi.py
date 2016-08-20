# coding: utf-8
"""
    hacks~wsgi.py
    `````````````

    hacks wsgi app module
"""

from blueprints import create_app
from configs.hacksAppConfig import hacksAppConfig
#{{ configs_import }}


configs = [hacksAppConfig]
#{{ configs_append }}


app = create_app(configs)