from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(Newtest.py)

@app.route('/create-class', methods=['POST'])
def create_class():
    class_name = request.form['class-name']
    class_period = request.form['period']
    
    conn = sqlite3.connect('Usertest.db')
    c = conn.cursor()
    c.execute("INSERT INTO classes (name, period) VALUES (?, ?)", (class_name, class_period))
    conn.commit()
    conn.close()

    return redirect('/classes.html')

@app.route('/')
def index():
    return render_template('Newclass.html')
