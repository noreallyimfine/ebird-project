from flask import render_template
from ebird import app

@app.route('/')
@app.route('/home')
def home():
    # display nice home page
    return render_template('home.html', title='Home')


@app.route('/rare_bird', methods=['GET', 'POST'])
def rare_bird():
    pass