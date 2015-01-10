from __future__ import print_function
from flask import Flask, render_template
import locale

locale.setlocale(locale.LC_ALL, locale.getdefaultlocale())

app = Flask(__name__)


items = [
    {'filename': 'gallery/pub.jpeg',
     'title': 'Scarborough Hotel',
     'medium': 'Oil on canvas',
     'size': '44 cm x 62 cm'},
    {'filename': 'gallery/cow.jpeg',
     'title': 'For the Saward family',
     'medium': 'Oil on canvas',
     'size': '42 cm x 59 cm'},
    {'filename': 'gallery/dog.jpeg',
     'title': 'Archie',
     'medium': 'Pencil and charcoal on paper',
     'size': '21 cm x 29 cm'},
    {'filename': 'gallery/owl.jpeg',
     'title': 'Bowland Hen Harrier',
     'medium': 'Pencil on paper',
     'size': '29 cm x 42 cm'},
    {'filename': 'gallery/he_and_she.jpeg',
     'title': 'He and She',
     'medium': 'Pencil on paper',
     'size': '40 cm x 25 cm'},
    {'filename': 'gallery/george.jpeg',
     'title': 'George the Boxer',
     'medium': 'Pencil, chalk, charcoal, watercolour and acrylic on paper',
     'size': '21 cm x 29 cm'},
    {'filename': 'gallery/bluebell.png',
     'title': 'Untitled',
     'medium': 'Ink, pencil, chalk, watercolour and acrylic on paper'},
]


@app.route('/index.html')
def home():
    return render_template('home.html')


@app.route('/gallery.html')
def gallery():
    return render_template('gallery.html', items=items)


if __name__ == '__main__':
    app.run(debug=True)
