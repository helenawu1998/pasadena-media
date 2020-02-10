import flask
from app.modules.login import blueprint
from app.modules.login.helpers import LoginForm
from app.modules.login.helpers import RegisterForm
from app.modules.login import helpers
from app import db
from app.models import User, Profile

@blueprint.route("/login", methods=['GET', 'POST'])
def login():
    # Check login authorization
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flask.flash('Invalid username or password')
            return redirect(url_for('login'))
        flask.flash('Successful login for user {}'.format(form.username.data))
        return flask.redirect('/index')
    return flask.render_template("login.html", title="Sign In", form=form)

@blueprint.route("/register", methods=['GET', 'POST'])
def register():
    # Hide this url later
    form = RegisterForm()
    if form.validate_on_submit():
        # Create account and store user and profile info in database
        user = User(email=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        profile = Profile(user_id = user.id, contact_email=form.username.data,
            first_name = form.first_name.data, last_name = form.last_name.data)
        db.session.add(profile)
        db.session.commit()
        flask.flash('Registered new user {} {}'.format(
            form.first_name.data, form.last_name.data))
        return flask.redirect('/index')
    return flask.render_template("register.html", title="Register", form=form)
