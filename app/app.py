from flask import Flask, request


app = Flask(__name__)

# TODO: load pickled encoder and model

def predict(data):
    # TODO: 
    # parse data
    # encode features
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
        # Pass to predict function
        req_values = ['name', 'season', 'region']
        # Check all required values are in the data
        # If not, return error
        if not all(value in data for value in req_values):
            message = """Error: Missing required features. 
                         Needs ['name', 'season', 'region']"""
            return message, 400
        pred = predict(data)
        # return redirect to results route
        return "Thank you for posting"
    # return "You are home"


@app.route('/results', methods=['GET'])
def results():
    # TODO: Display prediction
    # Display image of bird
    # Display map of that birds prevalence
    pass


if __name__ == "__main__":
    app.run(debug=True)
