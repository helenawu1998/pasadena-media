from flask import render_template
from app import app
from flask_login import current_user

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
