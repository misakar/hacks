# coding: utf-8

import json
from apis import orm
#{=> resources|blueprint|import <=}
#{=> resources|model|import_as <=}
from flask import request, jsonify


#{=> resources_search|route <=}
#{=> search_resources|function <=}
    except_results = []
    search_results = []
    search_args = request.args
    with orm.db_session:
        resources = orm.select(r for r in Resources)[:]

    for _field in search_args.keys():
        if not hasattr(Resources, _field):
            return jsonify(
                { 'msg': 'can not find field %s' % _field }
            ), 400
        for _resource in resources:
            if str(getattr(_resource, _field)) != search_args.get(_field):
                except_results.append(_resource)
                continue
    for _resource in resources:
        if _resource not in except_results:
            search_results.append(_resource)
    return json.dumps(
        [resource.to_dict() for resource in search_results],
        indent=1, ensure_ascii=False
    ), 200
