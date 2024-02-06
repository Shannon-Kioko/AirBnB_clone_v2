#!/usr/bin/python3
"""
This module starts a flask app on port 5000
"""

from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
def index():
    return "Hello HBNB"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')