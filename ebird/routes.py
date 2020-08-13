from flask import render_template, redirect, url_for, jsonify, request
from ebird import app
from ebird.forms import RareForm
from ebird.models import Bird, State, County, Region

lookup = {
    "Abert's Towhee": {
        "Autauga": {
            "Alabama": {
                "Winter": "Rare"
            }
        }
    }
}

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
    if form.validate_on_submit():
        bird_sighting = {
            'bird': form.bird.data,
            'county': form.county.data,
            'state': form.state.data,
            'season': form.season.data
        }
        result = lookup[form.bird.data][form.county.data][form.state.data][form.season.data]

        return redirect(url_for('results', result=result))
    return render_template('how_rare.html', form=form)


@app.route('/results/<string:result>')
def results(result):
    # query db to get the necessary objects
    # bird_obj = Bird.query.filter_by(id=bird).first()
    # state_obj = State.query.filter_by(id=state).first()
    # county_obj = County.query.filter_by(id=county).first()
    # get region
    # region = Region.query.filter_by(county_id=county).first()

    # execute query on lookup table
    # convert number to label
    return render_template('results.html',
                           title='Results',
                           result=result)
