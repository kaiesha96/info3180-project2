from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, TextAreaField
from wtforms.validators import InputRequired, Length, Regexp, Required

class RegisterForm(FlaskForm):
    first_name = StringField("Firstname", validators = [InputRequired()], render_kw = {'placeholder' : 'First Name'})
    last_name = StringField("Lastname", validators = [InputRequired()], render_kw = {'placeholder' : 'Last Name'})
    username = StringField("Username", validators = [InputRequired()], render_kw = {'placeholder' : 'Username'})
    password = PasswordField("Password", validators = [InputRequired()], render_kw = {'placeholder' : 'Password'})
    email = StringField("Email", validators = [InputRequired()], render_kw = {'placeholder' : 'Email'})
    biography = TextAreaField("Biography", validators = [InputRequired()], render_kw = {'placeholder' : 'Biography'})
    location = StringField("Location", validators = [InputRequired()], render_kw = {'placeholder' : 'Location'})
    profile_photo = FileField('Profile Photo', validators = [])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
     
 