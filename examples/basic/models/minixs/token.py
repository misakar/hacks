# coding: utf-8

import os
import binascii


class TokenMinxin(object):

    # self.token = orm.Optional(str)

    def generate_token(self):
        self.token = binascii.hexlify(os.urandom(32)).decode('utf-8')
        return self.token
