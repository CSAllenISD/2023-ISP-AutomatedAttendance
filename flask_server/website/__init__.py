from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import path
from flask_login import LoginManager
import sqlite3
import cv2
import face_recognition
import numpy as np
import datetime

db = SQLAlchemy()
HOST_NAME = "localhost"
HOST_PORT = 80
DBFILE = "User1.db"
camera = cv2.VideoCapture(0)


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "a0s98fhawepjif-a9s8jdf"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DBFILE}"
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists(DBFILE):
        db.create_all(app=app)
        SQLFILE = "allClasses.sql"

    # (C) DELETE OLD DATABASE IF EXIST
    if os.path.exists(DBFILE):
        os.remove(DBFILE)

    # (D) IMPORT SQL
    conn = sqlite3.connect(DBFILE)
    with open(SQLFILE) as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("Database created!")


def getstudents(period):
    conn = sqlite3.connect(DBFILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM " + period)
    results = cursor.fetchall()
    conn.close()
    return results


def getPeriod():
    now = datetime.datetime.now().time()
    if now.hour == 8 and now.minute >= 30 or now.hour == 9 and now.minute < 45:
        period = "Period1"
    elif now.hour == 9 and now.minute >= 45 or now.hour == 11 and now.minute < 25:
        period = "Period2"
    elif now.hour == 11 and now.minute >= 25 or now.hour == 13 and now.minute < 30:
        period = "Period3"
    elif now.hour == 13 and now.minute >= 30 or now.hour == 15 and now.minute < 10:
        period = "Period4"
    elif now.hour == 15 and now.minute >= 10 or now.hour == 16 and now.minute < 10:
        period = "Period8"
    else:
        period = "Period1"  # default for testing purposes
    return period


def update_attendance(period, stu_name):
    # Connect to the database
    conn = sqlite3.connect(DBFILE)
    c = conn.cursor()

    # get the current period
    c.execute("SELECT * FROM " + period)
    results = c.fetchall()

    if isTardy(period) == True:
        c.execute(
            "UPDATE " + period + " SET stu_attendance = ? WHERE stu_name= ?",
            ("Tardy", stu_name),
        )
    # Update attendance
    else:
        c.execute(
            "UPDATE " + period + " SET stu_attendance = ? WHERE stu_name= ?",
            ("Present", stu_name),
        )
    conn.commit()
    c.close()
    conn.close()


def isTardy(period):
    current = datetime.datetime.now().time()
    if period == "Period1":
        start = datetime.time(8, 30, 0)
        if current > start:
            return True
    if period == "Period2":
        start = datetime.time(9, 45, 0)
        if current > start:
            return True
    if period == "Period3":
        start = datetime.time(11, 25, 0)
        if current > start:
            return True
    if period == "Period4":
        start = datetime.time(1, 30, 0)
        if current > start:
            return True
    if period == "Period8":
        start = datetime.time(3, 10, 0)
        if current > start:
            return True
    else:
        return False


# camera
#
# FACE REC---------------------
obama_image = face_recognition.load_image_file("website/faces/obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Load a second sample picture and learn how to recognize it.
william_image = face_recognition.load_image_file("website/faces/william.jpg")
william_face_encoding = face_recognition.face_encodings(william_image)[0]

izzy_image = face_recognition.load_image_file("website/faces/izzy.jpg")
izzy_face_encoding = face_recognition.face_encodings(izzy_image)[0]

cameron_image = face_recognition.load_image_file("website/faces/cameron.jpg")
cameron_face_encoding = face_recognition.face_encodings(cameron_image)[0]

oliver_image = face_recognition.load_image_file("website/faces/oliver.jpg")
oliver_face_encoding = face_recognition.face_encodings(oliver_image)[0]

connor_image = face_recognition.load_image_file("website/faces/connor.jpg")
connor_face_encoding = face_recognition.face_encodings(connor_image)[0]


josh_image = face_recognition.load_image_file("website/faces/josh.jpg")
josh_face_encoding = face_recognition.face_encodings(josh_image)[0]

vijay_image = face_recognition.load_image_file("website/faces/facerecvijay.jpg")
vijay_face_encoding = face_recognition.face_encodings(vijay_image)[0]


# Create arrays of known face encodings and their names
known_face_encodings = [
    obama_face_encoding,
    william_face_encoding,
    izzy_face_encoding,
    cameron_face_encoding,
    oliver_face_encoding,
    connor_face_encoding,
    josh_face_encoding,
    vijay_face_encoding
]
known_face_names = [
    "Barack Obama",
    "William Clymire",
    "Isabelle Holden",
    "Cameron Farley",
    "Oliver Hankins",
    "Connor Church",
    "Joshua Lee",
    "Vijay Vemulapalli",
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True


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
                rgb_small_frame, face_locations
            )
            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(
                    known_face_encodings, face_encoding
                )
                name = "Unknown"
                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(
                    known_face_encodings, face_encoding
                )
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)
                update_attendance(period, name)

            # Display the results
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(
                    frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED
                )
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(
                    frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1
                )

            ret, buffer = cv2.imencode(".jpg", frame)
            frame = buffer.tobytes()
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


# def process_frame(frame, period):
#     # Resize frame of video to 1/4 size for faster face recognition processing
#     small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#     # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
#     rgb_small_frame = small_frame[:, :, ::-1]

#     # Find all the faces and face encodings in the current frame of video
#     face_locations = face_recognition.face_locations(rgb_small_frame)
#     face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
#     face_names = []
#     for face_encoding in face_encodings:
#         # See if the face is a match for the known face(s)
#         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#         name = "Unknown"
#         # Or instead, use the known face with the smallest distance to the new face
#         face_distances = face_recognition.face_distance(
#             known_face_encodings, face_encoding
#         )
#         best_match_index = np.argmin(face_distances)
#         if matches[best_match_index]:
#             name = known_face_names[best_match_index]

#         face_names.append(name)
#         update_attendance(period, name)

#     return (face_locations, face_names)


# def gen_frames(period):
#     camera = cv2.VideoCapture(0)
#     try:
#         while True:
#             success, frame = camera.read()
#             if not success:
#                 break
#             else:
#                 face_locations, face_names = process_frame(frame, period)

#                 # Display the results
#                 for (top, right, bottom, left), name in zip(face_locations, face_names):
#                     # Scale back up face locations since the frame we detected in was scaled to 1/4 size
#                     top *= 4
#                     right *= 4
#                     bottom *= 4
#                     left *= 4

#                     # Draw a box around the face
#                     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

#                     # Draw a label with a name below the face
#                     cv2.rectangle(
#                         frame,
#                         (left, bottom - 35),
#                         (right, bottom),
#                         (0, 0, 255),
#                         cv2.FILLED,
#                     )
#                     font = cv2.FONT_HERSHEY_DUPLEX
#                     cv2.putText(
#                         frame,
#                         name,
#                         (left + 6, bottom - 6),
#                         font,
#                         1.0,
#                         (255, 255, 255),
#                         1,
#                     )

#                 # Return the frame with the bounding boxes and names
#                 ret, buffer = cv2.imencode(".jpg", frame)
#                 frame = buffer.tobytes()
#                 yield (
#                     b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"
#                 )
#     finally:
#         camera.release()
