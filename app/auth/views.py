from flask import render_template,redirect,url_for,flash,request
from ..models import User
from .forms import SignupForm,LoginForm
from flask_login import login_user,logout_user,login_required
from . import auth
from .. import db

#LOGIN PAGE
@auth.route('/login',methods=['GET','POST'])
def login():
    '''
    View root page function that returns the signup page and its data
    '''

    # # Create the form instance and pass it into our template
    login_form = LoginForm()

    if request.method == 'POST':
        if login_form.validate_on_submit():
            #Get the email and password inputted
            email = login_form.email.data
            password = login_form.password.data

            #Search for a user from our database with the email we receive from the form
            user = User.query.filter_by(email=email).first()

            #Confirm that the password entered matches with the password hash stored in the database.
            if user is not None and user.verify_password(password):
                #The login_user function records the user as logged for that current session
                login_user(user)

                flash("Logged In Successfully!")

                return redirect(request.args.get('next') or url_for('main.profile'))

            flash('Invalid Email or Password')

        flash("Invalid Email or Password")

    return render_template('auth/login.html',login_form = login_form)

# SIGNUP PAGE
@auth.route('/signup',methods = ["GET","POST"])
def signup():

    '''
    View root page function that returns the signup page and its data
    '''

    signup_form = SignupForm()

    if request.method == 'POST':
        if signup_form.validate_on_submit():
            #Get the inputted email address
            email = signup_form.email.data

            #Check if there is an existing user with that email address
            user_email = User.query.filter_by(email=email).first()
            if user_email:
                flash("There is an account with that email!")
                return render_template('auth/signup.html', signup_form=signup_form)

            #Get the inputted username  
            username = signup_form.username.data

            #Check if there is an existing user with that username
            user_username = User.query.filter_by(username=username).first()
            if user_username:
                flash("There is an account with that username!")
                return render_template('auth/signup.html', signup_form=signup_form)

            #Get the inputted password
            password = signup_form.password.data

            user = User(username=username, email=email, password=password)
            db.session.add(user)
            db.session.commit()

            flash("Account created successfully!")

            return redirect(url_for('auth.login'))

        flash("Incorrect email or password. Please try again")

    return render_template('auth/signup.html',signup_form = signup_form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))