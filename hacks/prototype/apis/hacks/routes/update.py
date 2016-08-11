# coding: utf-8

import os
from .. import hacks
from apis.utils import generateModels, findResources
from flask import request, jsonify, current_app


@hacks.route('/', methods=['POST'])
def update_resources():
    if request.method == 'POST':
        rescs = request.args.get('rescs')
        apis_path = current_app.config['APIS_PATH']
        rescs_list = findResources(apis_path)
        config_json_path = os.path.join(apis_path, '%s/config.json' % rescs)
        models_path = os.path.join(apis_path, '%s/models.py' % rescs)

        if rescs in rescs_list:
            generateModels(config_json_path, models_path)
            return jsonify(
                {
                    'msg': 'update %s models' % rescs
                }
            ), 200
        else:
            return jsonify(
                {
                    'msg': 'resources %s not found' % rescs
                }
            ), 404
