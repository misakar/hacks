# coding: utf-8

from flask import Blueprint, jsonify, url_for, current_app
from apis.utils import findResources


hacks = Blueprint('hacks', __name__)
hacks.config = {}


@hacks.route('/')
def index():
    _resource_dict = {'root': url_for('hacks.index')}
    _resource_list = findResources(current_app.config['APIS_PATH'])
    for _resource in _resource_list:
        _resource_dict[_resource] = '/api/{}/'.format(_resource)
    return jsonify(
        {
            'hacks': {
                'github': 'https://github.com/neo1218/hacks'
            },
            'meta': {
                'project': current_app.config['PROJECT_ROOT_PATH'],
                'apis': current_app.config['APIS_PATH'],
                'urls': _resource_dict,
            }
        }
    ), 200


from .routes import create, update
