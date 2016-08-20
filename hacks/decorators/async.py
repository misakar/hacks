# coding: utf-8

"""
    decorators~async.py
    ```````````````````

    this decorator transforms a sync route to asynchronous by running it
    in a background thread.
"""

from flask import request, url_for, g
from celery import states
from werkzeug.exceptions import InternalServerError
try:
    from io import BytesIO
except ImportError:
    from cStringIO import StringIO as BytesIO
from functools import wraps
from blueprints import celery


text_types = (str, bytes)
try:
    text_types += (unicode,)
except NameError:
    # no unicode in python3
    pass


@celery.task
def run_ctx_request(environ):
    """
    run flask request context in celery worker
    """
    from blueprints import app  # wsgi.app

    if '_wsgi.input' in environ:
        # an input stream (file-like object) from which the HTTP request body can be read.
        # detail: https://www.python.org/dev/peps/pep-0333/#environ-variables
        environ['wsgi.input'] = BytesIO(environ['_wsgi.input'])

    with app.request_context():
        g.in_celery = True

        try:
            rv = app.full_dispatch_request()
        except InternalServerError:
            if app.debug:
                raise
            return app.make_response(InternalServerError())
        return (rv.get_data(), rv.status_code, rv.headers)


def async(f):
    """
    this decorator transforms a sync route to asynchronous by running it
    in a background thread.
    """
    @wraps(f)
    def decorator(*args, **kwargs):
        if getattr(g, 'in_celery', False):
            return f(*args, **kwargs)

        environ = {k: v for k, v in request.environ.items()
                   if isinstance(v, text_types)}
        if 'wsgi.input' in request.environ:
            environ['_wsgi.input'] = request.get_data()
        task = run_ctx_request.apply_async(args=(environ,))

        if task.state == states.PENDING or task.state == states.RECEIVED or \
           task.state == states.STARTED:
            return '', 202, {'Location': url_for('api.get_status', id=task.id)}

        return task.info
    return decorator