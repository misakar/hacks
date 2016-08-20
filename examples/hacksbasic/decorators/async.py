# coding: utf-8

"""
    decorators~async.py
    ```````````````````

    this decorator transforms a sync route to asynchronous by running it
    in a background thread.

    装饰路由函数, 从而将路由函数放到celery task中执行
"""

from functools import wraps
from tasks.run_ctx_request import run_ctx_request
from flask import request, url_for, g
from celery import states


text_types = (str, bytes)
try:
    text_types += (unicode,)
except NameError:
    # no unicode in python3
    pass


def async(f):
    """
    run request context route function in celery worker process
    """
    @wraps(f)
    def decorator(*args, **kwargs):

        if getattr(g, 'in_celery', False):
            return f(*args, **kwargs)

        environ = {k: v for k, v in request.environ.items()
                   if isinstance(v, text_types)}
        if 'wsgi.input' in request.environ:
            environ['_wsgi.input'] = request.get_data()  # request.body
        task = run_ctx_request.apply_async(args=(environ,))

        if task.state == states.PENDING or task.state == states.RECEIVED or \
           task.state == states.STARTED:
            return '', 202, {'Location': url_for('api.get_status', id=task.id)}

        return task.info
    return decorator
