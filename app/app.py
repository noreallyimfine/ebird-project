from flask import Flask, request
from joblib import load

app = Flask(__name__)

# TODO: load pickled encoder and model
# Path here is relative, may get messed up in future
encoder = load("sample\\cat_boost.joblib")
# model = load("sample\\rf.joblib")


def predict(data):
    # TODO: 
    # parse data
    name = data['name']
    season = data['season']
    region = data['region']
    # encode features
    X = [name, season, region]
    X_encoded = encoder.transform(X)
    
    # get prediction
    pass


@app.route('/', methods=['GET', 'POST'])
def home():
    print("Method:", request.method)
    if request.method == 'GET':
        # TODO: Display dropdowns to choose bird, season, and region
        # STRETCH: Let them input county and state and the app will find the region
        return "You are home"

    elif request.method == 'POST':
        # get values from post
        data = request.get_json()
        print("Data", data)

        # Check all required values are in the data
        # If not, return error
        req_values = ['name', 'season', 'region']
        if not all(value in data for value in req_values):
            message = """Error: Missing required features. 
                         Needs ['name', 'season', 'region']"""
            return message, 400

        # Pass to predict function
        pred = predict(data)
        # return redirect to results route
        return "Thank you for posting"


@app.route('/results', methods=['GET'])
def results():
    # TODO: Display prediction
    # Display image of bird
    # Display map of that birds prevalence
    pass


if __name__ == "__main__":
    app.run(debug=True)
