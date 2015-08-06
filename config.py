import os
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE_SETTINGS = {
    'name': 'open_ad_platform',
    'user': 'user',
    'password': 'pass',
    'host': 'localhost',
    'port': 3306,
}

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
    DATABASE_SETTINGS['user'],
    DATABASE_SETTINGS['password'],
    DATABASE_SETTINGS['host'],
    DATABASE_SETTINGS['port'],
    DATABASE_SETTINGS['name']
)

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
