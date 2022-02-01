import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


login_manager = LoginManager()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir, 'data.sql') #found DB on root,in any os
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #turn off flask track

db = SQLAlchemy(app)

Migrate(app,db)

login_manager.init_app(app)
login_manager.login_view = 'login'

from project.users.views import users_blueprint
from project.works.views import works_blueprint

app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(works_blueprint, url_prefix='/works')



