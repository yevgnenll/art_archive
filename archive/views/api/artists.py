from flask import render_template, request, jsonify, abort
from sqlalchemy.orm import sessionmaker

from archive import app, db
from archive.models import Artist, Image
from archive.utils import pagination_dict


@app.route('/api/artists/', methods=['GET', 'POST'])
def artist_list():

    if request.method == 'GET':
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

        content = []
        for artist in artists:
            content.append(artist.data_to_dict())

        return jsonify(
            cod=200,
            content=content,
            pagination=pagination_dict(page, count, list_amout, next_url),
        )

    elif request.method == 'POST':

        name = request.values.get('name', type=str)
        genre = request.values.get('genre')
        birth_year = request.values.get('birth_year', None, type=int)
        death_year = request.values.get('death_year', None, type=int)
        country = request.values.get('country')

        if not name:
            abort(400)

        db.session.add(
            Artist(
                name=name,
                genre=genre,
                birth_year=birth_year,
                death_year=death_year,
                country=country,
            )
        )

        db.session.commit()

        return jsonify(
            code=201,
            content={'result': 'Created'},
        )


@app.route('/api/artists/<id>', methods=['PUT'])
def modify(id):

    params = request.values
    result_param = {}
    for param in params:
        if params.get(param) == '':
            continue
        result_param[param] = params.get(param)

    artist = Artist.query.filter(Artist.id == id).update(result_param)
    Artist.query.session.commit()

    return jsonify(
        code=200,
        content={'result': 'OK'},
    )


@app.route('/api/artists/<id>', methods=['GET'])
def detail(id):

    artist = Artist.query.get_or_404(id)
    images = Image.query.filter(Image.artist_id == id).all()

    content = artist.detail_to_dict(images)

    return jsonify(
        code=200,
        content=content,
    )


@app.route('/api/artists/<id>', methods=['DELETE'])
def delete(id):

    image = Image.query.filter(Image.artist_id == id).delete()
    artist = Artist.query.filter(Artist.id == id).delete()

    Image.query.session.commit()
    Artist.query.session.commit()

    return jsonify(
        code=204,
        content={"result": "No Content"},
    )
