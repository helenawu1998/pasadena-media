from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Sample User 1'}
    return render_template('index.html', user=user)
