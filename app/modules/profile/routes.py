from flask import render_template, redirect, flash, url_for
from flask import current_app as app
from app.models import db, User, Profile, Course, Position, Production
from app.modules.profile.helpers import EditProfileForm, \
    serialize_positions, serialize_courses, deserialize
from app.modules.profile import blueprint
from flask_login import current_user

@blueprint.route("/profile", methods=['GET'])
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
    positions = profile.positions
    courses = profile.courses
    form = EditProfileForm()
    if form.validate_on_submit():
        if form.edit_preferred_name.data:
            profile.preferred_name = form.edit_preferred_name.data
        if form.edit_contact_email.data:
            profile.contact_email = form.edit_contact_email.data
        if form.edit_phone.data:
            profile.phone = form.edit_phone.data
        if form.edit_notes:
            profile.notes = form.edit_notes.data

        edit_positions = deserialize(form.edit_positions.data)
        if edit_positions:
            for position in positions:
                db.session.delete(position)
        for position in edit_positions:
            db.session.add(Position(profile_id=profile.id, position_name=position))

        edit_courses = deserialize(form.edit_courses.data)
        if edit_courses:
            for course in courses:
                db.session.delete(course)
        for course in edit_courses:
            db.session.add(Course(profile_id=profile.id, course_name=course))
        db.session.commit()
        flash('Your profile has been updated. ')
        return redirect(url_for('index'))
    #TODO: Add error-handling
    return render_template("account.html", title="Edit Profile",
        user=current_user, profile=profile, positions=serialize_positions(positions),
        courses=serialize_courses(courses), form=form)
