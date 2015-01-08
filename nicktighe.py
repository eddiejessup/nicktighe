from __future__ import print_function
from flask import Flask, render_template
import locale

locale.setlocale(locale.LC_ALL, 'en_GB')

app = Flask(__name__)


@app.route('/index.html')
def home():
    return render_template('home.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/gallery.html')
def gallery():
    return render_template('gallery.html')


# if __name__ == '__main__':
#     app.run(debug=True)
