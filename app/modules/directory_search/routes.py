import flask
from app.modules.directory_search import blueprint

@blueprint.route("/directory_search")
def directory_search():
    # Check login authorization
    return flask.render_template("directory_search.html")
