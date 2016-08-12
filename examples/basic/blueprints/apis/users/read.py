# coding: utf-8

import json
from models import db, orm
from models.users import User as Resources
from flask import jsonify, request, current_app
from blueprints.apis import api


@api.route('/users/', methods=['GET'])
def get_users():
    with orm.db_session:
        resources = orm.select(r for r in Resources)[:]

    page = request.args.get('page') or '1'
    current_page = int(page)
    per_page = current_app.config['RESOURCES_PAGINATION_PERPAGE']

    if per_page != 0:
        return json.dumps(
            [resource.to_dict() for resource in \
             resources[per_page*(current_page-1):per_page*current_page]],
            indent=1, ensure_ascii=False
        ), 200
    else:
        return json.dumps(
            [resource.to_dict() for resource in resources],
            indent=1, ensure_ascii=False
        ), 200


@api.route('/users/<int:id>/', methods=['GET'])
def get_id_users(id):
    with orm.db_session:
        resource = orm.get(r for r in Resources if r.id == id)
    return jsonify(resource.to_dict()), 200
