#!/usr/bin/env python3
from flask import Flask
from routes import main
from POSTGRES.PostgresDBManager import PostgresDBManager
from PYTHON_PROGRAMS.my_user_song_app import my_user_song_app
import sys
import os
from CONSTANTS.appconstants import appconstants

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Single factory function for Flask application instance
# This function initializes the Flask app, sets up the database connection,
# and registers the main blueprint for routing.
# It also handles the database connection and stores it in the app config for later use.
def create_app():
    """Application factory function to create the Flask app instance"""
    app = Flask(__name__, template_folder='html')
    
    # Set up configurations
    app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this in production
    
    # Initialize database connection
    try:
        print("Initializing postgreDB database connection...")
        # Initialize the connection pool with parameters from appconstants
        # Create a database manager instance
        songPostgresDBManager = PostgresDBManager()
        songPostgreConn = songPostgresDBManager.get_connection()
        if songPostgreConn:
            print("PostgreDB Database connection successful!")
            # Store database manager in app config for later use
            app.config['DB_CONNECTION'] = songPostgreConn
            app.config['DB_MANAGER'] = songPostgresDBManager
        else:
            print("PostgreDB Database connection failed!")
    except Exception as e:
        print(f"Error initializing song postgreDB database: {e}")
    
    # # Initialize the user song application logic
    # try:
    #     print("Initializing my_user_song_app...")
    #     # Create an instance of my_user_song_app and store it in the app context
    #     userSongApp = my_user_song_app()
    #     app.my_user_song_app = userSongApp
    #     print("my_user_song_app initialized successfully!")
    # except Exception as e:
    #     print(f"Error initializing my_user_song_app: {e}")
    
    # # Register the blueprint
    # app.register_blueprint(main)
    
    return app

if __name__ == '__main__':
    # Create the Flask application
    app = create_app()
    
    # Run the application
    print("Starting Flask application...")
    print("Available routes:")
    print("- GET  http://localhost:5001/        (Home page)")
    print("- GET  http://localhost:5001/health  (Health check)")
    print("- GET  http://localhost:5001/getUserBase  (Get user base)")
    print("- POST http://localhost:5001/addUser  (Add a user)")

    localhost = appconstants['localhost']
    port = appconstants['applicationPort']

    app.run(debug=True, host=localhost, port=port)
