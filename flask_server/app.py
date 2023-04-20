import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
HOST_NAME = "localhost"
HOST_PORT = 80
DBFILE = "User1.db"

def create_app():
    if __name__ == '__main__':
        app = Flask(__name__)
        app.config['SECRET_KEY'] = 'your secret key'
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DBFILE}'
        db.init_app(app)

    import views
    import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User
    # DB_NAME = User.id + ".db"
 


    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app





def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


