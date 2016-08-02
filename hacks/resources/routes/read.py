# coding: utf-8

import json
#{=> resources|blueprint|import <=}
from flask import jsonify, request, current_app
#{=> resources|model|import_as <=}


#{=> resources_get|route <=}
#{=> get_resources|function <=}
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


#{=> resource_get|route <==}
#{=> get_id_resources|function <=}
    resource = Resources.query.get_or_404(id)
    return jsonify(resource.to_json()), 200
