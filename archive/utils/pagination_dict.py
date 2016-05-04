from flask import request

from .params_and_url import get_next_url


def pagination_dict(params, amount):

    page = request.args.get('page', 1, type=int)
    count = request.args.get('count', 10, type=int)
    current_url = request.base_url
    start = page * count - count
    next_url = get_next_url(params)

    if start + count - 1 < amount:
        if "images" in current_url:
            next_url = "/api/images/?page=" + str(page + 1) + "&count=" + str(count) + next_url
        elif "artists" in current_url:
            next_url = "/api/artists/?page=" + str(page + 1) + "&count=" + str(count) + next_url
    else:
        next_url = None

    pagination = {
        "current_page": page,
        "next_url": next_url,
    }

    return pagination
