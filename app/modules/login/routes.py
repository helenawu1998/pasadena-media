import flask

@blueprint.route("/login")
def login():
    # Check login authorization
    return flask.render_template("login.html")
