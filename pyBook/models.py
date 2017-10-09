from sqlalchemy import Column, Integer, String, SmallInteger, Float
from pyBook.database import Base
import json, math


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

    def __init__(self, user_name=None, email=None, admin=0, first_name=None, last_name=None,
                 pw_salt=None, pw_hash=None, user_id=None):
        self.user_id = user_id
        self.email = email
        self.user_name = user_name
        self.admin = admin
        self.first_name = first_name
        self.last_name = last_name
        self.pw_salt = pw_salt
        self.pw_hash = pw_hash

    def json(self):
        return dict(id=self.user_id, email=self.email, uname=self.user_name, name=self.first_name + " " + self.last_name,
                    salt=self.pw_salt, hash=self.pw_hash)

    def __repr__(self):
        return '<User %r>' % self.user_name

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
    book_image = Column(String(100))

    def __init__(self, title=None, isbn_ten=None, isbn_thirteen=None,
                 author_first_name=None, author_last_name=None, stars=0, status=0, synopsis=None,
                 image='default.jpg', sort=None, book_id=None):
        self.book_id = book_id
        self.book_title = title
        self.book_sort = str(sort).lower()
        self.isbn_ten = isbn_ten
        self.isbn_thirteen = isbn_thirteen
        self.author_first_name = author_first_name
        self.author_last_name = author_last_name
        self.book_stars = stars
        self.status = status
        self.synopsis = synopsis
        self.book_image = image

    def __repr__(self):
        return '<Book %r>' % self.title

    def __str__(self):
        return json.dumps(self.json(), indent=4, sort_keys=True)

    def json(self):
        return dict(title=self.title, isbn_10=self.isbn_10, isbn_13=self.isbn_13, author=self.author_first_name +
             " " + self.author_last_name, stars=self.book_stars, status=self.status, synopsis=self.synopsis, image=self.image)

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
#            print(math.modf(self.book_stars)[0])
#            print("half star true")
            half_star = True
        if stars > 0:
            star_string = int(stars) * "<i class=\"fa fa-star\" aria-hidden=\"true\"></i>"
        if half_star:
            if stars == 0:
                star_string = "<i class=\"fa fa-star-half-o\" aria-hidden=\"true\"></i>"
            else:
                star_string += "<i class=\"fa fa-star-half-o\" aria-hidden=\"true\"></i>"
            if star_string != "unrated":
                for i in range(0 , 5 - (int(stars) + 1)):
                    star_string += "<i class =\"fa fa-star-o\" aria-hidden=\"true\"></i>"
        else:
            if star_string != "unrated":
                for i in range(0 , 5 - (int(stars))):
                    star_string += "<i class =\"fa fa-star-o\" aria-hidden=\"true\"></i>"
        return str(star_string)

