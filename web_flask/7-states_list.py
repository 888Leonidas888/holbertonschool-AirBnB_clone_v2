#!/usr/bin/python3
"""Corriendo web service con flask"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Esta ruta muestra un saludo en el home"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Nuestro primer recurso"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """Nuestro primera variable"""
    cleaned_text = text.replace('_', ' ')
    return f"C {cleaned_text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def Python_is_cool(text='is cool'):
    """Python si es genial!!!"""
    cleaned_text = text.replace('_', ' ')
    return f"Python {cleaned_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def is_it_a_number(n):
    """Python si es genial!!!"""
    if isinstance(n, int):
        return f"{n} is number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Python si es genial!!!"""
    if isinstance(n, int):
        return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """odd or even"""
    if isinstance(n, int):
        text = 'is odd'
        if n % 2 == 0:
            text = 'is even'
        return render_template('6-number_odd_or_even.html', number=n, t=text)


@app.teardown_appcontext()
def close_session():
    storage.close()


@app.route("/states_list", strict_slashes=False)
def list_states():
    dict_states = storage.all(State).values()
    sorted_states = sorted(dict_states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
