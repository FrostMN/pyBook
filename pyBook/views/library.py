from flask import Blueprint, render_template, redirect, url_for, request
from pyBook.models import Book, User
from pyBook.database import init_db, db_session

mod = Blueprint( 'library', __name__ )

init_db()

lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras in enim nibh. Mauris gravida dolor quis venenatis eleifend. Vivamus accumsan neque et aliquam placerat. Nulla et orci eget lorem consectetur dictum at non leo. Aliquam venenatis neque tincidunt sapien interdum pulvinar. Lorem ipsum dolor sit amet, consectetur adipiscing elit..."""

cryp = Book('Cryptonomicon', isbn_ten=679420266, isbn_thirteen=123, author_first_name='Neal', author_last_name='Stephenson', status=0, synopsis=lorem, image='Cryptonomicon.jpg')
harr = Book('Harry Potter and the Philospher\'s Stone', 747532699, 123, 'J.K.', 'Rowling', 0, lorem, 'Stone.jpg')
ream = Book('Reamde', 61977969, 123, 'Neal', 'Stephenson', 0, lorem, 'default.jpg')
stra = Book('The Stranger', 679420266, 123, 'Albert', 'Camus', 0, lorem, 'Stranger.jpg')
colo = Book('The Colour of Magic', 62225677, 123, 'Terry', 'Pratechett', 0, lorem, 'Magic.jpg')
test_books = [cryp, harr, ream, stra, colo]

asouer = User('asouer', 'asouer@gmail.com', 1, 'Aaron', 'Souer')

print (asouer)
print (asouer.email)
print (asouer.admin)
print (asouer.first_name)
print (asouer.last_name)
print (asouer.salt)
print (asouer.hash)
#print(cryp.title)

#db_session.add(cryp)
#db_session.commit()

@mod.route('/')
def index():
    test_filters = [] #[{"type": "Author", "value": "Neal"},{"Title": "Crypt"} ]

    #books = Book.query.all()

    #print(books)

    return render_template('library/index.html', Books=test_books, Filters=test_filters)

@mod.route('/save', methods=['GET', 'POST'])
def save():
    print (request.form)
    return redirect(url_for('library.index'))

@mod.route('/lend', methods=['GET', 'POST'])
def lend():
    print (request.form)
    return redirect(url_for('library.index'))

