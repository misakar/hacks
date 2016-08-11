# coding: utf-8

from apis import db, orm
from apis.utils import timestamp
from flask import abort
from datetime import datetime


class #{=> resources|model <=}(db.Entity):

    id = orm.PrimaryKey(int, auto=True)
    name = orm.Optional(str, unique=True)
    create_at = orm.Required(datetime, sql_default='CURRENT_TIMESTAMP')
    update_at = orm.Required(datetime, sql_default='CURRENT_TIMESTAMP')

    @staticmethod
    def create(data):
        resource = #{=> resources|model <=}()
        resource.from_dict(data)
        return resource

    def from_dict(self, data):
        """
        import user data from a dictionary
        """
        for field in ['name']:
            try:
                setattr(self, field, data[field])
                setattr(self, 'update_at', timestamp())
            except KeyError:
                abort(400)  # bad request

    def to_dict(self):
        """
        export a user to a dictionary
        """
        return {
            'id': self.id,
            'create_at': self.create_at.strftime("%Y-%m-%d %H:%M:%S"),
            'update_at': self.update_at.strftime("%Y-%m-%d %H:%M:%S"),
            'name': self.name,
        }
