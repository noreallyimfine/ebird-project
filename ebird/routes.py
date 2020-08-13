from flask import render_template, redirect, url_for
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
    if form.validate_on_submit():
        bird = form.bird.data,
        county = form.county.data,
        state = form.state.data,
        season = form.season.data
        return redirect(url_for('results',
                                bird=bird,
                                county=county,
                                state=state,
                                season=season))
    return render_template('how_rare.html', form=form)


@app.route('/results/<string:bird>/<string:county>/<string:state>/<string:season>')
def results(bird, county, state, season):
    return render_template('results.html', title='Results')

