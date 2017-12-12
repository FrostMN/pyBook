import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SECRET_KEY = 'secret_key'
DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'pyBook.db')
DATABASE_CONNECT_OPTIONS = {}

COVER_UPLOAD_FOLDER = os.path.join(_basedir, 'pyBook/static/img/covers')
ALLOWED_EXTENSIONS = set(['jpg'])

del os
