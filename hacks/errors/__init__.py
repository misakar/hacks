# coding: utf-8

"""
	hacks~http~errors

"""

# blueprints.errors
from flask import jsonify
from wsgi import app
from .json_errors.400 import BadRequest
from .json_errors.401 import UnAuthorized
from .json_errors.403 import Forbidden
from .json_errors.404 import NotFound
from .json_errors.500 import ServerError


# BadRequest -> errorhandler
# errorhandler -> register_error_handler
# register_error_handler ->  handlers
# {'exc_class': 'error_handler', None: {'403': {}}}
@app.errorhandler(BadRequest)
def handle_bad_request(error):
	response = jsonify(error.to_dict())
	response.status_code = error.status_code
	return response


@app.errorhandler(UnAuthorized)
def handle_un_authorized(error):
	response = jsonify(error.to_dict())
	response.status_code = error.status_code
	return response


@app.errorhandler(Forbidden)
def handle_forbidden(error):
	response = jsonify(error.to_dict())
	response.status_code = error.status_code
	return response


@app.errorhandler(NotFound)
def handle_not_found(error):
	response = jsonify(error.to_dict())
	response.status_code = error.status_code
	return response


@app.errorhandler(ServerError)
def handle_server_error(error):
	response = jsonify(error.to_dict())
	response.status_code = error.status_code
	return response