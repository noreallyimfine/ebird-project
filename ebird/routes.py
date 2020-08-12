from flask import render_template
from ebird import app
from ebird.forms import RareForm

@app.route('/')
@app.route('/home')
def home():
    # display nice home page
    return render_template('home.html', title='Home')


@app.route('/how_rare', methods=['GET', 'POST'])
def how_rare():
    form = RareForm()
    return render_template('how_rare.html', form=form)