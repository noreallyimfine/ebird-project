from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired


class SightingForm(FlaskForm):
    bird = SelectField("Which bird did you see?", validators=[DataRequired()])
    season = SelectField("Which season was it?", validators=[DataRequired()])
    state = SelectField("Which state were you in?", validators=[DataRequired()])
    county = SelectField("Which county were you in?", validators=[DataRequired()])
    submit = SubmitField("Check Rarity!")
