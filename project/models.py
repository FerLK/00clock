#set up dn inside __init__.py
from project import db

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