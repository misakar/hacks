# coding: utf-8

"""
	hacks~error~json(400)
	`````````````````````

	status_code -> 400 
	{
		'msg': 'bad request',
	}
"""


class BadRequest(Exception):

	status_code = 400
	message = 'bad request'

	def __init__(self, payload=None):
		Exception.__init__(self)
		self.message = message
		self.status_code = status_code
		self.payload = payload

	def to_dict(self):
		rv = dict(self.payload or {})
		rv['message'] = self.message
		return rv