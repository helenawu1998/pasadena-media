from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
# Database initialization
db = SQLAlchemy(app)
Bootstrap(app)

# Login initialization
login = LoginManager(app)

# Load blueprint modules
from app.modules import directory_search
app.register_blueprint(directory_search.blueprint)
from app.modules import login
app.register_blueprint(login.blueprint)
from app.modules import profile
app.register_blueprint(profile.blueprint)

from app import routes, models
