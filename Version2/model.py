from wtforms import SubmitField, BooleanField, StringField, PasswordField, validators, IntegerField
import email_validator
from flask_wtf import Form


class DonForm(Form):
    name_first = StringField('First Name', [validators.DataRequired()])
    name_last = StringField('Last Name', [validators.DataRequired()])
    email = StringField('Email Adress',
                        [validators.DataRequired(), validators.Email(), validators.Length(min=6, max=35)])
    money = IntegerField('Gift', [validators.DataRequired(), validators.NumberRange(min=0.5, max=10000)])
    checkbox = BooleanField('I Agree', [validators.DataRequired()])


class RegForm(Form):
    name_first = StringField('First Name', [validators.DataRequired()])
    name_last = StringField('Last Name', [validators.DataRequired()])
    email = StringField('Email Address',
                        [validators.DataRequired(), validators.Email(), validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm',
                           message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Submit')


class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')
