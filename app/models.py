from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager

#Callback function that retrieves a user when a unique identifier is passed.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255),unique = True,index = True)
    username = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    #Define the relationship with the Blog model.
    blogs = db.relationship('Blog', backref = 'user', lazy = 'dynamic')
    #Define the relationship with the Comments model.
    comments = db.relationship('Comments', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'


class Blog(db.Model):
    __tablename__= 'blogposts'

    id = db.Column(db.Integer,primary_key = True)
    blog_pic_path = db.Column(db.String())
    title = db.Column(db.String(255))
    category = db.Column(db.String(255))
    description = db.Column(db.String())
    postedDate = db.Column(db.DateTime,default=datetime.now)

    #Create Foreign key column where we store the id of the user who wrote the blog post
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    #Define the relationship with the Comments model.
    comments = db.relationship('Comments', backref = 'comments', lazy = 'dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete_blog(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all_blogs(cls):
        blogs = Blog.query.all()
        return blogs

    @classmethod
    def get_blogs(cls,cat):
        blogs = Blog.query.filter_by(category=cat).all()
        return blogs

    def __repr__(self):
        return f"Blog Posts {self.description}','{self.postedDate}')"

class Comments(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    postedDate = db.Column(db.DateTime,default=datetime.now)
    #Create Foreign key column where we store the id of the Blog Post to be commented on
    blog_id = db.Column(db.Integer,db.ForeignKey("blogposts.id"))
    #Create Foreign key column where we store the id of the user that commented on the Blog Post
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_comments(cls,id):
        comments = Comments.query.filter_by(blog_id=id).all()
        return comments

class Quote:
    def __init__(self, id, author, quote):
        self.id = id 
        self.author = author
        self.quote = quote 