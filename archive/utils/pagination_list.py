from flask import request

from .params_and_url import get_params


def pagination_dict(params, amount):

    page = request.args.get('page', 1, type=int)
    count = request.args.get('count', 10, type=int)
    current_url = request.base_url
    start = page * count - count
    uri_param = get_params(params)

    next_url = ""
    if start + count - 1 < amount:
        if "images" in current_url:
            next_url = "/api/images/?page=" + str(page + 1) + "&count=" + str(count) + uri_param
        elif "artists" in current_url:
            next_url = "/api/artists/?page=" + str(page + 1) + "&count=" + str(count) + uri_param
    else:
        next_url = None

    pagination = {
        "current_page": page,
        "next_url": next_url,
    }

    return pagination


def pagination_for_list(params, datas):

    page = params.get('page', 1, type=int)
    count = params.get('count', 10, type=int)

    start = page * count - count
    amount = datas.count()

    datas = datas.limit(count).offset(start)

    return datas
