from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from db import get_db

messages_routes = Blueprint("messages_routes", __name__, template_folder = "templates")

@messages_routes.route("/messages", methods = ["GET"])
@login_required
def messages_get():
    db = get_db()
    messages = db.messagestore.get_messages()
    return render_template("messages.html", messages = messages if messages else [])

@messages_routes.route("/messages", methods = ["POST"])
@login_required
def messages_post():
    db = get_db()

    title = request.form["title"]
    body = request.form["body"]

    user = db.userstore.get_user_by_id(current_user.get_id())

    db.messagestore.add_message(title, body, user)

    return redirect("/messages")
