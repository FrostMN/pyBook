import bcrypt, hashlib


def generate_salt():
    salt = bcrypt.gensalt()
    return hashlib.sha3_256(str(salt).encode('utf-8')).hexdigest()


def hash_password(password, salt):
    return hashlib.sha3_256(str(salt + password).encode('utf-8')).hexdigest()

