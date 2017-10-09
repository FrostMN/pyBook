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


# Adds test data for demo
@mod.route('/add_test', methods=['GET', 'POST'])
def add_test():
    if len(Book.query.all()) == 0:
        crypt_syn = "In 1942, Lawrence Pritchard Waterhouse, a young United States Navy code breaker and " \
                    "mathematical genius, is assigned to the newly formed joint British and American Detachment " \
                    "2702. This ultra-secret unit's role is to hide the fact that Allied intelligence has cracked " \
                    "the German Enigma code."

        crypt = Book('Cryptonomicon', '0380973464', '9780380973460', 'Neal', 'Stephenson', 5, 0, crypt_syn,
                     'crypt0380973464.jpg', 'cryptonomicon')

        stone_syn = "The most evil and powerful dark wizard in history, Lord Voldemort, murders James and Lily " \
                    "Potter but mysteriously disappears after failing to kill their infant son, Harry. While the " \
                    "wizarding world celebrates Voldemort's apparent downfall, Professor Dumbledore, Professor " \
                    "McGonagall and half-giant Rubeus Hagrid place the one-year-old orphan in the care of his surly " \
                    "and cold Muggle uncle and aunt, Vernon and Petunia Dursley and their spoilt and bullying " \
                    "son, Dudley."

        stone = Book('Harry Potter and the Philosopher\'s Stone', '0747532699', '9780747532699', 'J.K.', 'Rowling',
                     4, 0, stone_syn, 'harry0747532699.jpg', 'harry')

        chamber_syn = "In 1992, while the Dursley family—his uncle Vernon, aunt Petunia, and cousin Dudley—entertain " \
                      "a potential client for Vernon’s drill-manufacturing company Grunnings, Harry Potter " \
                      "reminisces upon the events of the previous year, including his enrolment in Hogwarts School " \
                      "of Witchcraft and Wizardry and confrontation with Lord Voldemort (the Dark wizard whose reign " \
                      "seemingly ended when he killed Harry’s parents and attempted but failed to kill Harry " \
                      "himself), and laments the fact that the best friends he made at the institution have not " \
                      "written to him, even for his birthday, on which the novel opens."

        chamber = Book('Harry Potter and the Chamber of Secrets', '0747538492', '9780747538493', 'J.K.', 'Rowling',
                       4, 0, chamber_syn, 'harry0747538492.jpg', 'harry')

        quick_syn = "The first book is a series of flashbacks from 1713 to the earlier life of Daniel Waterhouse. " \
                    "It begins as Enoch Root arrives in Boston in October 1713 to deliver a letter to Daniel " \
                    "containing a summons from Princess Caroline. She wants Daniel to return to England and attempt " \
                    "to repair the feud between Isaac Newton and Gottfried Leibniz. While following Daniel's decision "\
                    "to return to England and board a Dutch ship (the Minerva) to cross the Atlantic, the book flashes"\
                    " back to when Enoch and Daniel each first met Newton. During the flashbacks, the book refocuses " \
                    "on Daniel's life between 1661 and 1673."

        quick = Book('Quicksilver', '0380977427', '9780380977420', 'Neal', 'Stephenson', 4.5, 0, quick_syn,
                     'quick0380977427.jpg', 'quicksilver')

        ream_syn = "Reamde begins by introducing two members of the Forthrast family who reconnect at an annual " \
                   "family reunion: Richard \"Dodge\" Forthrast, a middle-aged man who is the second of the three " \
                   "Forthrast sons (John, Richard, and Jake), and Zula Forthrast, John's adopted Eritrean daughter, " \
                   "Richard's niece."

        ream = Book('Reamde', '0061977969', '9780061977961', 'Neal', 'Stephenson', 4.5, 0, ream_syn,
                    'reamd0061977969.jpg', 'reamde')

        conf_syn = "The beginning of The Confusion finds Jack Shaftoe awakened from a syphilitic blackout of nearly " \
                   "three years. During this time he was a pirate galley slave. The other members of his bench, a" \
                   " motley crew who call themselves \"The Cabal\" and who include men from Africa, the Far East and " \
                   "Europe, create a plot to capture silver illegally shipped from Central America by a Spanish " \
                   "Viceroy; they convince the Pasha of Algiers and their owner to sponsor this endeavor and " \
                   "negotiate for their freedom and a cut in the profit."

        conf = Book('The Confusion', '0060523867', '9780060523862', 'Neal', 'Stephenson', 4.5, 0, conf_syn,
                    'confu0060523867.jpg', 'confusion')

        strange_syn = "Meursault learns of his mother's death. At her funeral, he expresses none of the expected " \
                      "emotions of grief.[4] When asked if he wishes to view the body, he says no, and, instead, " \
                      "smokes and drinks coffee in front of the coffin. Rather than expressing his feelings, he " \
                      "comments to the reader only about the attendees at the funeral."

        strange = Book('The Stranger', '0679420266', '9780679420262', 'Albert', 'Camus', 0, 0, strange_syn,
                       'stran0679420266.jpg', 'stranger')

        color_syn = "The story begins in Ankh-Morpork, the biggest city on the Discworld. The main character is an " \
                    "incompetent and cynical wizard named Rincewind, who is hired as a guide to the rich but naive " \
                    "Twoflower, an insurance clerk from the Agatean Empire who has come to visit Ankh-Morpork. "

        color = Book('The Colour of Magic', '0062225677', '9780062225672', 'Terry', 'Pratechett', 0, 0, color_syn,
                     'color0062225677.jpg', 'colour')

        system_syn = "Daniel Waterhouse returns to England from his \"Technologickal College\" project in Boston " \
                     "in order to try to resolve the feud between Isaac Newton and Gottfried Leibniz over who " \
                     "invented calculus. Someone attempts to assassinate him with an \"Infernal Device\" (a bomb), " \
                     "and Waterhouse forms a club to find out who did it and prosecute them. It later turns out that" \
                     " the bomb was intended for his friend Isaac Newton."

        system = Book('The System of the World', '0060523875', '9780060523879', 'Neal', 'Stephenson', 4.5, 0,
                      system_syn, 'syste0060523875.jpg', 'system of the World')
        test_books = [crypt, stone, ream, strange, chamber, color, quick, conf, system]
        db_session.add_all(test_books)
        db_session.commit()
        return redirect(url_for('library.index'))
    return redirect(url_for('library.index'))


# TODO check for logged in and admin
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
    if request.method == 'GET':
        if len(User.query.all()) > 0:
            return redirect(url_for('library.index'))
        else:
            return render_template('library/setup.html')
    else:
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        uname = request.form['uname']
        pword = request.form['pword']
        isbndb = request.form['isbndb']

        salt = secrets.generate_salt()
        user = User(uname, email, 1, fname, lname, salt, secrets.hash_password(pword, salt))

        db_session.add(user)
        db_session.commit()

        file.updateConfig("testkey", secrets.generate_salt() + secrets.generate_salt())
        file.updateConfig("isbndb_Key", isbndb)

        ###################################################
        # TODO Uncomment following line when in production
        # file.updateConfig("DEBUG = True", "DEBUG = False")

        return redirect(url_for('library.index'))


# TODO finish fleshing out api
# TODO maybe move it into its own view/bookmark
@mod.route('/api/<isbn>')
def api_new(isbn):
        return api.getBook(isbn)
