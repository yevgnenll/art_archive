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
        images = images.limit(count).offset(start)

        list_amount = images.count()

        if start + count - 1 < list_amount:
            next_url = "/api/images/?page=" + str(page + 1) + "&count=" + str(count) + next_url
        else:
            next_url = None

        pagination = {
            "current_page": page,
            "next_url": next_url,
        }

        content = []
        for image in images:
            data = image.Image.data_to_dict(
                image.name
            )
            content.append(data)

        return jsonify(
            content=content,
            code=200,
            pagination=pagination,
        )
