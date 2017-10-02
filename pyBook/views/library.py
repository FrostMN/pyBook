from flask import Blueprint, render_template, redirect, url_for, request
from pyBook.models import Book, User
from pyBook.database import init_db, db_session
import pyBook.utils.files as file


mod = Blueprint( 'library', __name__ )

init_db()

lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras in enim nibh. Mauris gravida dolor quis venenatis eleifend. Vivamus accumsan neque et aliquam placerat. Nulla et orci eget lorem consectetur dictum at non leo. Aliquam venenatis neque tincidunt sapien interdum pulvinar. Lorem ipsum dolor sit amet, consectetur adipiscing elit..."""


#asouer = User('asouer', 'asouer@gmail.com', 1, 'Aaron', 'Souer')


#print(cryp.title)

#db_session.add(cryp)
#db_session.commit()

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
        asouer = User('asouer', 'asouer@gmail.com', 1, 'Aaron', 'Souer')
        db_session.add(asouer)
        db_session.commit()
        return redirect(url_for('library.setup'))

    books = Book.query.all()

    #for book in books:
    #    print(book)
    #    print(book.isbn_10)
    #    print(book.isbn_13)
    #    print(book.json())
    return render_template('library/index.html', Books=books, Filters=test_filters)


@mod.route('/save', methods=['GET', 'POST'])
def save():
    print("in save()")
    if request.method == 'POST':
        print('its a post')
        print (request.form)
        print("title: " + request.form['title'])
        print("author_fname: " + request.form['author_fname'])
        print("author_lname: " + request.form['author_lname'])
        print("ISBN 10: " + request.form['isbn_10'])
        print("ISBN 13: " + request.form['isbn_13'])
        print("synopsis: " + request.form['synopsis'])
        print("book_id: " + request.form['book_id'])

        title = request.form['title']
        isbn_10 = request.form['isbn_10']
        isbn_13 = request.form['isbn_13']
        fname = request.form['author_fname']
        lname = request.form['author_lname']
        synopsis = request.form['synopsis']
        id = request.form['book_id']

        #bk = Book.query.filter_by(book_id=int(id))

        bk = Book.query.get(int(id))

        print(bk)

        bk.book_title = title
        bk.isbn_ten = isbn_10
        bk.isbn_thirteen = isbn_13
        bk.author_first_name = fname
        bk.author_last_name = lname
        bk.synopsis = synopsis

        print(bk)


        db_session.commit()

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
    if request.method == "GET":
        cryp = Book('Cryptonomicon', '0380973464' , '9780380973460', 'Neal', 'Stephenson', 0, lorem, 'Cryptonomicon.jpg')
        harr = Book('Harry Potter and the Philosopher\'s Stone', '0747532699', '9780747532699', 'J.K.', 'Rowling', 0, lorem, 'Stone.jpg')
        ream = Book('Reamde', '0061977969', '9780061977961', 'Neal', 'Stephenson', 0, lorem, 'default.jpg')
        stra = Book('The Stranger', '0679420266', '9780679420262', 'Albert', 'Camus', 0, lorem, 'Stranger.jpg')
        colo = Book('The Colour of Magic', '0062225677', '9780062225672', 'Terry', 'Pratechett', 0, lorem, 'Magic.jpg')
        test_books = [cryp, harr, ream, stra, colo]

        db_session.add_all(test_books)
        db_session.add(cryp)
        db_session.commit()

        return redirect(url_for('library.index'))


@mod.route('/setup')
def setup():
    if len(User.query.all()) > 0:
        return redirect(url_for('library.index'))
    else:
        return render_template('library/setup.html')


