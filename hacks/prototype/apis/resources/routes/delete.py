# coding: utf-8

from apis import db
from .. import resources
from ..models import Resources
from flask import jsonify, request


@resources.route('/<int:id>/', methods=['DELETE'])
def delete_resource(id):
    if request.method == 'DELETE':
        resource = Resources.query.get_or_404(id)
        # db.session.remove(resource)
        db.session.delete(resource)
        db.session.commit()
        return jsonify(
            {
                'msg': 'delete resource',
                'id': id
            }
        ), 200
