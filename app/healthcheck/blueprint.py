"""app.healthcheck.blueprint

Module taht deals with Blueprint-related stuff."""
from flask import Blueprint
from app.healthcheck import healthcheck

def create_blueprint():
    """Creates a Blueprint"""
    blueprint = Blueprint('Health Check Blueprint', __name__)
    blueprint.route('/')(healthcheck.healthcheck)
    return blueprint
