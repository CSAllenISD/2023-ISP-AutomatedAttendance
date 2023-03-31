import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def landing_page():
    return render_template('landing.html')
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/signup/')
def signup():
    return render_template('signup.html')
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/dashboard/', methods=('GET','POST'))
def dahsboard():
    return render_template('dashboard.html')
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/attendanceTable.html/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        student_name = request.form['student_name']
        student_id = request.form['student_id']

        if not student_name:
            flash('student_id is required!')
        elif not student_id:
            flash('student_id is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (student_id, student_id) VALUES (?, ?)',
                         (student_name, student_id))
            conn.commit()
            conn.close()
            return redirect(url_for('dashboard.html'))

    return render_template('attendanceTable.html')