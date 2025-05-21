from flask import Blueprint, render_template
from .db.base import get_db

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    """Home page with bio and profile information"""
    db = get_db()
    # Fetch profile data from the database
    profile = db.execute("SELECT * FROM profile").fetchone()
    return render_template("index.html", profile=profile)


def register(app):
    app.register_blueprint(bp)
