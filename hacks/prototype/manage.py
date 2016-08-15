# coding: utf-8

from blueprints import app
from configs import connection
from flask_script import Manager


manager = Manager(app)


if __name__ == '__main__':
    app.debug = True
    manager.run()
