import pyBook
import os, re


def exists(file):
    if os.path.isfile(file):
        return True
    else:
        return False


def updateConfig(placeholder, value):
    conf = pyBook.app.root_path[:-7] + "/config.py"

    #
    # with open(conf, "rb") as f:
    #     content = f.read()
    #
    # with open(conf, 'wb') as f:
    #     f.write(pattern.sub(value, content))

    # with open(conf, "rt") as fin:
    #     with open(conf, "wt") as fout:
    #         for line in fin:
    #             fout.write(line.replace(placeholder, value))

    with open(conf) as f:
        s = f.read()
        print(s)
        if placeholder not in s:
            print( '"{placeholder}" not found in {conf}.'.format(**locals()) )
            return

    # Safely write the changed content, if found in the file
    with open(conf, 'w') as f:
        print( 'Changing "{placeholder}" to "{value}" in {conf}'.format(**locals()) )
        s = s.replace(placeholder, value)
        f.write(s)