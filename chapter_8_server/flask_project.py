'''
flask_project.py

simple flask project to show hello world and run a server.

From flask tutorial here:

'''
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    application.run(host='0.0.0.0')
    
