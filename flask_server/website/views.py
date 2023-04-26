from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . import db, HOST_NAME, HOST_PORT, getstudents

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def landing_page():
    return render_template("landing.html")


@views.route('/dashboard/', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)

@views.route('/P1/')
def P1():
  # (C1) GET ALL students
    students = getstudents('Period1')
 # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)

@views.route('/P2/')
def P2():
  # (C1) GET ALL students
    students = getstudents('Period2')
 # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)

@views.route('/P3/')
def P3():
  # (C1) GET ALL students
    students = getstudents('Period3')
 # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)

@views.route('/P4/')
def P4():
  # (C1) GET ALL students
    students = getstudents('Period4')
 # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)

@views.route('/P5/')
def P5():
  # (C1) GET ALL students
    students = getstudents('Period5')
 # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)

@views.route('/add-student/')
def add_student():
    return render_template('add-student.html')

@views.route('/classes/')
def classes():
    return render_template('classes.html')

#@app.route('/video/')
#def video():
 #   return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')


@views.route('/classes/')
def FAQ():
    return render_template('FAQ.html')
  
@views.route('/AttendanceRep/')
def AttendanceReport():
    return render_template('AttendanceReport.html')
    
@views.route('/Help/')
def HelpSupport():
    return render_template('HelpSupport.html')
    
@views.route('/Student-Info/')
def StudentInformation():
    return render_template('Student-Information.html')
    
@views.route('/base/')
def base():
    return render_template('base.html')
    
@views.route('/sign-in/')
def layout():
    return render_template('layout.html')
    

@views.route('/periods/')
def periods():
    return render_template('period-display.html')
    
@views.route('/temp-period/')
def temp():
    return render_template('temp.html')
