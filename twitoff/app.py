from flask import Flask 

""" how to run: FLASK_APP=app.py flask run"""

def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'hello twitoff'
    return app
