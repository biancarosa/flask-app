"""Module responsible for running the application"""
import os
from server import create_app

def main():
    """Runs the app through a Flask server.
       Not recommended for production use."""
    port = int(os.environ.get("PORT", 5000))
    app = create_app()
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    main()
