from flask import Blueprint, render_template, redirect, url_for
from project import db
from project.models import Work, User
from project.works.forms import AddForm, RegistrationForm
from flask_login import login_user, login_required, logout_user, current_user
from datetime import datetime

works_blueprint = Blueprint('works', __name__, template_folder='templates/works')


@works_blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    works = Work.query.filter_by(user_id=current_user.id)
    form = RegistrationForm()


    if form.validate_on_submit():
        id_ = current_user.id
        user_work = User.query.get(id_)
        if not user_work.working:
            user_work.working = True
            name = form.name.data
            time_init = datetime.now()
            new_work = Work(name, id_, time_init)
            db.session.add(new_work)
        else:
            user_work.working = False
            name = form.name.data
            work_final = Work.query.order_by(Work.id.desc()).first() #User.query.filter_by(username='admin').first() query(ObjectRes).order_by(ObjectRes.id.desc()).first()
            work_final.time_final = datetime.now()
            db.session.add(work_final)
        db.session.add(user_work)
        db.session.commit()

        return render_template('index.html')
    return render_template("add_work.html", form=form, works=works, active=current_user.working, name=(current_user.name, current_user.id))


    # work_name = db.Column(db.String(64), index=True)
    # time_init = db.Column(db.String(64), index=True)
    # time_final = db.Column(db.String(64), index=True)
    # active = db.Column(db.Boolean, default=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
