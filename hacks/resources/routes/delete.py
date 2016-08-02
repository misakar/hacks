# coding: utf-8

from apis import db
#from .. import resources
#{==> resources_blueprint_import <==}
#from ..models import Resources
#{==> resources_model_import_as <==}
from flask import jsonify, request


#@resources.route('/<int:id>/', methods=['DELETE'])
#{==> resources_delete_route <==}
#def delete_resource(id):
#{==> delete_resource_function <==}
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
