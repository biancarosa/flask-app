"""Deals with HealthCheck route."""
from flask import jsonify

def healthcheck():
    """Returns health information"""
    return jsonify({
        "message": "I feel good."
    })
    