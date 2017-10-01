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
    if not file.exists("pyBook.db"):
        init_db()

    users = User.query.all()
    if len(users) == 0:
        return redirect('https://www.asouer.com')

    books = Book.query.all()



    for book in books:
        print(book)
        print(book.isbn_10)
        print(book.isbn_13)
        print(book.json())



    return render_template('library/index.html', Books=books, Filters=test_filters)

@mod.route('/save', methods=['GET', 'POST'])
def save():
    print (request.form)
    return redirect(url_for('library.index'))

@mod.route('/lend', methods=['GET', 'POST'])
def lend():
    print (request.form)
    return redirect(url_for('library.index'))


@mod.route('/add_test', methods=['GET', 'POST'])
def add_test():
    cryp = Book('Cryptonomicon', 380973464 , 9780380973460, 'Neal', 'Stephenson', 0, lorem, 'Cryptonomicon.jpg')
    harr = Book('Harry Potter and the Philosopher\'s Stone', 747532699, 9780747532699, 'J.K.', 'Rowling', 0, lorem, 'Stone.jpg')
    ream = Book('Reamde', 61977969, 9780061977961, 'Neal', 'Stephenson', 0, lorem, 'default.jpg')
    stra = Book('The Stranger', 679420266, 9780679420262, 'Albert', 'Camus', 0, lorem, 'Stranger.jpg')
    colo = Book('The Colour of Magic', 62225677, 9780062225672, 'Terry', 'Pratechett', 0, lorem, 'Magic.jpg')
    test_books = [cryp, harr, ream, stra, colo]

    for book in test_books:
        print(book.image)
        print(book.isbn_10)
        print(book.isbn_13)

    db_session.add_all(test_books)
    db_session.commit()

    return redirect(url_for('library.index'))


