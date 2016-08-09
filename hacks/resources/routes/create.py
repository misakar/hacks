# coding: utf-8

import json
from flask import request
from apis import db, orm
#{=> resources|blueprint|import <=}
#{=> resources|model|import_as <=}


#{=> resources_post|route <=}
#{=> new_resource|function <=}
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
