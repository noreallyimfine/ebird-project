from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired
from bird_app.util import birds, seasons, states, counties


class SightingForm(FlaskForm):
    bird = SelectField("Which bird did you see?",
                       choices=[(bird, bird) for bird in birds],
                       validators=[DataRequired()])
    season = SelectField("Which season was it?",
                         choices=[(season, season) for season in seasons],
                         validators=[DataRequired()])
    state = SelectField("Which state were you in?",
                        choices=[(state, state) for state in states],
                        validators=[DataRequired()])
    county = SelectField("Which county were you in?",
                         choices=[(county, county) for county in counties],
                         validators=[DataRequired()])
    submit = SubmitField("Check Rarity!")
