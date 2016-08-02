# coding: utf-8

import json
from apis import db
#{=> resources|blueprint|import <=}
#{=> resources|model|import_as <=}
from flask import request


#{=> resources_post|route <=}
#{=> new_resource|function <=}}
    kwargs = {}
    if request.method == 'POST':
        json_data = request.get_json()
        for (_field, _value) in json_data.iteritems():
            kwargs[_field] = _value
        resource = Resources(kwargs)
        db.session.add(resource)
        db.session.commit()
        return json.dumps(
            {
                'msg': 'create resource',
                'json': json_data
            },
            indent=1, ensure_ascii=False
        ), 201
