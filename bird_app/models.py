from bird_app import db


class States(db.Model):
    state = db.Column(db.Integer, primary_key=True)
