# coding: utf-8

import json
from flask import request, jsonify, g

from blueprints.api_controllers import api
from blueprints.models import db, orm
from blueprints.models.users import User as Resources

from decorators.render_realtime_msg import render_realtime_msg
from decorators.async import async
from signals.emit_msg_from_http_2_socketio import FromHttpToSocketio
from tasks.post_resources import post_resources


@api.route('/users/', methods=['POST'])
@render_realtime_msg('post_user', 'hacks=>post a new user!')
def new_users():
    if request.method == 'POST':
        with orm.db_session:
            resource = Resources.create(request.get_json() or {})
        return json.dumps(
            {
                'msg': 'create resource',
                'json': request.get_json() or {},
            },
            indent=1, ensure_ascii=False
        ), 201