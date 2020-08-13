from ebird import db


class Bird(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)

class State(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    counties = db.relationship('County', backref='county_state', lazy=True)


class County(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(25), db.ForeignKey('state.id'), nullable=False)
    county_name = db.Column(db.String(50), nullable=False)
    region = db.relationship('Region', backref='region_county', lazy=True)

class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    county_id = db.Column(db.String(50), db.ForeignKey('county.id'), nullable=False)
    state = db.Column(db.String(25), nullable=False)
    region = db.Column(db.String(20), nullable=False)

class Season(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)