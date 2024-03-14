from flask_wtf import FlaskForm
from flask_wtf.file import FileField, file_allowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User, Post
from flask_login import current_user


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("That username is taken. Please choose a different one.")
        
    def validate_email(self, email_to_check):
        user = User.query.filter_by(email=email_to_check.data).first()
        if user:
            raise ValidationError("That email is taken. Please choose a different one.")


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update your profile picture', validators=[file_allowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username_to_check):
        if current_user.username != username_to_check.data:
            user = User.query.filter_by(username=username_to_check.data).first()
            if user:
                raise ValidationError("That username is taken. Please choose a different one.")
        
    def validate_email(self, email_to_check):
        if current_user.email != email_to_check.data:
            user = User.query.filter_by(email=email_to_check.data).first()
            if user:
                raise ValidationError("That email is taken. Please choose a different one.")