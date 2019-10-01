import os.path
import markdown
from flask import Flask

# Instance of Flask
app = Flask(__name__)


# Index page
@app.route("/")
def index():
    """Showing the API doc file"""
    with open(os.path.dirname(app.root_path) + "/README.md", "r") as doc_file :
        content = doc_file.read()
        return markdown.markdown(content)
