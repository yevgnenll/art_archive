from flask import request


def pagination_dict(page, count, amount, next_url):

    current_url = request.base_url
    start = page * count - count

    if start + count - 1 < amount:
        next_url = "/api/images/?page=" + str(page + 1) + "&count=" + str(count) + next_url
    else:
        next_url = None

    pagination = {
        "current_page": page,
        "next_url": next_url,
    }

    return pagination
