from . import db
from time import time
from datetime import date
from flask_login import UserMixin, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

class Posts(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    photo   = db.Column(db.String(255))
    caption = db.Column(db.String(80))
    created_on = db.Column(db.String(80))
    
    
    def __init__(self, id, user_id, photo, caption, created_on):
        self.user_id = user_id
        self.photo = photo
        self.caption = caption
        self.created_on = created_on


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    email = db.Column(db.String(80))
    location=db.Column(db.String(80))
    biography=db.Column(db.String(255))
    profile_photo=db.Column(db.String(255))
    joined_on=db.Column(db.String(80))

    
    def __init__(self, username, password, firstname, lastname, email, location, biography, profile_photo, joined_on):
        self.username = username
        self.password = generate_password_hash(password)
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.location = location
        self.biography = biography
        self.profile_photo = profile_photo
        self.joined_on = "{0:%A}, {0:%B} {0:%d}, 20{0:%y}".format(date.today())
    
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

    
class Likes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True)
    post_id = db.Column(db.Integer, unique=True)
    
    def __init__(self,post_id,user_id):
        self.user_id = user_id
        self.post_id = post_id
    
class Follows(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    user_id         = db.Column(db.Integer)
    follower_id     = db.Column(db.Integer)

    def __init__(self,user_id, follower_id):
        self.user_id=user_id
        self.follower_id=follower_id

    
