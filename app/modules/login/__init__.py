import flask
blueprint = flask.Blueprint(
    'login', __name__, template_folder='templates')

import app.modules.login.routes
