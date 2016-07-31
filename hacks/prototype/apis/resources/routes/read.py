# coding: utf-8

import json
from .. import resources
from flask import jsonify
from ..models import Resources


@resources.route('/', methods=['GET'])
def get_resources():
    resources = Resources.query.all()
    return json.dumps(
        [resource.to_json() for resource in resources],
        indent=1, ensure_ascii=False
    ), 200
