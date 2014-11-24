from __future__ import print_function
from flask import Flask, render_template
import locale

locale.setlocale(locale.LC_ALL, 'en_GB')

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.jinja')


@app.route('/about')
def about():
    return render_template('about.jinja')


@app.route('/contact')
def contact():
    return render_template('contact.jinja')


@app.route('/gallery')
def gallery():
    return render_template('gallery.jinja')


if __name__ == '__main__':
    app.run(debug=True)
