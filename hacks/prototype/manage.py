# coding: utf-8

from apis import api, db
from flask_script import Manager
from apis.configs import connection


manager = Manager(api)


if __name__ == '__main__':
    api.debug = True
    manager.run()
