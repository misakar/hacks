# coding: utf-8

from flask import jsonify, request
from blueprints.api_controllers import api

from blueprints.models import db, orm
from blueprints.models.users import User as Resources


@api.route('/users/<int:id>/', methods=['PUT'])
def update_users(id):
    if request.method == 'PUT':
        with orm.db_session:
            resource = orm.get(r for r in Resources if r.id == id)
            resource.from_dict(request.get_json() or {})
        return jsonify(
            {
                'msg': 'update resource',
                'json': request.get_json() or {}
            }
        ), 200