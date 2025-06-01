# New file - contains the simplified context processor registration
import json
from importlib.resources import open_text
from resume import resources


def load_json_resource(resource_name):
    """Load a JSON resource file."""
    try:
        with open_text(resources, f"{resource_name}.json") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def register_context_processors(app):
    """Register individual context processors for each data type."""

    @app.context_processor
    def inject_education():
        """Inject education data into template context."""
        return {"education": load_json_resource("education")}

    @app.context_processor
    def inject_experience():
        """Inject experience data into template context."""
        return {"experience": load_json_resource("experience")}

    @app.context_processor
    def inject_skills():
        """Inject skills data into template context."""
        return {"skills": load_json_resource("skills")}

    @app.context_processor
    def inject_profile():
        """Inject profile data into template context."""
        return {"profile": load_json_resource("profile")}
