import sqlite3

def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

def readBlobData(empId):
    try:
        sqliteConnection = sqlite3.connect('User1.db') #specific database name
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_fetch_blob_query = """SELECT * from new_employee where id = ?"""
        cursor.execute(sql_fetch_blob_query, (empId,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], "Name = ", row[1])
            name = row[1]
            photo = row[2]
            resumeFile = row[3]

            print("Storing employee image and resume on disk \n")
         #   photoPath = "E:\pynative\Python\photos\db_data\\" + name + ".jpg"
         #   resumePath = "E:\pynative\Python\photos\db_data\\" + name + ".txt"
            photoPath =  name + ".jpg"
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
readBlobData(2) 

# experiement to get COUNT func
# def readBlobData(empId):
#     try:
#         sqliteConnection = sqlite3.connect('User1.db') #specific database name
#         cursor = sqliteConnection.cursor()
#         print("Connected to SQLite")

#         sql_fetch_blob_query = """SELECT * from new_employee where id = ?"""
#         cursor.execute(sql_fetch_blob_query, (empId,))
#         record = cursor.fetchall()
#         for row in record:
#             print("Id = ", row[0], "Name = ", row[1])
#             name = row[1]
#             photo = row[2]
#             resumeFile = row[3]

#             print("Storing employee image and resume on disk \n")
#          #   photoPath = "E:\pynative\Python\photos\db_data\\" + name + ".jpg"
#          #   resumePath = "E:\pynative\Python\photos\db_data\\" + name + ".txt"
#             photoPath =  name + ".jpg"
#             #resumePath ="photos/" + name + ".txt"
#             writeTofile(photo, photoPath)
#           #  writeTofile(resumeFile, resumePath)

#         cursor.close()

#     except sqlite3.Error as error:
#         print("Failed to read blob data from sqlite table", error)
#     finally:
#         if sqliteConnection:
#             sqliteConnection.close()
#             print("sqlite connection is closed")

