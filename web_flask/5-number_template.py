#!/usr/bin/python3
"""
Script starts Flas web app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    num = int(n)
    if isinstance(num, int):
        return '{} is a number'.format(num)


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    num = int(n)
    if isinstance(num, int):
        return render_template('5-number.html', num=num)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
