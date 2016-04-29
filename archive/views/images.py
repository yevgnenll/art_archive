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
        ).limit(count).offset(page * count)

        result = []
        for image in images:
            data = image.Image.data_to_dict(
                image.name
            )
            result.append(data)

        return jsonify(result=result)
