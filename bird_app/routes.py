from flask import render_template, request, redirect, url_for
from bird_app import app
from bird_app.forms import SightingForm
from bird_app.predict import rare_pred


# Dict to map results from model to english
labels = {0: "Common", 1: "Uncommon", 2: "Rare"}


@app.route('/', methods=['GET', 'POST'])
def home():
    form = SightingForm()
    if request.method == 'POST':
        # Pass to predict function
        pred = rare_pred(form)
        label = labels[pred]
        # TODO: return redirect to results route
        return redirect(url_for('results', label=label))
    return render_template('home.html', form=form)


@app.route('/results', methods=['GET'])
def results():
    # TODO: Display prediction
    # Display image of bird
    # Display map of that birds prevalence
    pass


if __name__ == "__main__":
    app.run(debug=True)
