from flask import request, render_template, make_response
from flask import current_app as app
from app.models import db, User, Profile, Course, Position, Production
from app.modules.profile import blueprint

@blueprint.route("/profile")
def show_profile():
    # need to check login authorization
    user, profile = get_user()
    return render_template("profile.html", user=user, profile=profile)
@blueprint.route("/account")
def show_account():
    # need if not logged in, makes you login
    user, profile = get_user()
    return render_template("account.html", user=user, profile=profile)
def get_user():
    ''' Get a user's information. '''
    email = request.args.get('email')
    user = User.query.filter(User.email == email).first()
    contact_email = request.args.get('contact_email')
    profile = Profile.query.filter(Profile.contact_email == contact_email).first()
    return user, profile
