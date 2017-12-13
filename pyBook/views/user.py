from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from local import lang as local
from local import set_language
from pyBook.models import Book, User
from pyBook.database import init_db, db_session
import pyBook.utils.files as file
import pyBook.utils.secrets as secrets

mod = Blueprint( 'user', __name__ )


@mod.route('/user')
def index():
    if 'user' in session.keys():
        usr = secrets.get_user(session['user'])
        user_data = {
            "id": usr.id,
            "first_name": usr.get_first_name,
            "last_name": usr.get_last_name,
            "email": usr.get_email,
        }

        lang = set_language()
        return render_template('user/index.html', user=user_data, lang=local[lang])
    else:
        return redirect(url_for('library.index'))


@mod.route('/update', methods=['GET', 'POST'])
def update():
    if 'user' in session.keys():
        if request.method == 'POST':

            # get user id from form
            user_id = request.form['user_id']

            # get user by user_id
            edit_user = User.query.get(user_id)

            # get user data from form
            first_name = request.form['fname']
            last_name = request.form['lname']
            email = request.form['email']
            language = request.form['language']

            # update user in db
            edit_user.set_first_name(first_name)
            edit_user.set_last_name(last_name)
            edit_user.set_email(email)
            edit_user.set_lang(language)

            # commit changes
            db_session.commit()

            session['lang'] = language

            flash('You successfully updated your account')
            return redirect(url_for('library.index'))
        else:
            flash('Invalid Method')
            return redirect(url_for('library.index'))
    else:
        flash('You need to be logged in to do that')
        return redirect(url_for('library.index'))


@mod.route('/updatepassword', methods=['GET', 'POST'])
def update_password():
    if 'user' in session.keys():
        if request.method == 'POST':

            # get user id from form
            user_id = request.form['user_id']

            # get user by user_id
            edit_user = User.query.get(user_id)

            # get user data from form
            new_password = request.form['password']
            new_salt = secrets.generate_salt()
            new_hash = secrets.hash_password(new_password, new_salt)

            # update user in db
            edit_user.set_password_salt(new_salt)
            edit_user.set_password_hash(new_hash)

            # commit changes
            db_session.commit()

            flash('You successfully updated your password')
            return redirect(url_for('library.index'))
        else:
            flash('Invalid Method')
            return redirect(url_for('library.index'))
    else:
        flash('You need to be logged in to do that')
        return redirect(url_for('library.index'))

