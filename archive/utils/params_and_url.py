from archive.models import Artist, Image


def get_next_url(params):

    dict_params = params_to_dict(params)

    next_url = ""

    for param in dict_params:
        next_url = "&" + str(param) + "=" + params[param]

    return next_url


def params_to_dict(params):

    result = {}
    for param in params:
        result[param] = params.get(param, None)

    return result


def artist_data_filter(params, datas):

    if params.get('name'):
        datas = datas.filter(Artist.name == params.get('name'))

    if params.get('birth_year'):
        datas = datas.filter(Artist.birth_year == params.get('birth_year'))

    if params.get('genre'):
        datas = datas.filter(Artist.gerne == params.get('genre'))

    if params.get('country'):
        datas = datas.filter(Artist.country == params.get('country'))

    if params.get('death_year'):
        datas = datas.filter(Artist.death_year == params.get('death_year'))

    if params.get('title'):
        datas = datas.filter(
            Artist.id == Image.query.filter(
                Image.title == params.get('title')
            ).value('artist_id')
        )

    return datas
