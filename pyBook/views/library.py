from flask import Blueprint, render_template, redirect, url_for, request, session
from pyBook.models import Book, User
from pyBook.database import init_db, db_session
import pyBook
import os
import pyBook.utils.api as api
import pyBook.utils.files as file
import pyBook.utils.secrets as secrets


mod = Blueprint('library', __name__)


@mod.route('/')
def index():
    print(os.path.join(pyBook.app.root_path, "pyBook.db"))
    if file.exists(os.path.join(pyBook.app.root_path, "pyBook.db")):
        print('db exists')
    else:
        print("creating db")
        init_db()

    users = User.query.all()
    if len(users) == 0:
        print(url_for('library.setup'))
        return redirect(url_for('library.setup'))

    books = db_session.query(Book).order_by("book_sort").all()

    return render_template('library/index.html', Books=books)


# TODO need to figure out flash messages
# log in process
@mod.route('/log_in', methods=['GET', 'POST'])
def log_in():
    if (request.method == 'POST') and ('user' not in session):
        uname = request.form['uname']
        pword = request.form['pword']

        # Tests if the username is in the db
        if not secrets.user_exists(uname):
            print("bad username")
            return redirect(url_for('library.index'))
        # Tests if the password mateches
        elif not secrets.check_hash(uname, pword):
            print("bad password")
            return redirect(url_for('library.index'))
        else:
            session['logged_in'] = True
            usr = secrets.get_user(uname)
            session['user'] = usr.user
            session['admin'] = usr.is_admin
            return redirect(url_for('library.index'))
    else:
        return redirect(url_for('library.index'))


# logs out current user
@mod.route('/log_out', methods=['GET', 'POST'])
def log_out():
    if session.get('logged_in'):
        if session['logged_in']:
            session.clear()
            return redirect(url_for('library.index'))
    return redirect(url_for('library.index'))


# edits book already in db
@mod.route('/edit', methods=['GET', 'POST'])
def edit():
    if 'user' in session.keys() and session['admin']:
        if request.method == 'POST':
            # get book id from form
            book_id = request.form['book_id']

            # get book by book_id
            edit_book = Book.query.get(book_id)

            # update book in db
            edit_book.book_title = request.form['title']
            edit_book.author_first_name = request.form['author_fname']
            edit_book.author_last_name = request.form['author_lname']
            edit_book.isbn_ten = request.form['isbn_10']
            edit_book.isbn_thirteen = request.form['isbn_13']
            edit_book.synopsis = request.form['synopsis']
            edit_book.book_sort = request.form['sort']
            edit_book.book_stars = request.form['stars']

            # commit changes
            db_session.commit()
            return redirect(url_for('library.index'))
        else:
            return redirect(url_for('library.index'))
    else:
        return redirect(url_for('library.index'))


# TODO implement lending... have list of books attached to borrower... normalize db
@mod.route('/lend', methods=['GET', 'POST'])
def lend():
    print(request.form)
    return redirect(url_for('library.index'))


# Adds test data for demo purposes
# test data resides in pyBook.static.temp.test_data.py
# that folder and this decorator can be deleted when moved to
# production
@mod.route('/add_test', methods=['GET', 'POST'])
def add_test():
    if len(Book.query.all()) == 0:
        # loads test data from file
        from pyBook.static.temp.test_data import test_books
        db_session.add_all(test_books)
        db_session.commit()
        return redirect(url_for('library.index'))
    return redirect(url_for('library.index'))


# add book to db
@mod.route('/add', methods=['GET', 'POST'])
def add():
    if 'user' in session.keys() and session['admin']:
        if request.method == 'POST':
            title = request.form['title']
            isbn_10 = request.form['isbn_10']
            isbn_13 = request.form['isbn_13']
            author_first_name = request.form['author_fname']
            author_last_name = request.form['author_lname']
            synopsis = request.form['synopsis']
            print(synopsis)
            stars = request.form['stars']
            sort = request.form['sort']

            remote_image = request.form['image_url']
            if request.form['image_name'] != 'default.jpg':
                image_name = request.form['image_name'] + ".jpg"
                image_name = image_name.lower()
                image_name = image_name.replace(" ", "")
            else:
                image_name = 'default.jpg'

            book = Book(title, isbn_10, isbn_13, author_first_name,
                        author_last_name, stars, 0, synopsis, image_name, sort)

            if image_name != 'default.jpg':
                print('fetching' + image_name)
                file.retrieve(remote_image, image_name)

            db_session.add(book)
            db_session.commit()
            return redirect(url_for('library.index'))
        else:
            return redirect(url_for('library.index'))
    else:
        return redirect(url_for('library.index'))


# TODO check for logged in and admin
# Deletes book from the db
@mod.route('/delete', methods=['GET', 'POST'])
def delete():
    if 'user' in session.keys() and session['admin']:
        if request.method == 'POST':
            book_id = request.form['book_id']
            Book.query.filter(Book.book_id == book_id).delete()
            db_session.commit()
            return redirect(url_for('library.index'))
        else:
            return redirect(url_for('library.index'))
    else:
        return redirect(url_for('library.index'))


# TODO crate a page for adding an admin user on first run when there are no users yet
# TODO add session testing
@mod.route('/setup', methods=['GET', 'POST'])
def setup():
    if 'logged_in' in session:
        session.clear()
    if request.method == 'GET':
        if len(User.query.all()) > 0:
            return redirect(url_for('library.index'))
        else:
            return render_template('library/setup.html')
    else:
        first_name = request.form['fname']
        last_name = request.form['lname']
        email = request.form['email']
        user_name = request.form['uname']
        password = request.form['pword']
        isbn_db_key = request.form['isbndb']

        salt = secrets.generate_salt()
        user = User(user_name, email, 1, first_name, last_name, salt, secrets.hash_password(password, salt))

        db_session.add(user)
        db_session.commit()

        file.updateConfig("testkey", secrets.generate_salt() + secrets.generate_salt())
        file.updateConfig("isbndb_Key", isbn_db_key)

        ###################################################
        # TODO Uncomment following line when in production
        file.updateConfig("DEBUG = True", "DEBUG = False")

        return redirect(url_for('library.index'))


# TODO finish fleshing out api
# TODO maybe move it into its own view/bookmark
@mod.route('/api/<isbn>')
def api_new(isbn):
        return api.getBook(isbn)
