# coding: utf-8

from flask import Blueprint


main = Blueprint('main', __name__, static_folder='static', template_folder='template')


from . import forms, views
