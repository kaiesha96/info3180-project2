from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, TextAreaField
from wtforms.validators import InputRequired, Length, Regexp, Required, DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed



class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    firstname = StringField('First-name', validators=[InputRequired()])
    lastname = StringField('Last-name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    biography = TextAreaField('Biography',validators=[InputRequired()])
    photo= FileField('Profile Photo',validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])
    
    
    
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
     
 
class PostForm(FlaskForm):
    photo = FileField('Profile Picture',validators=[FileRequired(),FileAllowed(['png', 'jpg', 'jpeg', 'gif','Images only!'])])
    caption=TextAreaField('Caption', validators=[DataRequired()])