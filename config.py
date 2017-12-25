import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

SECRET_KEY = '64d7ef1373fdf1c598648f9f790392bc20e2a620486f20a4c5c6facf982628681aa2d773f73f6ca84388fc71085f322bc95cd4a392ab8120f336566e825dfc45'
DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'pyBook.db')
DATABASE_CONNECT_OPTIONS = {}

COVER_UPLOAD_FOLDER = os.path.join(_basedir, 'pyBook/static/img/covers')
ALLOWED_EXTENSIONS = set(['jpg'])

del os
