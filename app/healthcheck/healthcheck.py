"""app.healthcheck.healthcheck

Module that deals with HealthCheck route."""
from flask import jsonify

def healthcheck():
    """Returns health information"""
    return jsonify({
        "message": "I feel good."
    })
    