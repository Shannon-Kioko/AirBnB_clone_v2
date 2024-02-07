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


@app.route('/number_template/<n>')
def number_template(n):
    num = int(n)
    if isinstance(num, int):
        return render_template('5-number.html.', num=num)


@app.route('/number_odd_or_even/<n>')
def odd_or_even(n):
    type_of_num = None
    num = int(n)
    if isinstance(num, int):
        if num % 2 == 0:
            type_of_num = 'even'
        else:
            type_of_num = 'odd'
        return render_template('6-number_odd_or_even.html',
                               num=num,
                               type_of_num=type_of_num)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
