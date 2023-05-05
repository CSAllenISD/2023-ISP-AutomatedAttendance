from flask import Blueprint, Response, render_template, request, flash
from flask_login import login_required, current_user
from . import db, HOST_NAME, HOST_PORT, gen_frames, getstudents
import time
import datetime

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
    time.sleep(5.0)
 # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)

@views.route('/P2/')
def P2():
  # (C1) GET ALL students
    students = getstudents('Period2')
    time.sleep(3.0)
 # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)

@views.route('/P3/')
def P3():
  # (C1) GET ALL students
    students = getstudents('Period3')
    time.sleep(3.0)
 # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)

@views.route('/P4/')
def P4():
  # (C1) GET ALL students
    students = getstudents('Period4')
    time.sleep(3.0)
 # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)

@views.route('/P8/')
def P5():
  # (C1) GET ALL students
    students = getstudents('Period8')
    time.sleep(3.0)
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

# overhaul time funcs
@views.route('/video/') 
def video():
    period = 'Period1'
    # now = datetime.datetime.now().time()
    # if (now.hour == 8 and 30 <= now.minute) or (now.hour == 9 and now.minute < 45):
    #     period = 'Period1'
    # elif (now.hour == 9 and 45 <= now.minute) or (now.hour == 11 and now.minute < 25):
    #     period = 'Period2'
    # elif (now.hour == 11 and 25 <= now.minute) or (now.hour == 1 and now.minute < 30):
    #     period = 'Period3'
    # elif (now.hour == 1 and 30 <= now.minute) or (now.hour == 3 and now.minute < 10):
    #     period = 'Period4'
    # elif (now.hour == 3 and 10 <= now.minute) or (now.hour == 4 and now.minute < 10):
    #     period = 'Period8'
    # else:
    #     period = 'Period1' #testing purposes 

    return Response(gen_frames(period), mimetype='multipart/x-mixed-replace; boundary=frame')
    # return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

