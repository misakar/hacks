# coding: utf-8

from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
# from config import config
from configs.resourcesConfig import resourcesConfig


db = SQLAlchemy()


def create_api(configs=[], main=True):
    api = Flask(__name__)

    for config in configs:
        api.config.from_object(config)

    db.init_app(api)

    from .hacks import hacks
    api.register_blueprint(hacks, url_prefix='/api')

    from .resources import resources
    api.register_blueprint(resources, url_prefix='/api/resources')

    return api


api = create_api([resourcesConfig])
