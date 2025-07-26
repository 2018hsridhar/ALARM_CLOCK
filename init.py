# This file initializes the Flask application.
# -*- coding: utf-8 -*-

# Register the blueprint in the application factory

from flask import Flask
from .business_objects.my_user_song_app import my_user_song_app  # Import the application logic

# Application factory function to create the Flask app instance ( a single object )
def create_app():
    app = Flask(__name__)
    app.my_user_song_app = my_user_song_app()  # Initialize the application logic
    
    # Set up configurations here if needed
    # app.config['SECRET_KEY'] = 'your_secret_key'

    # Register blueprints or routes here
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
