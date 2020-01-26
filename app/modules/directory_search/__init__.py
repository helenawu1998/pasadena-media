import flask
blueprint = flask.Blueprint(
    'directory_search', __name__, template_folder='templates')

import app.modules.directory_search.routes
