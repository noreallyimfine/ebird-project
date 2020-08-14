from flask import render_template, redirect, url_for, jsonify, request
from ebird import app
from ebird.forms import RareForm
from ebird.models import Bird, State, County, Region, Lookup, Season


@app.route('/')
@app.route('/home')
def home():
    # display nice home page
    return render_template('home.html', title='Home')


def get_rareness(bird_sighting):
    region = Region.query.filter_by(county_id=bird_sighting['county']).first()
    season = Season.query.filter_by(id=bird_sighting['season']).first()
    bird = Bird.query.filter_by(id=bird_sighting['bird']).first()
    result = Lookup.query.filter_by(region=region.region,
                                    season=season.name,
                                    bird=bird.name).first()
    return result


def rareness_to_label(rareness):
    if rareness.pct_of_total > 0.005:
        return "Common"
    elif rareness.pct_of_total > 0.001:
        return "Uncommon"
    else:
        return "Rare"


@app.route('/how_rare', methods=['GET', 'POST'])
def how_rare():
    form = RareForm()
    form.county.choices = [(row.id, row.county_name) for row in County.query.all()] 
    if form.validate_on_submit():
        bird_sighting = {
            'bird': form.bird.data,
            'county': form.county.data,
            'state': form.state.data,
            'season': form.season.data
        }
        rareness = get_rareness(bird_sighting)
        result = rareness_to_label(rareness)
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
