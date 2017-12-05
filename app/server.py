# encoding: utf-8
"""Application.

Starts the Flask application
"""

from flask import Flask, jsonify

api = Flask(__name__)


@api.route('/', methods=['GET'])
def health_check():
    """Returns health information"""
    return jsonify({
        "message": "I'm alive and well, thank you very much for caring!"
    })
    