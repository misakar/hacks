# coding: utf-8

import json


def generateModels(config_json_path, models_path):
    with open(config_json_path, 'r') as f:
        data = json.load(f)

    resources_name = data['configs']["name"]
    _column_code = []; _init_code = []; _json_code = []

    for (_column, _type) in data["configs"]["columns"].iteritems():
        if   _type[0] == 'Integer':
            _code = "{} = db.Column(db.Integer)".format(_column)
        elif _type[0] == 'Text':
            _code = "{} = db.Column(db.Text)".format(_column)
        elif _type[0] == 'DateTime':
            _code = "{} = db.Column(db.DateTime, default=datetime.utcnow())".format(_column)
        elif _type[0].split('(')[0] == 'String':
            _code = "{0} = db.Column(db.{1})".format(_column, _type[0])
        else:
            raise TypeError
        _column_code.append(' '*4 + _code)

    for _column in data['configs']['views']:
        _type = data['configs']['columns'][_column]
        if   _type[0] == 'Integer':
            _json = "'{0}': self.{0},".format(_column)
        elif _type[0] == 'Text':
            _json = "'{0}': self.{0},".format(_column)
        elif _type[0] == 'DateTime':
            _json = "'{0}': self.{0}.strftime('%Y-%m-%d %H:%M:%S'),".format(_column)
        elif _type[0].split('(')[0] == 'String':
            _json = "'{0}': self.{0},".format(_column)
        else:
            raise TypeError
        _json_code.append(' '*12 + _json)

    for _column in data['configs']['fromjson']:
        _type = data['configs']['columns'][_column]
        if   _type[0] == 'Integer':
            _init = "self.{0} = kwargs.get('{0}')".format(_column)
        elif _type[0] == 'Text':
            _init = "self.{0} = kwargs.get('{0}')".format(_column)
        elif _type[0] == 'DateTime':
            _init = "self.{0} = kwargs.get('{0}')".format(_column)
        elif _type[0].split('(')[0] == 'String':
            _init = "self.{0} = kwargs.get('{0}')".format(_column)
        else:
            raise TypeError
        _init_code.append(' '*8 + _init)


    _models_code = """# coding: utf-8

from apis import db
from datetime import datetime


class %s(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    create_at = db.Column(db.DateTime, default=datetime.utcnow())
%s

    def __init__(self, kwargs):
%s

    def to_json(self):
        return {
            'id': self.id,
            'create_at': self.create_at.strftime("%s"),
%s
        }
""" % (resources_name[:-1].capitalize(), '\n'.join(_column_code),
       '\n'.join(_init_code), "%Y-%m-%d %H:%M:%S", '\n'.join(_json_code))

    with open(models_path, 'w+') as f:
        f.write(_models_code)
