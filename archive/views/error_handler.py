from archive import app

from flask import request, jsonify


@app.errorhandler(404)
def error404(e):

    params = request.args
    error_message = ""

    # page list -> "Data doesn't exist"
    if request.method == "GET":
        error_message = "Data doesnt't exist"

    # image detail -> o

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
