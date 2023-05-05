import sqlite3
# Prototype integration with server but not finished due to time constraint:
from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/')
# status = 0
# if status = 3:
#  status = 0
# def index():
#      return render_template('index.html')
#
#  @app.route('/my-link/')
#  def my_link():
#        print ('I got clicked!')
#
#          status += 1
#          return 'Click.'
#
#      if __name__ == '__main__':
#            app.run(debug=True)
def updateSqliteTable(stu_id, stu_attendance):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite3")

        sql_update_query = """Update allClasses.sql set stu_attendance = ? where stu_id = ?"""
        change = (stu_attendance, stu_id)
        cursor.execute(sql_update_query, change)
        sqliteConnection.commit()
        print("Change Was Implemented")
        cursor.close()
    except sqlite3.Error as error:
        print("Could not update database", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("Connection has been terminated")
updateSqliteTable(1, 1)
