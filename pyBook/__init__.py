from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')


from pyBook.views import admin
from pyBook.views import library
from pyBook.views import user
from pyBook.views import api
app.register_blueprint(admin.mod)
app.register_blueprint(library.mod)
app.register_blueprint(user.mod)
app.register_blueprint(api.mod)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


from pyBook.database import db_session


if __name__ == '__main__':
    app.run()
