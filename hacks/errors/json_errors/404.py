# coding: utf-8

"""
	hacks~errors~json(404)

	status_code -> 404
	{
		'message': 'not found'
	}
"""


class NotFound(Exception):

	status_code = status_code
	message = 'not found'

	def __init__(self, payload=None):
		Exception.__init__(self)
		self.status_code = status_code
		self.message = message
		self.payload = payload

	def to_dict(self):
		rv = dict(self.payload or {})
		rv['message'] = self.message
		return rv