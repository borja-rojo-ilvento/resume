import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from .db import get_db

bp = Blueprint('section', __name__, url_prefix='/section')

@bp.get('/education')
def education():
    """Studies and certifications"""
    db = get_db()
    education = db.execute('SELECT * FROM education')
    return render_template('/section/education.html', education=education)

@bp.get('/experience')
def experience():
    """Work experience"""
    db = get_db()
    experience = db.execute('SELECT * FROM experience')
    return render_template('/section/experience.html', experience=experience)

@bp.get('/contact')
def contact():
    """Contact information."""
    return render_template('/section/contact.html')

def register(app):
    app.register_blueprint(bp)

