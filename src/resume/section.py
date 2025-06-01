from flask import Blueprint, render_template

bp = Blueprint("section", __name__, url_prefix="")


@bp.get("/education/")
def education():
    """Studies and certifications"""
    # Context processor automatically injects 'education' into template context
    return render_template("/section/education.html")


@bp.get("/experience/")
def experience():
    """Work experience"""
    # Context processor automatically injects 'experience' into template context
    return render_template("/section/experience.html")


@bp.get("/skills/")
def skills():
    """Skills and competencies"""
    # Context processor automatically injects 'skills' into template context
    return render_template("/section/skills.html")


@bp.get("/contact/")
def contact():
    """Contact information."""
    return render_template("/section/contact.html")


def register(app):
    app.register_blueprint(bp)
