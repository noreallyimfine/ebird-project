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
        # STRETCH: Let them input county and state and the app will find the county
        return "You are home"
    elif request.method == 'POST':
        # get values from post
        data = request.get_json()
        print(data)
        # Pass to predict function
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
