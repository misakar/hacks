# coding: utf-8
#   ┌─┐┌─┐┬─┐┌─┐       ┬ ┬┌─┐┌─┐┬┌─┌─┐  ╔═╗╔═╗╦═╗╔═╗  
#   │  │ │├┬┘└─┐  ───  ├─┤├─┤│  ├┴┐└─┐  ║  ║ ║╠╦╝╚═╗  
#   └─┘└─┘┴└─└─┘       ┴ ┴┴ ┴└─┘┴ ┴└─┘  ╚═╝╚═╝╩╚═╚═╝  
#   ┌┬┐┬┌┬┐┌┬┐┬  ┌─┐┬ ┬┌─┐┬─┐┌─┐                      
#   ││││ ││ │││  ├┤ │││├─┤├┬┘├┤                       
#   ┴ ┴┴─┴┘─┴┘┴─┘└─┘└┴┘┴ ┴┴└─└─┘                      

# 	for cross-origin resource sharing
#   https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS


class CORSMiddleWare(object):
	"""
	cors middleware class
	"""

	def __init__(self, app):
		self.app = app  # the hacks app wrapped
		self.whitelist = []

	def origin(self, envrion)
		# origin .append()
		origin = environ.get('HTTP_ORIGIN')
		pass