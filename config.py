import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

SECRET_KEY = '433f87e131e5fd51657ba2ea4e94c11f9eb4f8b693acd4a0f3035ab02eeb3b77d554639ebd4e626671a7292f6370f01e7ad3bd5a9e45b0770b6a669b6ba41e74'
DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'pyBook.db')
DATABASE_CONNECT_OPTIONS = {}

ISBNDB_URL = 'http://isbndb.com/api/v2/json/{{KEY}}/book/'
ISBNDB_API_KEY = 'C4HB73TD'

COVER_UPLOAD_FOLDER = os.path.join(_basedir, 'pyBook/static/img/covers')
ALLOWED_EXTENSIONS = set(['jpg'])

#OPEN_LIB_COVERS_URI = 'http://covers.openlibrary.org/b/isbn/{{isbn}}-{{size}}.jpg'

del os
