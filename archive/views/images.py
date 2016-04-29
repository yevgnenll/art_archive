from flask import render_template, request, jsonify

from archive import app
from archive.models import Artist, Image


@app.route('/api/images/', methods=['GET', 'POST'])
def images_list():

    if request.method == 'GET':

        page = request.args.get('page', 1, type=int)
        count = request.args.get('count', 10, type=int)

        images = Image.query.all()

        result = []
        for image in images:
            data = {}
            data['title'] = image.title
            data['year'] = image.year
            data['image_url'] = image.image_url
            data['description'] = image.description
            data['artist_id'] = image.artist_id

            result.append(data)

        return jsonify(result=result)
