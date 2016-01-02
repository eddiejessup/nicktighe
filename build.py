from staticjinja import make_site

items = [
    {'filename': 'pub.jpeg',
     'title': 'Scarborough Hotel',
     'medium': 'Oil on canvas',
     'size': '44 cm x 62 cm'},
    {'filename': 'cow.jpeg',
     'title': 'For the Saward family',
     'medium': 'Oil on canvas',
     'size': '42 cm x 59 cm'},
    {'filename': 'dog.jpeg',
     'title': 'Archie',
     'medium': 'Pencil and charcoal on paper',
     'size': '21 cm x 29 cm'},
    {'filename': 'owl.jpeg',
     'title': 'Bowland Hen Harrier',
     'medium': 'Pencil on paper',
     'size': '29 cm x 42 cm'},
    {'filename': 'he_and_she.jpeg',
     'title': 'He and She',
     'medium': 'Pencil on paper',
     'size': '40 cm x 25 cm'},
    {'filename': 'george.jpeg',
     'title': 'George the Boxer',
     'medium': 'Pencil, chalk, charcoal, watercolour and acrylic on paper',
     'size': '21 cm x 29 cm'},
    {'filename': 'bluebell.jpeg',
     'title': 'Untitled',
     'medium': 'Ink, pencil, chalk, watercolour and acrylic on paper'},
]


def get_gallery_context():
    return {'items': items}


if __name__ == "__main__":
    site = make_site(
        contexts=[
            ('gallery.html', get_gallery_context),
        ],
        outpath='public',
        staticpaths=['static/'],
    )
    site.render(use_reloader=False)
