# coding: utf-8

from . import celery # 循环导入♻️
from werkzeug.exceptions import InternalServerError
from flask import g
try:
    from io import BytesIO
except ImportError:
    from cStringIO import StringIO as BytesIO


@celery.task
def run_ctx_request(environ):

    from blueprints import app
    # environ 编码转换
    # request body 利用 in-memory-buffer 转换成类似文件
    # 继而可以进行读写操作
    if '_wsgi.input' in environ:
        environ['wsgi.input'] = BytesIO(environ['_wsgi.input'])

    with app.request_context(environ):
        g.in_celery = True

        try:
            rv = app.full_dispatch_request()
        except:
            if app.debug:
                raise
            rv = app.make_response(InternalServerError())
        return (rv.get_data(), rv.status_code, rv.headers)
