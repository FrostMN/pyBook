import bcrypt, hashlib
from pyBook.database import init_db, db_session
import pyBook.models

# generates 64 random characters to use as salt
def generate_salt():
    salt = bcrypt.gensalt()
    return hashlib.sha3_256(str(salt).encode('utf-8')).hexdigest()


# hashes password with salt
def hash_password(password, salt):
    return hashlib.sha3_256(str(salt + password).encode('utf-8')).hexdigest()


# compares stored hash with newly generated hash
def check_hash(user, password):
    usr = db_session.query(pyBook.models.User).filter_by(user_name=user).first()
    salt = usr.salt
    if hash_password(password, salt) == usr.hash:
        #print('Hash matches.')
        return True
    else:
        #print('Hash does not match.')
        return False


def user_exists(uname):
    count = pyBook.models.User.query.filter_by(user_name=uname).count()
    if count == 1:
        return True
    else:
        return False


def get_user(uname):
    return pyBook.models.User.query.filter_by(user_name=uname).first()

