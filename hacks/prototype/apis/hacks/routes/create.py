# coding: utf-8

import os
from flask import jsonify, request, current_app
from apis.hacks import hacks
from apis.functions import findResources, updateJson, generateModels


@hacks.route('/', methods=['POST'])
def create_field():
    apis_path = current_app.config['APIS_PATH']
    recs_list = findResources(apis_path)
    config_json_path = os.path.join(apis_path, 'resources/config.json')
    models_path = os.path.join(apis_path, 'resources/models.py')

    if request.method == 'POST':
        rescs = request.args.get('rescs')
        field_name = request.get_json().get('field')
        field_type = request.get_json().get('type')
        if rescs in recs_list:
            updateJson(field_name, field_type, config_json_path)
            generateModels(config_json_path, models_path)
            return jsonify(
                {
                    'msg': 'create a field',
                    'resource': rescs
                }
            ), 201
        else:
            return jsonify(
                {
                    'msg': 'resource not found'
                }
            ), 404
