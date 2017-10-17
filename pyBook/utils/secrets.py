import bcrypt, hashlib
from pyBook.database import init_db, db_session
import pyBook.models


# generates random characters to use as salt default is 64
def generate_salt(length=64):
    salt = ""
    while len(salt) < length:
        salt += hashlib.sha3_256(str(bcrypt.gensalt()).encode('utf-8')).hexdigest()
    return salt[0:length]


# hashes password with salt
def hash_password(password, salt):
    return hashlib.sha3_256(str(salt + password).encode('utf-8')).hexdigest()


# compares stored hash with newly generated hash
def check_hash(user, password):
    usr = db_session.query(pyBook.models.User).filter_by(user_name=user).first()
    salt = usr.salt
    if hash_password(password, salt) == usr.hash:
        return True
    else:
        return False


def user_exists(uname):
    count = pyBook.models.User.query.filter_by(user_name=uname).count()
    if count == 1:
        return True
    else:
        return False


def get_user(uname):
    return pyBook.models.User.query.filter_by(user_name=uname).first()

