from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
#import cv2


db = SQLAlchemy()
HOST_NAME = "localhost"
HOST_PORT = 80
DBFILE = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'a0s98fhawepjif-a9s8jdf'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DBFILE}'
   # camera = cv2.VideoCapture(0)
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    
    # DB_NAME = User.id + ".db"
    from .models import User


    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DBFILE):
        db.create_all(app=app)
        print('Created Database!')