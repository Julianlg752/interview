from flask import Flask
app = Flask(__name__)


# /ping use this endpoint to check if the server is alive
@app.route('/ping')
def index():
    return "pong"
