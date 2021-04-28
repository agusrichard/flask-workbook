from flask import Flask


app = Flask(__name__)


@app.route('/service-two')
def index():
    return 'Hello World from service two'
