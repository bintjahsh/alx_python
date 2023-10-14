"""This module creates a script that starts a Flask
web application that creates five routes including
one that must receive a variable, an integer n
"""

from flask import Flask

"""This module creates a script that starts a Flask
web application
"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return ("Hello HBNB!")

@app.route('/hbnb', strict_slashes=False)
def second_hello():
    return ("HBNB")

@app.route('/c/<text>', strict_slashes=False)
def show_c(text):
    return ("C {}".format(text).replace('_', ' '))

@app.route('/python/', defaults={'text': 'is_cool'})

@app.route('/python/<text>', strict_slashes=False)
def show_python(text):
    return ("Python {}".format(text).replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def show_python(n):
    return ("{} is a number".format(n))

if __name__ == '__main__':
    app.run(port=5000)