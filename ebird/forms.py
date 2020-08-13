from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired
from ebird.models import Bird, State, County, Season

birds = Bird.query.all()
states = State.query.all()
counties = County.query.all()
seasons = Season.query.all()


class RareForm(FlaskForm):
    bird = SelectField('Choose a Bird',
                       validators=[DataRequired()],
                       choices=[(b.name, b.name) for b in birds])
    state = SelectField('Choose a State',
                        validators=[DataRequired()],
                        choices=[(s.name, s.name) for s in states])
    county = SelectField('Choose a County',
                         validators=[DataRequired()])
    season = SelectField('Choose a Season',
                         validators=[DataRequired()],
                         choices=[(s.name, s.name) for s in seasons])
    submit = SubmitField('How rare?')
