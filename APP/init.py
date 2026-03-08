# This file initializes the Flask application.
# -*- coding: utf-8 -*-

# Register the blueprint in the application factory

# from flask import Flask
# from .business_objects.my_user_song_app import my_user_song_app  # Import the application logic

# # Application factory function to create the Flask app instance ( a single object )
# def create_app():
#     app = Flask(__name__)
#     app.my_user_song_app = my_user_song_app()  # Initialize the application logic
    
#     # Set up configurations here if needed
#     # app.config['SECRET_KEY'] = 'your_secret_key'

#     # Register blueprints or routes here
#     from .routes import main as main_blueprint
#     app.register_blueprint(main_blueprint)

#     return app


# Connect to the PostgresDB and initialize the application logic

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from ALARM_CLOCK.POSTGRES.PostgresDBManager import connect_to_postgresDB  # Import the database connection function
from POSTGRES.PostgresDBManager import PostgresDBManager  # Import the database manager module
from my_user_song_app import my_user_song_app

def __init__():
    postgresManager = PostgresDBManager()  # Create an instance of the PostgresDBManager
    results = postgresManager.execute_query("SELECT 1")  # Example query to test the connection
    userSongApp = my_user_song_app()  # Initialize the application logic
    user_base = userSongApp.get_user_base(postgresManager)
    for user in user_base:
        print(f"User: {user}")
    userArgs = {
        "first_name": "Jane",
        "last_name": "Wang",
        "date_of_birth": "1994-01-01",
    }
    user_added_status = userSongApp.add_user(postgresManager, **userArgs)
    print(f"User added status: {user_added_status}")

# Call the function when the module is imported
if __name__ == "__main__":
    __init__()
