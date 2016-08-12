# coding: utf-8

import os.path as path
from models import db
from .apisConfig import project_path


## pony orm connection setting
################################ SQLite #######################################

## SQLite is a software library that implements a self-contained, serverless,
## zero-configuration, transactional SQL database engine.

#~~~~~~~~~~~~~~~~~~~~~~~~~ sqlite in memory ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Normally SQLite database is stored in a file on disk, but it also can be
## stored entirely in memory. This is a convenient way to create a SQLite
## database when playing with Pony in the interactive shell, but you should
## remember, that the entire in-memory database will be lost on program exit.
## Also you should not work with the same in-memory SQLite database simultaneously
## from several threads because in this case all threads share the same connection
## due to SQLite limitation.

# db.bind('sqlite', ':memory:')

#~~~~~~~~~~~~~~~~~~~~~~~~~ sqlite in  disk  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## If you specify a relative path, that path is appended to the directory path of
## the Python file where this database was created (and not to the current working
## directory). We did it this way because sometimes a programmer doesn’t have the
## control over the current working directory (e.g. in mod_wsgi application).
## This approach allows the programmer to create applications which consist of
## independent modules, where each module can work with a separate database.
## well, absolute file path is recommend:)

db.bind('sqlite', path.join(project_path, 'defaultDb.sqlite'), create_db=True)

###############################################################################


############################# PostgreSQL ######################################

## PostgreSQL is a powerful, open source object-relational database system.
## Pony uses psycopg2 driver in order to work with PostgreSQL.
## All the parameters that follow the Pony database provider name will be passed
## to the psycopg2.connect() method. Check the psycopg2.connect documentation
### [http://initd.org/psycopg/docs/module.html#psycopg2.connect]
## in order to learn what other parameters you can pass to this method.

# db.bind('postgres', user='', password='', host='', database='')

###############################################################################


############################### MySql #########################################

## MySQL Community Server is the world's most popular open source database.
## Pony tries to use the MySQLdb driver for working with MySQL. If this module
## cannot be imported, Pony tries to use pymysql.
## See the
### MySQLdb:http://mysql-python.sourceforge.net/MySQLdb.html#functions-and-attributes
## and
### pymysql:https://pypi.python.org/pypi/PyMySQL
## documentation for more information regarding these drivers.

# db.bind('mysql', host='', user='', passwd='', db='')

###############################################################################


############################### Oracle #########################################

## Pony uses cx_Oracle driver for connecting to Oracle databases. More
## information about the parameters which you can use for creating a connection
## to Oracle database can be found here.

# db.bind('oracle', 'user/password@dsn')

###############################################################################


## mapping entities to database tables
db.generate_mapping(create_tables=True)
