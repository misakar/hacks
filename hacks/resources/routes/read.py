# coding: utf-8

import json
from .. import resources
from flask import jsonify, request, current_app
from ..models import Resources


@resources.route('/', methods=['GET'])
def get_resources():
    resources = Resources.query.all()

    page = request.args.get('page') or '1'
    current_page = int(page)
    per_page = current_app.config['RESOURCES_PAGINATION_PERPAGE']

    if per_page != 0:
        return json.dumps(
            [resource.to_json() for resource in \
             resources[per_page*(current_page-1):per_page*current_page]],
            indent=1, ensure_ascii=False
        ), 200
    else:
        return json.dumps(
            [resource.to_json() for resource in resources],
            indent=1, ensure_ascii=False
        ), 200


@resources.route('/<int:id>/', methods=['GET'])
def get_id_resources(id):
    resource = Resources.query.get_or_404(id)
    return jsonify(resource.to_json()), 200

