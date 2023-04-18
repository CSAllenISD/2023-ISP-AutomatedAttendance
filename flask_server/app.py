import sqlite3
from flask import Flask, Response, render_template, request, make_response, url_for, flash, redirect
import face_recognition
import os
import cv2
import sys
import numpy as np
import math

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

        #read the cam frame
        success, frame=camera.read()
        if not success:
            break
        else:
            ret, buffer=cv2.imencode('.jpg', frame)
            frame=buffer.tobytes()
        
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def face_confidence(face_distance, face_match_threshold=0.6):
    range = (1.0 - face_match_threshold)
    linear_val = (1.0 - face_distance) / (range * 2.0)

    if face_distance > face_match_threshold:
        return str(round(linear_val * 100, 2)) + '%'
    else:
        value = (linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))) * 100
        return str(round(value, 2)) + '%'

class FaceRecognition:
    face_locations = []
    face_encodings = []
    face_names = []
    known_face_encodings = []
    known_face_names = []
    process_current_frame = True

    def __init__(self):
        self.encode_faces()

    #Pulls images from the faces file and encodes them
    def encode_faces(self):
        for image in os.listdir('faces'):
            face_image = face_recognition.load_image_file(f"faces/{image}")
            face_encoding = face_recognition.face_encodings(face_image)[0]

            self.known_face_encodings.append(face_encoding)
            self.known_face_names.append(image)
        print(self.known_face_names)

    #Runs video camera, finds faces
    def run_recognition(self):
        video_capture = cv2.VideoCapture(0)
            
        while True:

                #reads the camera frame 
            success, frame=video_capture.read()
            if not success:
                break
            else:
                ret, buffer=cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()

            yield(b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                
        if not video_capture.isOpened():
            sys.exit('Video source not found...')

        while True:
            ret, frame = video_capture.read()

            if self.process_current_frame:
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                #change colors from BGR to RGB
                rgb_small_frame = small_frame[:, :, ::-1]

                self.face_locations = face_recognition.face_locations(rgb_small_frame)
                self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

                self.face_names = []
                for face_encoding in self.face_encodings:
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                    name = "Unknown"
                    confidence = '???'

                    face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)

                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = self.known_face_names[best_match_index]
                        confidence = face_confidence(face_distances[best_match_index])

                    self.face_names.append(name)

            self.process_current_frame = not self.process_current_frame

            #Placing results
            for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                #Rendering the rectangle
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)

            #Displaying the box
            cv2.imshow('Face Recognition', frame)

            #Quit with q
            if cv2.waitKey(1) == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()

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

@app.route('/dashboard/', methods=('GET','POST'))
def dashboard():
    return render_template('dashboard.html')

@app.route('/P1/')
def P1():
  # (C1) GET ALL students
    students = getstudents('Period1')
 # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)

@app.route('/add-student/')
def add_student():
    return render_template('add-student.html')

@app.route('/classes/')
def classes():
    return render_template('classes.html')

@app.route('/cameraPage/')
def cameraPage():
    return render_template('camera.html')

@app.route('/video/')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video')
def videoRecognition():
    return Response(FaceRecognition(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(HOST_NAME, HOST_PORT)
    fr = FaceRecognition()
    fr.run_recognition
    