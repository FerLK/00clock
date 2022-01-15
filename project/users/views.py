from flask import Blueprint, render_template, redirect, url_for
from project import db
from project.models import User
from project.users.forms import AddForm, DelForm

users_blueprint = Blueprint('users', __name__, template_folder='templates/users')


@users_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        new_user = User(name, password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('users.list_users'))
    return render_template("add_user.html", form=form)


@users_blueprint.route('/del', methods=['GET', 'POST'])
def del_():
    form = DelForm()
    if form.validate_on_submit():
        _id = form.id.data
        new_user = User.query.get(_id)
        db.session.delete(new_user)
        db.session.commit()

        return redirect(url_for('users.list_users'))
    return render_template("delete_user.html", form=form)


@users_blueprint.route('/list')
def list_users():
    users = User.query.all()
    return render_template("list_users.html", all_users=users)
