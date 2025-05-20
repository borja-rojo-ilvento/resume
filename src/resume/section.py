from flask import Blueprint, render_template


from .db.base import get_db

bp = Blueprint("section", __name__, url_prefix="/section")


@bp.get("/education")
def education():
    """Studies and certifications"""
    db = get_db()
    education = db.execute("SELECT * FROM education")
    return render_template("/section/education.html", education=education)


@bp.get("/experience")
def experience():
    """Work experience"""
    db = get_db()
    experience = db.execute("SELECT * FROM experience").fetchall()
    return render_template("/section/experience.html", experience=experience)


@bp.get("/skills")
def skills():
    """Work experience"""
    db = get_db()
    skills = db.execute("SELECT * FROM skills").fetchall()
    return render_template("/section/skills.html", skills=skills)


@bp.get("/contact")
def contact():
    """Contact information."""
    return render_template("/section/contact.html")


def register(app):
    app.register_blueprint(bp)
