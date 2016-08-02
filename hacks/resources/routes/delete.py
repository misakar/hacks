# coding: utf-8

from apis import db
#{=> resources|blueprint|import <=}
#{=> resources|model|import_as <=}
from flask import jsonify, request


#{=> resources_delete|route <=}
#{=> delete_resource|function <=}
    if request.method == 'DELETE':
        resource = Resources.query.get_or_404(id)
        db.session.delete(resource)
        db.session.commit()
        return jsonify(
            {
                'msg': 'delete resource',
                'id': id
            }
        ), 200
