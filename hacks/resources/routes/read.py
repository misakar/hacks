# coding: utf-8

import json
#from .. import resources
#{==> resources_blueprint_import <==}
from flask import jsonify, request, current_app
#from ..models import Resources
#{==> resources_model_import_as <==}


#@resources.route('/', methods=['GET'])
#{==> resources_get_route <==}
#def get_resources():
#{==> get_resources_function <==}
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


#@resources.route('/<int:id>/', methods=['GET'])
#{==> resource_get_route <==}
#def get_id_resources(id):
#{==> get_id_resources_function <==}
    resource = Resources.query.get_or_404(id)
    return jsonify(resource.to_json()), 200
