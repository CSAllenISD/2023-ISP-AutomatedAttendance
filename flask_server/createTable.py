# (A) LOAD PACKAGES
import sqlite3, os
from sqlite3 import Error

# (B) DATABASE + SQL FILE
DBFILE = "User1.db"
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

# user.id + ".db"
# from .models import User
# DBFILE = User.id + ".db"
