#!/usr/bin/python3
"""
Script that starts a Flask Web app
"""
from flask import Flask
app = Flask(__name__)

@app.get('/', strict_slashes=False)
def index():
    return "Hello HBNB"

@app.get('/hbnb')
def hbnb():
    return "HBNB"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')