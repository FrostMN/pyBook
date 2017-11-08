import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SECRET_KEY = 'secret_key'
DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'pyBook.db')
DATABASE_CONNECT_OPTIONS = {}

ISBNDB_URL = 'http://isbndb.com/api/v2/json/{{KEY}}/book/'
ISBNDB_API_KEY = 'isbndb_Key'

COVER_UPLOAD_FOLDER = os.path.join(_basedir, 'pyBook/static/img/covers')
ALLOWED_EXTENSIONS = set(['jpg'])

#OPEN_LIB_COVERS_URI = 'http://covers.openlibrary.org/b/isbn/{{isbn}}-{{size}}.jpg'

del os
