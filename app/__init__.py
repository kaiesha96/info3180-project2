from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "XhshdbDdtJdu"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project2:project2@localhost/project2"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

DEBUG = True

CSRF_ENABLED = DEBUG
UPLOAD_FOLDER="./app/static/uploads"
ALLOWED_EXTENSIONS = {"png", 'jpg', 'jpeg', 'gif'}

app.config.from_object(__name__)
from app import views
