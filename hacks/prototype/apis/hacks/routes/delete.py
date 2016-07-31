# coding: utf-8

from .. import hacks
from flask import jsonify, request


@hacks.route('/', methods=['DELETE'])
def delete_field():
    if request.method == 'DELETE':
        return jsonify({'msg': 'delete a field'}), 200
