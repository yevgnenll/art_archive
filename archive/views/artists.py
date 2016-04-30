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
    death_year = request.args.get('death', None, type=int)

    artists = Artist.query

    if title:
        artists = artists.filter(
            Artist.id == Image.query.filter(
                Image.title == title
            ).value('artist_id')
        )
    if name:
        artists = artists.filter(Artist.name == name)
    if birth_year:
        artists = artists.filter(Artist.birth_year == birth_year)
    if genre:
        artists = artists.filter(Artist.genre == genre)
    if country:
        artists = artists.filter(Artist.country == country)
    if death_year:
        artists = artists.filter(Artist.death_year == death_year)

    start = page * count - count
    artists = artists.limit(count).offset(start)

    content = []
    for artist in artists:
        content.append(artist.data_to_dict())

    return jsonify(
        cod=200,
        content=content,
    )
