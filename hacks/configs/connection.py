# coding: utf-8

import os.path as path
from .. import db


apis_path = path.abspath(path.join(path.dirname(__file__), '..'))
project_path = path.abspath(path.join(apis_path, '..'))


## pony orm connection setting
#```````````````````` sqlite in memory ````````````````````````````````````````
# db.bind('sqlite', ':memory:')
#``````````````````````````````````````````````````````````````````````````````


#````````````````````` sqlite in disk `````````````````````````````````````````
db.bind('sqlite', path.join(project_path, 'defaultDb.sqlite'), create_db=True)
#``````````````````````````````````````````````````````````````````````````````


#``````````````````````` PostgreSQL ```````````````````````````````````````````
# db.bind('postgres', user='', password='', host='', database='')
#``````````````````````````````````````````````````````````````````````````````


#````````````````````````  MySQL   ````````````````````````````````````````````
# db.bind('mysql', host='', user='', passwd='', db='')
#``````````````````````````````````````````````````````````````````````````````


#```````````````````````  Oracle  `````````````````````````````````````````````
# db.bind('oracle', 'user/password@dsn')
#``````````````````````````````````````````````````````````````````````````````


## mapping entities to database tables
db.generate_mapping(create_tables=True)
