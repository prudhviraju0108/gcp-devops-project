from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():
    return "Hello this is a simple webapp and I'm running iside a container..."