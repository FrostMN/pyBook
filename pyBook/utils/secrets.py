import bcrypt, hashlib
from pyBook.database import init_db, db_session
import pyBook.models


def generate_salt():
    salt = bcrypt.gensalt()
    return hashlib.sha3_256(str(salt).encode('utf-8')).hexdigest()


def hash_password(password, salt):
    print("hashed: " + hashlib.sha3_256(str(salt + password).encode('utf-8')).hexdigest())
    return hashlib.sha3_256(str(salt + password).encode('utf-8')).hexdigest()


def check_hash(user, password):
    usr = db_session.query(pyBook.models.User).filter_by(user_name=user).first()
    salt = usr.salt
    print("new hash: " + hash_password(salt, password))
    print("db salt: " + salt)
    print("db hash: " + usr.hash)
    if hash_password(usr.salt, password) == usr.hash:
        print('Hash matches.')
        return True
    else:
        print('Hash does not match.')
        return False


def user_exists(uname):
    count = pyBook.models.User.query.filter_by(user_name=uname).count()
    print("count: " + str(count))
    if count == 1:
        return True
    else:
        return False


def get_user(uname):
    return pyBook.models.User.query.filter_by(user_name=uname).first()


