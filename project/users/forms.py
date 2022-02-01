from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from project.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='password wrong')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Email already registered')

    def validate_name(self, name):
        if User.query.filter_by(name=self.name.data).first():
            raise ValidationError('Username already registered')


class AddForm(FlaskForm):

    name = StringField('name->')
    password = StringField('password->')
    email = StringField('email')
    submit = SubmitField('add user')


class DelForm(FlaskForm):

    id = IntegerField('ID - REMOVE:')
    submit = SubmitField('Remove')