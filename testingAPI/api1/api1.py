#api1.py

#from flask import Flask

# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)


in_memory_datastore = {
    "Cameron" : {"name": "Cameron", "eye-color": "Brown" },
    "Oliver" : {"name": "Oliver", "eye-color": "Blue"},
    "Connor" : {"name": "Connor", "eye-color": "Brown"}   
}

@app.get('/students_in_school')
def students_in_school():
    return {"students_in_school":list(in_memory_datastore.values())}
