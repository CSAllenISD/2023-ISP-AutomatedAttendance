import sqlite3
from flask import Flask, Response, render_template, request, make_response, url_for, flash, redirect
import os
import cv2
import face_recognition
import numpy as np
import datetime
import time

app = Flask(__name__)
camera = cv2.VideoCapture(0)
app.config['SECRET_KEY'] = 'your secret key'

HOST_NAME = "localhost"
HOST_PORT = 80
DBFILE = "flask_server/User1.db"

# Load a sample picture and learn how to recognize it.
obama_image = face_recognition.load_image_file("flask_server/faces/obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Load a second sample picture and learn how to recognize it.
william_image = face_recognition.load_image_file("flask_server/faces/william.jpg")
william_face_encoding = face_recognition.face_encodings(william_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    obama_face_encoding,
    william_face_encoding
]
known_face_names = [
    "Barack Obama",
    "William Clymire"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

# webpage camera


def gen_frames(period):
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]

            # Only process every other frame of video to save time

            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(
                    known_face_encodings, face_encoding)
                name = "Unknown"
                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(
                    known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)
                update_attendance(period,name)

            # Display the results
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw a box around the face
                cv2.rectangle(frame, (left, top),
                              (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35),
                              (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6),
                            font, 1.0, (255, 255, 255), 1)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def getstudents(period):
    conn = sqlite3.connect(DBFILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM " + period)
    results = cursor.fetchall()
    conn.close()
    return results

def update_attendance(period,stu_name):
    # Connect to the database
    conn = sqlite3.connect(DBFILE)
    c = conn.cursor()

    # get the current period
    c.execute("SELECT * FROM " + period)
    results = c.fetchall()
    
    # Update attendance
    c.execute("UPDATE Period1 SET stu_attendance = ? WHERE stu_name= ?", ("Present", stu_name))
    conn.commit()
    c.close()
    conn.close()

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
    time.sleep(1.0)
 # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)


@app.route('/P2/')
def P2():
    # (C1) GET ALL students
    students = getstudents('Period2')
    time.sleep(1.0)
 # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)


@app.route('/P3/')
def P3():
    # (C1) GET ALL students
    students = getstudents('Period3')
    time.sleep(1.0)
 # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)


@app.route('/P4/')
def P4():
    # (C1) GET ALL students
    students = getstudents('Period4')
    time.sleep(1.0)
 # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)

# check if this one exists
@app.route('/P8/')
def P5():
    # (C1) GET ALL students
    students = getstudents('Period8')
    time.sleep(1.0)
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
    period = 'Period1'
    now = datetime.datetime.now().time()
    if (now.hour == 8 and 30 <= now.minute) or (now.hour == 9 and now.minute < 45):
        period = 'Period1'
    elif (now.hour == 9 and 45 <= now.minute) or (now.hour == 11 and now.minute < 25):
        period = 'Period2'
    elif (now.hour == 11 and 25 <= now.minute) or (now.hour == 1 and now.minute < 30):
        period = 'Period3'
    elif (now.hour == 1 and 30 <= now.minute) or (now.hour == 3 and now.minute < 10):
        period = 'Period4'
    elif (now.hour == 3 and 10 <= now.minute) or (now.hour == 4 and now.minute < 10):
        period = 'Period8'
    else:
        period = 'Period1' #testing purposes 

    return Response(gen_frames(period), mimetype='multipart/x-mixed-replace; boundary=frame')
    # return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/FAQ/')
def FAQ():
    return render_template('FAQ.html')


if __name__ == '__main__':
    app.run(HOST_NAME, HOST_PORT)
