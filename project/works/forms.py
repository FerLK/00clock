from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField


class AddForm(FlaskForm):

    name = StringField('name->')
    password = StringField('password->')
    submit = SubmitField('add user')


class DelForm(FlaskForm):

    id = IntegerField('ID - REMOVE:')
    submit = SubmitField('Remove')