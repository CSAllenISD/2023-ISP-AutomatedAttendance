import sqlite3
from datetime import datetime

# connect to User1.db
conn = sqlite3.connect('Usertest.db')
cursor = conn.cursor()

# execute SQL query to get attendance information for the given class and date
class_name = "Period 1"
date = str(datetime.now())
query = f"SELECT student_name, attendance_status FROM {class_name} WHERE date = ?"
cursor.execute(query, (date,))

# create a dictionary to store attendance status for each student
attendance_dict = {}
for row in cursor:
    attendance_dict[row[0]] = row[1]

# close database connection
conn.close()

# open AttendanceReport.html file
with open('AttendanceReport.html', 'r') as file:
    html = file.read()

# update attendance status for each student in the HTML table
for student in attendance_dict:
    html = html.replace(f'>{student}<', f'>{student}<option selected value="{attendance_dict[student]}">')
    html = html.replace(f'>{date}<', f'>{date}</td><td>{attendance_dict[student]}</td></tr><tr><td>{student}<')

# write updated HTML to file
with open('AttendanceReport.html', 'w') as file:
    file.write(html)
