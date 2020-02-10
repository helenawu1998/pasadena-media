import flask

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError
from app.models import User

# Credit to https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
class LoginForm(FlaskForm):
    username = StringField('User Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField('User Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Register Me')

    def validate_username(self, username):
        user = User.query.filter_by(email=username.data).first()
        if user is not None:
            raise ValidationError('Invalid: user email already exists.')
