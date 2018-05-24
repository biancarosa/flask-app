# encoding: utf-8
"""Application.

Starts the Flask application
"""
from flask import Flask

from healthcheck import blueprint as health_check_blueprint

def create_app():
    """Creates a Flask App"""
    app = Flask(__name__)
    app.register_blueprint(health_check_blueprint.create_blueprint())
    return app
