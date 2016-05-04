from archive import app

from flask import request, jsonify


@app.errorhandler(404)
def error404(e):

    error_message = ""

    if request.method == 'PUT' or request.method == 'DELETE':
        if 'artists' in request.url:
            error_message = "Artist is not exist"
        elif 'images' in request.url:
            error_message = "Image is not exist"
    else:
        error_message = "Data doesnt't exist"

    return jsonify(
        code=404,
        error=error_message
    )


@app.errorhandler(500)
def error500(e):

    return jsonify(
        code=500,
        error="Internal Server Error",
    )


@app.errorhandler(400)
def error400(e):

    return jsonify(
        code=400,
        error="Bad Request",
    )
