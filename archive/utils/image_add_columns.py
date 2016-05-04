from archive.models import Image, Artist


def image_add_columns(data):

    data = data.add_columns(
        Artist.name,
        Image.title,
        Image.year,
        Image.image_url,
        Image.description,
    )

    return data
