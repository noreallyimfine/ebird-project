from bird_app import db


class Bird(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bird = db.Column(db.String(50), nullable=False, unique=True)


class State(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(20))
    counties = db.relationship('County', backref='state_lookup', lazy=True)


class County(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(20), db.ForeignKey('state.id'), nullable=False)
    county = db.Column(db.String(50), nullable=False)
