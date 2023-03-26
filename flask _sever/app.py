import sqlite3
from flask import Flask, render_template
import os


app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

IMAGES = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = IMAGES

@app.route('/')
def landing_page():
    return render_template('landing.html')
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/signup/')
def signup():
    return render_template('signup.html')
if __name__ == '__main__':
    app.run(debug=True)

