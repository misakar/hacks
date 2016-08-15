# coding: utf-8
"""
    controllers~api.py
    ``````````````````

    api blueprint

        - define api blueprint
        - add api index rule
"""

from flask import Blueprint, jsonify, url_for, current_app
from utils import findResources


api = Blueprint('api', __name__)


@api.route('/')
def index():
    _resource_dict = {'root': url_for('api.index')}
    _resouce_list = findResources(current_app.config['APIS_PATH'])
    for _resource in _resouce_list:
        _resource_dict[_resource] = '/api/{}/'.format(_resource)
    return jsonify(
            {
                'hacks': {
                    'github': 'https://github.com/neo1218/hacks'
                },
                'meta': {
                    'project': current_app.config['PROJECT_ROOT_PATH'],
                    'controllers': current_app.config['APIS_PATH'],
                    'apis': _resource_dict,
                }
            }
    ), 200


# from .users import create, delete, read, update, search
from .controllers.users import create, update, read, delete, search
