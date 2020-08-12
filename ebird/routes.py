from flask import render_template
from ebird import app
from ebird.forms import RareForm
from ebird.models import County

@app.route('/')
@app.route('/home')
def home():
    # display nice home page
    return render_template('home.html', title='Home')


@app.route('/how_rare', methods=['GET', 'POST'])
def how_rare():
    # state = State.query.get(form.state.data)
    form = RareForm()
    form.county.choices = [(row.county_name, row.county_name) for row in County.query.all()] 
    return render_template('how_rare.html', form=form)