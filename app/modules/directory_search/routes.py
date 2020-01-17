import flask

@blueprint.route("/directory_search")
def directory_search():
    # Check login authorization
    return flask.render_template("directory_search.html")
