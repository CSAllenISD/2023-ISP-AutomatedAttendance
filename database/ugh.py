import sqlite3

conn = sqlite3.connect('database/User1.db')
c = conn.cursor()
#  ?creates new table
# c.execute("""CREATE TABLE new_employee(
#     id integer,
#     name varchar(255),
#     photo blob,
#     resume, blob
#     )""")

def convertToBinaryData(filename):
    # Convert digital data to binary format
    # 
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(empId, name, photo, resumeFile):
    try:
        sqliteConnection = sqlite3.connect('database/User1.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO new_employee
                                  (id, name, photo, resume) VALUES (?, ?, ?, ?)"""
    # error is here
        empPhoto = convertToBinaryData(photo)
        resume = convertToBinaryData(resumeFile)
        # Convert data into tuple format
        data_tuple = (empId, name, empPhoto, resume)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")

# insertBLOB(1, "Smith", "photos/Smith.jpg", "photos/random.txt")
insertBLOB(2,"Connor", "database/photos/Ayaan.jpg", "database/photos/random.txt")