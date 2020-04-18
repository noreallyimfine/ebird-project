import pandas as pd
from flask import Flask, request, jsonify, render_template
from joblib import load
from bird_app.forms import SightingForm

app = Flask(__name__)

# Path here is relative, may get messed up in future
encoder = load("bird_app/utils/cat_boost.joblib")
model = load("bird_app/utils/rf.joblib")

# Load birds, seasons, and regions
birds_list = load('bird_app/utils/birds_list.joblib')
seasons_list = load('bird_app/utils/seasons_list.joblib')
regions_list = load('bird_app/utils/regions_list.joblib')

# convert list to dict for displaying through flask template
# (Hoping this isn't necessary for displaying all the birds)
birds = [{'bird': bird} for bird in birds_list]
seasons = [{'season': season} for season in seasons_list]
regions = [{'region': region} for region in regions_list]

# Dict to map results from model to english
labels = {0: "Common", 1: "Uncommon", 2: "Rare"}


def predict(data):
    # parse data
    bird = data['bird']
    season = data['season']
    region = data['region']
    # encode features
    X = pd.DataFrame({
        'name': [bird],
        'season': [season],
        'RegionName': [region]
    })
    print(X.shape)
    X_encoded = encoder.transform(X)
    # get prediction
    pred = model.predict(X_encoded)
    print("Prediction:", pred)
    return pred[0]


@app.route('/', methods=['GET', 'POST'])
def home():
    print("Method:", request.method)
    if request.method == 'GET':
        # TODO: Let them input county and state and the app will find the region
        # This is not a stretch goal because the regions aren't intuitive
        return render_template('home.html',
                               seasons=seasons,
                               birds=birds,
                               regions=regions)

    elif request.method == 'POST':
        # get values from post
        print(dir(request))
        data = request.json
        print(request.args)
        print(request.form_data_parser_class())
        print("Data", data)

        # Check all required values are in the data
        # If not, return error
        req_values = ['bird', 'season', 'region']
        if not all(value in data for value in req_values):
            message = """Error: Missing required features.
                         Needs ['bird', 'season', 'region']"""
            return message, 400

        # Pass to predict function
        pred = predict(data)
        label = labels[pred]
        msg = {'prediction': label}
        # TODO: return redirect to results route
        return jsonify(msg)


@app.route('/results', methods=['GET'])
def results():
    # TODO: Display prediction
    # Display image of bird
    # Display map of that birds prevalence
    pass


if __name__ == "__main__":
    app.run(debug=True)
