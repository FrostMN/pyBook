from pyBook import app
import requests, json
from pyBook.models import Book, User
import pyBook.utils.secrets as secrets
import pyBook.utils.valid as valid
import pyBook.utils.files as file
import pyBook.utils.formatting as format
import pyBook.utils.isbn as isbn
from pyBook.database import db_session



# get api info from config file
# key = app.config['ISBNDB_API_KEY']
# isbn_db_uri = app.config['ISBNDB_URL'].replace("{{KEY}}", key)
#

# key-less api info below
open_library_uri = 'https://openlibrary.org/api/books?bibkeys=ISBN:{{isbn}}&jscmd=data&format=json'
google_api_url = "https://www.googleapis.com/books/v1/volumes/"


def getBook(ISBN):
    print("in getBook()")
    synopsis = "Synopsis not found."

    open_library_call = open_library_uri.replace("{{isbn}}", ISBN)
    open_library = json.loads(requests.get(open_library_call).text)['ISBN:' + ISBN]

    if len(open_library) != 0:
        if 'google' in open_library['identifiers']:
            google_key = str(open_library['ISBN:' + ISBN]['identifiers']['google'])[2:-2]
            google_api = json.loads(requests.get(google_api_url + google_key).text)
            if "error" not in google_api:
                synopsis = google_api['volumeInfo']['description']
        book_title = format.title(open_library['title'])
        try:
            if "," in str(open_library['data'][0]['author_data'][0]['name']):
                author_fname = str(open_library['authors'][0]['name']).split(',')[1].strip()
                author_lname = str(open_library['authors'][0]['name']).split(',')[0]
            else:
                author_fname = str(open_library['authors'][0]['name']).split(' ')[0]
                author_lname = str(open_library['authors'][0]['name']).split(' ')[1]
        except:
            author_fname = str("")
            author_lname = str("")
        if isbn.isbn_type(ISBN) == "ISBN10":
            isbn_10 = ISBN
            isbn_13 = isbn.to_isbn13(ISBN)
        else:
            isbn_10 = isbn.to_isbn10(ISBN)
            isbn_13 = ISBN
        return str(Book(book_title, isbn_10, isbn_13, author_fname, author_lname, 0, 0, synopsis, "default.jpg" ))
    else:
        return str(Book('not found', '', '', '', '', 0, 0, '', "default.jpg"))

def lend():
    return None


def keyExists(key):
    count = User.query.filter_by(api_key=key).count()
    if count == 1:
        return True
    else:
        return False


def bookIdExists(book_id):
    count = Book.query.filter_by(book_id=book_id).count()
    if count == 1:
        return True
    else:
        return False


def bookIsbnExists(isbn):
    if len(isbn) == 10:
        count = Book.query.filter_by(isbn_ten=isbn).count()
        if count > 0:
            return True
        else:
            return False
    elif len(isbn) == 13:
        count = Book.query.filter_by(isbn_thirteen=isbn).count()
        if count > 0:
            return True
        else:
            return False
    else:
        return False


def getBookCount(isbn):
    if len(isbn) == 10:
        print("in get book count 10")
        return Book.query.filter_by(isbn_ten=isbn).count()
    else:
        return Book.query.filter_by(isbn_thirteen=isbn).count()


def apiLogin(user_name, password):
    if secrets.user_exists(user_name):
        if secrets.check_hash(user_name, password):
            usr = secrets.get_user(user_name)

            return "{ \"error\": false, \"username\": \"" + \
                   usr.user_name + "\", \"admin\": \"" + str(usr.is_admin).lower() + \
                   "\", \"UserID\": " + str(usr.get_id) + ", \"ApiKey\": \"" + str(usr.get_key) + "\"  }"
        else:
            return "{\"error\": true, \"message\": \"bad username or password\"}"
    else:
        return "{\"error\": true, \"message\": \"bad username or password\"}"


def getUserByKey(key):
    return db_session.query(User).filter_by(api_key=key).first()


def getUserByID(UserID):
    return db_session.query(User).filter_by(user_id=UserID).first()


def getSynopsisByISBN(isbn10):
    return ""


def getBookCover(isbn):
    # if cover image is already on server returns filename of image
    if doesCoverExist(app.config['COVER_UPLOAD_FOLDER'] + "/" + isbn + ".jpg"):
        return isbn + ".jpg"
    else:
        # gets Url of Book Cover frim api
        cover_url = findBookCoverURI(isbn)

        # downloads image of book cover then calls itself
        if file.retrieve(cover_url , isbn + ".jpg"):
            return getBookCover(isbn)
        else:
            return "default.jpg"


def doesCoverExist(isbn):
    print('in doesCoverEXIST')
    if valid.isIsbnTen(isbn):
        print(" isbn is Ten")
        full_file_path = "" + isbn

        print(full_file_path)
        if file.exists(full_file_path):
            print('inf file does exist does cover exist')
            return True
    return False


def findBookCoverURI(isbn):
    if valid.isbn(isbn):
        return 'http://covers.openlibrary.org/b/isbn/' + isbn + '-L.jpg';
    else:
        return ""


def parseDataToDict(req):
    request_data = req.get_data()
    req_json = json.loads(str(request_data)[2:-1])
    return dict(req_json)


