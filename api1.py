#api1.py

from cv2 import applyColorMap
from flask import Flask
from os import path
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy



#initializing database, will attempt to change name later to be the users name + .db (ex: 'oliver.db')
db = SQLAlchemy()
DBFILE = ''

# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'a0s98fhawepjif-a9s8jdf'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DBFILE}'
    db.init_app(app)

    from flask_server.models import User

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = '/'
    login_manager.init_app()

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

#creates a database 
def create_database(app):
    if not path.exists('flask_server/' + DBFILE):
        db.create_all(app=app)
        print('Created Database!')

#Annotation that allows 
@app.route("/")

# Generic Python functino that returns "Hello world!"
def index():
    return "Hello world!"

# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
# Runs the Flask application only if the main.py file is being run.
    app.run()


