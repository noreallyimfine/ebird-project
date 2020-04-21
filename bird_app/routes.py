import pandas as pd
from flask import request, jsonify, render_template
from bird_app import app
from bird_app.forms import SightingForm
from bird_app.util import encoder, model, birds, seasons, regions

# Dict to map results from model to english
labels = {0: "Common", 1: "Uncommon", 2: "Rare"}


def predict(form):
    # parse data
    bird = form.bird.data
    season = form.season.data
    state = form.state.data
    county = form.county.data
    
    # TODO: Map State,county to region
    region = county + state
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
    form = SightingForm()
    if form.validate_on_submit():
        # Pass to predict function
        pred = predict(form)
        label = labels[pred]
        msg = {'prediction': label}
        # TODO: return redirect to results route
        return (msg)
    return render_template('home.html', form=form)


@app.route('/results', methods=['GET'])
def results():
    # TODO: Display prediction
    # Display image of bird
    # Display map of that birds prevalence
    pass


if __name__ == "__main__":
    app.run(debug=True)
