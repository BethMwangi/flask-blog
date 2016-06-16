#imports

from flaskblog import app, db, login_manager
from flask import render_template, request, flash, url_for, g, session, redirect



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')