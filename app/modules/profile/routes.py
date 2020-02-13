from flask import request, render_template, make_response, redirect
from flask import current_app as app
from app.models import db, User, Profile, Course, Position, Production
from app.modules.profile import blueprint
from flask_login import current_user

@blueprint.route("/profile")
def show_profile():
    #user, profile = get_user()
    #return render_template("profile.html", user=user, profile=profile)
    return render_template("profile.html")
@blueprint.route("/account")
def show_account():
    if current_user.is_authenticated:
        if current_user.profile:
            profile = current_user.profile[0]
        return render_template("account.html", user=current_user, profile=profile)
    return redirect(url_for('login.login'))
    #user, profile = get_user()

'''def get_user():
    # Get a user's information.
    email = request.args.get('email')
    user = User.query.filter(User.email == email).first()
    contact_email = request.args.get('contact_email')
    profile = Profile.query.filter(Profile.contact_email == contact_email).first()
    return user, profile'''
