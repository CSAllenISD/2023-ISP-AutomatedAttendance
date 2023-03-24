import sqlite3
import os.path
import json

def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

def readBlobData(empId):
    try:
        sqliteConnection = sqlite3.connect('database/User1.db') #specific database name
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_fetch_blob_query = """SELECT * FROM new_employee WHERE id = ?"""
        cursor.execute(sql_fetch_blob_query, (empId,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], "Name = ", row[1])
            name = row[1]
            photo = row[2]
            resumeFile = row[3]

            print("Storing student image and resume on disk \n")
         #   photoPath = "E:\pynative\Python\photos\db_data\\" + name + ".jpg"
         #   resumePath = "E:\pynative\Python\photos\db_data\\" + name + ".txt"
            photoPath =  "photos" + name + ".jpg"
            resumePath = name + ".txt"

            writeTofile(photo, photoPath)
            writeTofile(resumeFile, resumePath)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
# Get the data based on id
json.dumps(readBlobData(2))


