from flask import Blueprint, redirect
from flask_login import logout_user, current_user
from db import get_db

logout_routes = Blueprint("logout_routes", __name__, template_folder = "templates")

@logout_routes.route("/logout")
def logout():
    if not current_user.is_authenticated:
        return redirect("/")

    logout_user()
    return redirect("/login")
