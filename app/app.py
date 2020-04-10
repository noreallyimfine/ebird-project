from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    print("Method:", request.method)
    if request.method == 'GET':
        return "You are home"
    elif request.method == 'POST':
        return "Thank you for posting"
    # return "You are home"


if __name__ == "__main__":
    app.run(debug=True)