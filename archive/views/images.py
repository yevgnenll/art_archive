from flask import render_template, request, jsonify
from sqlalchemy.orm import sessionmaker

from archive import app
from archive.models import Artist, Image

from archive import db


@app.route('/api/images/', methods=['GET', 'POST'])
def images_list():

    if request.method == 'GET':

        page = request.args.get('page', 1, type=int)
        count = request.args.get('count', 10, type=int)

        images = Image.query.join(Artist, Image.artist_id == Artist.id)
        images = images.add_columns(
            Artist.name,
            Image.title,
            Image.year,
            Image.image_url,
            Image.description
        )

        # apply serialize
        result = []
        for image in images:
            data = {}
            data['title'] = image.title
            data['year'] = image.year
            data['image_url'] = image.image_url
            data['description'] = image.description
            data['artist_name'] = image.name

            result.append(data)

        return jsonify(result=result)
