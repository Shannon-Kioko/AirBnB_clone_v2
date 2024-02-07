#!/usr/bin/python3
"""
Module starts a Flask Web app
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello HBNB'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    return 'C {} {} {}'.format(text, text, text)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
