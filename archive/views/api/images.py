from flask import render_template, request, jsonify, abort
from sqlalchemy.orm import sessionmaker

from archive import app
from archive.models import Artist, Image

from archive.utils import pagination_dict


@app.route('/api/images/', methods=['GET', 'POST'])
def images():

    # abort(404)

    if request.method == 'GET':

        page = request.args.get('page', 1, type=int)
        count = request.args.get('count', 10, type=int)

        title = request.args.get('title', None, type=str)
        name = request.args.get('name', None, type=str)
        year = request.args.get('year', None, type=int)
        description = request.args.get('description', None, type=str)

        images = Image.query.join(Artist, Image.artist_id == Artist.id)

        images = images.add_columns(
            Artist.name,
            Image.title,
            Image.year,
            Image.image_url,
            Image.description
        )

        next_url = ""

        if title:
            images = images.filter(Image.title == title)
            next_url += "&title=" + title
        if name:
            images = images.filter(Artist.name == name)
            next_url += "&name=" + name
        if year:
            images = images.filter(Image.year == year)
            next_url += "&year=" + year
        if description:
            images = images.filter(Image.description == description)
            next_url += "&description=" + description

        start = page * count - count
        list_amount = images.count()

        images = images.limit(count).offset(start)

        content = []
        for image in images:
            data = image.Image.data_to_dict(
                image.name
            )
            content.append(data)

        return jsonify(
            content=content,
            code=200,
            pagination=pagination_dict(page, count, list_amount, next_url),
        )

    elif request.method == 'POST':

        datas = request.values

        title = datas.get('title')
        artist_id = datas.get('artist_id')

        is_check = Image.query.filter(Image.artist_id == artist_id).\
            filter(Image.title == title)

        print(is_check.all())

        if is_check.all():
            abort(400)

        image = Image()
        Image.query.session.add(
            image.data_get_as_dict(datas)
        )

        Image.query.session.commit()

        return jsonify(
            code=201,
            result="Created",
        )


@app.route('/api/images/<id>', methods=['GET'])
def images_detail(id):

    image = Image.query.get_or_404(id)
    name = Artist.query.filter(Artist.id == image.artist_id)

    content = image.data_to_dict(
        name.one().name,
    )

    return jsonify(
        code=200,
        content=content,
    )


@app.route('/api/images/<id>', methods=['PUT'])
def images_update(id):

    image = Image.query.get_or_404(id)
    name = Artist.query.filter(Artist.id == image.artist_id)

    content = image.data_to_dict(
        name.one().name,
    )

    return jsonify(
        code=200,
        content=content,
    )
