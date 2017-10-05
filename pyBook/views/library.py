from flask import Blueprint, render_template, redirect, url_for, request, session
from pyBook.models import Book, User
from pyBook.database import init_db, db_session
import pyBook.utils.api as api
import pyBook.utils.files as file
import pyBook.utils.secrets as secrets


mod = Blueprint( 'library', __name__ )

init_db()

lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras in enim nibh. Mauris gravida dolor quis venenatis eleifend. Vivamus accumsan neque et aliquam placerat. Nulla et orci eget lorem consectetur dictum at non leo. Aliquam venenatis neque tincidunt sapien interdum pulvinar. Lorem ipsum dolor sit amet, consectetur adipiscing elit..."""


@mod.route('/')
def index():
    test_filters = [] #[{"type": "Author", "value": "Neal"},{"Title": "Crypt"} ]
    if file.exists("pyBook.db"):
        print('db exists')
    else:
        print("creating db")
        init_db()

    users = User.query.all()
    if len(users) == 0:
        salt = '4135adc2956ffc180323adc96ed37625c30911f7c8bc18e6c5e2bccceaef55e7'
        asouer = User('asouer', 'asouer@gmail.com', 1, 'Aaron', 'Souer', salt, secrets.hash_password(salt, 'asouer'))
        guest = User('guest', 'guest@gmail.com', 0, 'Guest', 'User', salt, secrets.hash_password(salt, 'guest'))


        test_users = [asouer, guest]


        db_session.add_all(test_users)
        db_session.commit()
        return redirect(url_for('library.setup'))

    for item in session.items():
        print(item)
    books = Book.query.all()

    #for book in books:
    #    print(book)
    #    print(book.isbn_10)
    #    print(book.isbn_13)
    #    print(book.json())
    return render_template('library/index.html', Books=books, Filters=test_filters)


@mod.route('/log_in', methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        uname = request.form['uname']
        pword = request.form['uname']
        if not secrets.user_exists(uname):
            print("no username")
        elif not secrets.check_hash(uname, pword):
            print("bad password")
        else:
            session['logged_in'] = True
            usr = secrets.get_user(uname)
            session['user'] = usr.user
            session['admin'] = usr.is_admin
            return redirect(url_for('library.index'))
    return redirect(url_for('library.index'))


@mod.route('/log_out', methods=['GET', 'POST'])
def log_out():
    if session.get('logged_in'):
        if session['logged_in']:
            session.clear()
            return redirect(url_for('library.index'))
    return redirect(url_for('library.index'))


@mod.route('/save', methods=['GET', 'POST'])
def save():
    print("in save()")
    if request.method == 'POST':
        print('its a post')
        #print (request.form)
        print("title: " + request.form['title'])
        return redirect(url_for('library.index'))
    else:
        print('just a get')
        return redirect(url_for('library.index'))


@mod.route('/lend', methods=['GET', 'POST'])
def lend():
    print (request.form)
    return redirect(url_for('library.index'))


@mod.route('/add_test', methods=['GET', 'POST'])
def add_test():
    cryp = Book('Cryptonomicon', '0380973464' , '9780380973460', 'Neal', 'Stephenson', 0, lorem, 'Cryptonomicon.jpg')
    harr = Book('Harry Potter and the Philosopher\'s Stone', '0747532699', '9780747532699', 'J.K.', 'Rowling', 0, lorem, 'Stone.jpg')
    ream = Book('Reamde', '0061977969', '9780061977961', 'Neal', 'Stephenson', 0, lorem, 'default.jpg')
    stra = Book('The Stranger', '0679420266', '9780679420262', 'Albert', 'Camus', 0, lorem, 'Stranger.jpg')
    colo = Book('The Colour of Magic', '0062225677', '9780062225672', 'Terry', 'Pratechett', 0, lorem, 'Magic.jpg')
    test_books = [cryp, harr, ream, stra, colo]

    db_session.add_all(test_books)
    db_session.commit()

    return redirect(url_for('library.index'))

@mod.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        isbn_10 = request.form['isbn_10']
        isbn_13 = request.form['isbn_13']
        fname = request.form['author_fname']
        lname = request.form['author_lname']
        synopsis = request.form['synopsis']

        book = Book(title, isbn_10, isbn_13, fname, lname, 0, synopsis, 'default.jpg')

        db_session.add(book)
        db_session.commit()
        return redirect(url_for('library.index'))
    else:
        return redirect(url_for('library.index'))


@mod.route('/setup')
def setup():
    if len(User.query.all()) > 0:
        return redirect(url_for('library.index'))
    else:
        return render_template('library/setup.html')


@mod.route('/api/<isbn>')
def api_new(isbn):
        return api.getBook(isbn)


