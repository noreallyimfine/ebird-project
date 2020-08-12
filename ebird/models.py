from ebird import db


class Bird(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)

class State(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)


class County(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(25), db.ForeignKey('state.name'), nullable=False)
    county_name = db.Column(db.String(50), nullable=False)