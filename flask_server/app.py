import sqlite3
from flask import Flask, render_template, request, make_response, url_for, flash, redirect
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

HOST_NAME = "localhost"
HOST_PORT = 80
DBFILE = "students.db"
# app.debug = True

# (B) HELPER - GET ALL USERS FROM DATABASE
def getstudents():
  conn = sqlite3.connect(DBFILE)
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM `students`")
  results = cursor.fetchall()
  conn.close()
  return results


@app.route('/')
def landing_page():
    return render_template('landing.html')
if __name__ == '__main__':
    app.run(HOST_NAME, HOST_PORT)

@app.route('/signup/')
def signup():
    return render_template('signup.html')
if __name__ == '__main__':
    app.run(HOST_NAME, HOST_PORT)

@app.route('/dashboard/', methods=('GET','POST'))
def dashboard():
    return render_template('dashboard.html')
if __name__ == '__main__':
    app.run(HOST_NAME, HOST_PORT)

@app.route("/table1/")
def table1():
  # (C1) GET ALL USERS
    students = getstudents()
  # print(users)
 # (C2) RENDER HTML PAGE
    return render_template("table1.html", student=students)
if __name__ == '__main__':
    app.run(HOST_NAME, HOST_PORT)

