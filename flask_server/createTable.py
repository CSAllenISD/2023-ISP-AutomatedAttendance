# (A) LOAD PACKAGES
import sqlite3, os
from sqlite3 import Error

# (B) DATABASE + SQL FILE
# user.id + ".db"
# from .models import User
# DBFILE = User.id + ".db"
DBFILE = "students.db"
SQLFILE = "students.sql"

# (C) DELETE OLD DATABASE IF EXIST
def farts():
  if os.path.exists(DBFILE):
    os.remove(DBFILE)
 
# (D) IMPORT SQL
  conn = sqlite3.connect(DBFILE)
  with open(SQLFILE) as f:
    conn.executescript(f.read())
  conn.commit()
  conn.close()
  print("Database created!")