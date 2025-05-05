import os
from flask import Flask
from markupsafe import escape
from flask import render_template

# NOTE (BRI) What is `app.instance_path`?


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev", DATABASE=os.path.join(app.instance_path, "resume.sqlite")
    )

    # Load runtime config unless testing
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.register(app)

    from . import section
    section.register(app)

    return app
