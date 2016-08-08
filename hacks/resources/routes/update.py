# coding: utf-8

from apis import db, orm
#{=> resources|blueprint|import <=}
#{=> resources|model|import_as <=}
from flask import jsonify, request


#{=> resources_patch|route <=}
#{=> update_resource|function <=}
    if request.method == 'PATCH':
        json_data = request.get_json()
        with orm.db_session:
            resource = orm.get(r for r in Resources if r.id == id)
            for (_field, _value) in json_data.iteritems():
                setattr(resource, _field, _value)
        return jsonify(
            {
                'msg': 'update resource',
                'json': json_data
            }
        ), 200
