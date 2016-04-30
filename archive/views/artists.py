from flask import render_template

from archive import app


@app.route('/artist/write/', methods=['GET'])
def artist_write():

    return render_template(
        'artist/write.html',
    )
