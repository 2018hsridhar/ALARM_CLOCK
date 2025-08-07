#!/usr/bin/env python3
from flask import Flask
from routes import main
from POSTGRES.PostgresDBManager import PostgresDBManager
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
    
    # Initialize database connection
    try:
        print("Initializing database connection...")
        postgresDBManager = PostgresDBManager()
        postgresDBManager.initialize_pool()
        conn = postgresDBManager.get_connection()
        if conn:
            print("Database connection successful!")
            # Store connection in app config for later use
            app.config['DB_CONNECTION'] = conn
        else:
            print("Database connection failed!")
    except Exception as e:
        print(f"Error initializing database: {e}")
    
    # Register the blueprint
    app.register_blueprint(main)
    
    return app

if __name__ == '__main__':
    # Create the Flask application
    app = create_app()
    
    # Run the application
    print("Starting Flask application...")
    print("Available routes:")
    print("- GET  http://localhost:5001/        (Home page)")
    print("- GET  http://localhost:5001/health  (Health check)")

    localhost = appconstants['localhost']
    port = appconstants['applicationPort']

    app.run(debug=True, host=localhost, port=port)
