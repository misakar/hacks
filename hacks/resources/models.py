# coding: utf-8

from apis import db, orm
from flask import abort
from datetime import datetime


#{=> resources|model <=}

    id = orm.PrimaryKey(int, auto=True)
    name = orm.Optional(str, unique=True)
    create_at = orm.Required(datetime, sql_default='CURRENT_TIMESTAMP')

    @staticmethod
    def create(data):
        user = User()
        user.from_dict(data)
        return user

    def from_dict(self, data):
        """
        import user data from a dictionary
        """
        for field in ['name']:
            try:
                setattr(User, field, data[field])
            except KeyError:
                abort(400)  # bad request

    def to_dict(self):
        """
        export a user to a dictionary
        """
        return {
            'id': self.id,
            'create_at': self.create_at.strftime("%Y-%m-%d %H:%M:%S"),
            'name': self.name,
        }
