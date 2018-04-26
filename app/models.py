from . import db
from time import time
from datetime import date
from flask_login import UserMixin, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

class Posts(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    photo   = db.Column(db.String())
    caption = db.Column(db.String())
    created_on = db.Column(db.String())

    
class Likes(db.Model):
    likes_id        = db.Column(db.Integer, primary_key=True)
    user_id         = db.Column(db.Integer)
    post_id         = db.Column(db.Integer)
    
class Follows(db.Model):
    follow_id       = db.Column(db.Integer, primary_key=True)
    user_id         = db.Column(db.Integer)
    follower_id     = db.Column(db.Integer)

class Users(db.Model):
    user_id	        = db.Column(db.Integer, primary_key=True)
    username		= db.Column(db.String())
    password		= db.Column(db.String())
    email       	= db.Column(db.String())
    first_name  	= db.Column(db.String())
    last_name		= db.Column(db.String())
    profile_photo	= db.Column(db.String())
    biography	  	= db.Column(db.String())
    location	  	= db.Column(db.String())
    joined_on	    = db.Column(db.String())
    
    def __init__(self, username, password, first_name, last_name, email, photo, location, bio):
 		self.user_id 		= long(time())
 		self.email		 	= email
 		self.first_name 	= first_name
 		self.last_name 		= last_name
 		self.username 		= username
 		self.password 		= generate_password_hash(password)
 		self.profile_photo  = photo
		self.biography 		= bio
		self.location		= location
 		self.joined_on	= "{0:%A}, {0:%B} {0:%d}, 20{0:%y}".format(date.today())

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.user_id)  # python 2 support
        except NameError:
            return str(self.user_id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
