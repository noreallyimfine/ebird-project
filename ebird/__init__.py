from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "SOME STRING"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"

