import os
from flask import Flask
from markupsafe import escape
from flask import render_template


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

    # Add the current year to jinja templates
    @app.context_processor
    def inject_now():
        from datetime import datetime

        return {"now": datetime.now}

    # Initialize context processors for static compilation (Flask-native approach)
    from .resources.registry import register_context_processors

    register_context_processors(app)

    # from .db import base

    # base.register(app)

    from . import main

    main.register(app)

    from . import section

    section.register(app)

    return app
