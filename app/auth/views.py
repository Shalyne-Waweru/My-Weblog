from flask import render_template
from . import auth

# LOGIN PAGE
@auth.route('/login')
def login():

    '''
    View root page function that returns the login page and its data
    '''
    return render_template('auth/login.html')

# SIGNUP PAGE
@auth.route('/signup')
def signup():

    '''
    View root page function that returns the signup page and its data
    '''
    return render_template('auth/signup.html')