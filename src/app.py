from flask import Flask, render_template, g, redirect
from flask_login import LoginManager, current_user
from sqlite3 import connect

from message import Message
from user import User
from db import Database, get_db
from userstore import UserStore
from messagestore import MessageStore

from admin_routes import admin_routes
from login_routes import login_routes
from logout_routes import logout_routes
from messages_routes import messages_routes
from users_routes import users_routes

app = Flask(__name__)
app.register_blueprint(admin_routes)
app.register_blueprint(login_routes)
app.register_blueprint(logout_routes)
app.register_blueprint(messages_routes)
app.register_blueprint(users_routes)
app.secret_key = b"SECRET"

login_manager = LoginManager()
login_manager.init_app(app)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

@login_manager.user_loader
def load_user(user_id):
    with app.app_context():
        db = get_db()
        return db.userstore.get_user_by_id(user_id)

@app.route("/")
def index():
    if current_user.is_authenticated:
        return redirect("/messages")

    return render_template("login.html")

def main():
    with app.app_context():
        db = get_db()
        db.initialize()

    app.run(debug = False)

if __name__ == "__main__":
    main()
