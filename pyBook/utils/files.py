import os


def exists(file):
    if os.path.isfile(file):
        return True
    else:
        return False