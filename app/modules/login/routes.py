import flask
from app.modules.login import blueprint

@blueprint.route("/login")
def login():
    # Check login authorization
    return flask.render_template("login.html")
