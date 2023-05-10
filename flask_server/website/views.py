from flask import Blueprint, Response, render_template, request, flash
from flask_login import login_required, current_user
from . import db, HOST_NAME, HOST_PORT, gen_frames, getstudents, getPeriod
import datetime


views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def landing_page():
    return render_template("landing.html")


@views.route("/dashboard/", methods=["GET", "POST"])
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)


@views.route("/period/<period>")
def classPeriod(period):
    students = getstudents(period)
    return render_template("dashboardTable.html", student=students, period=period)


@views.route("/period/")
def currentPeriod():
    period = getPeriod()
    students = getstudents(period)
    return render_template("dashboardTable.html", student=students, period=period)


@views.route("/video/<period>")
def video(period):
    return Response(
        gen_frames(period), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@views.route("/add-student/")
def add_student():
    return render_template("add-student.html")


@views.route("/classes/")
def classes():
    return render_template("classes.html")


# @app.route('/video/')
# def video():
#   return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')


@views.route("/classes/")
def FAQ():
    return render_template("FAQ.html")


@views.route("/AttendanceRep/")
def AttendanceReport():
    return render_template("AttendanceReport.html")


@views.route("/Help/")
def HelpSupport():
    return render_template("HelpSupport.html")


@views.route("/Student-Information/")
def StudentInformation():
    return render_template("Student-Information.html")


@views.route("/base/")
def base():
    return render_template("base.html")


@views.route("/sign-in/")
def layout():
    return render_template("layout.html")


@views.route("/editClass/")
def editClass():
    return render_template("period-display.html")


@views.route("/temp-period/")
def temp():
    return render_template("temp.html")
