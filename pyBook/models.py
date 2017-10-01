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
                 salt=None, pw_hash=None, user_id=None):
        self.user_id = user_id
        self.email = email
        self.user_name = user_name
        self.admin = admin
        self.first_name = first_name
        self.last_name = last_name
        self.salt = salt
        self.hash = pw_hash

    def __repr__(self):
        return '<User %r>' % self._user_name

    # @property
    # def admin(self):
    #     if self._admin == 1:
    #         return True
    #     else:
    #         return False
    #
    # @property
    # def user_name(self):
    #     return self._user_name
    #
    # @property
    # def email(self):
    #     return self._email
    #
    # @property
    # def first_name(self):
    #     return self._first_name
    #
    # @property
    # def last_name(self):
    #     return self._last_name
    #
    # @property
    # def salt(self):
    #     return self._salt
    #
    # @property
    # def hash(self):
    #     return self._hash


class Book(Base):
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key=True)
    book_title = Column(String(200), unique=False)
    book_sort = Column(String(200), unique=False)
    isbn_ten = Column(String(10), unique=False)
    isbn_thirteen = Column(String(13), unique=False)
    author_first_name = Column(String(50))
    author_last_name = Column(String(50))
    status = Column(SmallInteger)
    synopsis = Column(String(1000))
    book_image = Column(String(100))

    def __init__(self, title=None, isbn_ten=None, isbn_thirteen=None,
                 author_first_name=None, author_last_name=None, status=0, synopsis=None,
                 image='default.jpg', book_id=None):
        self.book_id = book_id
        self.book_title = title
        self.isbn_ten = isbn_ten
        self.isbn_thirteen = isbn_thirteen
        self.author_first_name = author_first_name
        self.author_last_name = author_last_name
        self.status = status
        self.synopsis = synopsis
        self.book_image = image

    def __repr__(self):
        return '<Book %r>' % self.title

    def json(self):
        return dict(title=self.title, isbn_10=self.isbn_10, isbn_13=self.isbn_13, author=self.author_first_name +
             " " + self.author_last_name, status=self.status, synopsis=self.synopsis, image=self.image)

    @property
    def image(self):
        return "static/img/covers/" + self.book_image

    @property
    def title(self):
        return str(self.book_title)

    @property
    def isbn_10(self):
        return str(self.isbn_ten).zfill(10)

    @property
    def isbn_13(self):
        return str(self.isbn_thirteen).zfill(13)


    # @property
    # def id(self):
    #     return self._book_id
    #
    # @property
    # def title(self):
    #     return self._title
    #
    # @property
    # def isbn_10(self):
    #     return str(self._isbn_10).zfill(10)
    #
    # @property
    # def isbn_13(self):
    #     return str(self._isbn_13).zfill(13)
    #
    # @property
    # def author_first_name(self):
    #     return self._author_first_name
    #
    # @property
    # def author_last_name(self):
    #     return self._author_last_name
    #
    # @property
    # def status(self):
    #     if self._status == 1:
    #         return True
    #     else:
    #         return False
    #
    # @property
    # def synopsis(self):
    #     return self._synopsis
    #
