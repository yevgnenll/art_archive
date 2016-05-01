from flask import render_template

from archive import app
from archive.models import Artist, Image


@app.route('/image/write/', methods=['GET'])
def image_write():

    authors = Artist.query.all()

    return render_template(
        'image/write.html',
        artists=authors,
    )


@app.route('/image/update/<id>', methods=['GET'])
def image_update(id):

    image = Image.query.get_or_404(id)
    authors = Artist.query.all()

    return render_template(
        'image/update.html',
        artists=authors,
        image=image,
    )


@app.route('/image/delete/<id>', methods=['GET'])
def image_delete(id):

    image = Image.query.get_or_404(id)

    return render_template(
        'image/delete.html',
        image=image,
    )
