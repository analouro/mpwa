from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

app.config["SECRET_KEY"] = "today"

db = SQLAlchemy(app)

from application import routes