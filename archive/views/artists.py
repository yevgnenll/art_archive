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
    next_url = ""

    if title:
        artists = artists.filter(
            Artist.id == Image.query.filter(
                Image.title == title
            ).value('artist_id')
        )
        next_url += "&title=" + title
    if name:
        artists = artists.filter(Artist.name == name)
        next_url += "&name=" + name
    if birth_year:
        artists = artists.filter(Artist.birth_year == birth_year)
        next_url += "&born=" + str(birth_year)
    if genre:
        artists = artists.filter(Artist.genre == genre)
        next_url += "&genre=" + genre
    if country:
        artists = artists.filter(Artist.country == country)
        next_url += "&country=" + country
    if death_year:
        artists = artists.filter(Artist.death_year == death_year)
        next_url += "&death=" + death_year

    list_amout = artists.count()
    start = page * count - count
    artists = artists.limit(count).offset(start)

    if start + count - 1 < list_amout:
        next_url = "/api/artists/?page=" + str(page + 1) + "&count=" + str(count) + next_url
    else:
        next_url = None

    pagination = {
        "current_page": page,
        "next_url": next_url,
    }

    content = []
    for artist in artists:
        content.append(artist.data_to_dict())

    return jsonify(
        cod=200,
        content=content,
        pagination=pagination,
    )
