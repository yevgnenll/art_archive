from flask import render_template

from archive import app
from archive.models import Artist


@app.route('/image/write/', methods=['GET'])
def image_write():

    authors = Artist.query.all()

    return render_template(
        'image/write.html',
        artists=authors,
    )
