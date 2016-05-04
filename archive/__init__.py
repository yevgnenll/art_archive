from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

"""
from werkzeug import Request


class MethodRewriteMiddleware(object):

    def __init__(self, app, input_name='_method'):
        self.app = app
        self.input_name = input_name

    def __call__(self, environ, start_response):
        request = Request(environ)

        if self.input_name in request.form:
            method = request.form[self.input_name].upper()

            if method in ['GET', 'POST', 'PUT', 'DELETE']:
                environ['REQUEST_METHOD'] = method

        return self.app(environ, start_response)

"""
app = Flask(__name__)
app.config.from_object('config')
# app.wsgi_app = MethodRewriteMiddleware(app.wsgi_app)

db = SQLAlchemy(app)


from archive import views
