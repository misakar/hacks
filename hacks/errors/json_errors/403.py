# coding: utf-8

"""
	hacks~errors~json(403)

	status_code -> 403
	{
		'message': 'forbidden'
	}
"""


class Forbidden(Exception):

	status_code = status_code
	message = 'forbidden'

	def __init__(self, payload=None):
		Exception.__init__(self)
		self.status_code = status_code
		self.message = message
		self.payload = payload

	def to_dict(self):
		rv = dict(self.payload or {})
		rv['message'] = self.message
		return rv