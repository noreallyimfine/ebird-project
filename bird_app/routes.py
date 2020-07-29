from flask import jsonify, request
from bird_app import app
from joblib import load


# Dict to map results from model to english
labels = {0: "Common", 1: "Uncommon", 2: "Rare"}

birds = load('bird_app/utils/birds_list.joblib')
seasons = load('bird_app/utils/seasons_list.joblib')

county_state_list = load('bird_app/utils/county_state.joblib')
counties = [x.split(',')[0] for x in county_state_list]
states = [x.split(',')[1] for x in county_state_list]


@app.route('/api/birds', methods=['GET'])
def get_birds():
    response = {
        'birds': birds
    }
    return jsonify(response)


@app.route('/api/seasons', methods=['GET'])
def get_seasons():
    response = {
        'seasons': seasons
    }
    return jsonify(response)


@app.route('/api/states', methods=['GET'])
def get_states():
    response = {
        'states': states
    }
    return jsonify(response)

@app.route('', methods=['GET', 'POST'])
def home():
    pass


if __name__ == "__main__":
    app.run(debug=True)