from flask import Blueprint, render_template, redirect, url_for, request, session
from local import lang as local
from pyBook.models import Book, User
from pyBook.database import init_db, db_session
import pyBook.utils.files as file
import pyBook.utils.secrets as secrets


mod = Blueprint( 'admin', __name__ )

@mod.route('/admin')
def index():

    if session.get('lang'):
        lang = session['lang']
    else:
        lang = "eng"

    return render_template('admin/index.html', lang=local[lang])

