from flask import render_template

from archive import app
from archive.models import Artist


@app.route('/artist/write/', methods=['GET'])
def artist_write():

    return render_template(
        'artist/write.html',
    )


@app.route('/artist/update/<id>', methods=['GET'])
def artist_update(id):

    artist = Artist.query.get_or_404(id)

    return render_template(
        'artist/update.html',
        artist=artist,
    )
