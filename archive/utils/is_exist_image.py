from archive.models import Image


def title_artist_exist(params):

    title = params.get('title')
    artist_id = params.get('artist_id')

    is_check_image = Image.query.filter(Image.artist_id == artist_id).\
        filter(Image.title == title).filter(Image.artist_id == artist_id)

    if is_check_image.all():
        return False
    else:
        return True
