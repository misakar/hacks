# coding: utf-8

from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from configs.hacksConfig import hacksConfig
#{==> import_configs <==}


db = SQLAlchemy()


def create_api(configs=[], main=True):
    api = Flask(__name__)

    for config in configs:
        api.config.from_object(config)

    db.init_app(api)

    from .hacks import hacks
    api.register_blueprint(hacks, url_prefix='/api')

    #{==> register_blueprint <==}

    return api


configs = [hacksConfig]
#{==> configs_append <==}
api = create_api(configs)
