import os

from flask import Flask
from flask.ext import sqlalchemy
from flaskext import login, openid
import config

lm = login.LoginManager()
lm.setup_app(app)
old = openid.OpenID(app, os.path.join(config.basedir, 'tmp'))
app = Flask(__name__)
app.config.from_object('config')
db = sqlalchemy.SQLAlchemy(app)

from app import views, models
