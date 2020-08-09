from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ
# from decouple import config

app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from bird_app import routes
