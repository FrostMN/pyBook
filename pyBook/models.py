from sqlalchemy import Column, Integer, String, SmallInteger, Float
from pyBook.database import Base
import pyBook.utils.secrets as secrets
import json
import math


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True)
    user_name = Column(String(50), unique=True)
    admin = Column(SmallInteger)
    first_name = Column(String(50))
    last_name = Column(String(50))
    pw_salt = Column(String(64))
    pw_hash = Column(String(64))
    api_key = Column(String(15), unique=True)
    language = Column(String(3))

    def __init__(self, user_name=None, email=None, admin=0, first_name=None, last_name=None, lang=None,
                 pw_salt=None, pw_hash=None, key=None, user_id=None):
        self.user_id = user_id
        self.email = email
        self.user_name = user_name
        self.admin = admin
        self.first_name = first_name
        self.last_name = last_name
        self.language = lang
        self.pw_salt = pw_salt
        self.pw_hash = pw_hash
        self.api_key = key

    def json(self):
        return dict(id=self.user_id, email=self.email, uname=self.user_name,
                    name=self.first_name + " " + self.last_name,
                    salt=self.pw_salt, hash=self.pw_hash)

    def api_json(self):
        return dict(id=self.user_id, email=self.email, uname=self.user_name,
                    name=self.first_name + " " + self.last_name)

    def __repr__(self):
        return '<User %r>' % self.user_name

    @property
    def id(self):
        return self.user_id

    @property
    def user(self):
        return self.user_name

    @property
    def is_admin(self):
        if self.admin == 1:
            return True
        else:
            return False

    @property
    def salt(self):
        return self.pw_salt

    @property
    def hash(self):
        return self.pw_hash

    @property
    def get_key(self):
        return self.api_key

    @property
    def get_id(self):
        return self.user_id

    @property
    def lang(self):
        return self.language

    def set_lang(self, lang):
        self.language = lang

    @property
    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    @property
    def get_first_name(self):
        return self.first_name

    @property
    def get_last_name(self):
        return self.last_name

    def set_first_name(self, fname):
        self.first_name = fname

    def set_last_name(self, lname):
        self.last_name = lname

    def set_password_hash(self, hash):
        self.pw_hash = hash

    def set_password_salt(self, salt):
        self.pw_salt = salt


class Book(Base):
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key=True)
    book_title = Column(String(200), unique=False)
    book_sort = Column(String(200), unique=False)
    isbn_ten = Column(String(10), unique=False)
    isbn_thirteen = Column(String(13), unique=False)
    author_first_name = Column(String(50))
    author_last_name = Column(String(50))
    book_stars = Column(Float)
    status = Column(SmallInteger)
    synopsis = Column(String(1000))
    lent_to_user_id = Column(Integer)
    lent_to_user_name = Column(String(200))
    book_image = Column(String(100))

    def __init__(self, title=None, isbn_ten=None, isbn_thirteen=None,
                 author_first_name=None, author_last_name=None, stars=0, status=0, synopsis=None,
                 image='default.jpg', sort=None, lendee_fname=None, lendee_lname=None, book_id=None):
        self.book_id = book_id
        self.book_title = title
        self.book_sort = str(sort).lower()
        self.isbn_ten = isbn_ten
        self.isbn_thirteen = isbn_thirteen
        self.author_first_name = author_first_name
        self.author_last_name = author_last_name
        self.book_stars = stars
        self.status = status
        if lendee_fname is not None or lendee_lname is not None:
            self.lent_to_user_name = lendee_fname + " " + lendee_lname
        else:
            self.lent_to_user_id = None
        self.synopsis = synopsis
        self.book_image = image

    def __repr__(self):
        return '<Book %r>' % self.title

    def __str__(self):
        return json.dumps(self.json(), indent=4, sort_keys=True)

    def json(self):
        return dict(id=self.book_id, title=self.title, isbn_10=self.isbn_10, isbn_13=self.isbn_13,
                    author=self.author_first_name + " " + self.author_last_name, stars=self.book_stars,
                    status=self.status, lendee=self.lendee, synopsis=self.synopsis, image=self.image)

    def lend_to(self, id, name):
        self.status = 1
        self.lent_to_user_id = id
        self.lent_to_user_name = name

    def return_book(self):
        self.status = 0
        self.lent_to_user_id = None
        self.lent_to_user_name = None


    @property
    def image(self):
        return "static/img/covers/" + self.book_image

    @property
    def title(self):
        return str(self.book_title)

    @property
    def sort(self):
        return str(self.book_sort)

    @property
    def isbn_10(self):
        return str(self.isbn_ten).zfill(10)

    @property
    def isbn_13(self):
        return str(self.isbn_thirteen).zfill(13)

    @property
    def id(self):
        return str(self.book_id)

    @property
    def stars(self):
        star_string = "unrated"
        half_star = False
        stars = math.modf(self.book_stars)[1]
        if math.modf(self.book_stars)[0] != 0:
            half_star = True
        if stars > 0:
            star_string = int(stars) * "<i class=\"fa fa-star\" aria-hidden=\"true\"></i>"
        if half_star:
            if stars == 0:
                star_string = "<i class=\"fa fa-star-half-o\" aria-hidden=\"true\"></i>"
            else:
                star_string += "<i class=\"fa fa-star-half-o\" aria-hidden=\"true\"></i>"
            if star_string != "unrated":
                for i in range(0, 5 - (int(stars) + 1)):
                    star_string += "<i class =\"fa fa-star-o\" aria-hidden=\"true\"></i>"
        else:
            if star_string != "unrated":
                for i in range(0, 5 - (int(stars))):
                    star_string += "<i class =\"fa fa-star-o\" aria-hidden=\"true\"></i>"
        return str(star_string)

    @property
    def lendee(self):
        return str(self.lent_to_user_name)

    @property
    def lendee_id(self):
        return str(self.lent_to_user_id)

    @property
    def is_lent(self):
        if self.status == 1:
            return True
        else:
            return False

