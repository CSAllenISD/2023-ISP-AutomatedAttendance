#api1.py

from flask import Flask

# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)

#Annotation that allows 
@app.route("/")

# Generic Python functino that returns "Hello world!"
def index():
    return "Hello world!"

# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
# Runs the Flask application only if the main.py file is being run.
    app.run()