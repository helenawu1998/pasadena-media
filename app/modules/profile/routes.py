import flask
from app.modules.profile import blueprint

@blueprint.route("/profile")
def show_profile():
    # Check login authorization
    return flask.render_template("profile.html")
