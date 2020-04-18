from flask import Flask

app = Flask(__name__)

from bird_app import routes
