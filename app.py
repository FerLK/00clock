import os
from flask import Flask, render_template,url_for,redirect
from forms import AddForm,DelForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = "fer"

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir, 'data.sql') #found DB on root,in any os
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #turn off flask track

db = SQLAlchemy(app)

Migrate(app,db)

################################

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    password = db.Column(db.Text)
    work = db.relationship('Work', backref="nameRef", lazy='dynamic')

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return f"User -> {self.name} ; id -> {self.id};"

    def report_work(self):
        for wor in self.work:
            print(wor.work_name)

class Work(db.Model):
    __tablename__ = "works"

    id = db.Column(db.Integer, primary_key=True)
    work_name = db.Column(db.Text)
    work_time = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, time):
        self.work_name = name
        self.work_time = time

    def __repr__(self):
        return f"User -> {self.name} ; id -> {self.id};"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reg", methods = ['GET','POST'])
def register():
    form = AddForm()
    users = User.query.all()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        new_user = User(name, password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('list_users'))
    return render_template("register_user.html", all_users=users, form=form)


@app.route('/list')
def list_users():
    users = User.query.all()
    return render_template('list.html', all_users=users)


@app.route('/del', methods=['GET', 'POST'])
def delete_all():
    form = DelForm()
    users = User.query.all()
    if form.validate_on_submit():
        _id = form.id.data
        de = User.query.get(_id)
        db.session.delete(de)
        db.session.commit()
        return redirect(url_for('list_users'))
    return render_template('delete_all.html', all_users=users, form=form)

@app.route('/login', methods = ['GET','POST'])
def login():
    form = DelForm()
    if form.validate_on_submit():
        _id = form.id.data
        de = User.query.get(_id)
        db.session.delete(de)
        db.session.commit()
        return redirect(url_for('list_users'))
    return render_template('login.html', form=form)


if __name__ == "__main__":
    app.run(port=5000, debug=True)

