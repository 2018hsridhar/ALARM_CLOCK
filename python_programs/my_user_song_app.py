from CONSTANTS.appconstants import appconstants as appconstants
from CONSTANTS.music_database_select_queries import postgresql_queries as queries
from POSTGRES.PostgresDBManager import PostgresDBManager  # Import the database manager module

# I see -> PGADMIN enables expeditious development of the application.
class my_user_song_app:
    def __init__(self):
        pass
        # Initialize the user base with some default users
        # This is a simple in-memory user base for demonstration purposes.
        self.my_user_base = []
        self.user_songs = dict()
        # self.user_songs['Hari'] = ['Song1', 'Song2']
        # self.user_songs['Julian'] = ['Song5']
        # self.user_songs['Shrinal'] = ['Song6', 'Song7', 'Song8']
        # self.user_songs['Sophia'] = ['Song3', 'Song4']

    def get_user_base(self, postgresDBManager:PostgresDBManager):
        """
        Get the list of users.
        """
        select_user_query = queries["get_all_users_query"]
        try:
            self.my_user_base = [] # Reset the user base
            results = postgresDBManager.execute_query(select_user_query)
            for row in results:
                first_name = row[0]
                last_name = row[1]
                full_name = f"{first_name} {last_name}"
                self.my_user_base.append(full_name)
        except Exception as e:
            print(f"Error occurred while fetching user base: {e}")
        return self.my_user_base
    
    def add_user(self, postgresDBManager:PostgresDBManager, first_name, last_name, date_of_birth) -> int:
        """
        Add a new user to the user base.
        If the user already exists, do nothing.
        """
        status_code = 0
        raw_user_query = queries["insert_user_query"]
        user_query = raw_user_query % (f"'{first_name}'", f"'{last_name}'", f"'{date_of_birth}'")
        try:
            user_id = postgresDBManager.execute_query(user_query)  # Execute the insert query
            if user_id is not None:
                print(f"User {first_name} {last_name} added successfully with userId = {user_id}.")
            else:
                print(f"User {first_name} {last_name} already exists in the user base.")
                status_code = 1
        except Exception as e:
            print(f"Error occurred while adding user: {e}")
            status_code = 2
        return status_code

    def delete_user(self,postgresDBManager:PostgresDBManager, first_name, last_name):
        """
        Delete a user from the user base.
        If the user does not exist, do nothing.
        """
        delete_user_query = f"""
            DELETE FROM Users
            WHERE first_name = {first_name} AND last_name = {last_name};
        """
        try:
            postgresDBManager.execute_query(delete_user_query)
            print(f"User {first_name} {last_name} deleted successfully.")
        except Exception as e:
            print(f"Error occurred while deleting user: {e}")
            self.my_user_base.remove(user)
            # Also remove the user's song list if it exists
            if user in self.user_songs:
                del self.user_songs[user]
            else:
                print(f"User {user} exists in the userbase, but, does not have a song list to delete.")
        else:
            print(f"User {user} does not exist in the user base.")

    # Is case-sensitive here ( for safety ) 
    def get_song_list_by_user_id(self,user_id):
        """
        Get the song list for a specific user.
        If the user does not have a song list, return an empty list.
        """
        if(user_id not in self.my_user_base):
            return []
        if user_id not in self.user_songs:
            return []
        return self.user_songs.get(user_id)
    
    def add_song_to_user(self, user_id, song):
        """
        Add a song to the user's song list.
        If the user does not exist, create a new entry.
        """
        if user_id not in self.user_songs:
            self.user_songs[user_id] = []
        self.user_songs[user_id].append(song)

    def delete_song_from_user(self, user_id, song):
        """
        Delete a song from the user's song list.
        If the user does not exist or the song is not in the user's list, do nothing.
        """
        if user_id in self.user_songs and song in self.user_songs[user_id]:
            self.user_songs[user_id].remove(song)

    


    
