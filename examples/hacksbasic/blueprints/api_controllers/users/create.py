# coding: utf-8

import json
from flask import request, jsonify, g
from decorators.async import async
from blueprints.api_controllers import api
from blueprints.models import db, orm
from blueprints.models.users import User as Resources
from signals.emit_msg_from_http_2_socketio import FromHttpToSocketio
from tasks.post_resources import post_resources
from decorators.render_realtime_msg import render_realtime_msg


@api.route('/users/', methods=['POST'])
@render_realtime_msg('post_user', 'hacks=>post a new user!')
def new_users():
    """
    send the response to server-side events
    :return:
    """
    if request.method == 'POST':
        with orm.db_session:
            resource = Resources.create(request.get_json() or {})
        # signal is now work...
        # from_http_to_socketio = FromHttpToSocketio(msg)
        # from_http_to_socketio.send()  # send a signal
        return json.dumps(
            {
                'msg': 'create resource',
                'json': request.get_json() or {},
            },
            indent=1, ensure_ascii=False
        ), 201

# now, I need a `realMiddleWare` to send the restful api response message
# to server-side socketio events!
# yes, it not wsgi...orz
# it can be a celery task, I can use a decorator wrap the restful api function
# and when function successful execute, just emit the server-side socketio event,
# the socketio send the msg to client-side.
# In that, message send procedure is not in request context but wrap the request context!

# it just a hook, but decorator is still http context. I just need signal, use signal pass message
# but still have this things....
