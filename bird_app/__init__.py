from flask import Flask
from os import environ
# from decouple import config

app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')

from bird_app import routes
