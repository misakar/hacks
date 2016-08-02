# coding: utf-8

from apis import db
#from .. import resources
#{=> resources|blueprint|import <=}
#from ..models import Resources
#{=> resources|model|import_as <=}
from flask import jsonify, request


#@resources.route('/<int:id>/', methods=['DELETE'])
#{=> resources_delete|route <=}
#def delete_resource(id):
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
