from flask import Blueprint, render_template, redirect, url_for, request, session, jsonify, abort
from flask_api import status
import json
from pyBook.models import Book, User
from pyBook.database import db_session
import pyBook
import os
import pyBook.utils.api as api
import pyBook.utils.formatting as formatting
import pyBook.utils.files as file
import pyBook.utils.secrets as secrets


mod = Blueprint('api', __name__)


# TODO finish fleshing out api

@mod.route('/api/v1/login', methods=['GET', 'POST'])
def api_login():
    if request.method == 'POST':

        request_data = request.get_data()

        req_json = json.loads(str(request_data)[2:-1])

        req_dict = dict(req_json)

        if 'user' in req_dict.keys() and 'password' in req_dict.keys():
            username = req_dict.get("user")
            password = req_dict.get("password")
            login_json = api.apiLogin(username, password)
            return login_json
        else:
            return "{ \"error\": true, \"message\": \"missing parameter\" }"
    else:
        return "{ \"error\": true, \"message\": \"method not allowed\" }"


@mod.route('/api/get/<key>/<isbn>')
def api_get(key, isbn):
    if api.keyExists(key):
        return api.getBook(isbn)
    else:
        return "no key exists"


@mod.route('/api/add/<key>/<isbn>')
def api_new(key, isbn):
    return api.getBook(isbn)


# I dont think Im actualy using the
# TODO remove if not needed
@mod.route('/api/lend/<key>/isbn=<isbn>&to=<uname>', methods=['GET', 'POST'])
def api_lend(key, isbn, uname):
    code = "500"
    sucess = True
    api_user = db_session.query(pyBook.models.User).filter_by(api_key=key).first()
    lendee = db_session.query(pyBook.models.User).filter_by(user_name=uname).first()
    if api_user.is_admin:
        # print(isbn)
        # print(uname)
        # print(lendee.user)
        user = str(api_user.user)
        if sucess:
            code = "200"
    return code


@mod.route('/api/v1/<key>/books/', methods=['GET'])
def get_books(key):
    if api.keyExists(key):
        books = Book.query.all()
        books_json = "{  "
        for b in books:
            books_json += str(b.json()) + ", "
        books_json = books_json[0:-2]
        books_json += " }"
        print(books_json)
        return jsonify(books_json) #json.dumps(books_json)), status.HTTP_200_OK
    return abort(401) #"not allowed", status.HTTP_401_UNAUTHORIZED


# TODO Need to flash out create method
@mod.route('/api/v1/<key>/books/', methods=['POST'])
def post_books(key, book=None):
    api_user = api.getUserByKey(key)
    admin = api_user.is_admin
    if book is not None:
        if admin:
            # Make new book
            return "made book", status.HTTP_201_CREATED
        else:
            return abort(401) # "not allowed", status.HTTP_401_UNAUTHORIZED
    else:
        return abort(400) # "no info", status.HTTP_400_BAD_REQUEST


# TODO Need to flesh out 'put' method
@mod.route('/api/v1/<key>/books/', methods=['PUT'])
def put_books(key):
    return abort(400)


# Method to delete all books from db
@mod.route('/api/v1/<key>/books/', methods=['DELETE'])
def delete_books(key):
    api_user = api.getUserByKey(key)
    if api_user.is_admin:
        Book.query.delete()
        db_session.commit()
        return "deleted all", status.HTTP_204_NO_CONTENT
    else:
        return abort(401)


# Gets book/books by isbn
@mod.route('/api/v1/<key>/books/<isbn>', methods=['GET'])
def get_book(key, isbn):
    if api.keyExists(key):
        if api.getBookCount(isbn) == 0:
            return abort(status.HTTP_404_NOT_FOUND)
        else:
            books_json = "[  "
            if len(isbn) == 10:
                bk = db_session.query(pyBook.models.Book).filter_by(isbn_ten=isbn).all()
                for b in bk:
                    books_json += str(b.json()) + ", "
            else:
                bk = db_session.query(pyBook.models.Book).filter_by(isbn_thirteen=isbn).all()
                for b in bk:
                    books_json += str(b.json()) + ", "
            books_json = books_json[0: -2] + " ]"

            print(type(books_json))
            print(books_json.replace("'", "\""))
            return books_json.replace("'", '"'), status.HTTP_200_OK
    else:
        return abort(401)


# Gets if ISBN exists in DB
@mod.route('/api/v1/<key>/exists/<isbn>', methods=['GET'])
def isbn_exists(key, isbn):
    if api.keyExists(key):
        if api.bookIsbnExists(isbn):
            return "{ \"isbnExists\": true }"
        else:
            return "{ \"isbnExists\": false }"
    else:
        return "bad key"


# Workaround to make a web-form PUT, also cannot POST aspecific ISBN
@mod.route('/api/v1/<key>/books/<id>', methods=['POST'])
def post_book(key, id=None):
    if api.keyExists(key):
        print(request.form['_method'])
        if request.form['_method']:
            if request.form['_method'] == "PUT":
                user_name = request.form['user']
                return put_book(key, id, user_name)
            else:
                return abort(status.HTTP_405_METHOD_NOT_ALLOWED)

        return abort(status.HTTP_405_METHOD_NOT_ALLOWED)
    else:
        return abort(status.HTTP_401_UNAUTHORIZED)


# TODO Need to flesh out 'put' method, this will be how to lend a book
@mod.route('/api/v1/<key>/books/<id>', methods=['PUT'])
def put_book(key, id=None, user_name=None):
    if (id is not None) and (user_name is not None):
        if user_name == "returning":
            # TODO return book code
            print("return book")
        else:
            bk = Book.query.get(id)
            user_id = str(user_name).split(";")[0]
            user_first_name = str(user_name).split(";")[1]
            user_last_name = str(user_name).split(";")[2]
            bk.lend_to(user_id, user_first_name + " " + user_last_name)
            db_session.commit()
            return redirect(url_for("library.index"))
    else:
        if request.method == 'PUT':
            print("put")
            if api.keyExists(key):
                print("good key")
                api_user = api.getUserByKey(key)

                if api_user.is_admin:

                    print(request.get_data())
                    req_dict = dict(json.loads(str(request.get_data())[2:-1]))

                    print(req_dict["action"])

                    if req_dict["action"] == "lend":
                        print("do lend")

                        user_id = req_dict["userID"]
                        usr = api.getUserByID(user_id)
                        user_first_name = usr.get_first_name
                        user_last_name = usr.get_last_name
                        user_full_name = user_first_name + " " + user_last_name

                        book_id = req_dict["bookID"]
                        bk = Book.query.get(book_id)

                        bk.lend_to(user_id, user_full_name)
                        db_session.commit()

                        return str(status.HTTP_202_ACCEPTED), status.HTTP_202_ACCEPTED
                    elif req_dict["action"] == "return":
                        print("do return")

                        book_id = req_dict["bookID"]
                        bk = Book.query.get(book_id)

                        bk.return_book()
                        db_session.commit()
                        return str(status.HTTP_202_ACCEPTED), status.HTTP_202_ACCEPTED
                    else:
                        return str(status.HTTP_400_BAD_REQUEST), status.HTTP_400_BAD_REQUEST
                else:
                    return "unauthorized"
            else:
                return "bad key"
        else:
            return abort(status.HTTP_400_BAD_REQUEST)


# Method to delete a book from the db
@mod.route('/api/v1/<key>/books/<id>', methods=['DELETE'])
def delete_book(key, id):
    if api.keyExists(key):
        api_user = api.getUserByKey(key)
        if api_user.is_admin:
            Book.query.get(id)
            db_session.commit()
            return "deleted book id: " + str(id), status.HTTP_204_NO_CONTENT
        else:
            return abort(401) # status.HTTP_401_UNAUTHORIZED
    else:
        return abort(401) # status.HTTP_401_UNAUTHORIZED


# add book to db
@mod.route('/api/v1/<key>/add', methods=['GET', 'POST'])
def add(key):
    if request.method == 'POST':
        # get data from POST and parse to useable format
        req_dict = api.parseDataToDict(request)

        if api.keyExists(key):

            # finds registered user by api key
            api_user = api.getUserByKey(key)

            if api_user.is_admin:
                print("user is admin")
                # gets and formats title from req_dict
                title = formatting.title(req_dict['title'])

                # gets isbn 10 from req_dict
                isbn10 = req_dict["isbn_ten"]

                # gets isbn 13 from req_dict
                isbn13 = req_dict["isbn_thr"]

                # gets author first name from req_dict
                author_first_name = req_dict["author_fname"]

                # gets author last name from req_dict
                author_last_name = req_dict["author_lname"]

                synopsis = api.getSynopsisByISBN(isbn10)

                stars = 0

                book_cover = api.getBookCover(isbn10)
                sort_title = formatting.sort_title(req_dict['title'])

                book = Book(title, isbn10, isbn13, author_first_name,
                            author_last_name, stars, 0, synopsis, book_cover, sort_title)

                # print(book)

                db_session.add(book)
                db_session.commit()
                return "{ \"error\": \"false\" }"
            else:
                return "user not admin" # TODO make this a useful return for production
    else:
        return "not post" # TODO make this a useful return for production


# Gets book/books by isbn
@mod.route('/api/v1/<key>/users', methods=['GET'])
def get_users(key):
    if api.keyExists(key):
        user = api.getUserByKey(key)
        if user.is_admin:
            users_json = "[  "
            users = db_session.query(pyBook.models.User).all()
            for user in users:
                users_json += str(user.api_json()) + ", "
            users_json = users_json[0: -2] + " ]"

            print(type(users_json))
            print(users_json.replace("'", "\""))
            return users_json.replace("'", '"'), status.HTTP_200_OK
        else:
            return abort(status.HTTP_401_UNAUTHORIZED)
    else:
        return abort(status.HTTP_401_UNAUTHORIZED)
