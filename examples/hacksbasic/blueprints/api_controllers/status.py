# coding: utf-8

from . import api
from tasks.run_ctx_request import run_ctx_request
from flask import abort, url_for
from celery import states


@api.route('/status/<id>/', methods=['GET'])
def get_status(id):
    """
    get specific id celery task status
    """
    task = run_ctx_request.AsyncResult(id)
    if task.state == states.PENDING:
        abort(404)
    if task.state == states.RECEIVED or task.state == states.STARTED:
        return '', 202, {'Location': url_for('api.get_status', id=id)}
    return task.info
