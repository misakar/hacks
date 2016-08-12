# coding: utf-8

import json
from flask import request
from blueprints.apis import api
from models import orm, db
from models.users import User as Resources


@api.route('/users/', methods=['POST'])
def new_users():
    if request.method == 'POST':
        with orm.db_session:
            resource = Resources.create(request.get_json() or {})
        return json.dumps(
            {
                'msg': 'create resource',
                'json': request.get_json() or {}
            },
            indent=1, ensure_ascii=False
        ), 201
