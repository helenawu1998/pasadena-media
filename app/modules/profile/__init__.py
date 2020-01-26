import flask
blueprint = flask.Blueprint(
    'profile', __name__, template_folder='templates')

import app.modules.profile.routes
