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
from forms import RegistrationForm, LoginForm
from models import Posts, Users, Likes, Follows
import jwt
from functools import wraps

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('index.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

def jwt_token(t):
    @wraps(t)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization', None)
        if not auth:
            return jsonify({'error': 'Access Denied : No Token Found'}), 401
        else:
            try:
                userdata = jwt.decode(auth, app.config['SECRET_KEY'])
                currentUser = User.query.filter_by(username = userdata['user']).first()
            except jwt.exceptions.InvalidSignatureError:
                return jsonify({'error':'Invalid Token'})
            except jwt.exceptions.DecodeError:
                return jsonify({'error': 'Invalid Token'})
            return t(currentUser,*args, **kwargs)
    return decorated
    
    

@app.route('/api/users/register', methods=['POST'])
def register():
    form = RegistrationForm()
    
    
    if request.method=='POST' and form.validate_on_submit():
        uname = form.username.data
        password = form.password.data
        fname = form.firstname.data
        lname = form.lastname.data
        email = form.email.data
        location = form.location.data
        biography=form.biography.data
        photo=form.profile_photo.data
        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        photo=photo.filename
        date = datetime.date.today()
        
        filename = str(uid)+".jpg"
        photograph.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        user = Users(id= uid,firstname=fname, lastname = lname,location=location,biography= biography,email=email,created_on=created_on)
        db.session.add(user)
        db.session.commit()
        flash('Profile created!', 'success')
        
        
        photo.save(os.path.join(filefolder, profile_picture))
        registering = [{"message": "User successfully registered"}]
        return jsonify(result=registering)
    error_collection = form_errors(form)
    error = [{'errors': error_collection}]
    return  jsonify(errors=error)
        
        
        
@app.route('/api/auth/login',methods=["POST"])
def login():
     form = LoginForm()
     if request.method == "POST" and form.validate_on_submit():
         username = form.username.data
         password = form.password.data
         users = Users.query.filter_by(username=username).all()
         
         if len(users) == 0:
             return jsonify({'error': 'Invalid username or password'})
         elif not check_password_hash(users[0].password,password):
             return jsonify({'error': 'Invalid username or password'})
         else:
             user = users[0]
             jwt_token = jwt.encode({'user': user.username},app.config['SECRET_KEY'],algorithm = "HS256")
             response = {'message': 'User successfully logged in','jwt_token':jwt_token}
             return jsonify(response)             
     return jsonify_errors(form_errors(form))
     
     

     
     
     


@app.route('/api/auth/logout',methods=['GET']) 
@login_required
def logout():
    """logout users"""
    g.active_user = None
    logout_user()  
    logout={"message": " User successfully logged out"}
    return jsonify(logout)     
    
    
    
        
@app.route('/api/posts/<post_id>/like',methods = ['POST'])
@jwt_token
def like(currentUser,post_id):
    post = Post.query.filter_by(post_id).first()
    
    if not post:
        return jsonify_errors(['post does not exist'])
        
    if request.method == 'POST':
        like = Like(postid = request.values.get('post_id'),userid = request.values.get('user_id'))
        db.session.add(like)
        db.session.commit()
        
        total_likes = len(Like.query.filter_by(postid = post_id).all())
        return jsonify({'message': 'post liked','likes':total_likes})
    return jsonify_errors(['Only POST requests are accepted'])

        
@app.route('/api/users/{user_id}/follow',methods=['POST'])
@jwt_token
def follow(user_id):
    if request.method=="POST":
        follow=Follows(user_id,current_user.id)
        db.session.add(follow)
        db.session.commit()
        user=Users.query.filter_by(id=user_id).first()
        return jsonify(response={'message':'You are now following '+user.username})       
   
    
@app.route('/api/posts',methods=['GET']) 
@jwt_token
def get_AllPost():
    """return all post for all users."""
    pass 


@app.route('/secure-page')
@jwt_token
def secure_page():
    """Render a secure page on our website that only logged in users can access."""
    return render_template('secure_page.html')



# Flash errors from the form if validation fails
def flash_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages
  


    

        
        
    
       
        
    












@app.route('/explore')
def explore():
    users = Users.query.all()
    return render_template("explore.html", users = users)


# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

###
# The functions below should be applicable to all Flask apps.
###


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
