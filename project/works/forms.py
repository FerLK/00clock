from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from project.models import Work


class AddForm(FlaskForm):

    name = StringField('name->')
    password = StringField('password->')
    submit = SubmitField('add user')


class DelForm(FlaskForm):

    id = IntegerField('ID - REMOVE:')
    submit = SubmitField('Remove')


class RegistrationForm(FlaskForm):
    name = StringField('Name ->')
    submit = SubmitField('Register')

    # id = db.Column(db.Integer, primary_key=True)
    # work_name = db.Column(db.Text)
    # time_init = db.Column(db.DateTime)
    # time_final = db.Column(db.DateTime)
    # active = db.Column(db.Boolean, default=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))



    # password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='password wrong')])
    # pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    #
    # def validate_email(self, email):
    #     if User.query.filter_by(email=self.email.data).first():
    #         raise ValidationError('Email already registered')
    #
    # def validate_name(self, name):
    #     if User.query.filter_by(name=self.name.data).first():
    #         raise ValidationError('Username already registered')