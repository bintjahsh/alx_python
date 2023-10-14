"""This module creates a script that starts a Flask
web application that creates five routes including
one that must receive a variable, an integer n
"""
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

@app.route('/python/', defaults={'text': 'is_cool'})

@app.route('/python/<text>')
def show_python(text):
    return ("Python {}".format(text).replace('_', ' '))

@app.route('/number/<int:n>')
def show_python(n):
    return ("{} is a number".format(n))

if __name__ == '__main__':
    app.run()