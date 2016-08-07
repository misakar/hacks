# coding: utf-8

from apis import db, orm
from .. import users
from ..models import User as Resources
from flask import jsonify, request


@users.route('/<int:id>/', methods=['DELETE'])
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
