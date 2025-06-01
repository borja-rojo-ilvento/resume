from flask_frozen import Freezer
from resume import create_app
import os
import shutil

# Create the app
app = create_app()

# Use current working directory (where script is run from)
docs_dir = os.path.join(os.getcwd(), "docs")

print(f"Working directory: {os.getcwd()}")
print(f"Docs directory: {docs_dir}")

if os.path.exists(docs_dir):
    shutil.rmtree(docs_dir)
os.makedirs(docs_dir, exist_ok=True)

# Configure Freezer
app.config["FREEZER_DESTINATION"] = docs_dir
app.config["FREEZER_RELATIVE_URLS"] = True

freezer = Freezer(app)


# Tell Flask-Frozen about all your routes explicitly
@freezer.register_generator
def url_generator():
    yield "main.index", {}
    yield "section.education", {}
    yield "section.experience", {}
    yield "section.skills", {}
    yield "section.contact", {}


@freezer.register_generator
def static_generator():
    yield "static", {"filename": "style.css"}


if __name__ == "__main__":
    print("Freezing Flask app...")

    # Suppress warnings
    import warnings
    from flask_frozen import MimetypeMismatchWarning

    warnings.filterwarnings("ignore", category=MimetypeMismatchWarning)

    freezer.freeze()

    # Add .nojekyll for GitHub Pages
    with open(os.path.join(docs_dir, ".nojekyll"), "w") as f:
        f.write("")

    print(f"Done! Static site in '{docs_dir}' directory")
