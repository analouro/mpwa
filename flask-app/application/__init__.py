from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")

SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = SECRET_KEY

from application import routes