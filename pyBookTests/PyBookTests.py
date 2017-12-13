import os
import pyBook
import pyBook.database as database
from pyBook.models import User
import pyBook.utils.secrets as secrets
import unittest
import tempfile


class pyBookTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, pyBook.app.config['DATABASE_URI'] = tempfile.mkstemp()
        pyBook.app.testing = True
        self.app = pyBook.app.test_client()
        with pyBook.app.app_context():
            database.init_db()
        if not (len(User.query.all()) > 0):
            from pyBookTests.test_admin import test_user
            database.db_session.add(test_user)
            database.db_session.commit()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(pyBook.app.config['DATABASE_URI'])

    def login(self, username, password):
        return self.app.post('/log_in', data=dict(
            uname=username,
            pword=password
        ), follow_redirects=True)

    def add_book(self):
        return self.app.post('/add', data=dict(
            image_url="http://covers.openlibrary.org/b/isbn/0451524934-L.jpg",
            image_name="0451524934",
            title="1984",
            author_fname="George",
            author_lname="Orwell",
            isbn_10="0451524934",
            isbn_13="9870451524935",
            synopsis="Synopsis not found",
            start="4.5"
        ), follow_redirects=True)

    def get_book(self):
        # 0451524934
        usr = secrets.get_user('admin')
        print("user key:")
        print(usr.get_key)



        return self.app.get('/api/v1/'+ usr.get_key +'/books/0451524934', follow_redirects=True)

    def logout(self):
        return self.app.get('/log_out', follow_redirects=True)

    def test_empty_db(self):
        rv = self.app.get('/')
        assert b'no books in db' in rv.data

    def test_login(self):
        rv = self.login('admin', 'default')
        assert b'You where successfully logged in' in rv.data

    def test_logout(self):
        rv = self.login('admin', 'default')
        assert b'You where successfully logged in' in rv.data
        rv = self.logout()
        assert b'You where successfully logged out' in rv.data

    def test_bad_login(self):
        rv = self.login('adminx', 'default')
        assert b'Invalid username or password' in rv.data
        rv = self.login('admin', 'defaultx')
        assert b'Invalid username or password' in rv.data



    def test_add_book(self):
        print("in test add book")
        rs = self.add_book()
        print(rs.data)
        rs = self.get_book()
        print(rs.data)




if __name__ == '__main__':
    unittest.main()
