import flask

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
# from wtforms.validators import Email
from wtforms.widgets import TextArea

class EditProfileForm(FlaskForm):
    edit_preferred_name = StringField('Preferred name:')
    edit_contact_email = StringField('Contact email:')
    edit_phone = StringField('Contact phone:')
    edit_notes = StringField('Profile description:', widget=TextArea())
    edit_positions = StringField('Position(s):')
    edit_courses = StringField('Classes:')
    submit = SubmitField('Submit changes')

def deserialize(lst_str):
    if lst_str == "" or lst_str.strip() == "":
        return []
    lst = lst_str.split(",")
    lst = [item.strip() for item in lst]
    return lst

def serialize_positions(lst):
    if not lst:
        return ""
    lst = [item.position_name for item in lst]
    return ", ".join(lst)

def serialize_courses(lst):
    if not lst:
        return ""
    lst = [item.course_name for item in lst]
    return ", ".join(lst)
