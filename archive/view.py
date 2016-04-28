from archive import app

from flask import render_template

from archive.models import Artist
from archive.models import Image


@app.route('/')
def index():

    return render_template(
        'home.html',
    )
