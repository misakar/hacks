# coding: utf-8

from apis import db, orm
from datetime import datetime


class User(db.Entity):

    id = orm.PrimaryKey(int, auto=True)    # auto generated
    name = orm.Required(str, unique=True)  # must have value
    create_at = orm.Required(datetime, sql_default='CURRENT_TIMESTAMP')

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.name = kwargs.get('name')

    def to_json(self):
        return {
            'id': self.id,
            'create_at': self.create_at.strftime("%Y-%m-%d %H:%M:%S"),
            'name': self.name,
        }
