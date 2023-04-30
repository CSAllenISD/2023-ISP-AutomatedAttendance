from flask import Flask, render_template
import sqlite3

app = Flask(Newtest.py)

@app.route('/classes.html')
def show_classes():
    conn = sqlite3.connect('Usertest.db')
    c = conn.cursor()
    c.execute("SELECT * FROM classes")
    classes = c.fetchall()
    conn.close()

    return render_template('classes.html', classes=classes)
