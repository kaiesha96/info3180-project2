"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
from forms import RegisterForm, LoginForm
from models import Posts, Users, Likes, Follows


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/api/users/register', methods = ['POST','GET'])
def register():
    form = RegisterForm()
    error = None
    # return render_template('register.html',form=form)
    if request.method == "POST":
        if form.validate_on_submit():
            if(Users.query.filter_by(email = form.email.data).first()):
                error = "Email already in use."
            else:
                target = os.path.join('./app/static','uploads/')
                print (target)
        
                if not os.path.isdir(target):
                    os.mkdir(target)
                
                photo       = form.profile_photo.data
                filename    = secure_filename(form.email.data.split("@")[0]+"."+photo.filename.split(".")[-1])
                db.session.add(Users(username = form.username.data, password = form.password.data, first_name = form.first_name.data, last_name = form.last_name.data, email = form.email.data, profile_photo = filename, location = form.location.data, biography = form.biography.data))
                photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
                db.session.commit()
                return "Successfully Added"
        else:
            error = "Invalid Data Received"
        # pass
    return render_template("register.html", form = form, error = error)
# 	data = request.get_json()
# 	if request.method == 'POST':
# 		if not db.session.query(exists().where(User.username == data['username'])).scalar():
# 			if data['password'] == data['conpassword']:
# 				user = User(first_name = data['firstname'], last_name = data['lastname'],  username = data['username'], password = data['password'] , profile_photo = ['photo'])
# 				db.session.add(user)
# 				db.session.commit()
# 				return dumps({'message' : '200-OK', 'error' : 'null'})
# 			else:
# 				return dumps({'message' : '200-OK', 'error' : 'INCORRECT PASSWORDS'})
# 		return dumps({'message' : '200-OK', 'error' : 'USER EXIST'})
# 	return dumps({'message':'400-ERROR', 'error' : '0X51427'})


@app.route('/api/auth/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    # user = Users()
    
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = Users.query.filter_by(username=username,password=password).first()
        if user:
            login_user(user)
            flash("Logged in successfully.")
            return redirect(url_for("about"))
        else:
            flash("Incorrect Username or Password!")
    return render_template("login.html", form=form)

# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/api/auth/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.")
    return redirect(url_for('home')) 

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
