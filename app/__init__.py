from flask import Flask
from .api import api_blueprint
from .home import home_blueprint

def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_extensions(app):
    pass


def register_blueprints(app):
    app.register_blueprint(api_blueprint)
    app.register_blueprint(home_blueprint)
