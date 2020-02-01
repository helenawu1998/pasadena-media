import flask
blueprint = flask.Blueprint(
    'directory_search', __name__, template_folder='templates', static_folder='static', static_url_path='/static/directory_search')

import app.modules.directory_search.routes
