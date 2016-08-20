# coding: utf-8

"""
	hacks~errors~json(500)

	status_code -> 500
	{
		'message': 'server error'
	}
"""


class ServerError(Exception):

	status_code = status_code
	message = 'server error'

	def __init__(self, payload=None):
		Exception.__init__(self)
		self.status_code = status_code
		self.message = message
		self.payload = payload

	def to_dict(self):
		rv = dict(self.payload or {})
		rv['message'] = self.message
		return rv