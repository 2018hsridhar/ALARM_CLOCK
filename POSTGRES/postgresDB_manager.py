from asyncio.log import logger
import psycopg2
from psycopg2 import sql

def connect_to_postgresDB():
    logger.info("Connecting to PostgresDB...")
    """
    Connect to the Postgres database and return the connection object.
    """
    try:
        # Connect to your postgres DB
        db_name = "harisrid"
        db_user = "harisrid"
        db_password = "harisrid"
        host = "localhost"
        port = "5432"

        connectionString = f"dbname={db_name} user={db_user} password={db_password} host={host} port={port}"
        conn = psycopg2.connect(connectionString)

        # Open a cursor to perform database operations
        cur = conn.cursor()

        # Return the connection and cursor
        return conn, cur
    except Exception as e:
        print(f"Error connecting to the PostgresDB: {e}")
        return None, None
