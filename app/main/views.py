from os import uname
from flask import render_template,redirect,url_for,flash,request,abort
from flask_login import login_required,current_user
from sqlalchemy import desc
from . import main
from ..models import User,Blog,Comments
from .. import db,photos,blogPhotos
from .forms import BlogForm,CommentForm

# LANDING PAGE
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    recent_posts = Blog.query.order_by(Blog.postedDate).limit(3).all()
    return render_template('index.html', recent_posts = recent_posts)

# CREATE POSTS PAGE
@main.route('/create', methods = ['GET','POST'])
@login_required
def create():

    '''
    View root page function that returns the create posts page and its data
    '''

    blog_form = BlogForm()

    if request.method == 'POST':

        if blog_form.validate_on_submit():

            #Get the inputted data
            filename = blogPhotos.save(blog_form.blog_pic_path.data)
            title = blog_form.title.data
            category = blog_form.category.data
            description = blog_form.description.data
                
            #Create a new_blog object and save it
            new_blog = Blog(blog_pic_path=filename, title=title, category=category, description= description, user_id=current_user.id)
            new_blog.save_blog()

            flash("Post Created Successfully!")

            return redirect(url_for('main.profile', uname = current_user.username))

        flash("Enter the Correct Details")

    return render_template('create.html',blog_form= blog_form)

# DISPLAY POSTS BY CATEGORY
@main.route('/category/<cat>')
def category(cat):
    '''
    function to return the blog posts by category
    '''

    category_posts = Blog.get_blogs(cat)

    return render_template('category.html', category_posts = category_posts)

#READ MORE REDIRECT
@main.route('/blog/<int:blog_id>', methods = ['GET','POST'])
def open_post(blog_id):
    '''
    function to return the blog posts by category
    '''
    blog_cat_post = Blog.query.first()

    blog_post = Blog.query.filter_by(id=blog_id).first()

    #Create an instance of the CommentForm class and name it comments_form
    comments_form = CommentForm()

    if request.method == 'POST':
        #The method returns True when the form is submitted and all the data has been verified by the validators
        if comments_form.validate_on_submit():
            #If True we gather the data from the form input fields
            comment = comments_form.comment.data

            #Create a new comment object and save it
            new_comment = Comments(comment=comment, blog_id=blog_id )
            new_comment.save_comment()

            return redirect(url_for('main.open_post',blog_id=blog_id))

    #Get all the Comments
    all_comments = Comments.get_comments(blog_id)

    return render_template('single-post.html', blog_post = blog_post, comments_form = comments_form,all_comments = all_comments,blog_cat_post = blog_cat_post)


#PROFILE PAGE
@main.route('/profile/<uname>')
@login_required
def profile(uname):
    '''
    View root page function that returns the profile page and its data
    '''

    #Query the database to find the user according to the username passed.
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    all_blogs = Blog.get_all_blogs()
    comments_count = Comments.query.count()

    return render_template("profile.html", user = user,all_blogs = all_blogs, comments_count = comments_count)

#UPDATE PROFILE PIC
@main.route('/profile/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):

    user = User.query.filter_by(username = uname).first()

    #Check if any parameter with the name photo has been passed into the request
    if 'photo' in request.files:
        #Save the file into our application
        filename = photos.save(request.files['photo'])

        #Create a path variable to where the file is stored
        path = f'photos/{filename}'

        #Update the profile_pic_path property in our user table and store the path to the file
        user.profile_pic_path = path
        db.session.commit()

        flash("Profile Updated Successfully!")

    return redirect(url_for('main.profile',uname=uname))