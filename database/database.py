import sqlite3

conn = sqlite3.connect('student.db')

c = conn.cursor()
#
#c.execute("""CREATE TABLE students(
#    first_name text,
#    last_name text,
#    PersonID integer
#    )""")

#c.execute("INSERT INTO students VALUES ('Corey', 'Smith', 50000)")

c.execute("SELECT * FROM students WHERE last_name='Smith'")

print(c.fetchone())

conn.commit()

conn.close()