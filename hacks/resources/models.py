# coding: utf-8

from apis import db
from datetime import datetime


class Resources(db.Model):

    __tablename__ = 'resources'
    id = db.Column(db.Integer, primary_key=True)
    create_at = db.Column(db.DateTime, default=datetime.utcnow())
    age = db.Column(db.Integer)
    name = db.Column(db.String(164))

    def __init__(self, kwargs):
        self.name = kwargs.get('name')
        self.age = kwargs.get('age')

    def to_json(self):
        return {
            'id': self.id,
            'create_at': self.create_at.strftime("%Y-%m-%d %H:%M:%S"),
            'name': self.name,
            'age': self.age,
        }
