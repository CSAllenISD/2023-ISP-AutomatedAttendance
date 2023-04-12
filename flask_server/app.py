import sqlite3
from flask import Flask, render_template, request, make_response, url_for, flash, redirect
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

HOST_NAME = "localhost"
HOST_PORT = 80
DBFILE = "User1.db"
# app.debug = True

# (B) HELPER - GET ALL USERS FROM DATABASE
def getstudents(period):
  conn = sqlite3.connect(DBFILE)
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM " + period)
  results = cursor.fetchall()
  conn.close()
  return results


@app.route('/')
def landing_page():
    return render_template('landing.html')
if __name__ == '__main__':
    app.run(HOST_NAME, HOST_PORT)

# login and signup may need GET and PUT
@app.route('/signup/')
def signup():
    return render_template('signup.html')
if __name__ == '__main__':
    app.run(HOST_NAME, HOST_PORT)

@app.route('/login/')
def login():
    return render_template('login.html')
if __name__ == '__main__':
    app.run(HOST_NAME, HOST_PORT)

@app.route('/dashboard/', methods=('GET','POST'))
def dashboard():
    return render_template('dashboard.html')
if __name__ == '__main__':
    app.run(HOST_NAME, HOST_PORT)

@app.route('/P1/')
def P1():
  # (C1) GET ALL students
    students = getstudents('Period1')
 # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)
if __name__ == '__main__':
    app.run(HOST_NAME, HOST_PORT)


@app.route('/add-student/')
def add_student():
    return render_template('add-student.html')
if __name__ == '__main__':
    app.run(HOST_NAME, HOST_PORT)

@app.route('/classes/')
def classes():
    return render_template('classes.html')
if __name__ == '__main__':
    app.run(HOST_NAME, HOST_PORT)