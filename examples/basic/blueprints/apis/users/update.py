# coding: utf-8

from models import db, orm
from models.users import User as Resources
from flask import jsonify, request
from blueprints.apis import api


@api.route('/users/<int:id>/', methods=['PATCH'])
def update_users(id):
    if request.method == 'PATCH':
        with orm.db_session:
            resource = orm.get(r for r in Resources if r.id == id)
            resource.from_dict(request.get_json() or {})
        return jsonify(
            {
                'msg': 'update resource',
                'json': request.get_json() or {}
            }
        ), 200
