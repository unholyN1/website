from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/generic/')
def generic():
    return render_template('generic.html', title='Home')

@app.route('/elements/')
def elements():
    return render_template('elements.html', title='Home')


