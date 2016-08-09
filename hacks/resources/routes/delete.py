# coding: utf-8

from apis import db, orm
from flask import jsonify, request
#{=> resources|blueprint|import <=}
#{=> resources|model|import_as <=}


#{=> resources_delete|route <=}
#{=> delete_resource|function <=}
    if request.method == 'DELETE':
        with orm.db_session:
            resource = orm.get(r for r in Resources if r.id == id)
            resource.delete()
        return jsonify(
            {
                'msg': 'delete resource',
                'id': id
            }
        ), 200
