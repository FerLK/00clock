from flask import Blueprint, render_template, redirect, url_for
from project import db
from project.models import Work
from project.works.forms import AddForm

works_blueprint = Blueprint('works', __name__, template_folder='templates/users')


@works_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        new_work = Work(name)
        db.session.add(new_work)
        db.session.commit()

        return redirect(url_for('#'))
    return render_template("add_work.html", form=form)

