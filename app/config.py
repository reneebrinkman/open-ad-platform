import os
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE_SETTINGS = {
    'name': '',
    'user': '',
    'password': '',
    'host': '',
    'port': '',
}

SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}:{}/{}'.format(
    DATABASE_SETTINGS['user'],
    DATABASE_SETTINGS['password'],
    DATABASE_SETTINGS['host'],
    DATABASE_SETTINGS['port'],
    DATABASE_SETTINGS['name'],
)

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
