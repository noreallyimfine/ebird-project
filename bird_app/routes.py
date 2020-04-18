import pandas as pd
from flask import request, jsonify, render_template
from bird_app import app
from bird_app.forms import SightingForm
from bird_app.util import encoder, model, birds, seasons, regions

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
        # print(dir(request))
        # data = request.json
        # print(request.args)
        # print(request.form_data_parser_class())
        # print("Data", data)

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
