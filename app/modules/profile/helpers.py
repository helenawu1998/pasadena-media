import flask

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Email
from wtforms.widgets import TextArea

class EditProfileForm(FlaskForm):
    edit_contact_email = StringField('Contact email:', validators=[Email()])
    edit_phone = StringField('Contact phone:')
    edit_notes = StringField('Profile description:', widget=TextArea())
    submit = SubmitField('Submit changes')
