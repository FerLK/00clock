from project import app, db

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField

from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from project.models import User
from project.users.forms import LoginForm, RegistrationForm


class OtherForm(FlaskForm):
    name = StringField('name->')
    password = StringField('password->')
    email = StringField('email')
    submit = SubmitField('add user')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/welcome')
@login_required
def welcome_user():
    return "WELCOME"


@app.route('/login_user', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('logged success')

            next = request.args.get('next')
            if next == None or not next[0]=='/':
                next = url_for('welcome_user')

            return redirect(url_for("works.add"))

            # return redirect(url_for('welcome_user'))

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)