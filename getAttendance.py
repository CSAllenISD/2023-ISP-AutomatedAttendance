import sqlite3
from datetime import datetime

# Connect to SQLite database
conn = sqlite3.connect('attendance.db')
cur = conn.cursor()

# Retrieve attendance records from database
class_name = 'Class 1'
date_str = '2023-01-01' # Format: YYYY-MM-DD
date_obj = datetime.strptime(date_str, '%Y-%m-%d')
start_date = date_obj.replace(hour=0, minute=0, second=0)
end_date = date_obj.replace(hour=23, minute=59, second=59)
query = "SELECT * FROM attendance WHERE class = ? AND date BETWEEN ? AND ?"
cur.execute(query, (class_name, start_date, end_date))
attendance_data = cur.fetchall()

# Generate HTML attendance report page
html = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Attendance Report</title>
  <link rel="stylesheet" href="attendancereport.css">
</head>
<body>
  <div class="container">
    <h1>Attendance Report</h1>
    <form>
      <label for="class">Class:</label>
      <select id="class" name="class">
        <option value="class1">Class 1</option>
        <option value="class2">Class 2</option>
        <option value="class3">Class 3</option>
      </select>
      <label for="date">Date:</label>
      <input type="date" id="date" name="date" value="{}">
      <button type="submit">Filter</button>
    </form>
    <table>
      <thead>
        <tr>
          <th>Student Name</th>
          <th>Attendance Status</th>
          <th>Date</th>
        </tr>
      </thead>
      <tbody>
'''.format(date_str)

for attendance_record in attendance_data:
    student_name = attendance_record[1]
    attendance_status = attendance_record[3]
    attendance_date = attendance_record[2].strftime('%m/%d/%Y')
    html += '''
        <tr>
          <td>{}</td>
          <td>{}</td>
          <td>{}</td>
        </tr>
    '''.format(student_name, attendance_status, attendance_date)

html += '''
      </tbody>
    </table>
  </div>
</body>
</html>
'''

# Write HTML page to file
with open('attendance_report.html', 'w') as f:
    f.write(html)

# Close database connection
conn.close()