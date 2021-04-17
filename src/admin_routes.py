from flask import Blueprint, render_template
from flask_login import current_user
from db import get_db

admin_routes = Blueprint("admin_routes", __name__, template_folder = "templates")

@admin_routes.route("/admin")
def admin():
    db = get_db()
    users = db.userstore.get_users()
    return render_template(
            "admin.html",
            users = users if users else [],
            current_user = current_user
            )

