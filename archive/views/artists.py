from flask import render_template, request, jsonify, abort
from sqlalchemy.orm import sessionmaker

from archive import app
from archive.models import Artist, Image

from archive import db


@app.route('/api/artists/', methods=['GET'])
def artist_list():

    page = request.args.get('page', 1, type=int)
    count = request.args.get('count', 10, type=int)

    name = request.args.get('name', None, type=str)
    birth_year = request.args.get('born', None, type=int)
    genre = request.args.get('genre', None, type=str)
    title = request.args.get('title', None, type=str)
    country = request.args.get('country', None, type=str)
    death = request.args.get('death', None, type=int)

    artists = Artist.query.join(Image, Artist.id == Image.artist_id)

    content = []
    for artist in artists:
        content.append(artist.data_to_dict())

    return jsonify(result=content)
