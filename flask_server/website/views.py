from flask import Blueprint, Response, render_template, request, flash
from flask_login import login_required, current_user
<<<<<<< HEAD
from . import db, HOST_NAME, HOST_PORT, getstudents
from .models import Period
=======
from . import db, HOST_NAME, HOST_PORT, gen_frames, getstudents
import datetime
import time
>>>>>>> 368bab642d665c4fa9e67462812f2dec74414c44

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def landing_page():
    return render_template("landing.html")


@views.route("/dashboard/", methods=["GET", "POST"])
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)

<<<<<<< HEAD
@views.route('/p1/')
=======

@views.route("/P1/")
>>>>>>> 368bab642d665c4fa9e67462812f2dec74414c44
def P1():
    # (C1) GET ALL students
    students = getstudents("Period1")
    time.sleep(2.0)
    # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)

<<<<<<< HEAD
@views.route('/p2/')
=======

@views.route("/P2/")
>>>>>>> 368bab642d665c4fa9e67462812f2dec74414c44
def P2():
    # (C1) GET ALL students
    students = getstudents("Period2")
    time.sleep(3.0)
    # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)

<<<<<<< HEAD
@views.route('/p3/')
=======

@views.route("/P3/")
>>>>>>> 368bab642d665c4fa9e67462812f2dec74414c44
def P3():
    # (C1) GET ALL students
    students = getstudents("Period3")
    time.sleep(3.0)
    # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)

<<<<<<< HEAD
@views.route('/p4/')
=======

@views.route("/P4/")
>>>>>>> 368bab642d665c4fa9e67462812f2dec74414c44
def P4():
    # (C1) GET ALL students
    students = getstudents("Period4")
    time.sleep(3.0)
    # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)

<<<<<<< HEAD
@views.route('/p5/')
=======

@views.route("/P8/")
>>>>>>> 368bab642d665c4fa9e67462812f2dec74414c44
def P5():
    # (C1) GET ALL students
    students = getstudents("Period8")
    time.sleep(3.0)
    # (C2) RENDER HTML PAGE
    return render_template("dashboardTable.html", student=students)


@views.route("/add-student/")
def add_student():
    return render_template("add-student.html")


@views.route("/classes/")
def classes():
<<<<<<< HEAD
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
=======
    return render_template("classes.html")
>>>>>>> 368bab642d665c4fa9e67462812f2dec74414c44


# @app.route('/video/')
# def video():
#   return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')


@views.route("/classes/")
def FAQ():
<<<<<<< HEAD
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
    
=======
    return render_template("FAQ.html")
>>>>>>> 368bab642d665c4fa9e67462812f2dec74414c44


@views.route("/AttendanceRep/")
def AttendanceReport():
    return render_template("AttendanceReport.html")


@views.route("/Help/")
def HelpSupport():
    return render_template("HelpSupport.html")


@views.route("/Student-Info/")
def StudentInformation():
    return render_template("Student-Information.html")


@views.route("/base/")
def base():
    return render_template("base.html")


@views.route("/sign-in/")
def layout():
    return render_template("layout.html")


@views.route("/periods/")
def periods():
    return render_template("period-display1.html")


@views.route("/temp-period/")
def temp():
    return render_template("temp.html")


# overhaul time funcs
@views.route("/video/")
def video():
    period = "Period1"
    # now = datetime.datetime.now().time()
    # if (now.hour == 8 and 30 <= now.minute) or (now.hour == 9 and now.minute < 45):
    #     period = "Period1"
    # elif (now.hour == 9 and 45 <= now.minute) or (now.hour == 11 and now.minute < 25):
    #     period = "Period2"
    # elif (now.hour == 11 and 25 <= now.minute) or (now.hour == 1 and now.minute < 30):
    #     period = "Period3"
    # elif (now.hour == 1 and 30 <= now.minute) or (now.hour == 3 and now.minute < 10):
    #     period = "Period4"
    # elif (now.hour == 3 and 10 <= now.minute) or (now.hour == 4 and now.minute < 10):
    #     period = "Period8"
    # else:
    #     period = "Period1"  # testing purposes

    return Response(
        gen_frames(period), mimetype="multipart/x-mixed-replace; boundary=frame"
    )
