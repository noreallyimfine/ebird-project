from bird_app import db


class State(db.Model):
    state = db.Column(db.String(20), primary_key=True)


