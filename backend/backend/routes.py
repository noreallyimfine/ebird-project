from flask import jsonify, request
from backend import app
from backend.models import Bird, County, State, Region, Season, Lookup


@app.route('/api/birds', methods=['GET'])
def birds():
    birds = Bird.query.all()
    response = {
        "birds": [bird.name for bird in birds]
    }
    return jsonify(response)


@app.route('/api/seasons', methods=['GET'])
def seasons():
    seasons = Season.query.all()
    response = {
        "seasons": [season.name for season in seasons]
    }
    return jsonify(response)


@app.route('/api/states', methods=['GET'])
def states():
    states = State.query.all()
    response = {
        "states": [state.name for state in states]
    }
    return jsonify(response)


@app.route('/api/counties', methods=['POST'])
def counties():
    data = request.get_json()
    state = data['state']
    state_id = State.query.filter_by(name=state).first()
    counties = County.query.filter_by(state_id=state_id.id).all()
    response = {
        'counties': [county.county_name for county in counties]
    }
    return jsonify(response)


def lookup_result(bird, season, region):
    # get pct of total from lookup table
    lookup = Lookup.query.filter_by(region=region, season=season, bird=bird).first()

    # if elif to decide string output
    if lookup.pct_of_total > 0.005:
        return "Common"
    elif lookup.pct_of_total > 0.001:
        return "Uncommon"
    else:
        return "Rare"


@app.route('/api/results', methods=['POST'])
def results():
    data = request.get_json()

    bird = data['bird']
    season = data['season']

    state = State.query.filter_by(name=data['state']).first()
    county = County.query.filter_by(county_name=data['county'], state_id=state.id).first()
    region = Region.query.filter_by(county_id=county.id).first()

    result = lookup_result(bird, season, region.region)

    response = {
        'result': result
    }
    return jsonify(response)
