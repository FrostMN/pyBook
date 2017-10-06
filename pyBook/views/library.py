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
    if file.exists("pyBook.db"):
        print('db exists')
    else:
        print("creating db")
        init_db()
    users = User.query.all()
    if len(users) == 0:
        return redirect(url_for('library.setup'))

    books = db_session.query(Book).order_by("book_sort").all()

    for book in books:
        print(book.title)

    #books = Book.query.all()  #.order_by('books.book_sort')
    return render_template('library/index.html', Books=books)


# log in process
@mod.route('/log_in', methods=['GET', 'POST'])
def log_in():
    if (request.method == 'POST') and ('user' not in session):
        uname = request.form['uname']
        pword = request.form['pword']
        print(uname)
        print(pword)
        if not secrets.user_exists(uname):
            print("bad username")
            return redirect(url_for('library.index'))
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

# TODO add check for loged in and admin
@mod.route('/edit', methods=['GET', 'POST'])
def edit():
    print("in edit()")
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
        edit_book.book_sort = request.form['sort'];

        # commit changes
        db_session.commit()
        return redirect(url_for('library.index'))
    else:
        return redirect(url_for('library.index'))

# TODO implement lending... have list of books attached to borrower... normalize db
@mod.route('/lend', methods=['GET', 'POST'])
def lend():
    print (request.form)
    return redirect(url_for('library.index'))


# TODO probably remove... see if it still double adds
@mod.route('/add_test', methods=['GET', 'POST'])
def add_test():
    if len(Book.query.all()) == 0:
        cryp = Book('Cryptonomicon', '0380973464' , '9780380973460', 'Neal', 'Stephenson', 0, lorem, 'crypt0380973464.jpg', 'cryptonomicon')
        harr = Book('Harry Potter and the Philosopher\'s Stone', '0747532699', '9780747532699', 'J.K.', 'Rowling', 0, lorem, 'harry0747532699.jpg', 'harry')
        quic = Book('Quicksilver', '0380977427', '9780380977420', 'Neal', 'Stephenson', 0, lorem, 'quick0380977427.jpg', 'quicksilver')
        ream = Book('Reamde', '0061977969', '9780061977961', 'Neal', 'Stephenson', 0, lorem, 'reamd0061977969.jpg', 'reamde')
        conf = Book('The Confusion', '0060523867', '9780060523862', 'Neal', 'Stephenson', 0, lorem, 'confu0060523867.jpg', 'confusion')
        stra = Book('The Stranger', '0679420266', '9780679420262', 'Albert', 'Camus', 0, lorem, 'stran0679420266.jpg', 'stranger')
        colo = Book('The Colour of Magic', '0062225677', '9780062225672', 'Terry', 'Pratechett', 0, lorem, 'color0062225677.jpg', 'colour')
        syst = Book('The System of the World', '0060523875', '9780060523879', 'Neal', 'Stephenson', 0, lorem, 'SystemWorld.jpg', 'system of the World')
        test_books = [cryp, harr, ream, stra, colo, quic, conf, syst]
        db_session.add_all(test_books)
        db_session.commit()
        return redirect(url_for('library.index'))
    return redirect(url_for('library.index'))



# TODO check for logged in
@mod.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        isbn_10 = request.form['isbn_10']
        isbn_13 = request.form['isbn_13']
        fname = request.form['author_fname']
        lname = request.form['author_lname']
        synopsis = request.form['synopsis']
        sort = request.form['sort']

        remote_image = request.form['image_url']
        print("request.form['image_name']: " + request.form['image_name'])
        if request.form['image_name'] != 'default.jpg':
            image_name = request.form['image_name'] + ".jpg"
            image_name = image_name.lower()
            image_name = image_name.replace(" ", "")

        else:
            image_name = 'default.jpg'

        print(image_name)
        print(remote_image)


        book = Book(title, isbn_10, isbn_13, fname, lname, 0, synopsis, image_name, sort)

        print(image_name)

        if image_name != 'default.jpg':
            print('fetching' + image_name)
            file.retrieve(remote_image, image_name)

        db_session.add(book)
        db_session.commit()
        return redirect(url_for('library.index'))
    else:
        return redirect(url_for('library.index'))


# TODO crate a page for adding an admin user on first run when there are no users yet
# TODO add session testing
@mod.route('/setup', methods=['GET', 'POST'])
def setup():
    if request.method == 'GET':
        if len(User.query.all()) > 0:
            return redirect(url_for('library.index'))
        else:
            salt = '4135adc2956ffc180323adc96ed37625c30911f7c8bc18e6c5e2bccceaef55e7'
            asouer = User('asouer', 'asouer@gmail.com', 1, 'Aaron', 'Souer', salt, secrets.hash_password(salt, 'asouer'))
            guest = User('guest', 'guest@gmail.com', 0, 'Guest', 'User', salt, secrets.hash_password(salt, 'guest'))

            test_users = [asouer, guest]

            db_session.add_all(test_users)
            db_session.commit()

            #file.updateConfig("testkey", secrets.generate_salt() + secrets.generate_salt())
            #file.updateConfig("isbndb_Key", "")
            #file.updateConfig("DEBUG = True", "DEBUG = False")

            return render_template('library/setup.html')
    else:
        return render_template('library/setup.html')


# TODO finish fleshing out api
# TODO maybe move it into its own view
@mod.route('/api/<isbn>')
def api_new(isbn):
        return api.getBook(isbn)


@mod.route('/file_test')
def file_test():
    return """
    <form action="/upload" method="post" enctype="multipart/form-data">
    Select image to upload:
    <input type="file" name="fileToUpload" id="fileToUpload">
    <input type="submit" value="Upload Image" name="submit">
    </form>
    """