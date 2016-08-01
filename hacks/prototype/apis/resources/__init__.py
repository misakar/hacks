# coding: utf-8

from flask import Blueprint


resources = Blueprint('resources', __name__)


from .routes import create, read, update, delete, search
