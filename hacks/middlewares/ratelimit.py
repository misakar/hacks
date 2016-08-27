# coding: utf-8

#  ┬─┐┌─┐┌┬┐┌─┐┬  ┬┌┬┐┬┌┬┐       ┬ ┬┌─┐┌─┐┬┌─┌─┐        
#  ├┬┘├─┤ │ ├┤ │  │││││ │   ───  ├─┤├─┤│  ├┴┐└─┐        
#  ┴└─┴ ┴ ┴ └─┘┴─┘┴┴ ┴┴ ┴        ┴ ┴┴ ┴└─┘┴ ┴└─┘        
#  ┬─┐┌─┐┌┬┐┌─┐┬  ┬┌┬┐┬┌┬┐  ┌┬┐┬┌┬┐┌┬┐┬  ┌─┐┬ ┬┌─┐┬─┐┌─┐
#  ├┬┘├─┤ │ ├┤ │  │││││ │   ││││ ││ │││  ├┤ │││├─┤├┬┘├┤ 
#  ┴└─┴ ┴ ┴ └─┘┴─┘┴┴ ┴┴ ┴   ┴ ┴┴─┴┘─┴┘┴─┘└─┘└┴┘┴ ┴┴└─└─┘

import time
import redis


rate = redis.StrictRedis(host='localhost', port=6386, db=0) # for rate limit


class RateLimit(object):

    def __init__(self, app, limit, per): # send_x_headers):
        self.app = app  # wsgi app

        self.reset = int(time.time()) + per
        self.limit = limit
        self.per = per
        # self.send_x_headers = send_x_headers

    def __call__(self, environ, start_response):
        """
        add ratelimit for all apis
        """
        uip = environ.get('REMOTE_ADDR')
        url = environ.get('PATH_INFO')
        key_prefix = 'ratelimit/%s/%s' % (uip, url)
        self.key = key_prefix + str(self.reset)

        pipe = rate.pipeline()
        pipe.incr(self.key)
        pipe.expireat(self.key, self.reset)

        self.current = pipe.execute()[0]
        self.remaining = self.limit - self.current
        self.over_limit = self.current >= self.limit

        if self.over_limit:
            start_response('400 Bad Request', 
                         [('Content-Type', 'application/json')])
            return []
        return self.app(environ, start_response)