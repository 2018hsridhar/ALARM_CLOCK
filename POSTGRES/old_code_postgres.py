

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
