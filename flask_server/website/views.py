from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . import db, HOST_NAME, HOST_PORT, getstudents
from .models import Period

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def landing_page():
    return render_template("landing.html")


@views.route('/dashboard/', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)

@views.route('/p1/')
def P1():
  # (C1) GET ALL students
    students = getstudents('Period1')
 # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)

@views.route('/p2/')
def P2():
  # (C1) GET ALL students
    students = getstudents('Period2')
 # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)

@views.route('/p3/')
def P3():
  # (C1) GET ALL students
    students = getstudents('Period3')
 # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)

@views.route('/p4/')
def P4():
  # (C1) GET ALL students
    students = getstudents('Period4')
 # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)

@views.route('/p5/')
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
    if request.method == 'POST': 
        period = request.form.get('period')#Gets the periods from the database
        
    else:
        new_period = Period(data=period, user_id=current_user.id)  #providing the schema for the period  
        db.session.add(new_period) #adding the period to the database 
        db.session.commit()
        flash('Period added!', category='success')
        
    return render_template('classes.html')

#@app.route('/video/')
#def video():
 #   return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')


@views.route('/classes/')
def FAQ():
    return render_template('FAQ.html')
  
@views.route('/attendance-rep/')
def AttendanceReport():
    return render_template('AttendanceReport.html')
    
@views.route('/help/')
def HelpSupport():
    return render_template('HelpSupport.html')
    
@views.route('/student-info/')
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
