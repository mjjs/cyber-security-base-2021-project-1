from flask import Blueprint, redirect, request
from flask_login import login_user, login_required
from db import get_db

users_routes = Blueprint("users_routes", __name__, template_folder = "templates")

@users_routes.route("/users/delete/<int:user_id>")
@login_required
def delete_user(user_id):
    db = get_db()
    db.userstore.delete_user_by_id(user_id)
    return redirect("/admin")

@users_routes.route("/users/admin/<int:user_id>")
@login_required
def change_user_admin_status(user_id):
    db = get_db()
    db.userstore.switch_admin_status(user_id)
    return redirect("/admin")

@users_routes.route("/users", methods = ["POST"])
def add_user():
    db = get_db()

    username = request.form["username"]
    password = request.form["password"]

    user = db.userstore.add_user(username, password, False)
    login_user(user)

    return redirect("/")

