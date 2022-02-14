from flask import Blueprint, render_template, redirect, url_for, request
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
    time = datetime.now()
    try:
        id_ = current_user.id
        user_work = User.query.get(id_)
        work_final = Work.query.filter_by(user_id=current_user.id).order_by(Work.id.desc()).first()
        time = datetime.now() - work_final.time_init
        if work_final.time_init.strftime("%x") == datetime.now().strftime("%x") and not user_work.working:
            return render_template('index.html', actives=False)
            pass

    except:
        pass

    if request.method == "POST":
        id_ = current_user.id
        user_work = User.query.get(id_)

        if not user_work.working:
            user_work.working = True
            name = request.form.get("name")
            local = request.form.get("local")
            time_init = datetime.now()
            new_work = Work(name,local, id_, time_init)
            db.session.add(new_work)
        else:
            user_work.working = False
            work_final.time_final = datetime.now()
            db.session.add(work_final)
        db.session.add(user_work)
        db.session.commit()

        return redirect(url_for("works.add"))
    return render_template("add_work.html", time=time, form=form, works=works, active=current_user.working, name=current_user.name)


@works_blueprint.route('/profile_work', methods=['GET', 'POST'])
@login_required
def profile_work():
    works = Work.query.filter_by(user_id=current_user.id)
    form = RegistrationForm()
    time = datetime.now()

    if False:
        return redirect(url_for("works.add"))
    return render_template("profile_work.html")
