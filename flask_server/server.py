# (A) INIT
# (A1) LOAD MODULES
from flask import Flask, render_template, request, make_response
import sqlite3
 
# (A2) FLASK SETTINGS + INIT
HOST_NAME = "localhost"
HOST_PORT = 80
DBFILE = "students.db"
app = Flask(__name__)
# app.debug = True

# (B) HELPER - GET ALL USERS FROM DATABASE
def getstudents():
  conn = sqlite3.connect(DBFILE)
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM `students`")
  results = cursor.fetchall()
  conn.close()
  return results

# (C) DEMO PAGE - SHOW USERS IN TABLE
@app.route("/")
def index():
  # (C1) GET ALL USERS
  users = getstudents()
  # print(users)
 
  # (C2) RENDER HTML PAGE
  return render_template("killme.html", usr=users)
 
# (D) START
if __name__ == "__main__":
  app.run(HOST_NAME, HOST_PORT)