import flask
from app.modules.profile import blueprint

@blueprint.route("/profile")
def show_profile():
    # Check login authorization
    return flask.render_template("profile.html")
@blueprint.route("/account")
def show_account():
    # If not logged in, makes you login
    return flask.render_template("account.html")
