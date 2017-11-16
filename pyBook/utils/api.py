from pyBook import app
import requests, json
from pyBook.models import Book, User
import pyBook.utils.secrets as secrets

# get api info from config file
key = app.config['ISBNDB_API_KEY']
isbn_db_uri = app.config['ISBNDB_URL'].replace("{{KEY}}", key)


# key-less api info below
open_library_uri = 'https://openlibrary.org/api/books?bibkeys=ISBN:{{isbn}}&jscmd=data&format=json'
google_apis_uri = "https://www.googleapis.com/books/v1/volumes/"


def getBook(isbn):
    google_key = ""
    synopsis = "Synopsis not found."

    open_library_call = open_library_uri.replace("{{isbn}}", isbn)
    open_library = json.loads(requests.get(open_library_call).text)

    if len(open_library) != 0:
        if 'google' in open_library['ISBN:' + isbn]['identifiers']:
            google_key = str(open_library['ISBN:' + isbn]['identifiers']['google'])[2:-2]

    google_api = json.loads(requests.get(google_apis_uri + google_key).text)

    if "error" not in google_api:
        synopsis = google_api['volumeInfo']['description']

    isbn_db = requests.get(isbn_db_uri + isbn).text
    isbn_db_json = json.loads(isbn_db)

    if 'data' in isbn_db_json:
        title = isbn_db_json['data'][0]['title']
        try:
            if "," in str(isbn_db_json['data'][0]['author_data'][0]['name']):
                author_fname = str(isbn_db_json['data'][0]['author_data'][0]['name']).split(',')[1].strip()
                author_lname = str(isbn_db_json['data'][0]['author_data'][0]['name']).split(',')[0]
            else:
                author_fname = str(isbn_db_json['data'][0]['author_data'][0]['name']).split(' ')[0]
                author_lname = str(isbn_db_json['data'][0]['author_data'][0]['name']).split(' ')[1]
        except:
            author_fname = str("")
            author_lname = str("")
        isbn_10 = isbn_db_json['data'][0]['isbn10']
        isbn_13 = isbn_db_json['data'][0]['isbn13']
        return str(Book(title, isbn_10, isbn_13, author_fname, author_lname, 0, 0, synopsis, "default.jpg" ))
    return str(Book('not found', '', '', '', '', 0, 0, '', "default.jpg" ))


def getBookImage():
    return ""


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


def getBookCount(isbn):
    if len(isbn) == 10:
        print("in get book count 10")
        print()
        return Book.query.filter_by(isbn_ten=isbn).count()
    else:
        return Book.query.filter_by(isbn_thirteen=isbn).count()


def apiLogin(user_name, password):
    if secrets.user_exists(user_name):
        if secrets.check_hash(user_name, password):
            usr = secrets.get_user(user_name)

            return "{\"error\": false, \"username\": \"" + \
                   usr.user_name + "\", \"admin\": \"" + str(usr.is_admin).lower() + \
                   "\", \"UserID\": " + str(usr.get_id) + "  }"
        else:
            return "{\"error\": true, \"message\": \"bad username or password\"}"
    else:
        return "{\"error\": true, \"message\": \"bad username or password\"}"
