# coding: utf-8

from apis import api, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


manager = Manager(api)
migrate = Migrate(api, db)


manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    api.debug = True
    manager.run()
