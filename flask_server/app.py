import sqlite3
from flask import Flask, Response, render_template, request, make_response, url_for, flash, redirect
import os
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)
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

# webpage camera


def generate_frames():
    while True:

        # read the cam frame
        success, frame = camera.read()
        if not success:
            break
        else:
            # HERE

            #
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def landing_page():
    return render_template('landing.html')

# login and signup may need GET and PUT


@app.route('/signup/')
def signup():
    return render_template('signup.html')


@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/dashboard/', methods=('GET', 'POST'))
def dashboard():
    return render_template('dashboard.html')


@app.route('/P1/')
def P1():
    # (C1) GET ALL students
    students = getstudents('Period1')
 # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)


@app.route('/P2/')
def P2():
    # (C1) GET ALL students
    students = getstudents('Period2')
 # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)


@app.route('/P3/')
def P3():
    # (C1) GET ALL students
    students = getstudents('Period3')
 # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)


@app.route('/P4/')
def P4():
    # (C1) GET ALL students
    students = getstudents('Period4')
 # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)


@app.route('/P5/')
def P5():
    # (C1) GET ALL students
    students = getstudents('Period5')
 # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)


@app.route('/add-student/')
def add_student():
    return render_template('add-student.html')


@app.route('/classes/')
def classes():
    return render_template('classblock.html')


@app.route('/video/')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/FAQ/')
def FAQ():
    return render_template('FAQ.html')


if __name__ == '__main__':
    app.run(HOST_NAME, HOST_PORT)