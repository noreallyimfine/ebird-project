from ebird import db


class Bird(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, unique=True)
    image_file = db.Column(db.String(20),
                           nullable=False,
                           default='default.jpg')

    def __repr__(self):
        return f"<Bird {self.id}: {self.name}>"


class State(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False, unique=True)
    counties = db.relationship('County', backref='county_state', lazy=True)

    def __repr__(self):
        return f"<State {self.id}: {self.name}>"


class County(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    county_name = db.Column(db.String(50), nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey('state.id'), nullable=False)
    region = db.relationship('Region', backref='region_county', lazy=True)

    def __repr__(self):
        return f"<County {self.id}: {self.county_name}, {self.state_id.name}>"


class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    county_id = db.Column(db.Integer,
                          db.ForeignKey('county.id'),
                          nullable=False)
    region = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<Region {self.id}: {self.region}>"


class Season(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False, unique=True)

    def __repr__(self):
        return f"<Season {self.id}: {self.name}>"


class Lookup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(20), nullable=False)
    season = db.Column(db.String(10), nullable=False)
    bird = db.Column(db.String(40), nullable=False)
    pct_of_total = db.Column(db.Numeric(5, 0), nullable=False)
