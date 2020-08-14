from flask import render_template, redirect, url_for
from ebird import app
from ebird.forms import RareForm
from ebird.models import County
from ebird.utils import get_rareness, rareness_to_label


@app.route('/')
@app.route('/home')
def home():
    # display nice home page
    return render_template('home.html', title='Home')


@app.route('/how_rare', methods=['GET', 'POST'])
def how_rare():
    form = RareForm()
    form.county.choices = [(row.id, row.county_name) for row in County.query.filter_by(state_id=1).all()]
    if form.validate_on_submit():
        bird_sighting = {
            'bird': form.bird.data,
            'county': form.county.data,
            'season': form.season.data
        }
        rareness = get_rareness(bird_sighting)
        result = rareness_to_label(rareness)
        return redirect(url_for('results', result=result))
    return render_template('how_rare.html', form=form)


@app.route('/results/<string:result>')
def results(result):
    return render_template('results.html',
                           title='Results',
                           result=result)
