from flask import render_template, request, redirect, url_for
from bird_app import app, db
from bird_app.forms import SightingForm
from bird_app.lookup import rareness_lookup
from bird_app.models import State


# Dict to map results from model to english
labels = {0: "Common", 1: "Uncommon", 2: "Rare"}


@app.route('/', methods=['GET', 'POST'])
def home():
    form = SightingForm()
    if request.method == 'POST':
        # Pass to predict function
        label = rareness_lookup(form)
        # TODO: return redirect to results route
        return render_template('results.html', label=label)
    return render_template('home.html', form=form)


@app.route('/states', methods=['GET'])
def states():
    states = State.query.all()
    return render_template('states.html', states=states)


@app.route('/results', methods=['GET'])
def results():
    # TODO: Display prediction
    # Display image of bird
    # Display map of that birds prevalence
    pass


if __name__ == "__main__":
    app.run(debug=True)
