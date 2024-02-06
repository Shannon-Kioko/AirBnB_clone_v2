#!/usr/bin/python3
"""
Module uses Flask to render cities
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    """reload storage after each request
    """
    storage.close()

@app.route('/cities_by_states')
def cities_by_states():
    states = storage.all("State")
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    return render_template('cities_by_states.html', states=sorted_states)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
