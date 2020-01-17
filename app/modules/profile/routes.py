import flask

@blueprint.route("/profile")
def show_profile():
    # Check login authorization
    return flask.render_template("profile.html")
