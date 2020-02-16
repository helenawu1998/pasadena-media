from flask import render_template, redirect, flash, url_for
from flask import current_app as app
from app.models import db, User, Profile, Course, Position, Production
from app.modules.profile.helpers import EditProfileForm
from app.modules.profile import blueprint
from flask_login import current_user

@blueprint.route("/profile")
def show_profile():
    #user, profile = get_user()
    #return render_template("profile.html", user=user, profile=profile)
    return render_template("profile.html")

@blueprint.route("/account", methods=['GET', 'POST'])
def show_account():
    if not current_user.is_authenticated or not current_user.profile:
        # TODO: error-handling
        return redirect(url_for('login.login'))

    profile = current_user.profile[0]
    form = EditProfileForm()
    if form.validate_on_submit():
        if form.edit_contact_email.data:
            profile.contact_email = form.edit_contact_email.data
        if form.edit_phone.data:
            profile.phone = form.edit_phone.data
        if form.edit_notes:
            profile.notes = form.edit_notes.data
        db.session.commit()
        flash('Your profile has been updated. ')
        return redirect(url_for('index'))
    #TODO: Add error-handling
    return render_template("account.html", title="Edit Profile",
        user=current_user, profile=profile, form=form)
