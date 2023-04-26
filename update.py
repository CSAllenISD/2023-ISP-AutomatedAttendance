import sqlite3

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
