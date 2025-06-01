from flask import Blueprint, render_template

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    """Home page with bio and profile information"""
    # Fetch profile data from the database
    return render_template("index.html")


def register(app):
    app.register_blueprint(bp)
