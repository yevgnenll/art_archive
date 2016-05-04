from flask import render_template, request, jsonify, abort
from sqlalchemy.orm import sessionmaker

from archive import app, db
from archive.models import Artist, Image
from archive.utils import pagination_dict, artist_data_filter, pagination_for_list


@app.route('/api/artists/', methods=['GET'])
def artist_list():

    artists = artist_data_filter(request.args, Artist.query)
    list_amout = artists.count()

    artists = pagination_for_list(request.args, artists)

    content = []
    for artist in artists:
        content.append(artist.data_to_dict())

    return jsonify(
        cod=200,
        content=content,
        pagination=pagination_dict(request.args, list_amout),
    )


@app.route('/api/artists/', methods=['POST'])
def artist_insert():

    datas = request.values
    name = datas.get('name', type=str)

    if not name:
        abort(400)

    artist = Artist()
    db.session.add(
        artist.data_get_as_dict(datas)
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
