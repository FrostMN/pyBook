from sqlalchemy import Column, Integer, String, SmallInteger
from pyBook.database import Base
from pyBook.utils.secrets import hash_password, generate_salt


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True)
    user_name = Column(String(50), unique=True)
    admin = Column(SmallInteger)
    first_name = Column(String(50))
    last_name = Column(String(50))
    salt = Column(String(64))
    hash = Column(String(64))

    def __init__(self, user_name=None, email=None, admin=0, first_name=None, last_name=None,
                 salt=generate_salt(), hash=generate_salt(), uid=None):
        self._user_id = uid
        self._email = email
        self._user_name = user_name
        self._admin = admin
        self._first_name = first_name
        self._last_name = last_name
        self._salt = salt
        self._hash = hash

    def __repr__(self):
        return '<User %r>' % self._user_name

    @property
    def admin(self):
        if self._admin == 1:
            return True
        else:
            return False

    @property
    def user_name(self):
        return self._user_name

    @property
    def email(self):
        return self._email

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def salt(self):
        return self._salt

    @property
    def hash(self):
        return self._hash


class Book(Base):
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key=True)
    book_title = Column(String(200), unique=False)
    isbn_ten = Column(Integer, unique=True)
    isbn_thirteen = Column(Integer, unique=True)
    author_first_name = Column(String(50))
    author_last_name = Column(String(50))
    status = Column(SmallInteger)
    synopsis = Column(String(1000))
    image = Column(String(100))

    def __init__(self, title=None, isbn_ten=None, isbn_thirteen=None,
                 author_first_name=None, author_last_name=None, status=0, synopsis=None,
                 image='default.jpg', image_path = "static/img/covers/", book_id=None):
        self._book_id = book_id
        self._title = title
        self._isbn_10 = isbn_ten
        self._isbn_13 = isbn_thirteen
        self._author_first_name = author_first_name
        self._author_last_name = author_last_name
        self._status = status
        self._synopsis = synopsis
        self._image = image
        self._image_path = image_path

    def __repr__(self):
        return '<Book %r>' % self._title

    @property
    def id(self):
        return self._book_id

    @property
    def title(self):
        return self._title

    @property
    def isbn_10(self):
        return str(self._isbn_10).zfill(10)

    @property
    def isbn_13(self):
        return str(self._isbn_13).zfill(13)

    @property
    def author_first_name(self):
        return self._author_first_name

    @property
    def author_last_name(self):
        return self._author_last_name

    @property
    def status(self):
        if self._status == 1:
            return True
        else:
            return False

    @property
    def synopsis(self):
        return self._synopsis

    @property
    def image(self):
        return self._image_path + self._image
