import os

basedir = os.path.abspath(os.path.dirname(__file__))
# print(basedir)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..' , 'projectparser.db')
BASE_URL = 'http://sroroo.ru'
SQLALCHEMY_TRACK_MODIFICATIONS = False
