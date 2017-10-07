import pyBook, os, urllib
from flask import request, redirect, url_for
from werkzeug.utils import secure_filename


def exists(file):
    if os.path.isfile(file):
        return True
    else:
        return False


# changes placeholder in config file to given value
def updateConfig(placeholder, value):
    conf = pyBook.app.root_path[:-7] + "/config.py"
    with open(conf) as f:
        s = f.read()
        if placeholder not in s:
            return
    with open(conf, 'w') as f:
        s = s.replace(placeholder, value)
        f.write(s)


# tests if file type is an allowed extention
def allowed(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in pyBook.app.config['ALLOWED_EXTENSIONS']


# TODO add flash messages to function
def upload(file):
    if request.method == 'Post':
        if 'file' not in request.files:
            return redirect(url_for('library.index'))
        if file and allowed(file.filename):
            filename = secure_filename(file.filename)
            file.save(pyBook.app.config['COVER_UPLOAD_FOLDER'], filename)
            return redirect(url_for('library.index'))
        return redirect(url_for('library.index'))
    return redirect(url_for('library.index'))


def retrieve(url, file):
    file = file.lower()
    file = file.replace(" ", "")
    save_to = pyBook.app.config['COVER_UPLOAD_FOLDER'] + "/" + file
    if not exists(save_to):
        print("creating " + file)
        print(len(urllib.request.urlopen(url).read()))
        if len(urllib.request.urlopen(url).read()) != 807:
            with open(save_to, "wb") as f:
                f.write(urllib.request.urlopen(url).read())
                f.close()
        else:
            return False
    else:
        print(file + " exists")
