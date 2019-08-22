"""Main application and routing logic for twitoff."""
""" how to run: FLASK_APP=twitoff:APP flask run/shell"""
from flask import Flask, render_template, request
from .models import DB, User


def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['ENV'] = 'debug' # TODO change before deploying
    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)
    
    return app
