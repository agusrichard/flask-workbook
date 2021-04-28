from flask import Flask


app = Flask(__name__)


@app.route('/service-one')
def index():
    return 'Hello World from service one'
