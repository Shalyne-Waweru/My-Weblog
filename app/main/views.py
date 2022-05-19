from flask import render_template
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