# coding: utf-8

from apis import db
#from .. import resources
#{=> resources|blueprint|import <=}
#from ..models import Resources
#{=> resources|model|import_as <=}
from flask import jsonify, request


#@resources.route('/<int:id>/', methods=['PATCH'])
#{=> resources_patch|route <=}
#def update_resource(id):
#{=> update_resource|function <=}
    if request.method == 'PATCH':
        json_data = request.get_json()
        resource = Resources.query.get_or_404(id)
        for (_field, _value) in json_data.iteritems():
            setattr(resource, _field, _value)
        db.session.add(resource)
        db.session.commit()
        return jsonify(
            {
                'msg': 'update resource',
                'json': json_data
            }
        ), 200
