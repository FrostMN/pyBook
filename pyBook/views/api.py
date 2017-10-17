from flask import Blueprint, render_template, redirect, url_for, request, session, jsonify, abort
from flask_api import status
import json
from pyBook.models import Book, User
from pyBook.database import db_session
import pyBook
import os
import pyBook.utils.api as api
import pyBook.utils.files as file
import pyBook.utils.secrets as secrets


mod = Blueprint('api', __name__)


# TODO finish fleshing out api


@mod.route('/api/get/<key>/<isbn>')
def api_get(key, isbn):
    if api.keyExists(key):
        return api.getBook(isbn)
    else:
        return "no key exists"


@mod.route('/api/add/<key>/<isbn>')
def api_new(key, isbn):
    return api.getBook(isbn)


@mod.route('/api/lend/<key>/isbn=<isbn>&to=<uname>', methods=['GET', 'POST'])
def api_lend(key, isbn, uname):
    code = "500"
    sucess = True
    api_user = db_session.query(pyBook.models.User).filter_by(api_key=key).first()
    lendee = db_session.query(pyBook.models.User).filter_by(user_name=uname).first()
    if api_user.is_admin:
        print(isbn)
        print(uname)
        print(lendee.user)
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
    api_user = db_session.query(pyBook.models.User).filter_by(api_key=key).first()
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
    api_user = db_session.query(pyBook.models.User).filter_by(api_key=key).first()
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
            return abort(404)
        elif api.getBookCount(isbn) == 1:
            if len(isbn) == 10:
                bk = db_session.query(pyBook.models.Book).filter_by(isbn_ten=isbn).first()
            else:
                bk = db_session.query(pyBook.models.Book).filter_by(isbn_thirteen=isbn).first()
            return json.dumps(bk.json()), status.HTTP_200_OK
        else:
            books_json = "{  "
            if len(isbn) == 10:
                bk = db_session.query(pyBook.models.Book).filter_by(isbn_ten=isbn).all()
                for b in bk:
                    books_json += str(b.json()) + ", "
            else:
                bk = db_session.query(pyBook.models.Book).filter_by(isbn_thirteen=isbn).all()
                for b in bk:
                    books_json += str(b.json()) + ", "
            books_json = books_json[0: -2] + " }"
            return json.dumps(books_json), status.HTTP_200_OK
    else:
        return abort(401)


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
            # print(bk)
            # print(key)
            # print(id)
            # print(user_id)
            # print(user_first_name)
            # print(user_last_name)
            bk.lend_to(user_id, user_first_name + " " + user_last_name)
            db_session.commit()
            return redirect(url_for("library.index"))
    else:
        return abort(status.HTTP_400_BAD_REQUEST)


# Method to delete a book from the db
@mod.route('/api/v1/<key>/books/<id>', methods=['DELETE'])
def delete_book(key, id):
    if api.keyExists(key):
        api_user = db_session.query(pyBook.models.User).filter_by(api_key=key).first()
        if api_user.is_admin:
            Book.query.get(id)
            db_session.commit()
            return "deleted book id: " + str(id), status.HTTP_204_NO_CONTENT
        else:
            return abort(401) # status.HTTP_401_UNAUTHORIZED
    else:
        return abort(401) # status.HTTP_401_UNAUTHORIZED
