# coding: utf-8
"""
使用Minix类以后, 可以方便`配置json格式的文件`定义数据库model(API)的行为:)
"""

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


class PasswordMinix(object):

    # password_hash = Required(str)

    @property
    def password(self):
        raise AttributeError("password is not readable")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
