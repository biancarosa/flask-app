"""Deals with HealthCheck route."""
from flask import jsonify

def healthcheck():
    """Returns health information"""
    return jsonify({
        "message": "I'm alive and well, thank you very much for caring!"
    })
    