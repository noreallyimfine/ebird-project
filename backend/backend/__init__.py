import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()

db_url = os.getenv("DATABASE_URL")
pg_user = os.getenv("DATABASE_USER")
pg_pass = os.getenv("DATABASE_PW")
db_name = os.getenv("DATABASE_NAME")


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{pg_user}:{pg_pass}@{db_url}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from backend import routes
