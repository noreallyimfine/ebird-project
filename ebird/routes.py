from flask import render_template
from ebird import app

@app.route('/')
@app.route('/home')
def home():
    # display nice home page
    return render_template('home.html', title='Home')


@app.route('/how_rare', methods=['GET', 'POST'])
def how_rare():
    return render_template('how_rare.html')
    pass