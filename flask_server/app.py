import sqlite3
from flask import Flask, Response, render_template, request, make_response, url_for, flash, redirect
from os import path
#import cv2
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash



db = SQLAlchemy()
app = Flask(__name__)
#camera = cv2.VideoCapture(0)
app.config['SECRET_KEY'] = 'your secret key'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))


HOST_NAME = "localhost"
HOST_PORT = 80
DBFILE = "User1.db"
# app.debug = True

#I don't know what to call this
def filler_login():

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'app.login'
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app




# (B) HELPER - GET ALL USERS FROM DATABASE
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


@app.route('/')
def landing_page():
    return render_template('landing.html')

# login and signup may need GET and PUT




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)



@app.route('/dashboard/', methods=('GET','POST'))
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
    return render_template('classes.html')

#@app.route('/video/')
#def video():
 #   return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(HOST_NAME, HOST_PORT)


@app.route('/classes/')
def FAQ():
    return render_template('FAQ.html')
if __name__ == '__main__':
    app.run(HOST_NAME, HOST_PORT)
  
@app.route('/AttendanceRep/')
def AttendanceReport():
    return render_template('AttendanceReport.html')
    
@app.route('/Help/')
def HelpSupport():
    return render_template('HelpSupport.html')
    
@app.route('/Student-Info/')
def StudentInformation():
    return render_template('Student-Information.html')
    
@app.route('/base/')
def base():
    return render_template('base.html')
    
@app.route('/sign-in/')
def layout():
    return render_template('layout.html')
    

@app.route('/periods/')
def periods():
    return render_template('period-display.html')
    
@app.route('/temp-period/')
def temp():
    return render_template('temp.html')
