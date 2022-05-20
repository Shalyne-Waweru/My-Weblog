from flask import render_template
from flask_login import login_required
from . import main

# LANDING PAGE
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

# TRAVEL POSTS PAGE
@main.route('/travel')
def travel():

    '''
    View root page function that returns the travel posts page and its data
    '''
    return render_template('travel.html')

# LIFESTYLE POSTS PAGE
@main.route('/lifestyle')
def lifestyle():

    '''
    View root page function that returns the lifestyle posts page and its data
    '''
    return render_template('lifestyle.html')

# CREATE POSTS PAGE
@main.route('/create')
@login_required
def create():

    '''
    View root page function that returns the create posts page and its data
    '''
    return render_template('create.html')

# PROFILE PAGE
@main.route('/profile')
@login_required
def profile():

    '''
    View root page function that returns the profile page and its data
    '''
    return render_template('profile.html')
