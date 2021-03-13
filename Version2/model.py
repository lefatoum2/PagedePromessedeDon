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


