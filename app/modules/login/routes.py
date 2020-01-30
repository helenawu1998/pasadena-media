import flask
from app.modules.login import blueprint
from app.modules.login.helpers import LoginForm

@blueprint.route("/login")
def login():
    # Check login authorization
    form = LoginForm()
    return flask.render_template("login.html", title="Sign In", form=form)
