"""app.main

Module that starts the Flask application
"""
from flask import Flask

from app.healthcheck import blueprint as health_check_blueprint

# pylint: disable=C0103
app = Flask(__name__)
app.register_blueprint(health_check_blueprint.create_blueprint())
