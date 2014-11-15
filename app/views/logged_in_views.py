import datetime

from flask import render_template, flash, redirect, url_for
from flask.ext.login import login_required, current_user
from flask.ext.mail import Message

from app import app, db
from ..models import User, Person

@app.route('/home')
@login_required
def home():
    return render_template('logged_in/home.html', title='Home', current_user=current_user)

@app.route('/upload')
@login_required
def upload():
    return render_template('logged_in/upload.html', title='Upload Pictures', current_user=current_user)

@app.route('/my/groups')
@login_required
def groups():
    return render_template('logged_in/my_groups.html', title='My Groups', current_user=current_user)

@app.route('/my/pictures')
@login_required
def groups():
    return render_template('logged_in/my_pictures.html', title='My Groups', current_user=current_user)