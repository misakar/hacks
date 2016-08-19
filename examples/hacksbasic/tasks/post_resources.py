# coding: utf-8

from . import celery
from blueprints.models import orm
from flask_socketio import emit, send
from flask import request, g


@celery.task
def post_resources(Model, data):
    with orm.db_session:
        setattr(g, 'in_celery', True)
        # this is just a virtual test
        # emit("user created!")
        print "get data: ", data
        send(data)

# where can I put my celery task:(
