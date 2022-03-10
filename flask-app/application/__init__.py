from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db = SQLAlchemy(app)

app.config["DATABASE_URI"] = "mysql+pymysql://root:password123@mysql:3306/app-db"

SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = SECRET_KEY

from application import routes