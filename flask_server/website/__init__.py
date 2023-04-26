from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import sqlite3


db = SQLAlchemy()
HOST_NAME = "localhost"
HOST_PORT = 80
DBFILE = "User1.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'a0s98fhawepjif-a9s8jdf'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DBFILE}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

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


def getstudents(period):
  conn = sqlite3.connect(DBFILE)
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM " + period)
  results = cursor.fetchall()
  conn.close()
  return results

  # webpage camera
#def generate_frames():
 #   while True:
#
 #       #read the cam frame
  #      success, frame=camera.read()
   #     if not success:
    #        break
     #   else:
      #      ret, buffer=cv2.imencode('.jpg', frame)
       #     frame=buffer.tobytes()
        #
        #yield(b'--frame\r\n'
         #     b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
