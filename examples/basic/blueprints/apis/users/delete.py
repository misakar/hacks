# coding: utf-8

from models import db, orm
from flask import jsonify, request
from models.users import User as Resources
from blueprints.apis import api


@api.route('/users/<int:id>/', methods=['DELETE'])
def delete_users(id):
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
