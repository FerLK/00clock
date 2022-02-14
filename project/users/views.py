from flask import Blueprint, render_template, redirect, url_for
from project import db
from project.models import User, Work
from project.users.forms import AddForm, DelForm
from flask_login import login_user, login_required, logout_user, current_user

users_blueprint = Blueprint('users', __name__, template_folder='templates/users')


@users_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    error = None
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        #!!! Verificar se ha registro igual
        # data = UserRegister.parser.parse_args()
        #
        # if UserModel.find_by_username(data['username']):
        #     return {"message": "name already taken"}, 400


        new_user = User(name, email, password)
        db.session.add(new_user)
        db.session.commit()

        user = User.query.filter_by(email=form.email.data).first()
        login_user(user)

        return redirect(url_for('works.add'))

    return render_template("add_user.html", form=form, error=error)


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
    works = Work.query.all()
    return render_template("list_users.html", all_users=users, all_works = works)


@users_blueprint.route('/profile')
@login_required
def profile_users():
    works = Work.query.filter_by(user_id=current_user.id)
    alltime_work = Work.query.filter_by(user_id=current_user.id).count()
    return render_template("profile.html", alltime_work=alltime_work, name=current_user.name,
                           id_=current_user.id, working=current_user.working, all_works=works)

