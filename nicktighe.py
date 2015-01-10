from __future__ import print_function
from flask import Flask, render_template
import locale

locale.setlocale(locale.LC_ALL, locale.getdefaultlocale())

app = Flask(__name__)


items = [
    {'filename': 'gallery/pub.jpeg',
     'title': 'Scarborough Hotel. Oil on canvas, 44 cm by 62 cm'},
    {'filename': 'gallery/cow.jpeg',
     'title': 'For the Saward family. Oil on canvas, 42 cm by 59 cm'},
    {'filename': 'gallery/dog.jpeg',
     'title': 'Archie. Pencil and charcoal on paper, 21 cm by 29 cm'},
    {'filename': 'gallery/owl.jpeg',
     'title': 'Bowland Hen Harrier. Pencil on paper, 29 cm by 42 cm'},
    {'filename': 'gallery/bluebell.png',
     'title': 'Untitled. Ink, pencil, chalk, watercolour and acrylic.'},
]


@app.route('/index.html')
def home():
    return render_template('home.html')


@app.route('/gallery.html')
def gallery():
    return render_template('gallery.html', items=items)


# if __name__ == '__main__':
#     app.run(debug=True)
