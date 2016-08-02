# coding: utf-8

from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from configs.hacksConfig import hacksConfig
#{=> configs|import <=}


db = SQLAlchemy()


def create_api(configs=[], main=True):
    api = Flask(__name__)

    for config in configs:
        api.config.from_object(config)

    db.init_app(api)

    from .hacks import hacks
    api.register_blueprint(hacks, url_prefix='/api')

    #{=> register|blueprint <=}

    return api


configs = [hacksConfig]
#{=> configs|append <=}
api = create_api(configs)
