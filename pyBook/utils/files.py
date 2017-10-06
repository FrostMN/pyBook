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
        print(s)
        if placeholder not in s:
            print( '"{placeholder}" not found in {conf}.'.format(**locals()) )
            return

    # Safely write the changed content, if found in the file
    with open(conf, 'w') as f:
        print( 'Changing "{placeholder}" to "{value}" in {conf}'.format(**locals()) )
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
        with open(save_to, "wb") as f:
            f.write(urllib.request.urlopen(url).read())
            f.close()
    else:
        print(file + " exists")

img_url = 'http://covers.openlibrary.org/b/isbn/0385472579-L.jpg'

retrieve(img_url, "Test 123456678.jpg")

