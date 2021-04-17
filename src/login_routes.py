from flask import Blueprint, render_template, request, redirect
from flask_login import login_user, current_user
from db import get_db

login_routes = Blueprint("login_routes", __name__, template_folder = "templates")

@login_routes.route("/login", methods = ["GET"])
def login_get():
    if current_user.is_authenticated:
        return redirect("/")

    return render_template("login.html")

@login_routes.route("/login", methods = ["POST"])
def login_post():
    db = get_db()

    username = request.form["username"]
    password = request.form["password"]

    user = db.userstore.get_user_by_username_and_password(username, password)

    login_user(user)
    return redirect("/messages")

