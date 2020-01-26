from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

# Load blueprint modules
from app.modules import directory_search
app.register_blueprint(directory_search.blueprint)
from app.modules import login
app.register_blueprint(login.blueprint)
from app.modules import profile
app.register_blueprint(profile.blueprint)

from app import routes
