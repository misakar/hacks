# coding: utf-8

"""
	hacks~errors~json~401

	status_code -> 401
	{
		'msg': 'unauthorized'
	}	
"""


class Unauthorized(Exception):

	status_code = 401
	message = 'unauthorized'

	def __init__(self, payload=None):
		Exception.__init__(self)
		self.status_code = status_code
		self.message = message
		self.payload = payload  # what is the payload? why I need a payload

	def to_dict(self):
		# payload register rv{'message': message}
		rv = dict(self.payload or {})
		rv['message'] = self.message
		return rv