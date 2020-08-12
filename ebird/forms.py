from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired
from ebird.models import Bird

birds = Bird.query.all()

class RareForm(FlaskForm):
    bird = SelectField('Which bird did you see?',
                       validators=[DataRequired()],
                       choices=[(b.name, b.name) for b in birds])
    submit = SubmitField('How rare?')