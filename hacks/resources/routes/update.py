# coding: utf-8

from apis import db, orm
from .. import users
from ..models import User as Resources
from flask import jsonify, request


@users.route('/<int:id>/', methods=['PATCH'])
def update_users(id):
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
