# coding: utf-8

import json
from apis import orm
#{=> resources|blueprint|import <=}
#{=> resources|model|import_as <=}
from flask import jsonify, request, current_app


#{=> resources_get|route <=}
#{=> get_resources|function <=}
    with orm.db_session:
        resources = orm.select(r for r in Resources)[:]

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


#{=> resource_get|route <=}
#{=> get_id_resources|function <=}
    with orm.db_session:
        resource = orm.get(r for r in Resources if r.id == id)
    return jsonify(resource.to_json()), 200
