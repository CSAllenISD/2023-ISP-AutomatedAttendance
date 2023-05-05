import sqlite3
from datetime import date

def manual_update_attendance(student_id, class_id, attendance_status):
    # Connect to the SQLite database
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # Get the current date
    current_date = date.today()

    try:
        # Update the attendance record in the table
        cursor.execute("UPDATE attendance SET status = ? WHERE student_id = ? AND class_id = ? AND date = ?",
                       (attendance_status, student_id, class_id, current_date))

        # Check if any rows were affected
        if cursor.rowcount > 0:
            # Commit the changes to the database
            conn.commit()
            print("Attendance updated successfully.")
        else:
            print("No matching attendance record found.")

    except sqlite3.Error as e:
        print("Error occurred while updating attendance:", e)

    # Close the database connection
    conn.close()
