from . import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255),unique = True,index = True)
    username = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'