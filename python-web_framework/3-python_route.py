""" This module creates a script that starts a Flask
web application
"""

from flask import Flask, url_for

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello():
    return ("Hello HBNB!")

@app.route('/hbnb')
def second_hello():
    return ("HBNB")

@app.route('/c/<text>')
def show_c(text):
    return ("C {}".format(text).replace('_', ' '))

@app.route('/python/<text>')
def show_python(text):
    return ("Python {}".format(text).replace('_', ' '))

with app.test_request_context():
    print(url_for('show_python', text='is cool'))

if __name__ == '__main__':
    app.run()