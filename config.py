import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SECRET_KEY = '0adc8788b500980ddaef0f93c1bf69e5e94c3f173724a8fc9c1f46b7747b1af101855f76eb0cd1f34f488c51ae63e16f471c216b5857c52836f995aa56e29934'
DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'pyBook.db')
DATABASE_CONNECT_OPTIONS = {}

ISBNDB_URL = 'http://isbndb.com/api/v2/json/{{KEY}}/book/'
ISBNDB_API_KEY = 'C4HB73TD'

COVER_UPLOAD_FOLDER = os.path.join(_basedir, 'pyBook/static/img/covers')
ALLOWED_EXTENSIONS = set(['jpg'])

#OPEN_LIB_COVERS_URI = 'http://covers.openlibrary.org/b/isbn/{{isbn}}-{{size}}.jpg'

del os
