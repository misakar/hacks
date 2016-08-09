# coding: utf-8

from apis import db, orm
#{=> resources|blueprint|import <=}
#{=> resources|model|import_as <=}
from flask import jsonify, request


#{=> resources_patch|route <=}
#{=> update_resource|function <=}
    if request.method == 'PATCH':
        with orm.db_session:
            resource = orm.get(r for r in Resources if r.id == id)
            resource.from_dict(request.get_json() or {})
        return jsonify(
            {
                'msg': 'update resource',
                'json': request.get_json() or {}
            }
        ), 204
