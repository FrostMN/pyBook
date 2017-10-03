from flask import Flask

app = Flask(__name__)
app.config.from_object('config')


from pyBook.views import admin
from pyBook.views import library
from pyBook.views import user
app.register_blueprint(admin.mod)
app.register_blueprint(library.mod)
app.register_blueprint(user.mod)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


from pyBook.database import db_session


if __name__ == '__main__':
    app.run()
