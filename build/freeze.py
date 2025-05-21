from flask_frozen import Freezer
from resume import create_app
import os

# Create the app
app = create_app()

artifacts_dir = os.path.join("build", "artifacts")
os.makedirs(artifacts_dir, exist_ok=True)
# Configure Freezer
app.config["FREEZER_DESTINATION"] = artifacts_dir
app.config["FREEZER_RELATIVE_URLS"] = True
freezer = Freezer(app)

if __name__ == "__main__":
    # Run the freezer
    freezer.freeze()
