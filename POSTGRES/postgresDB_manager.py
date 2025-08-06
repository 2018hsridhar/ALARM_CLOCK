from asyncio.log import logger
import psycopg2
from psycopg2 import sql
from psycopg2 import pool

from CONSTANTS.appconstants import appconstants

import psycopg2
from psycopg2 import pool

# DatabaseManager class to manage the connection pool
# This class provides methods to initialize the pool, get a connection, return a connection, and
# close the pool. It is designed to be used as a singleton, ensuring that only one instance of the
# connection pool exists throughout the application lifecycle.
# The pool is initialized with a minimum and maximum number of connections, and it can be configured
# with additional parameters such as user, password, host, port, and database name.

# Connection pool for managing database connections
# Reduce the number of connections to the database by using a connection pool by reusing existing connections
# And enable response times

class DatabaseManager:
    _connection_pool = None

    @classmethod
    def initialize_pool(cls, min_connections, max_connections, **kwargs):
        """
        Initializes the connection pool. This should be called once at application startup.
        :param min_connections: Minimum number of connections in the pool.
        :param max_connections: Maximum number of connections in the pool.
        :param kwargs: Additional keyword arguments for the connection (e.g., user, password,
        host, port, database).
        """
        if cls._connection_pool is None:
            try:
                cls._connection_pool = pool.SimpleConnectionPool(
                    min_connections,
                    max_connections,
                    **kwargs
                )
                print("Connection pool initialized successfully.")
            except Exception as e:
                print(f"Error initializing connection pool: {e}")
                # Handle error appropriately, e.g., exit or log

    @classmethod
    def get_connection(cls):
        """
        Retrieves a connection from the pool.
        """
        if cls._connection_pool is None:
            raise RuntimeError("Connection pool not initialized. Call initialize_pool first.")
        try:
            return cls._connection_pool.getconn()
        except Exception as e:
            print(f"Error getting connection from pool: {e}")
            raise

    @classmethod
    def put_connection(cls, connection):
        """
        Returns a connection to the pool.
        """
        if cls._connection_pool is not None and connection is not None:
            cls._connection_pool.putconn(connection)

    @classmethod
    def close_pool(cls):
        """
        Closes all connections in the pool. This should be called at application shutdown.
        """
        if cls._connection_pool is not None:
            cls._connection_pool.closeall()
            cls._connection_pool = None
            print("Connection pool closed.")

# Example Usage:
if __name__ == "__main__":
    # Initialize the pool once at the beginning of your application
    db_name = appconstants["db_name"]
    db_user = appconstants["db_user"]
    db_password = appconstants["db_password"]
    host = appconstants["host"]
    port = appconstants["port"]
    if not db_name or not db_user or not db_password or not host or not port:
        raise ValueError("Database connection parameters are not set in appconstants.")
    # Initialize the connection pool with the database parameters
    DatabaseManager.initialize_pool(
        min_connections=1,
        max_connections=10,
        user=db_user,
        password=db_password,
        host=host,
        port=port,
        database=db_name
    )

    # Get a connection, perform operations, and return it to the pool
    conn = None
    try:
        conn = DatabaseManager.get_connection()
        cursor = conn.cursor()
        versionSelectQuery = "SELECT version();"
        cursor.execute(versionSelectQuery)
        status = cursor.fetchone()
        print(f"Connected to the database successfully: {status[0]}")
        cursor.close()
    except Exception as e:
        print(f"Operation failed: {e}")
    finally:
        if conn:
            DatabaseManager.put_connection(conn)

    # Close the pool when your application shuts down
    DatabaseManager.close_pool()



# def connect_to_postgresDB():
#     print("Connecting to PostgresDB...")
#     """
#     Connect to the Postgres database and return the connection object.
#     """
#     try:
#         # Connect to your postgres DB
#         db_name = appconstants["db_name"]
#         db_user = appconstants["db_user"]
#         db_password = appconstants["db_password"]
#         host = appconstants["host"]
#         port = appconstants["port"]

#         connectionString = f"dbname={db_name} user={db_user} password={db_password} host={host} port={port}"
#         conn = psycopg2.connect(connectionString)

#         # Open a cursor to perform database operations
#         cur = conn.cursor()

#         # Return the connection and cursor
#         print("Connection to PostgresDB successful!")
#         return conn, cur
#     except Exception as e:
#         print(f"Error connecting to the PostgresDB: {e}")
#         return None, None
