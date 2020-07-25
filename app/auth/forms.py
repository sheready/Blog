from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import Required, Email, EqualTo

from ..models import User



#registration form for new users
class RegistrationForm(FlaskForm):

    email = StringField('Enter Your Email Address', validators=[Required(), Email()])
    username = StringField('Enter User Name', validators=[Required()])
    password = PasswordField('Enter Password', validators=[Required(),
                                                     EqualTo('password_confirm', message='Passwords do not match!')])
    password_confirm = PasswordField('Confirm Passwords', validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('Email already exists')

    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('Username already taken')



#login form for already registered users
class LoginForm(FlaskForm):

    email = StringField('Email Address', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In') 