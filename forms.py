#!/usr/bin/python3


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('username',
                           validators=[DataRequired(), Length(min=8, max=30)])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('passwoard', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('sign up')


class LoginForm(FlaskForm):

    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('passwoard', validators=[DataRequired()])
    remember = BooleanField('remember me')
    submit = SubmitField('sign in')


if __name__ == "__main__":
    pass

# test
