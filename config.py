import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SECRET_KEY = '5e5b8070b7a5ac87c5e161497925b6e3a987ff9954b936a1258673b04e54d87bffd217d9aadb46f1238177b630268499c3d5f31fd76f300ba69f082d24d411ac'
DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'pyBook.db')
DATABASE_CONNECT_OPTIONS = {}

ISBNDB_URL = 'http://isbndb.com/api/v2/json/{{KEY}}/book/'
ISBNDB_API_KEY = 'C4HB73TD'

COVER_UPLOAD_FOLDER = os.path.join(_basedir, 'pyBook/static/img/covers')
ALLOWED_EXTENSIONS = set(['jpg'])

#OPEN_LIB_COVERS_URI = 'http://covers.openlibrary.org/b/isbn/{{isbn}}-{{size}}.jpg'

del os
