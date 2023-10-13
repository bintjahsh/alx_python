""" This module creates a script that starts a Flask
web application
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello():
    return "<p>Hello HBNB!</p>"

if __name__ == '__main__':
    app.run()